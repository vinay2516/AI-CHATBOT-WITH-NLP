import nltk
import random
import string

# Download required NLTK data (run once)
nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Sample chatbot responses
responses = {
    "greeting": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "goodbye": ["Goodbye!", "See you later!", "Have a nice day!"],
    "thanks": ["You're welcome!", "No problem!", "Anytime!"],
    "name": ["I am a simple chatbot created using Python and NLTK."],
    "default": ["I’m not sure I understand that.", "Could you please rephrase?", "I’m still learning!"],
}

# Keywords for intent recognition
keywords = {
    "greeting": ["hello", "hi", "hey"],
    "goodbye": ["bye", "goodbye", "see you"],
    "thanks": ["thanks", "thank you"],
    "name": ["your name", "who are you"],
}


# NLP Preprocessing
def preprocess(text):
    text = text.lower()
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in string.punctuation]
    tokens = [t for t in tokens if t not in stopwords.words('english')]
    return tokens


# Intent matching
def get_intent(user_input):
    tokens = preprocess(user_input)
    for intent, keys in keywords.items():
        for word in tokens:
            if word in keys or any(key in user_input.lower() for key in keys):
                return intent
    return "default"


# Chatbot response
def chatbot_response(user_input):
    intent = get_intent(user_input)
    return random.choice(responses[intent])


# Run chatbot
def run_chatbot():
    print("Chatbot: Hello! I’m your AI assistant. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot:", random.choice(responses["goodbye"]))
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)


if __name__ == "__main__":
    run_chatbot()
