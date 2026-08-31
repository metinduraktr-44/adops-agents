/**
 * Canva Connect API client — SCAFFOLD / STUBS ONLY (Bölüm 9, Mod A2).
 *
 * =====================================================================
 * SAFETY: This module DOES NOT make real network calls. Every method is a
 * documented stub that throws `NotImplementedError`. It exists so the owner
 * can wire the real Canva Connect API later. No secrets are stored here.
 *
 * Türkçe not: Bu dosya SADECE iskelettir. Gerçek Canva API çağrısı YAPMAZ.
 * OAuth ve anahtar yönetimi kullanıcı eylemidir; sırlar repoya konmaz.
 *
 * DOC-VERIFY: Confirm all endpoints, scopes, PKCE details, job shapes, and
 * field names against the official docs before implementing:
 *   https://www.canva.dev/docs/connect/
 * =====================================================================
 */
import { logError, registerDesign, nowIso } from "./log.js";
import { pollJob, withRetry } from "./poll.js";
import type {
  AutofillRequest,
  CanvaClientConfig,
  DesignRef,
  ExportRequest,
  Job,
  PkceChallenge,
  ResizeRequest,
  TokenSet,
  UploadedAsset,
} from "./types.js";

export class NotImplementedError extends Error {
  constructor(what: string) {
    super(
      `[canva-client SCAFFOLD] ${what} is not implemented. ` +
        `Wire the real Canva Connect API here (DOC-VERIFY endpoints/scopes).`,
    );
    this.name = "NotImplementedError";
  }
}

const DEFAULTS = {
  // DOC-VERIFY: confirm these base URLs against Canva Connect docs.
  apiBaseUrl: "https://api.canva.com/rest/v1",
  authBaseUrl: "https://www.canva.com/api/oauth",
};

export class CanvaClient {
  private config: Required<CanvaClientConfig>;
  private tokens: TokenSet | null = null;

  constructor(config: CanvaClientConfig) {
    this.config = {
      apiBaseUrl: DEFAULTS.apiBaseUrl,
      authBaseUrl: DEFAULTS.authBaseUrl,
      ...config,
    };
  }

  // ------------------------------------------------------------------
  // OAuth2 PKCE flow (stubs)
  // ------------------------------------------------------------------

  /**
   * Build a PKCE code_verifier/code_challenge + state.
   * TODO: implement with crypto.randomBytes + base64url(SHA-256(verifier)).
   * DOC-VERIFY: challenge method must be "S256".
   */
  createPkceChallenge(): PkceChallenge {
    throw new NotImplementedError("createPkceChallenge");
  }

  /**
   * Build the authorization URL the USER opens in a browser to grant consent.
   * OAuth is a USER ACTION — this client never handles the user's password.
   * TODO: assemble `${authBaseUrl}/authorize?...` with client_id, redirect_uri,
   * scope, code_challenge, code_challenge_method, state, response_type=code.
   */
  buildAuthorizeUrl(_challenge: PkceChallenge): string {
    throw new NotImplementedError("buildAuthorizeUrl");
  }

  /**
   * Exchange an authorization code (+ code_verifier) for a TokenSet.
   * TODO: POST `${authBaseUrl}/token` with grant_type=authorization_code.
   * DOC-VERIFY: token endpoint + params. Store tokens only in memory/secure store.
   */
  async exchangeCodeForToken(
    _code: string,
    _codeVerifier: string,
  ): Promise<TokenSet> {
    throw new NotImplementedError("exchangeCodeForToken");
  }

  /**
   * Refresh an expired access token using the refresh token.
   * TODO: POST `${authBaseUrl}/token` with grant_type=refresh_token.
   */
  async refreshToken(): Promise<TokenSet> {
    throw new NotImplementedError("refreshToken");
  }

  /** Return a valid access token, refreshing if near expiry. */
  private async ensureAccessToken(): Promise<string> {
    if (!this.tokens) {
      throw new NotImplementedError("ensureAccessToken (no token; run OAuth first)");
    }
    if (Date.now() >= this.tokens.expiresAt - 30_000) {
      // Refresh with retry/backoff (stub).
      this.tokens = await withRetry(() => this.refreshToken());
    }
    return this.tokens.accessToken;
  }

