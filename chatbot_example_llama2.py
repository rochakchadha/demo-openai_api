import openai
import os
import time
from colorama import Fore, Style

# Initialize the OpenAI API with your key
openai.api_key = "EMPTY"
openai.api_base = "http://172.29.40.249:8000/v1"

max_tokens = 1024 # change when using openAI API
model = "Llama-2-7b-chat-hf"
Temperature = 0.1

conversation_history = []
messages=[
        {"role": "system", "content": "You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.  Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."},
    
  ]
conversation_history.append(messages[0])

def chat_with_LLM(prompt):
    
    global conversation_history
    conversation_history.append({"role": "user", "content": prompt})
   
    response = openai.ChatCompletion.create(
      model=model,
      Temperature=Temperature,
      max_tokens=max_tokens,  
      messages=conversation_history,
      stream=True, # If you set stream=True you can keep calling response.choices[0].text to get the next tokens
    )
    end_time = time.time()
 

    # Print the streamed output from the API
    assistant_message = ""
    print("Assistant: ", end='')
    for chunk in response:
        event_text= chunk["choices"][0]["delta"].get("content", "")
        assistant_message += event_text
        print(event_text,end="",flush=True )
    print()
     

    # Extract the assistant's message from the response   
    # assistant_message = response.choices[0].message['content']

    # Append the assistant's message to the conversation history
    conversation_history.append({"role": "assistant", "content": assistant_message})
 

    return assistant_message

def main():
    print(f"\nChat with {model} running on {openai.api_base } Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        
        response = chat_with_LLM(user_input)
        


if __name__ == "__main__":
    main()
