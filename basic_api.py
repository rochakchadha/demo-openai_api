import os
import openai

openai.api_key = "EMPTY"
openai.api_base = "http://172.29.40.171:8000/v1"



response = openai.ChatCompletion.create(
    model = "Llama-2-7b-chat-hf",
    temperature=0.9,
    max_tokens=100,
    messages=[
        {"role": "system", "content": "You are a 23 year old, who's free to express their opinion. You always respond and express your honest opinion. You are a very opinionated person."},
        {"role": "user", "content": "What's your name?"}
    ]
)
print(response.choices[0].message.content)