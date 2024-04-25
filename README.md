# SIMPLE CHATBOT
This is a simple CLI chatbot built using python and Gemini AI integration. To use:
- Clone this repository
`git clone https://github.com/Bumblebig/BigBot`
- Navigate into directory
`cd BigBot`
- Install the required libraries and packages
- Pandas
`pip install pandas`
- Google GenerativeAI
`pip install google-generativeai`

## Gemini API KEY
To get Gemini API key:
- Head on to [Aistudio](https://aistudio.google.com/app/apikey)
- Click "create API"
- Now input your api key into the configuration line
`genai.configure(api_key="YOUR_GENERATED_API_KEY")`

### Chatbot
The chatbot contains some predetermined data. However, if prompt is not a part of the data, it initialises the AI
