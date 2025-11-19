# Import the logging module to enable logging of health check status
import logging

# Configure logging to write to both a file (app.log) and the console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()]
)

def main():
    try:
        # Try to import critical modules to check if they are available and error-free
        import choice_processor
        import combat
        # Log and print a success message if imports succeed
        logging.info("Health check passed: All modules imported successfully.")
        print("Health check passed.")
    except Exception as e:
        # Log and print an error message if any import fails
        logging.error(f"Health check failed: {e}")
        print("Health check failed.")
        # Exit with a non-zero status code to indicate failure (important for CI)
        import sys
        sys.exit(1)

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()