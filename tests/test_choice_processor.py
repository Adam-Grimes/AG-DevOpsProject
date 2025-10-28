import unittest
# The core testing framework built into Python


from choice_processor import process_choice

class TestChoiceProcessor(unittest.TestCase):
    # This class inherits from unittest.TestCase, which provides all the 
    # assertion methods (like self.assertEqual).

    def test_chose_lowercase_x(self):
        """Test the case where the input is lowercase 'x'."""
        # Assert the function output for the 'x' input is correct.
        self.assertEqual(process_choice("x"), "You chose x")

    def test_chose_uppercase_x(self):
        """Test the case where the input is uppercase 'X'."""
        # This confirms the case-insensitivity works for 'X'.
        self.assertEqual(process_choice("X"), "You chose x")

    def test_chose_lowercase_y(self):
        """Test the case where the input is lowercase 'y'."""
        self.assertEqual(process_choice("y"), "You chose y")

    def test_chose_uppercase_y(self):
        """Test the case where the input is uppercase 'Y'."""
        # This confirms the case-insensitivity works for 'Y'.
        self.assertEqual(process_choice("Y"), "You chose y")

    def test_invalid_choice(self):
        """Test the case where the input is neither 'x' nor 'y'."""
        # Test a single letter that is not 'x' or 'y'.
        self.assertEqual(process_choice("z"), "You didn't enter a correct letter (x/y)")
        # Test a longer, invalid string.
        self.assertEqual(process_choice("hello"), "You didn't enter a correct letter (x/y)")

if __name__ == '__main__':
    # This block executes the tests only when this file is run directly (e.g., via the test suite runner).
    unittest.main()