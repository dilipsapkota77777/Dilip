import "dotenv/config";
import Anthropic from "@anthropic-ai/sdk";

type Result = { key: string; status: "ok" | "missing" | "invalid" | "skipped"; detail?: string };

async function checkAnthropic(): Promise<Result> {
  const key = process.env.ANTHROPIC_API_KEY;
  if (!key) return { key: "ANTHROPIC_API_KEY", status: "missing" };

  try {
    const client = new Anthropic({ apiKey: key });
    const response = await client.messages.create({
      model: "claude-opus-4-8",
      max_tokens: 8,
      messages: [{ role: "user", content: "Hi" }],
    });
    return {
      key: "ANTHROPIC_API_KEY",
      status: "ok",
      detail: `model=${response.model}`,
    };
  } catch (err: unknown) {
    const msg = err instanceof Error ? err.message : String(err);
    return { key: "ANTHROPIC_API_KEY", status: "invalid", detail: msg };
  }
}

async function checkOptionalHttpKey(
  envKey: string,
  url: string,
  headers: Record<string, string>
): Promise<Result> {
  const key = process.env[envKey];
  if (!key) return { key: envKey, status: "skipped", detail: "not set (optional)" };

  try {
    const res = await fetch(url, { headers });
    if (res.ok || res.status === 404) {
      return { key: envKey, status: "ok", detail: `HTTP ${res.status}` };
    }
    if (res.status === 401 || res.status === 403) {
      return { key: envKey, status: "invalid", detail: `HTTP ${res.status} — key rejected` };
    }
    return { key: envKey, status: "ok", detail: `HTTP ${res.status}` };
  } catch (err: unknown) {
    const msg = err instanceof Error ? err.message : String(err);
    return { key: envKey, status: "invalid", detail: msg };
  }
}

function icon(status: Result["status"]) {
  return { ok: "✓", missing: "✗", invalid: "✗", skipped: "—" }[status];
}

function color(status: Result["status"], text: string) {
  const codes = { ok: "\x1b[32m", missing: "\x1b[31m", invalid: "\x1b[31m", skipped: "\x1b[33m" };
  return `${codes[status]}${text}\x1b[0m`;
}

async function main() {
  console.log("\nVerifying credentials...\n");

  const results = await Promise.all([
    checkAnthropic(),
    checkOptionalHttpKey(
      "HUNTER_API_KEY",
      "https://api.hunter.io/v2/account",
      { Authorization: `Bearer ${process.env.HUNTER_API_KEY ?? ""}` }
    ),
    checkOptionalHttpKey(
      "APOLLO_API_KEY",
      "https://api.apollo.io/api/v1/auth/health",
      { "x-api-key": process.env.APOLLO_API_KEY ?? "" }
    ),
    checkOptionalHttpKey(
      "SENDGRID_API_KEY",
      "https://api.sendgrid.com/v3/user/profile",
      { Authorization: `Bearer ${process.env.SENDGRID_API_KEY ?? ""}` }
    ),
    checkOptionalHttpKey(
      "CLEARBIT_API_KEY",
      "https://company.clearbit.com/v2/companies/find?domain=clearbit.com",
      { Authorization: `Bearer ${process.env.CLEARBIT_API_KEY ?? ""}` }
    ),
  ]);

  const maxKeyLen = Math.max(...results.map((r) => r.key.length));

  for (const r of results) {
    const badge = color(r.status, `${icon(r.status)} ${r.status.toUpperCase().padEnd(7)}`);
    const keyPad = r.key.padEnd(maxKeyLen);
    const detail = r.detail ? `  ${r.detail}` : "";
    console.log(`  ${badge}  ${keyPad}${detail}`);
  }

  const failed = results.filter((r) => r.status === "missing" || r.status === "invalid");

  if (failed.some((r) => r.key === "ANTHROPIC_API_KEY")) {
    console.log("\n\x1b[31mANTHROPIC_API_KEY is required. Copy .env.example to .env and add your key.\x1b[0m\n");
    process.exit(1);
  }

  const badOptional = failed.filter((r) => r.key !== "ANTHROPIC_API_KEY");
  if (badOptional.length) {
    console.log(`\n\x1b[33mWarning: ${badOptional.map((r) => r.key).join(", ")} set but invalid.\x1b[0m`);
  }

  console.log("\n\x1b[32mAll required credentials OK.\x1b[0m\n");
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
