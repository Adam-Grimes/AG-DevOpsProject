import logging

# Configure logging 
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()]
)

# Function to process user's choice ('x' or 'y')
def process_choice(choice: str) -> str:
    """Process the user's choice (x or y) and return a corresponding message."""
    # Make input lowercase (handles 'X' or 'Y')
    cleaned_choice = choice.lower()
    logging.info(f"Processing choice: {choice}")

    # Check the choice
    if cleaned_choice == "x":
        logging.info("User chose x")
        return "You chose x"
    elif cleaned_choice == "y":
        logging.info("User chose y")
        return "You chose y"
    else:
        logging.warning(f"Invalid choice entered: {choice}")
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