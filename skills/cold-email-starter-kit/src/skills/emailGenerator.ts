import Anthropic from "@anthropic-ai/sdk";
import { ProspectProfile, PersonalizationStrategy, ColdEmail, ColdEmailSchema } from "../types.js";

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

export async function generateEmail(
  prospect: ProspectProfile,
  strategy: PersonalizationStrategy,
  senderName: string,
  senderCompany: string,
  productDescription: string,
  wordLimit = 150
): Promise<ColdEmail> {
  const prompt = `Write a cold email following this strategy exactly.

RECIPIENT:
- Name: ${prospect.name}
- Title: ${prospect.title}
- Company: ${prospect.company}

STRATEGY:
- Subject angle: ${strategy.subjectAngle}
- Opening hook: ${strategy.openingHook}
- Value proposition: ${strategy.valueProposition}
- CTA: ${strategy.callToAction}
- Tone: ${strategy.tone}

SENDER:
- Name: ${senderName}
- Company: ${senderCompany}
- Product/Service: ${productDescription}

RULES:
- Body must be under ${wordLimit} words
- No fluff, no buzzwords, no generic statements
- Sound like a human wrote it, not a template
- Use first name only when addressing the prospect
- One CTA only — do not ask multiple questions
- No fake urgency or pressure tactics

Respond ONLY with this exact JSON (no markdown):
{
  "subject": "the email subject line",
  "previewText": "35-50 char preview shown in inbox before opening",
  "body": "the full email body including greeting and sign-off"
}`;

  const stream = client.messages.stream({
    model: "claude-opus-4-8",
    max_tokens: 2048,
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    thinking: { type: "adaptive" } as any,
    messages: [{ role: "user", content: prompt }],
  });

  const response = await stream.finalMessage();
  const textBlock = response.content.find((b) => b.type === "text");
  if (!textBlock || textBlock.type !== "text") throw new Error("No text in response");

  const raw = textBlock.text;
  const json = JSON.parse(raw.slice(raw.indexOf("{"), raw.lastIndexOf("}") + 1));

  return ColdEmailSchema.parse(json);
}

export async function generateSimpleEmail(
  prospectName: string,
  prospectTitle: string,
  prospectCompany: string,
  senderName: string,
  senderCompany: string,
  productDescription: string,
  keyBenefit: string
): Promise<ColdEmail> {
  const prompt = `Write a concise, personalized cold email.

TO: ${prospectName}, ${prospectTitle} at ${prospectCompany}
FROM: ${senderName} at ${senderCompany}
OFFERING: ${productDescription}
KEY BENEFIT FOR THEM: ${keyBenefit}

Write a cold email under 120 words. Make the subject line specific and intriguing.
No buzzwords. No generic openers like "I hope this finds you well."
End with a single, low-commitment CTA (e.g., "worth a 15-min call?").

Respond ONLY with this exact JSON (no markdown):
{
  "subject": "...",
  "previewText": "...",
  "body": "..."
}`;

  const stream = client.messages.stream({
    model: "claude-opus-4-8",
    max_tokens: 1024,
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    thinking: { type: "adaptive" } as any,
    messages: [{ role: "user", content: prompt }],
  });

  const response = await stream.finalMessage();
  const textBlock = response.content.find((b) => b.type === "text");
  if (!textBlock || textBlock.type !== "text") throw new Error("No text in response");

  const raw = textBlock.text;
  const json = JSON.parse(raw.slice(raw.indexOf("{"), raw.lastIndexOf("}") + 1));

  return ColdEmailSchema.parse(json);
}