  // ------------------------------------------------------------------
  // Assets
  // ------------------------------------------------------------------

  /**
   * Upload a local asset (image/video) to Canva.
   * TODO: POST to the asset-upload endpoint with the token from ensureAccessToken().
   * DOC-VERIFY: multipart vs. upload-URL flow.
   */
  async uploadAsset(_filePath: string, _name?: string): Promise<UploadedAsset> {
    throw new NotImplementedError("uploadAsset");
  }

  // ------------------------------------------------------------------
  // Autofill (bulk create)
  // ------------------------------------------------------------------

  /**
   * Submit an autofill job against a brand template, then poll to completion.
   * TODO: POST autofill endpoint -> get job id -> pollJob(fetchAutofillJob).
   * On success, registerDesign(...) for each produced design.
   */
  async autofillDesign(_req: AutofillRequest): Promise<DesignRef> {
    throw new NotImplementedError("autofillDesign");
  }

  /** Fetch autofill job status. TODO: GET autofill/{id}. */
  async getAutofillJob(_jobId: string): Promise<Job<DesignRef>> {
    throw new NotImplementedError("getAutofillJob");
  }

  // ------------------------------------------------------------------
  // Resize
  // ------------------------------------------------------------------

  /**
   * Submit a resize job (design -> new dimensions), then poll to completion.
   * TODO: POST resize endpoint -> job id -> pollJob(getResizeJob).
   */
  async resizeDesign(_req: ResizeRequest): Promise<DesignRef> {
    throw new NotImplementedError("resizeDesign");
  }

  /** Fetch resize job status. TODO: GET resize/{id}. */
  async getResizeJob(_jobId: string): Promise<Job<DesignRef>> {
    throw new NotImplementedError("getResizeJob");
  }

  // ------------------------------------------------------------------
  // Export
  // ------------------------------------------------------------------

  /**
   * Submit an export job (design -> file URL), then poll to completion.
   * TODO: POST export endpoint -> job id -> pollJob(getExportJob).
   * DOC-VERIFY: supported formats/quality per placement.
   */
  async exportDesign(_req: ExportRequest): Promise<{ urls: string[] }> {
    throw new NotImplementedError("exportDesign");
  }

  /** Fetch export job status. TODO: GET export/{id}. */
  async getExportJob(_jobId: string): Promise<Job<{ urls: string[] }>> {
    throw new NotImplementedError("getExportJob");
  }
}

/**
 * Example wiring (NOT executed): shows the intended production flow.
 * Kept as a stub-safe reference; every call throws NotImplementedError today.
 */
export async function exampleProductionFlow(config: CanvaClientConfig): Promise<void> {
  const client = new CanvaClient(config);
  try {
    // 1) USER completes OAuth (browser). buildAuthorizeUrl -> exchangeCodeForToken.
    // 2) const asset = await client.uploadAsset("path/to/image.png");
    // 3) const design = await client.autofillDesign({ brandTemplateId: "...", data: {} });
    // 4) const resized = await client.resizeDesign({ designId: design.designId, width: 1080, height: 1920 });
    // 5) const exported = await client.exportDesign({ designId: resized.designId, format: "jpg" });
    // 6) registerDesign({ ... }) — record the result row.
    await registerDesign({
      timestamp: nowIso(),
      operation: "example",
      designId: "STUB",
      channel: "",
      placement: "",
      width: "",
      height: "",
      format: "",
      status: "scaffold-noop",
      url: "",
      notes: "exampleProductionFlow is a doc-only stub; no API called",
    });
    void pollJob; // referenced to document intended usage
  } catch (err) {
    await logError("exampleProductionFlow", err);
    throw err;
  }
}

export * from "./types.js";
export { pollJob, withRetry } from "./poll.js";
export { logError, registerDesign } from "./log.js";
