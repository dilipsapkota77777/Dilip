import os
import anthropic
from pydantic import BaseModel


class ProspectProfile(BaseModel):
    name: str
    title: str
    company: str
    industry: str
    pain_points: list[str]
    recent_news: list[str]
    personalization_hooks: list[str]


class ProspectResearchSkill:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    def research(
        self,
        name: str,
        title: str,
        company: str,
        extra_context: str = "",
    ) -> ProspectProfile:
        prompt = f"""Research this sales prospect and extract key information for cold email personalization.

Prospect:
- Name: {name}
- Title: {title}
- Company: {company}
{f"- Additional context: {extra_context}" if extra_context else ""}

Based on what you know about this person and company, provide:
1. The industry they operate in
2. Likely pain points for someone in their role
3. Any notable recent news or developments about their company
4. Personalization hooks (specific angles to make outreach feel relevant)

Respond in this exact JSON format:
{{
  "industry": "...",
  "pain_points": ["...", "..."],
  "recent_news": ["...", "..."],
  "personalization_hooks": ["...", "..."]
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

        return ProspectProfile(
            name=name,
            title=title,
            company=company,
            industry=data["industry"],
            pain_points=data["pain_points"],
            recent_news=data.get("recent_news", []),
            personalization_hooks=data["personalization_hooks"],
        )
