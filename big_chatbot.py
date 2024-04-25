import pandas as pd
import openai

# OpenAI API key
openai.api_key = "key"

# read data from Excel
data = pd.read_excel("BigBotData.xlsx")

# extract user input and bot responses
responses = {}
for idx, row in data.iterrows():
    user_input = row['user_input'].lower()
    bot_response = row['bot_response']
    responses[user_input] = bot_response

# generate bot response using GPT-3

def generate_bot_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return response.choices[0].message.content.strip()

# Initialize the chat bot
print("BigBot: Hi! I'm your chatbot")
while True:
    user_input = input("You: ").lower()
    
    if user_input == "exit":
        print("BigBot: Goodbye!")
        break
    
    if user_input in responses:
        print("BigBot:", responses[user_input])
    else:
        bot_response = generate_bot_response(user_input)
        print("BigBot:", bot_response)

