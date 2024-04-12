# Telegram WeatherBot

## Overview
This project is a Telegram bot that provides weather forecasts for cities and offers additional features such as generating playlist links based on weather conditions, sharing interesting weather facts, telling weather-related jokes, and engaging in conversation using AI-powered responses.

## Setup Instructions
1. Obtain API tokens:
   - Telegram Bot API token: Message the BotFather on Telegram to create a new bot and obtain its API token.
   - OpenWeatherMap API key: Register on [OpenWeatherMap](https://openweathermap.org/api) to get an API key for accessing weather data.
   - OpenRouter AI API key: Sign up on [OpenRouter AI](https://openrouter.ai/) to get an API key for generating AI-powered responses.
     
## Running Instructions
   **Add API Tokens:**
   - Created a `config.py` file in  project directory and add the three API key in that file for safety purpose only not to show in hard code.
   - Add  API tokens as follows in config.py file:
     ```python
     TOKEN = 'your_telegram_bot_token'
     OPENWEATHERMAP_API_KEY = 'your_openweathermap_api_key'
     OPENROUTER_AI_API_KEY = 'your_openrouter_ai_api_key'
   - Created a `telebot.py` file in my project directory and write code in that file and run in vscode 
**Run the Bot:**
   - Open a terminal.
   - Navigate to the project directory.
   - Run the Python script `telebot.py`:
     
## Usage
- Start the bot by sending the `/start` command to it on Telegram.
- Use the `/weather` command followed by the name of a city to get its weather forecast.
- Enjoy additional features such as song playlist recommendations, weather facts, jokes, and AI-powered conversations.

## Documentation
- This project utilizes various APIs and Python programming for bot development. 
- Chat transcripts with ChatGPT are used to enhance the conversational aspect of the bot.
-Here's the [link](https://chat.openai.com/share/6819c6a9-8ba5-4e2b-b3ae-9535c44445a2) to the chat transcripts with ChatGPT.


## Credits
- This project was developed by [Rishu Kuamr].
- Special thanks to the creators of Telegram Bot API, OpenWeatherMap, OpenRouter AI, and ChatGPT.


