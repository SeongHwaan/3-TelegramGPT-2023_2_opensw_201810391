import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key = os.environ.get("OPENAI_API_KEY")
)

def chatgpt(request_message):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": request_message}
    ]
    )
    return (completion.choices[0].message.content)