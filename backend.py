import webbrowser
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from googletrans import Translator
import csv
import logging
from flask import send_file
from fuzzywuzzy import fuzz

app = Flask(__name__)
CORS(app)

translator = Translator()

UNSPLASH_ACCESS_KEY = "DhlUxW-wjOCy7CJ804OwdHaMjmPx6TLt9d5l9szc7U4"

def google_search(query):
    api_key = "AIzaSyBouiU08dJmI-4mBqFLMk96sD8YwwYSbYE"
    search_engine_id = "91c6eae1e875a4925"
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={search_engine_id}"
    response = requests.get(url)
    data = response.json()

    if "items" in data:
        return data["items"][0]["snippet"]
    else:
        return "I'm sorry, I couldn't find an answer."
def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": "1befac90c6e79b8eb85e2977a3bb5c61",
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        weather_report = (
            f"The current weather in {city_name} is {weather_description}. "
            f"The temperature is {temperature}°C with {humidity}% humidity "
            f"and a wind speed of {wind_speed} km/h."
        )
        return weather_report
    else:
        return "Sorry, I couldn't fetch the weather information at the moment."

# Usage example:
city_name = "Asansol"  # Replace with the desired city name
api_key = "1befac90c6e79b8eb85e2977a3bb5c61"  # Replace with your OpenWeatherMap API key

weather_report = get_weather(city_name, api_key)

def get_news_summaries(location):
    # Use the location parameter to fetch news using the NewsAPI
    api_key = '99f38cf5243e4d2197f9d006ffeddcff'
    url = f"https://newsapi.org/v2/top-headlines?country={location}&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()

    if data.get("articles"):
        news_list = [article["title"] for article in data["articles"]]
        news_summaries = ". ".join(news_list)
        return news_summaries
    else:
        return "Sorry, I couldn't fetch the news at the moment."

def solve_math_problem(query):
    try:
        result = eval(query)  # Evaluate the mathematical expression
        return f"The result of {query} is {result}"
    except Exception as e:
        return "Sorry, I couldn't solve that mathematical problem."   
def get_nasa_image_of_the_day():
    api_key = "kIErSunsaJNqBsVK3dhLh3MgrtbkH68ZathXsKPt"
    base_url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

    response = requests.get(base_url)
    data = response.json()

    if "url" in data and "explanation" in data:
        image_url = data["url"]
        explanation = data["explanation"]
        return image_url, explanation
    else:
        return None
def get_dad_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    
    response = requests.get(url, headers=headers)
    data = response.json()

    if response.status_code == 200:
        joke = data.get('joke', '')
        return joke
    else:
        return "Sorry, I couldn't fetch a dad joke at the moment." 
def get_random_dog_breed():
    base_url = "https://api.thedogapi.com/v1"
    headers = {
        "x-api-key": "live_1xeiOGbN7709B1soNc7mpqgdAysHuSgehQNZUmmA2ljla8d92hSojAZfXEqUHr7O"  # Replace with your Dog API key
    }

    response = requests.get(f"{base_url}/images/search", headers=headers, params={"mime_types": "jpg,png"})
    data = response.json()

    if response.status_code == 200 and data:
        breed_name = data[0].get("breeds", [{}])[0].get("name", "Unknown Breed")
        breed_temperament = data[0].get("breeds", [{}])[0].get("temperament", "Unknown Temperament")
        breed_description = data[0].get("breeds", [{}])[0].get("description", "No description available.")
        breed_image_url = data[0].get("url", None)
        
        return breed_name, breed_temperament, breed_description, breed_image_url
    else:
        return None, None, None, None
def get_country_info(country_name):
    api_url = f"https://restcountries.com/v2/name/{country_name}"
    
    response = requests.get(api_url)
    data = response.json()
    
    if response.status_code == 200 and data:
        country_data = data[0]
        name = country_data.get("name", "")
        population = country_data.get("population", "")
        languages = ", ".join(language["name"] for language in country_data.get("languages", []))
        currencies = ", ".join(currency["name"] for currency in country_data.get("currencies", []))
        region = country_data.get("region", "")
        subregion = country_data.get("subregion", "")
        capital = country_data.get("capital", "")
        area = country_data.get("area", "")
        timezones = country_data.get("timezones", [])
        calling_codes = country_data.get("callingCodes", [])
        
        country_info = (
            f"Country: {name}\n"
            f"Population: {population}\n"
            f"Languages: {languages}\n"
            f"Currencies: {currencies}\n"
            f"Region: {region}"
            f"Subregion: {subregion}\n"
            f"Capital: {capital}\n"
            f"Area: {area} square kilometers\n"
            f"Timezones: {', '.join(timezones)}\n"
            f"Calling Codes: {', '.join(calling_codes)}\n"
            
        )
        return country_info
    else:
        return "Sorry, I couldn't fetch information about that country."

