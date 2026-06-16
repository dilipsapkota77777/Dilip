import os
import anthropic
from pydantic import BaseModel
from .prospect_research import ProspectProfile
from .email_personalization import PersonalizationStrategy


class ColdEmail(BaseModel):
    subject: str
    body: str
    preview_text: str


class EmailGeneratorSkill:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    def generate(
        self,
        prospect: ProspectProfile,
        strategy: PersonalizationStrategy,
        sender_name: str,
        sender_company: str,
        product_description: str,
        word_limit: int = 150,
    ) -> ColdEmail:
        prompt = f"""Write a cold email following this strategy exactly.

RECIPIENT:
- Name: {prospect.name}
- Title: {prospect.title}
- Company: {prospect.company}

STRATEGY:
- Subject angle: {strategy.subject_angle}
- Opening hook: {strategy.opening_hook}
- Value proposition: {strategy.value_proposition}
- CTA: {strategy.call_to_action}
- Tone: {strategy.tone}

SENDER:
- Name: {sender_name}
- Company: {sender_company}
- Product/Service: {product_description}

RULES:
- Body must be under {word_limit} words
- No fluff, no buzzwords, no generic statements
- Sound like a human wrote it, not a template
- Use first name only when addressing the prospect
- One CTA only — do not ask multiple questions
- No fake urgency or pressure tactics

Respond in this exact JSON format:
{{
  "subject": "the email subject line",
  "preview_text": "35-50 char preview shown in inbox before opening",
  "body": "the full email body including greeting and sign-off"
}}"""

        with self.client.messages.stream(
            model="claude-opus-4-8",
            max_tokens=2048,
            thinking={"type": "adaptive"},
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            response = stream.get_final_message()

        import json
        text = next(
            block.text for block in response.content if block.type == "text"
        )
        start = text.find("{")
        end = text.rfind("}") + 1
        data = json.loads(text[start:end])

        return ColdEmail(**data)

    def generate_simple(
        self,
        prospect_name: str,
        prospect_title: str,
        prospect_company: str,
        sender_name: str,
        sender_company: str,
        product_description: str,
        key_benefit: str,
    ) -> ColdEmail:
        prompt = f"""Write a concise, personalized cold email.

TO: {prospect_name}, {prospect_title} at {prospect_company}
FROM: {sender_name} at {sender_company}
OFFERING: {product_description}
KEY BENEFIT FOR THEM: {key_benefit}

Write a cold email under 120 words. Make the subject line specific and intriguing.
No buzzwords. No generic openers like "I hope this finds you well."
End with a single, low-commitment CTA (e.g., "worth a 15-min call?").

Respond in this exact JSON format:
{{
  "subject": "...",
  "preview_text": "...",
  "body": "..."
}}"""

        with self.client.messages.stream(
            model="claude-opus-4-8",
            max_tokens=1024,
            thinking={"type": "adaptive"},
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            response = stream.get_final_message()

        import json
        text = next(
            block.text for block in response.content if block.type == "text"
        )
        start = text.find("{")
        end = text.rfind("}") + 1
        data = json.loads(text[start:end])

        return ColdEmail(**data)
