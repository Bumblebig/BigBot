import pandas as pd
import textwrap
import re
import google.generativeai as genai
from IPython.display import Markdown


# read data from Excel
data = pd.read_excel("BigBotData.xlsx")

# extract user input and bot responses
responses = {}
for idx, row in data.iterrows():
    user_input = row['user_input'].lower()
    bot_response = row['bot_response']
    responses[user_input] = bot_response

# Initializing Gemini
genai.configure(api_key="API_KEY")
model = genai.GenerativeModel('gemini-pro')

# Format bot response
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# generate bot response using Gemini
def generate_bot_response(user_input):
    response = model.generate_content(user_input)
    return to_markdown(response.text)

# Remove unwanted charcters
def format_text(text):
    pattern = r'[>*]'
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text

# Initialize the chat bot
print("BigBot: Hi! I'm your chatbot. Type 'exit' to quit")
while True:
    user_input = input("You: ").lower()
    
    if user_input == "exit":
        print("BigBot: Goodbye!")
        break
    
    if user_input in responses:
        print("BigBot:", responses[user_input])
    else:
        bot_response = generate_bot_response(user_input)
        print(f"BigBot:{format_text(bot_response.data)}")
