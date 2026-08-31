/**
 * Polling + retry/backoff utilities (SCAFFOLD).
 *
 * Türkçe not: Uzun süren işler (autofill/resize/export) için poll + geri-çekilme.
 * Gerçek ağ çağrısı YOK — sadece yeniden kullanılabilir yardımcılar.
 */
import type { Job } from "./types.js";

export interface RetryOptions {
  maxAttempts?: number;
  baseDelayMs?: number;
  maxDelayMs?: number;
}

export async function sleep(ms: number): Promise<void> {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

/**
 * Retry an async op with exponential backoff + jitter.
 * Retries on any thrown error up to maxAttempts.
 */
export async function withRetry<T>(
  fn: (attempt: number) => Promise<T>,
  opts: RetryOptions = {},
): Promise<T> {
  const maxAttempts = opts.maxAttempts ?? 4;
  const baseDelayMs = opts.baseDelayMs ?? 500;
  const maxDelayMs = opts.maxDelayMs ?? 8000;
  let lastErr: unknown;
  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    try {
      return await fn(attempt);
    } catch (err) {
      lastErr = err;
      if (attempt >= maxAttempts) break;
      const backoff = Math.min(maxDelayMs, baseDelayMs * 2 ** (attempt - 1));
      const jitter = Math.floor(Math.random() * (backoff / 2));
      await sleep(backoff + jitter);
    }
  }
  throw lastErr instanceof Error ? lastErr : new Error(String(lastErr));
}

export interface PollOptions {
  intervalMs?: number;
  timeoutMs?: number;
}

/**
 * Poll a job-fetching function until it reaches a terminal state or times out.
 * DOC-VERIFY: adjust terminal-state detection to Canva's real status enum.
 */
export async function pollJob<T>(
  fetchJob: () => Promise<Job<T>>,
  opts: PollOptions = {},
): Promise<Job<T>> {
  const intervalMs = opts.intervalMs ?? 1500;
  const timeoutMs = opts.timeoutMs ?? 120000;
  const start = Date.now();
  // eslint-disable-next-line no-constant-condition
  while (true) {
    const job = await fetchJob();
    if (job.status === "success" || job.status === "failed") {
      return job;
    }
    if (Date.now() - start > timeoutMs) {
      return { ...job, status: "failed", error: "poll timeout" };
    }
    await sleep(intervalMs);
  }
}
