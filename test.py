import os
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

class TicketClassification(BaseModel):
    category: str = Field(description="One of: billing, technical, account, other")
    urgency: int = Field(description="Urgency score from 1 (low) to 5 (critical)", ge=1, le=5)
    summary: str = Field(description="One-sentence summary of the customer issue")

response = client.beta.chat.completions.parse(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": "Classify the incoming support ticket into the required schema."},
        {"role": "user", "content": "I was charged twice on my card this morning and need a refund urgently."}
    ],
    response_format=TicketClassification,
    temperature=0
)

ticket = response.choices[0].message.parsed
print("Category:", ticket.category)
print("Urgency:", ticket.urgency)
print("Summary:", ticket.summary)