/**
 * Error log + design registry writers (SCAFFOLD).
 *
 * Türkçe not: Hatalar CANVA_OPS/ERRORS.md'ye, üretilen tasarımlar
 * CANVA_OPS/DESIGN_REGISTRY.csv'ye yazılır. Registry append-only'dir.
 */
import { appendFile, mkdir, readFile, writeFile } from "node:fs/promises";
import { existsSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import type { RegistryRow } from "./types.js";

const __dirname = dirname(fileURLToPath(import.meta.url));
// tools/canva-client/src -> repo root is three levels up.
const REPO_ROOT = resolve(__dirname, "..", "..", "..");
const CANVA_OPS = resolve(REPO_ROOT, "CANVA_OPS");
const ERRORS_PATH = resolve(CANVA_OPS, "ERRORS.md");
const REGISTRY_PATH = resolve(CANVA_OPS, "DESIGN_REGISTRY.csv");

const REGISTRY_HEADER =
  "timestamp,operation,design_id,channel,placement,width,height,format,status,url,notes";

function nowIso(): string {
  return new Date().toISOString();
}

function csvCell(value: unknown): string {
  const s = value === null || value === undefined ? "" : String(value);
  if (/[",\n]/.test(s)) {
    return '"' + s.replace(/"/g, '""') + '"';
  }
  return s;
}

/** Append a dated error entry to CANVA_OPS/ERRORS.md. Never throws. */
export async function logError(context: string, error: unknown): Promise<void> {
  try {
    await mkdir(CANVA_OPS, { recursive: true });
    const msg = error instanceof Error ? error.stack ?? error.message : String(error);
    const entry = `\n## ${nowIso()} — ${context}\n\n\`\`\`\n${msg}\n\`\`\`\n`;
    await appendFile(ERRORS_PATH, entry, "utf-8");
  } catch {
    // fail-open: logging must never crash the caller
  }
}

/** Append a row to the design registry, creating the header if missing. Never throws. */
export async function registerDesign(row: RegistryRow): Promise<void> {
  try {
    await mkdir(CANVA_OPS, { recursive: true });
    let needsHeader = true;
    if (existsSync(REGISTRY_PATH)) {
      const current = await readFile(REGISTRY_PATH, "utf-8");
      needsHeader = current.trim().length === 0;
    }
    if (needsHeader) {
      await writeFile(REGISTRY_PATH, REGISTRY_HEADER + "\n", "utf-8");
    }
    const line = [
      row.timestamp,
      row.operation,
      row.designId,
      row.channel,
      row.placement,
      row.width,
      row.height,
      row.format,
      row.status,
      row.url,
      row.notes,
    ]
      .map(csvCell)
      .join(",");
    await appendFile(REGISTRY_PATH, line + "\n", "utf-8");
  } catch (err) {
    await logError("registerDesign", err);
  }
}

export { nowIso };
