import os
from openai import OpenAI

key ="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"

messages = []


client = OpenAI(
    # This is the default and can be omitted
    api_key=key,
)

messages = []  # Add this at the top, after imports

def completion(message):
    global messages
    messages.append(
        {
            "role": "user",
            "content": message,
        }
    )
    chat_completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    # Get the assistant's reply
    message = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }
    messages.append(message)
    print(f"Jarvis: {message['content']}")

if __name__ == "__main__":
    print(f"Jarvis: Hi I am Jarvis, How may I help you today?")
    while True:
        user_question = input()
        print((f"User: {user_question}"))
        completion(user_question)