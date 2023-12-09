import openai
import os
import time
from colorama import Fore, Style

# Initialize the OpenAI API with your key
openai.api_key = "EMPTY"
openai.api_base = "http://172.29.40.249:8000/v1"

max_tokens = 200 # change when using openAI API
model = "Mistral_7b_dolly_15k"
Temperature = 0.6
repeat_penalty = 0.5

conversation_history = []
system_instruct = "Below is an instruction that describes a task. Write a response that appropriately completes the request.\n\n"


messages=[
        {"role": "system", "content": system_instruct},
  ]
conversation_history.append(messages[0])

def chat_with_LLM(prompt):
  
    global conversation_history
    conversation_history.append({"role": "user", "content": prompt})
    
    response = openai.ChatCompletion.create(
      model=model,
      Temperature=Temperature,
      repeat_penalty=repeat_penalty,
      max_tokens=max_tokens,  # You can adjust the number of tokens (words) you want in the response
      messages=conversation_history,
      stream=True, # If you set stream=True you can keep calling response.choices[0].text to get the next tokens
    )
    end_time = time.time()

    assistant_message = ""
    print("### Response\n")
    for chunk in response:
        event_text= chunk["choices"][0]["delta"].get("content", "")
   
        assistant_message += event_text
        print(event_text, end="", flush=True)
        # Check for [/RESP], [OUT], or [INST] in the entire accumulated message
        if any(marker in assistant_message for marker in ["[/RESP]", "[OUT]", "[INST]"]):
            stop_marker = next(marker for marker in ["[/RESP]", "[OUT]", "[INST]"] if marker in assistant_message)
            assistant_message = assistant_message.split(stop_marker)[0]  # Keep only text before the first found marker
            break # Stop processing further chunks
     

    conversation_history.append({"role": "assistant", "content": assistant_message})
    print()
 
    return assistant_message

def main():
    print(f"\nChat with {model} running on {openai.api_base } Type 'exit' to end the chat.")
    while True:
        user_input = input("###Instruction\n")
        if user_input.lower() == 'exit':
            break
        
        response = chat_with_LLM(user_input)
        

if __name__ == "__main__":
    main()
