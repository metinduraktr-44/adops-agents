# Datadog + Sentry monitors wired to PagerDuty (critical) and Slack (warn/critical).
# TR: Referans modül — gerçek apply için provider credentials gerekir (owner secrets).
# Domain 2 uyumu: /sentry-create-alert /ddconfig /pagerduty-mcp-setup /kibana-alerting-rules

terraform {
  required_version = ">= 1.5.0"
  required_providers {
    datadog   = { source = "DataDog/datadog", version = "~> 3.35.0" }
    sentry    = { source = "jianyuan/sentry", version = "~> 0.12.0" }
    pagerduty = { source = "PagerDuty/pagerduty", version = "~> 3.11.0" }
  }
}

variable "environment"           { type = string  default = "production" }
variable "service_name"          { type = string  default = "api-service-prod" }
variable "datadog_api_key"       { type = string  sensitive = true }
variable "datadog_app_key"       { type = string  sensitive = true }
variable "sentry_auth_token"     { type = string  sensitive = true }
variable "sentry_organization"   { type = string }
variable "sentry_project_slug"   { type = string }
variable "pagerduty_user_email"  { type = string }
variable "slack_channel_critical" { type = string default = "alerts-critical" }
variable "slack_channel_warnings" { type = string default = "alerts-warnings" }
variable "error_rate_warn"       { type = number  default = 0.02 }
variable "error_rate_critical"   { type = number  default = 0.05 }
variable "error_spike_critical"  { type = number  default = 50 }

provider "datadog" {
  api_key = var.datadog_api_key
  app_key = var.datadog_app_key
  api_url = "https://api.datadoghq.com"
}

provider "sentry" {
  token = var.sentry_auth_token
}

provider "pagerduty" {
  # Uses PAGERDUTY_TOKEN from environment
}

data "pagerduty_user" "oncall" {
  email = var.pagerduty_user_email
}

resource "pagerduty_escalation_policy" "backend" {
  name      = "[${upper(var.environment)}] ${var.service_name} backend"
  num_loops = 2

  rule {
    escalation_delay_in_minutes = 10
    target {
      type = "user_reference"
      id   = data.pagerduty_user.oncall.id
    }
  }
}

resource "pagerduty_service" "api" {
  name                    = "${var.service_name}-${var.environment}"
  description             = "Domain-2 critical path — Datadog/Sentry → PD"
  auto_resolve_timeout    = 14400
  acknowledgement_timeout = 600
  escalation_policy       = pagerduty_escalation_policy.backend.id
  alert_creation          = "create_alerts_and_incidents"
}

resource "pagerduty_service_integration" "events_v2" {
  name    = "Events API V2"
  type    = "events_api_v2_inbound_integration"
  service = pagerduty_service.api.id
}

# --- Datadog: WARNING (Slack only — no page) ---
resource "datadog_monitor" "error_rate_warn" {
  name    = "[${upper(var.environment)}] ${var.service_name} error rate WARN"
  type    = "metric alert"
  message = <<-EOT
    {{#is_alert}}Error rate above warn threshold.{{/is_alert}}
    {{#is_recovery}}Recovered.{{/is_recovery}}
    @slack-${var.slack_channel_warnings}
  EOT

  query = "avg(last_5m):sum:trace.servlet.request.errors{service:${var.service_name},env:${var.environment}}.as_count() / sum:trace.servlet.request.hits{service:${var.service_name},env:${var.environment}}.as_count() > ${var.error_rate_warn}"

  monitor_thresholds {
    critical = var.error_rate_warn
  }

  tags = ["domain:2", "severity:warn", "service:${var.service_name}", "managed:adops-agents"]
}

# --- Datadog: CRITICAL (Slack + PagerDuty page) ---
resource "datadog_monitor" "error_rate_critical" {
  name    = "[${upper(var.environment)}] ${var.service_name} error rate CRITICAL"
  type    = "metric alert"
  message = <<-EOT
    {{#is_alert}}Error rate CRITICAL — paging on-call.{{/is_alert}}
    {{#is_recovery}}Recovered — auto-resolve PD.{{/is_recovery}}
    @slack-${var.slack_channel_critical}
    @pagerduty-${pagerduty_service.api.name}
  EOT

  query = "avg(last_5m):sum:trace.servlet.request.errors{service:${var.service_name},env:${var.environment}}.as_count() / sum:trace.servlet.request.hits{service:${var.service_name},env:${var.environment}}.as_count() > ${var.error_rate_critical}"

  monitor_thresholds {
    critical = var.error_rate_critical
  }

  tags = ["domain:2", "severity:critical", "service:${var.service_name}", "managed:adops-agents"]
}

resource "datadog_monitor" "error_spike_critical" {
  name    = "[${upper(var.environment)}] ${var.service_name} error spike CRITICAL"
  type    = "metric alert"
  message = <<-EOT
    {{#is_alert}}≥${var.error_spike_critical} errors/1m — paging.{{/is_alert}}
    {{#is_recovery}}Spike cleared.{{/is_recovery}}
    @slack-${var.slack_channel_critical}
    @pagerduty-${pagerduty_service.api.name}
  EOT

  query = "sum(last_1m):sum:trace.servlet.request.errors{service:${var.service_name},env:${var.environment}}.as_count() > ${var.error_spike_critical}"

  monitor_thresholds {
    critical = var.error_spike_critical
  }

  tags = ["domain:2", "severity:critical", "service:${var.service_name}", "managed:adops-agents"]
}

# --- Sentry issue alerts ---
resource "sentry_issue_alert" "warn_volume" {
  organization = var.sentry_organization
  project      = var.sentry_project_slug
  name         = "[${upper(var.environment)}] warn volume"

  action_match = "any"
  filter_match = "all"
  frequency    = 30

  conditions_v2 = jsonencode([
    { id = "sentry.rules.conditions.event_frequency.EventFrequencyCondition", value = 20, interval = "1h" }
  ])
  filters_v2 = jsonencode([])
  actions_v2 = jsonencode([
    {
      id        = "sentry.integrations.slack.notify_action.SlackNotifyServiceAction"
      workspace = "default"
      channel   = "#${var.slack_channel_warnings}"
    }
  ])
}

resource "sentry_issue_alert" "critical_spike" {
  organization = var.sentry_organization
  project      = var.sentry_project_slug
  name         = "[${upper(var.environment)}] critical spike → PD"

  action_match = "any"
  filter_match = "all"
  frequency    = 5

  conditions_v2 = jsonencode([
    { id = "sentry.rules.conditions.event_frequency.EventFrequencyCondition", value = 50, interval = "1m" }
  ])
  filters_v2 = jsonencode([])
  actions_v2 = jsonencode([
    {
      id        = "sentry.integrations.slack.notify_action.SlackNotifyServiceAction"
      workspace = "default"
      channel   = "#${var.slack_channel_critical}"
    },
    {
      id              = "sentry.integrations.pagerduty.notify_action.PagerDutyNotifyServiceAction"
      account         = "default"
      service         = pagerduty_service.api.name
      severity        = "critical"
      integration_key = pagerduty_service_integration.events_v2.integration_key
    }
  ])
}

output "pagerduty_service_id" {
  value = pagerduty_service.api.id
}

output "pagerduty_routing_key" {
  value     = pagerduty_service_integration.events_v2.integration_key
  sensitive = true
}

output "datadog_monitor_ids" {
  value = {
    warn     = datadog_monitor.error_rate_warn.id
    critical = datadog_monitor.error_rate_critical.id
    spike    = datadog_monitor.error_spike_critical.id
  }
}