# Modify the chatbot_response function to use the new function
def chatbot_response(user_message):
    greetings = ["hello", "hi", "hlw", "hii", "hiii", "what's up"]
    user_message_lower = user_message.lower()  # Convert user's message to lowercase
    abusive_words=["sala","bokachoda","madarchod","vosribala","son of a bitch","bitch","ass hole","fuck u","fuck you","lawra","khankir chala","gudmarani","bahenchod"]
    user_message_lower = user_message.lower()  # Convert user's message to lowercase
    
    if user_message_lower.startswith(tuple(greetings)):
        return "Hello! I am your personal assistant. How can I help you today? 😊"
    
    elif "visit" in user_message:
        words = user_message.split()
        open_index = words.index("visit") if "visit" in words else -1
        if open_index != -1 and open_index < len(words) - 1:
            website_name = words[open_index + 1]
            website_url = f"https://www.{website_name}.com/"
            webbrowser.open(website_url)
            return f"Opening {website_name.capitalize()}..."
        else:
            return "Please specify a valid website name."
    elif "terms of use" in user_message:
        return "You can find our terms of use on our website. Please visit the 'Terms of Use' section to learn more about our policies and guidelines."
            
    elif "data security" in user_message or "data protection" in user_message:
        return "We take data security seriously. Your information is stored securely and we use encryption to protect your data. We are committed to ensuring the safety of your personal information."
            
    elif "delete my data" in user_message:
        return "If you would like to request the deletion of your data, please contact our support team. We will be happy to assist you with your data removal request."
    elif "contact support" in user_message:
        return "Our support team is available to assist you. You can reach out to us through our website or contact our support email at support@example.com."
    
    elif "thank you" in user_message or "bye" in user_message or "exit" in user_message:
        return "You're welcome! If you have any more questions or need assistance in the future, feel free to ask. Goodbye!" 
    elif "news" in user_message:
        news_summaries = get_news_summaries("in")
        return news_summaries
    elif "translate" in user_message:
    # Check if the query contains "translate" and extract the text to be translated
        translate_query = user_message.split("translate", 1)[-1].strip()    
        if translate_query:
            translation = translator.translate(translate_query, src='en', dest='hi')
            return f"Translation in Hindi: {translation.text}"
        else:
            return "Please specify the text you want to translate."
    elif "solve" in user_message or "calculate" in user_message:
        math_query = user_message.replace("solve", "").replace("calculate", "").strip()
        math_result = solve_math_problem(math_query)
        return math_result
    elif "nasa" in user_message or "space" in user_message:
        a = ("Sure, I can provide you with an interesting space-related image of the day.")
        image_url, explanation = get_nasa_image_of_the_day()
        if image_url:
            b = (explanation)
            c = ("Here is the image. You can find it at the following URL:")
            return a,b,c,image_url
        else:
            return "Sorry, I couldn't fetch the NASA image of the day at the moment."
    elif "joke" in user_message:
        dad_joke = get_dad_joke()
        return dad_joke
    elif "dog" in user_message or "breed" in user_message:
        x = "Sure, let me find information about a random dog breed for you."
        breed_name, breed_temperament, breed_description, breed_image_url = get_random_dog_breed()
        if breed_name:
            p = "Here is information about a random dog breed:"
            q = f"Breed Name: {breed_name}\n"
            r = f"Temperament: {breed_temperament}\n"
            s = f"Description: {breed_description}\n"
            t = "And here is an image of the dog breed:\n"
            a = breed_image_url

            return x, p, q, r, s, t, a
        else:
            return "Sorry, I couldn't fetch information about a dog breed at the moment."
    elif "country" in user_message:
        # Extract the country name from the user's message
        country_keywords = ["country", "of"]
        country_name = None
        words = user_message.split()
        for i, word in enumerate(words):
            if word.lower() in country_keywords and i < len(words) - 1:
                country_name = words[i + 1]
                break

        if country_name:
            country_info = get_country_info(country_name)
            if country_info:
                return country_info
            else:
                return f"Sorry, I couldn't fetch information about {country_name} at the moment."
        else:
            return "Please specify the name of the country you want to learn about."   

    elif "health advice" in user_message:
        # Extract the organ for which the user wants health advice
        organ_keywords = ["brain","heart","lungs","liver","kidneys","stomach","pancreas","intestines","skin","bones","muscles","eyes","ears","reproductive organs male","reproductive organs female","spleen","gallbladder","bladder","thyroid gland","adrenal glands","pituitary gland","blood vessels","lymph nodes","prostate gland male","uterus female","ovaries female","testes male","appendix","ligaments","cartilage","nervous system","respiratory system","blood-forming organs","hypothalamus","basal ganglia","intervertebral discs","pons","dendrites","pineal gland","placenta during pregnancy","adipose tissue brown fat","bile ducts","stratum corneum","vas deferens male reproductive system","corpus luteum female reproductive system","pancreatic islets islets of langerhans","zygote during fertilization","tendons","stratum granulosum","gastrointestinal mucosa","humerus arm bone","esophagus","thymus","blood","bone marrow","joints","teeth","tongue","nails","hair follicles","blood-brain barrier","urethra","nervous system peripheral nerves","skin sebaceous glands","endocrine glands various glands producing hormones","diaphragm","erythrocytes red blood cells"]
        organ_input = None
        words = user_message.split()
        for word in words:
            if word.lower() in organ_keywords:
                organ_input = word.lower()
                break

        if organ_input:
            # Read health advice from a CSV file
            with open('health_advice_csv_path', mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                organ_advice = {row['Organ']: row['Health Advice'] for row in reader}
            
            if organ_input in organ_advice:
                return f"Here is some health advice for {organ_input.capitalize()}:\n{organ_advice[organ_input]}"
            else:
                return f"Sorry, I couldn't find health advice for {organ_input} at the moment."
        else:
            return "Please specify a specific organ for which you'd like health advice."
        
    elif "heart rate" in user_message:
        heart_rate_str = user_message.split("heart rate", 1)[-1].strip()
        if heart_rate_str.isdigit():
            heart_rate = int(heart_rate_str)
            if 60 <= heart_rate <= 100:
                return "Your heart rate is within the normal range. Keep up the good work!"
            elif heart_rate < 60:
                return "Your heart rate is lower than the normal range. Consider resting and relaxing."
            else:
                return "Your heart rate is higher than the normal range. Take deep breaths and stay calm."
        else:
            return "Sorry, I couldn't understand your heart rate. Please provide a valid number (e.g., 'heart rate 75')."
    elif user_message_lower.startswith(tuple(abusive_words)):
        return "Don't use any abusive words 🤐"
    else:
        if user_message:
            response = google_search(user_message)
            return response
        else:
            return "I didn't understand the request...."
            
@app.route('/')
def index():
    return 'Welcome to my Flask application!'


@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        user_message = request.json.get('user_message')
        chatbot_reply = chatbot_response(user_message)
        response_data = {'chatbot_response': chatbot_reply}
        if "weather" in user_message:
            # Extract the city name from the user's message
            words = user_message.split()
            city_name = None
            for i, word in enumerate(words):
                if word.lower() == "weather" and i < len(words) - 1:
                    city_name = words[i + 1]
                    break

            if city_name:
                # Get the weather information for the specified city
                api_key = "1befac90c6e79b8eb85e2977a3bb5c61"  # Replace with your OpenWeatherMap API key
                weather_report = get_weather(city_name, api_key)
                if weather_report:
                    response_data = {'chatbot_response': weather_report}
                else:
                    response_data = {'chatbot_response': "Sorry, I couldn't fetch the weather information at the moment."}
            else:
                response_data = {'chatbot_response': "Please specify the name of the city for weather information."}
            return jsonify(response_data)
        return jsonify(response_data)
    
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
