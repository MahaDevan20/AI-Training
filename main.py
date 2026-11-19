from openai import OpenAI
import os 
from dotenv import load_dotenv


load_dotenv() 
client = OpenAI(base_url="https://api.groq.com/openai/v1",
                api_key=os.getenv("GROQ_API_KEY")) 



response= client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[{"role":"system","content":"You are chemist"},
            {"role":"user","content":"Whats the chemical name of water"}],
     temperature=0.5,
)

print(response.choices[0].message.content)
