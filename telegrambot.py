import telebot
import requests
import random
from config import TOKEN, OPENWEATHERMAP_API_KEY, OPENROUTER_AI_API_KEY

# Create a new Telebot instance
bot = telebot.TeleBot(TOKEN)


# Fetch music playlist links based on weather conditions and some facts also
def get_playlist_link_with_story(weather_description):
    story = ""  # Initialize an empty string for the story
    
    # Add a story based on the weather description
    if 'clear' in weather_description.lower():
        story = "The sun shines brightly in the sky, casting warm rays of light across the landscape. Birds chirp happily as they flit from tree to tree, and a gentle breeze rustles through the leaves. It's a perfect day to bask in the sunlight and enjoy the beauty of nature."
    elif 'rain' in weather_description.lower():
        story = "Dark clouds gather overhead, blocking out the sun's rays and casting a shadow over the world below. The pitter-patter of raindrops can be heard as they dance upon the rooftops and sidewalks. It's a cozy day to stay indoors, snuggled up with a warm blanket and a hot cup of tea, listening to the soothing sound of rain."
    elif 'snow' in weather_description.lower():
        story = "The world is transformed into a winter wonderland as delicate snowflakes drift gently from the sky, blanketing the ground in a layer of soft white powder. The air is crisp and cold, but there's a sense of magic in the air as children bundle up in their warmest clothes to build snowmen and go sledding. It's a serene and peaceful scene, perfect for enjoying the beauty of the season."
    else:
        story = "The weather is neither sunny, rainy, nor snowy, but that doesn't mean it's any less special. Every day is a new opportunity to explore, discover, and enjoy the world around us. So why not take a moment to sit back, relax, and listen to some feel-good tunes that will brighten your day, no matter what the weather may be?"

    # Get the playlist link based on the weather description
    playlist_link = get_playlist_link(weather_description)
    
    # Combine the story and playlist link
    return f"{story}\n\n{playlist_link}"

def get_playlist_link(weather_description):
    if 'clear' in weather_description.lower():
        return "🌞 Enjoy the sunny weather with this upbeat playlist: [Sunny Day Vibes](https://open.spotify.com/playlist/37i9dQZF1DX1BzILRveYHb?si=0b42c70acecd43bf)"
    elif 'rain' in weather_description.lower():
        return "☔️ It's raining outside! Cozy up with this relaxing rainy day playlist: [Rainy Day Melodies](https://open.spotify.com/album/15yoUd8TSy0W2oSYw9qRBU?si=1TTSABlNRFSiQ2qBv3Xf2Q)"
    elif 'snow' in weather_description.lower():
        return "❄️ Embrace the snowy weather with these ambient tracks: [Snowfall Serenity](https://open.spotify.com/playlist/37i9dQZF1DWXR9b9fYSEj4?si=5b9e713a63e6428f)"
    else:
        return "🎵 Here's a feel-good playlist recommendation: [Feel-Good Tunes](https://open.spotify.com/playlist/37i9dQZF1DX7xOpGPUVNE5?si=03f83f1b90324208)"



# Response gebration function from LLM ai
def generate_router_ai_response(query):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_AI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "mistralai/mistral-7b-instruct:free",
        "messages": [
            {"role": "user", "content": query}
        ]
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes
        json_response = response.json()
        return json_response['choices'][0]['message']['content']
    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors (4xx and 5xx status codes)
        return f"An HTTP error occurred: {http_err}"
    except Exception as err:
        # Handle other types of exceptions
        return f"An error occurred: {err}"

# Function to get a random weather fact
def get_random_weather_fact():
    weather_facts = [
        "Did you know that the highest temperature ever recorded on Earth was 134 degrees Fahrenheit (56.7 degrees Celsius) in Death Valley, California?",
        "The average raindrop falls at a speed of about 7 miles per hour (11 kilometers per hour).",
        "Lightning strikes the Earth about 8 million times per day.",
        "In Antarctica, the coldest temperature ever recorded was minus 128.6 degrees Fahrenheit (minus 89.2 degrees Celsius).",
        "The term 'wind chill' describes the rate at which heat is lost from exposed skin due to wind and cold temperatures.",
        "Hurricanes, typhoons, and cyclones are all names for the same weather phenomenon, known as tropical cyclones, but are called different names depending on the region where they occur.",
        "The most snowfall ever recorded in a single day occurred in Capracotta, Italy, on March 5, 2015, with 100.8 inches (256 centimeters) of snowfall."
    ]
    return random.choice(weather_facts)

# Function to craft a joke about the current weather
def craft_weather_joke(weather_description):
    weather_jokes = {
        "clear": ["Why did the sun go to school? To get a little brighter!", "Why was the math book sad? Because it had too many problems!"],
        "rain": ["What falls in winter but never gets hurt? Snow!", "Why did the umbrella break? It had too many rain drops!"],
        "snow": ["What do snowmen wear on their heads? Ice caps!", "Why did the snowman call his dog Frost? Because Frost bites!"]
    }
    return random.choice(weather_jokes.get(weather_description.lower(), ["I can't think of a joke for this weather!"]))

def interaction_initiation():
    return "Alright, I've given you a glimpse into the weather world, but there's so much more to explore! What secrets of the universe can I uncover for you today? The choice is yours! 🔮✨"


# Main command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to WeatherBot! Send me the name of a city to get its weather forecast.")

# Weather command handler
@bot.message_handler(commands=['weather'])
def get_weather(message):
    city_name = message.text.split(maxsplit=1)[1]

    # Fetch weather data from OpenWeatherMap API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={OPENWEATHERMAP_API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        # Get playlist link based on weather
        adventure_soundtrack = get_playlist_link_with_story(weather_description)
        Some_fact  = get_random_weather_fact()
        Some_joke =  craft_weather_joke(weather_description)
        interaction = interaction_initiation()
        
        # Construct bot response
        reply_text = f"Weather in {city_name}:\nDescription: {weather_description}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s\n\n{adventure_soundtrack} \n\n{Some_fact} \n\n{Some_joke} \n\n{interaction}"
    else:
        reply_text = "Sorry, I couldn't find weather data for that city."

    bot.reply_to(message, reply_text)

@bot.message_handler(func=lambda m: True)
def handle_other_queries(message):
    # Assuming the user's message is the query they want to send to the AI
    ai_response = generate_router_ai_response(message.text)
    bot.reply_to(message, ai_response)

bot.polling()
