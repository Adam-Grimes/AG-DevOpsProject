# Import the 'unittest' module, which is Python's built-in testing framework
import unittest
# Import the function we want to test from its file (assumed to be 'choice_processor.py')
from choice_processor import process_choice

# Create a test class that inherits from 'unittest.TestCase'
# This class will hold all our tests for the 'process_choice' function
class TestChoiceProcessor(unittest.TestCase):

    # Define a test method. It MUST start with 'test_' to be run
    def test_chose_lowercase_x(self):
        """Test the case where the input is lowercase 'x'."""
        # 'self.assertEqual' is an assertion that checks if two values are equal
        # We check if calling process_choice("x") returns "You chose x"
        self.assertEqual(process_choice("x"), "You chose x")

    # Define another test for the uppercase 'X' case
    def test_chose_uppercase_x(self):
        """Test the case where the input is uppercase 'X'."""
        # This tests if the function correctly handles uppercase input
        self.assertEqual(process_choice("X"), "You chose x")

    # Test for the lowercase 'y' case
    def test_chose_lowercase_y(self):
        """Test the case where the input is lowercase 'y'."""
        self.assertEqual(process_choice("y"), "You chose y")

    # Test for the uppercase 'Y' case
    def test_chose_uppercase_y(self):
        """Test the case where the input is uppercase 'Y'."""
        self.assertEqual(process_choice("Y"), "You chose y")

    # Test for invalid inputs
    def test_invalid_choice(self):
        """Test the case where the input is neither 'x' nor 'y'."""
        # Check if input "z" returns the error message
        self.assertEqual(process_choice("z"), "You didn't enter a correct letter (x/y)")
        # Check if a longer string "hello" also returns the error message
        self.assertEqual(process_choice("hello"), "You didn't enter a correct letter (x/y)")

# This standard 'if' block allows the test file to be run directly
# by executing 'python your_test_file_name.py' in the terminal
if __name__ == '__main__':
    # This command discovers and runs all the tests in this file
    unittest.main()