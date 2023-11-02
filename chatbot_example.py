import openai
import os
import time
from colorama import Fore, Style

# Initialize the OpenAI API with your key
openai.api_key = os.getenv("OPENAI_API_KEY")
conversation_history = []

def chat_with_gpt3(prompt):
    """
    Send a prompt to GPT-4 and get the completion.
    """
    global conversation_history
    conversation_history.append({"role": "user", "content": prompt})
    # calculate the response time from GPT-3
    start_time = time.time()
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      max_tokens=100,  # You can adjust the number of tokens (words) you want in the response
      messages=conversation_history,
    )
    end_time = time.time()
    print(Fore.RED) # All prints after this in the function will be red

    # print the response time
    print(f"Response time: {end_time - start_time} seconds")
    # get number of generated tokens
    generated_tokens = response['usage']['completion_tokens']    
    print(f"Generated tokens: {generated_tokens}")
    # calculate generated tokens per second
    print(f"Generated tokens per second: {generated_tokens / (end_time - start_time)} Tks/s")

    # Extract the assistant's message from the response   
    assistant_message = response.choices[0].message['content']

    # Append the assistant's message to the conversation history
    conversation_history.append({"role": "assistant", "content": assistant_message})

      # Print the number of tokens used
    tokens_used = response['usage']['total_tokens']
    print(f"Total Tokens used: {tokens_used}")
    print(Style.RESET_ALL) # Reset the colorama style to normal White
    return assistant_message

def main():
    print("Chat with GPT-3.5! Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        
        response = chat_with_gpt3(user_input)
        
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main()