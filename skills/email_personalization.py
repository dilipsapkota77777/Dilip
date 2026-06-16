import os
import anthropic
from pydantic import BaseModel
from .prospect_research import ProspectProfile


class PersonalizationStrategy(BaseModel):
    subject_angle: str
    opening_hook: str
    value_proposition: str
    call_to_action: str
    tone: str


class EmailPersonalizationSkill:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    def build_strategy(
        self,
        prospect: ProspectProfile,
        sender_name: str,
        sender_company: str,
        product_description: str,
    ) -> PersonalizationStrategy:
        pain_points = "\n".join(f"- {p}" for p in prospect.pain_points)
        hooks = "\n".join(f"- {h}" for h in prospect.personalization_hooks)
        news = "\n".join(f"- {n}" for n in prospect.recent_news) if prospect.recent_news else "None available"

        prompt = f"""You are an expert cold email strategist. Create a personalization strategy for a cold email.

PROSPECT:
- Name: {prospect.name}
- Title: {prospect.title}
- Company: {prospect.company}
- Industry: {prospect.industry}

PAIN POINTS:
{pain_points}

PERSONALIZATION HOOKS:
{hooks}

RECENT NEWS:
{news}

SENDER:
- Name: {sender_name}
- Company: {sender_company}
- Product/Service: {product_description}

Design a personalization strategy. Respond in this exact JSON format:
{{
  "subject_angle": "the core angle for the subject line",
  "opening_hook": "how to open the email to immediately grab attention",
  "value_proposition": "the specific value to highlight for this prospect",
  "call_to_action": "the specific CTA that fits this prospect's context",
  "tone": "professional/conversational/casual — pick one that fits"
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

        return PersonalizationStrategy(**data)
