import unittest
from combat import calculate_damage # Imports the new function

class TestDamageCalculator(unittest.TestCase):

    def test_standard_damage(self):
        """Test case where attack is clearly greater than defense."""
        # Expected: 10 Attack - 5 Defense = 5 Damage
        self.assertEqual(calculate_damage(10, 5), 5)
        
    def test_minimum_damage(self):
        """Test case where defense is much higher, ensuring damage is capped at 1."""
        # Expected: 5 Attack - 10 Defense = -5, should be 1
        self.assertEqual(calculate_damage(5, 10), 1)

    def test_equal_stats(self):
        """Test the edge case where attack equals defense."""
        # Expected: 10 Attack - 10 Defense = 0, should be 1
        self.assertEqual(calculate_damage(10, 10), 1)
        
    def test_high_damage(self):
        """Test a higher damage output to verify calculation accuracy."""
        # Expected: 50 Attack - 15 Defense = 35 Damage
        self.assertEqual(calculate_damage(50, 15), 35)

if __name__ == '__main__':
    unittest.main()