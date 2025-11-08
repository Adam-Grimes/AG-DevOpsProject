# Function to process user's choice ('x' or 'y')
def process_choice(choice: str) -> str:
    
    # Make input lowercase (handles 'X' or 'Y')
    cleaned_choice = choice.lower()

    # Check the choice
    if cleaned_choice == "x":
        return "You chose x"
    elif cleaned_choice == "y":
        return "You chose y"
    else:
        # Handle wrong input
        return "You didn't enter a correct letter (x/y)"


# This block runs when the script is executed directly
if __name__ == "__main__":
    # Get user input
    user_input = input("Enter x or y: ")
    
    # Call the function with the input
    message = process_choice(user_input)
    
    # Print the result
    print(message)