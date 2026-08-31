/**
 * Canva Connect API client — shared types (SCAFFOLD / STUBS ONLY).
 *
 * Türkçe not: Yalnızca tip iskeleti. Alan adları Canva Connect API dokümanına
 * karşı DOĞRULANMALI (doc-verify) — aşağıdaki alanlar tahmini/örnek olabilir.
 *
 * DOC-VERIFY: Confirm every field name, endpoint, scope, and job shape against
 * the official Canva Connect API docs (https://www.canva.dev/docs/connect/)
 * before wiring real calls. Do NOT assume these are correct.
 */

export interface CanvaClientConfig {
  /** OAuth2 client id (public). Provided by the user at runtime — never hard-coded. */
  clientId: string;
  /** Redirect URI registered for the OAuth app. */
  redirectUri: string;
  /** Requested OAuth scopes. DOC-VERIFY exact scope strings. */
  scopes: string[];
  /** API base URL. DOC-VERIFY. */
  apiBaseUrl?: string;
  /** Authorization + token endpoints. DOC-VERIFY. */
  authBaseUrl?: string;
}

export interface PkceChallenge {
  codeVerifier: string;
  codeChallenge: string;
  /** Always "S256" for Canva Connect PKCE. DOC-VERIFY. */
  method: "S256";
  state: string;
}

export interface TokenSet {
  accessToken: string;
  refreshToken?: string;
  /** Epoch millis when the access token expires. */
  expiresAt: number;
  tokenType: string;
  scope?: string;
}

/** Generic long-running job status. DOC-VERIFY status enum values. */
export type JobStatus = "in_progress" | "success" | "failed";

export interface Job<T = unknown> {
  id: string;
  status: JobStatus;
  result?: T;
  error?: string;
}

export interface UploadedAsset {
  assetId: string;
  name?: string;
}

export interface AutofillRequest {
  /** Brand template id to autofill against. DOC-VERIFY. */
  brandTemplateId: string;
  /** Field name -> value map. DOC-VERIFY field payload shape. */
  data: Record<string, unknown>;
}

export interface ResizeRequest {
  designId: string;
  width: number;
  height: number;
}

export interface ExportRequest {
  designId: string;
  /** e.g. "jpg" | "png" | "pdf" | "mp4". DOC-VERIFY supported formats. */
  format: string;
  quality?: string;
}

export interface DesignRef {
  designId: string;
  title?: string;
  url?: string;
}

/** One row written to CANVA_OPS/DESIGN_REGISTRY.csv. */
export interface RegistryRow {
  timestamp: string;
  operation: string;
  designId: string;
  channel: string;
  placement: string;
  width: number | "";
  height: number | "";
  format: string;
  status: string;
  url: string;
  notes: string;
}
