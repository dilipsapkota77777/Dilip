import Anthropic from "@anthropic-ai/sdk";
import { ProspectProfile, PersonalizationStrategy, PersonalizationStrategySchema } from "../types.js";

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

export async function buildPersonalizationStrategy(
  prospect: ProspectProfile,
  senderName: string,
  senderCompany: string,
  productDescription: string
): Promise<PersonalizationStrategy> {
  const painPoints = prospect.painPoints.map((p) => `- ${p}`).join("\n");
  const hooks = prospect.personalizationHooks.map((h) => `- ${h}`).join("\n");
  const news = prospect.recentNews.length
    ? prospect.recentNews.map((n) => `- ${n}`).join("\n")
    : "None available";

  const prompt = `You are an expert cold email strategist. Create a personalization strategy for a cold email.

PROSPECT:
- Name: ${prospect.name}
- Title: ${prospect.title}
- Company: ${prospect.company}
- Industry: ${prospect.industry}

PAIN POINTS:
${painPoints}

PERSONALIZATION HOOKS:
${hooks}

RECENT NEWS:
${news}

SENDER:
- Name: ${senderName}
- Company: ${senderCompany}
- Product/Service: ${productDescription}

Respond ONLY with this exact JSON (no markdown):
{
  "subjectAngle": "the core angle for the subject line",
  "openingHook": "how to open the email to immediately grab attention",
  "valueProposition": "the specific value to highlight for this prospect",
  "callToAction": "the specific CTA that fits this prospect's context",
  "tone": "professional"
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

  return PersonalizationStrategySchema.parse(json);
}
