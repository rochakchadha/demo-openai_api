import os
import openai

openai.api_key = "EMPTY"
openai.api_base = "http://172.29.40.171:8000/v1"

response = openai.ChatCompletion.create(
    model = "Llama-2-7b-chat-hf",
    temperature=0.9,
    max_tokens=1024,
    messages=[
        {"role": "system", "content": "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."},
        {"role": "user", "content": "Computer, what is the meaning of life?"}],
        stream=True,
)
for chunk in response:
    content = chunk["choices"][0]["delta"].get("content", "")
    print(content, end="", flush=True)
print()