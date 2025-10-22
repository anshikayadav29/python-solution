# Simple AI Chatbot using Python
import random

responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm good, thanks for asking!", "Doing great! What about you?"],
    "name": ["I'm your AI assistant.", "You can call me ChatBot."],
    "bye": ["Goodbye!", "See you later!", "Take care!"]
}

def chatbot():
    print("🤖 ChatBot: Hi! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'bye':
            print("🤖 ChatBot:", random.choice(responses["bye"]))
            break
        elif user_input in responses:
            print("🤖 ChatBot:", random.choice(responses[user_input]))
        else:
            print("🤖 ChatBot: Sorry, I didn’t understand that.")

chatbot()
