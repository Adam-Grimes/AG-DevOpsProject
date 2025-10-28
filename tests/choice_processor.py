def process_choice(choice: str) -> str:
    """
    Processes a user's choice between 'x' and 'y', case-insensitively, 
    and returns a corresponding message.

    Args:
        choice: The string input from the user.

    Returns:
        A string message indicating the choice or an error.
    """
    
    # Convert the input to lowercase to handle 'X' and 'Y'
    cleaned_choice = choice.lower()

    # --- Core Logic ---
    if cleaned_choice == "x":
        return "You chose x"
    elif cleaned_choice == "y":
        return "You chose y"
    # --- Error Handling ---
    else:
        return "You didn't enter a correct letter (x/y)"

# This block ensures the code runs only when the file is executed directly 
# (i.e., not when imported by the unit tests).
if __name__ == "__main__":
    user_input = input("Enter x or y: ")
    message = process_choice(user_input)
    print(message)