# CodeAlpha Internship: Task 4 - Basic Chatbot

def get_chatbot_responses():
    # Predefined replies mapped to specific user keywords as required
    return {
        "hello": "Hi there! How can I help you today?",
        "hi": "Hello! Hope you are having a great day.",
        "how are you": "I'm just a bundle of code, but I'm running perfectly! How are you?",
        "what is your name": "I am AlphaBot, your friendly neighborhood rule-based assistant.",
        "bye": "Goodbye! Have a wonderful day ahead!",
        "goodbye": "See you later! Take care.",
        "help": "I can chat with you! Try saying 'hello', 'how are you', or 'what is your name'."
    }

def main():
    responses = get_chatbot_responses()
    
    print("="*50)
    print("   WELCOME TO ALPHABOT (Rule-Based Chatbot)   ")
    print("   Type 'bye' or 'goodbye' to exit the chat.  ")
    print("="*50)
    
    while True:
        # Get input from user, remove extra spaces, and convert to lowercase
        user_input = input("\nYou: ").strip().lower()
        
        # Check if the user wants to exit
        if user_input in ["bye", "goodbye"]:
            print(f"AlphaBot: {responses[user_input]}")
            print("="*50)
            print("Chat session ended.")
            break
            
        # Check if the exact input matches our dictionary keys
        if user_input in responses:
            print(f"AlphaBot: {responses[user_input]}")
        else:
            # Smart fallback mechanism if the keyword isn't recognized
            print("AlphaBot: I'm sorry, I don't quite understand that. Type 'help' to see what I can do!")

if __name__ == "__main__":
    main()
