# Simple Rule-Based Chatbot in Python

def chatbot(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I am a simple AI chatbot 🤖"
    elif "ai" in user_input or "ml" in user_input:
        return "AI is Artificial Intelligence and ML is Machine Learning!"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I don’t understand that yet."

print("🤖 AI Chatbot: Type 'bye' to exit.")

while True:
    user_message = input("You: ")
    reply = chatbot(user_message)
    print("Bot:", reply)

    if "bye" in user_message.lower():
        break
