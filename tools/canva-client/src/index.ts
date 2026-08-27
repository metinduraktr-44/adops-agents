/**
 * Canva client scaffold — implement after owner OAuth (Phase 6).
 * Do not hardcode tokens. Read CANVA_ACCESS_TOKEN from process.env.
 */
export interface CanvaClientConfig {
  accessToken?: string;
  baseUrl?: string;
}

export function createCanvaClient(config: CanvaClientConfig = {}) {
  const token = config.accessToken ?? process.env.CANVA_ACCESS_TOKEN;
  if (!token) {
    throw new Error("CANVA_ACCESS_TOKEN not set — use Cursor MCP or owner env");
  }
  return {
    baseUrl: config.baseUrl ?? "https://api.canva.com/rest/v1",
    token,
  };
}
