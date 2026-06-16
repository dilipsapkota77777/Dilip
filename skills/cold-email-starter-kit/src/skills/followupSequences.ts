import Anthropic from "@anthropic-ai/sdk";
import { ProspectProfile, ColdEmail, FollowupSequence, FollowupSequenceSchema } from "../types.js";

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

export async function generateFollowupSequence(
  prospect: ProspectProfile,
  initialEmail: ColdEmail,
  senderName: string,
  senderCompany: string,
  numFollowups = 3
): Promise<FollowupSequence> {
  const followupDays = [3, 7, 14].slice(0, numFollowups);

  const prompt = `Generate ${numFollowups} follow-up emails for a cold email sequence.

PROSPECT: ${prospect.name}, ${prospect.title} at ${prospect.company}
INDUSTRY: ${prospect.industry}
SENDER: ${senderName} at ${senderCompany}

INITIAL EMAIL SENT:
Subject: ${initialEmail.subject}
Body: ${initialEmail.body}

FOLLOW-UP SCHEDULE (days after initial): ${followupDays.join(", ")}

Rules for follow-ups:
- Each must add new value — never just "following up"
- Vary the angle: social proof, case study, new insight, direct question
- Get shorter with each follow-up
- Last follow-up is a polite break-up email
- Reference the initial email naturally without being needy

Respond ONLY with a JSON array (no markdown):
[
  {
    "day": ${followupDays[0]},
    "strategy": "brief description of the angle used",
    "subject": "...",
    "body": "..."
  }
]`;

  const stream = client.messages.stream({
    model: "claude-opus-4-8",
    max_tokens: 3000,
    // eslint-disable-next-line @typescript-eslint/no-explicit-any
    thinking: { type: "adaptive" } as any,
    messages: [{ role: "user", content: prompt }],
  });

  const response = await stream.finalMessage();
  const textBlock = response.content.find((b) => b.type === "text");
  if (!textBlock || textBlock.type !== "text") throw new Error("No text in response");

  const raw = textBlock.text;
  const json = JSON.parse(raw.slice(raw.indexOf("["), raw.lastIndexOf("]") + 1));

  return FollowupSequenceSchema.parse({ initialEmail, followups: json });
}
