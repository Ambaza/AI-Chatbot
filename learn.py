import config

def learn_output(user_input: str) -> str:
    # Replace this with the actual implementation for learning based on user_input
    # This is just a placeholder
    return f"Learning from: {user_input}"

def main():
    while True:
        user_input = input("Enter the information you want me to learn: ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        response = learn_output(user_input)
        print(response)

if __name__ == "__main__":
    main()
