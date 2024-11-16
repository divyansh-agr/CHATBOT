#CHATBOT 

def chatbot_response(user_input):
    
    if "hii" in user_input or "hello" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a program, but thanks for asking! How about you?"
    elif "help" in user_input:
        return "Sure! What do you need help with?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

#main function
def main():
    print("")
    print("Welcome to the chatbot! Type 'bye' to exit.")
    print("")
    print("please type all your messages in lowercase")
    print("")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Chatbot:", response)
        
        if "bye" in user_input:
            break

if __name__ == "__main__":
    main()