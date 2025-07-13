import google.generativeai as genai
import os

# Configure the API key
# It's recommended to set your API key as an environment variable for security
# For example, in your terminal: export GEMINI_API_KEY="YOUR_API_KEY"
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create a generative model instance
model = genai.GenerativeModel('gemini-2.0-flash') # Or other available models like 'gemini-pro' [1]

# Start a chat session
chat = model.start_chat(history=[])

print("Welcome to the Gemini Chatbot! Type 'exit' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    response = chat.send_message(user_input)
    print(f"Gemini: {response.text}")