# Contributing

Component structure mirrors `claude-code-templates` (aitmpl.com).

## Add an agent
```
components/agents/[category]/[name].md
```
Frontmatter: `name`, `description` (with "Use when ..." triggers), `tools`, `model`.
Sections: purpose, ## Expertise, ## Instructions, ## Examples, ## Self-check.

## Add a command
```
components/commands/[category]/[name].md
```
Frontmatter: `description`. Body: single-purpose instruction with clear I/O.

## Add a skill
```
components/skills/[category]/[name]/SKILL.md
```
Frontmatter: `name`, `description`, `allowed-tools`, `model`, `user-invocable`.
Keep SKILL.md short; put heavy content under `references/` (progressive disclosure).

## Before committing
Run `npm run validate`. All 6 checks must pass. Bump version in `VERSIONS.md`.
