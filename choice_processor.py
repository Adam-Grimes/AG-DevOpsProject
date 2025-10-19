def process_choice(choice: str) -> str:
    
    # Convert the input to lowercase to handle 'X' and 'Y'
    cleaned_choice = choice.lower()

    if cleaned_choice == "x":
        return "You chose x"
    elif cleaned_choice == "y":
        return "You chose y"
    else:
        return "You didn't enter a correct letter (x/y)"

# The main execution block remains the same
if __name__ == "__main__":
    user_input = input("Enter x or y: ")
    message = process_choice(user_input)
    print(message)