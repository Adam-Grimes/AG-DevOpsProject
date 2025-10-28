import unittest
# The core testing framework built into Python



from combat import calculate_damage 

class TestDamageCalculator(unittest.TestCase):
    # This class groups all the tests for the calculate_damage function.

    def test_standard_damage(self):
        """Test case where attack is clearly greater than defense."""
        # This confirms the basic subtraction works correctly.
        # Expected: 10 Attack - 5 Defense = 5 Damage
        self.assertEqual(calculate_damage(10, 5), 5)
        
    def test_minimum_damage(self):
        """Test case where defense is much higher, ensuring damage is capped at 1."""
        # This confirms the core game rule: damage cannot be 0 or negative.
        # Expected: 5 Attack - 10 Defense = -5, should be 1
        self.assertEqual(calculate_damage(5, 10), 1)

    def test_equal_stats(self):
        """Test the edge case where attack equals defense."""
        # This confirms the minimum damage rule applies even when the result is exactly zero.
        # Expected: 10 Attack - 10 Defense = 0, should be 1
        self.assertEqual(calculate_damage(10, 10), 1)
        
    def test_high_damage(self):
        """Test a higher damage output to verify calculation accuracy."""
        # This confirms accuracy for larger numbers.
        # Expected: 50 Attack - 15 Defense = 35 Damage
        self.assertEqual(calculate_damage(50, 15), 35)

if __name__ == '__main__':
    # This block allows you to run this specific test file directly from the command line,
    # though it will also be run automatically by the run_tests.py test suite.
    unittest.main()