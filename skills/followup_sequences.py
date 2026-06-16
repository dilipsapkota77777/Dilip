import os
import anthropic
from pydantic import BaseModel
from .prospect_research import ProspectProfile
from .email_generator import ColdEmail


class FollowupEmail(BaseModel):
    day: int
    subject: str
    body: str
    strategy: str


class FollowupSequence(BaseModel):
    initial_email: ColdEmail
    followups: list[FollowupEmail]


class FollowupSequencesSkill:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

    def generate_sequence(
        self,
        prospect: ProspectProfile,
        initial_email: ColdEmail,
        sender_name: str,
        sender_company: str,
        num_followups: int = 3,
    ) -> FollowupSequence:
        followup_days = [3, 7, 14][:num_followups]

        prompt = f"""Generate {num_followups} follow-up emails for a cold email sequence.

PROSPECT: {prospect.name}, {prospect.title} at {prospect.company}
INDUSTRY: {prospect.industry}
SENDER: {sender_name} at {sender_company}

INITIAL EMAIL SENT:
Subject: {initial_email.subject}
Body: {initial_email.body}

FOLLOW-UP SCHEDULE (days after initial):
{', '.join(str(d) for d in followup_days)}

Rules for follow-ups:
- Each must add new value — never just "following up"
- Vary the angle: social proof, case study, new insight, direct question
- Get shorter with each follow-up
- Last follow-up is a polite break-up email
- Reference the initial email naturally without being needy

Respond with a JSON array of follow-up objects:
[
  {{
    "day": {followup_days[0]},
    "strategy": "brief description of the angle used",
    "subject": "...",
    "body": "..."
  }},
  ...
]"""

        with self.client.messages.stream(
            model="claude-opus-4-8",
            max_tokens=3000,
            thinking={"type": "adaptive"},
            messages=[{"role": "user", "content": prompt}],
        ) as stream:
            response = stream.get_final_message()

        import json
        text = next(
            block.text for block in response.content if block.type == "text"
        )
        start = text.find("[")
        end = text.rfind("]") + 1
        followups_data = json.loads(text[start:end])

        followups = [FollowupEmail(**f) for f in followups_data]

        return FollowupSequence(initial_email=initial_email, followups=followups)
