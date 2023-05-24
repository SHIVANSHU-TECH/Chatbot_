import nltk
import requests
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

# Preprocess user input
def preprocess_input(user_input):
    stop_words = set(stopwords.words("english"))
    tokens = word_tokenize(user_input.lower())
    tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
    preprocessed_input = " ".join(tokens)
    return preprocessed_input

# Get weather information from an external API
def get_weather():
    response = requests.get("https://api.weather.com/...")
    # Process the API response and extract relevant weather information
    weather_info = process_response(response)
    return weather_info

# Placeholder function to process API response
def process_response(response):
    # Implement your logic here to extract weather information from the response
    # Return the extracted information as a string
    return "Today's weather is sunny and warm."

# Define pattern-response pairs
pattern_responses = [
    (re.compile(r"my name is (?P<name>.+)", re.IGNORECASE), ["Hello {name}! How can I assist you today?"]),
    (re.compile(r"hi", re.IGNORECASE), ["Hello!", "Hey there!", "Hi! How can I help you?"]),
    (re.compile(r"what is your name", re.IGNORECASE), ["You can call me ChatBot. How can I assist you?"]),
    (re.compile(r"tell me a joke", re.IGNORECASE), ["Sure! Why don't scientists trust atoms? Because they make up everything!"]),
    (re.compile(r"what is the weather today", re.IGNORECASE), ["Today's weather is sunny and warm."]),
    (re.compile(r"bye", re.IGNORECASE), ["Goodbye! Have a great day!", "Bye! Take care."]),
    # Add more pattern-response pairs as needed
]

# Create a list of (pattern, response) tuples
#pairs = [(nltk.re.compile(pattern, nltk.re.IGNORECASE), response) for pattern, response in pattern_responses]
# Create a Chat instance
#chatbot = Chat(pairs, reflections)

#start the converstaion loop
print("Welcome! How can I assist you today?")
while True:
    user_input = input("> ")
    if user_input.lower() == "quit":
        break
    
    matched_response = None
    for pattern, response in pattern_responses:
        match = pattern.search(user_input)
        if match:
            groups = match.groupdict()
            if "{name}" in response:
                response = [r.format(**groups) for r in response]
            if callable(response):
                matched_response = response()
            else:
                matched_response = response
            break
    
    if matched_response:
        if callable(matched_response):
            print(matched_response())
        else:
            print(matched_response)
    else:
        print("I'm sorry, I didn't understand. Can you please rephrase your query?")

    

    
    
    
