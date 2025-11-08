# Import the 'unittest' module, Python's built-in testing library
import unittest
# Import the 'calculate_damage' function from the 'combat.py' file
from combat import calculate_damage # Imports the new function

# Define a new test class that inherits from 'unittest.TestCase'
class TestDamageCalculator(unittest.TestCase):

    # A test case for standard damage calculation
    def test_standard_damage(self):
        """Test case where attack is clearly greater than defense."""
        # Expected: 10 Attack - 5 Defense = 5 Damage
        # Assert that the function's result (5) is equal to the expected value (5)
        self.assertEqual(calculate_damage(10, 5), 5)
        
    # A test case to check the minimum damage rule (floor of 1)
    def test_minimum_damage(self):
        """Test case where defense is much higher, ensuring damage is capped at 1."""
        # Expected: 5 Attack - 10 Defense = -5, should be 1
        # Assert that the function returns 1, not -5
        self.assertEqual(calculate_damage(5, 10), 1)

    # A test case for the edge case where stats are equal
    def test_equal_stats(self):
        """Test the edge case where attack equals defense."""
        # Expected: 10 Attack - 10 Defense = 0, should be 1
        # Assert that the function returns 1, not 0
        self.assertEqual(calculate_damage(10, 10), 1)
        
    # A test case for a simple high-damage calculation
    def test_high_damage(self):
        """Test a higher damage output to verify calculation accuracy."""
        # Expected: 50 Attack - 15 Defense = 35 Damage
        self.assertEqual(calculate_damage(50, 15), 35)

# This block allows the script to be run directly to start the tests
if __name__ == '__main__':
    # unittest.main() finds and runs all 'test_' methods in this file
    unittest.main()