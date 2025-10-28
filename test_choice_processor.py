import unittest
from choice_processor import process_choice

class TestChoiceProcessor(unittest.TestCase):

    def test_chose_lowercase_x(self):
        """Test the case where the input is lowercase 'x'."""
        self.assertEqual(process_choice("x"), "You chose x")

    def test_chose_uppercase_x(self):
        """Test the case where the input is uppercase 'X'."""
        self.assertEqual(process_choice("X"), "You chose x")

    def test_chose_lowercase_y(self):
        """Test the case where the input is lowercase 'y'."""
        self.assertEqual(process_choice("y"), "You chose y")

    def test_chose_uppercase_y(self):
        """Test the case where the input is uppercase 'Y'."""
        self.assertEqual(process_choice("Y"), "You chose y")

    def test_invalid_choice(self):
        """Test the case where the input is neither 'x' nor 'y'."""
        self.assertEqual(process_choice("z"), "You didn't enter a correct letter (x/y)")
        self.assertEqual(process_choice("hello"), "You didn't enter a correct letter (x/y)")

if __name__ == '__main__':
    unittest.main()