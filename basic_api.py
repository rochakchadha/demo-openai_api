import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    temperature=0.9,
    max_tokens=10,
    messages=[
        {"role": "system", "content": "You are a 23 year old, who's free to express their opinion. You always respond and express your honest opinion. You are a very opinionated person."},
        {"role": "user", "content": "Tell me your thoughts on the January 6th insurrection."}
    ]
)
print(response)