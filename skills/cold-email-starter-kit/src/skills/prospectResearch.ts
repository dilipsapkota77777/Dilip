import Anthropic from "@anthropic-ai/sdk";
import { ProspectProfile, ProspectProfileSchema } from "../types.js";

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

export async function researchProspect(
  name: string,
  title: string,
  company: string,
  extraContext = ""
): Promise<ProspectProfile> {
  const prompt = `Research this sales prospect and extract key information for cold email personalization.

Prospect:
- Name: ${name}
- Title: ${title}
- Company: ${company}
${extraContext ? `- Additional context: ${extraContext}` : ""}

Based on what you know about this person and company, provide:
1. The industry they operate in
2. Likely pain points for someone in their role
3. Any notable recent news or developments about their company
4. Personalization hooks (specific angles to make outreach feel relevant)

Respond ONLY with this exact JSON (no markdown, no explanation):
{
  "industry": "...",
  "painPoints": ["...", "..."],
  "recentNews": ["...", "..."],
  "personalizationHooks": ["...", "..."]
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

  return ProspectProfileSchema.parse({ name, title, company, ...json });
}
