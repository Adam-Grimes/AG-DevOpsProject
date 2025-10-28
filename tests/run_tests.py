import unittest
import sys

def run_full_suite():
    """
    Automatically discovers and runs all tests in the project.
    """
    # 1. Create a TestLoader
    loader = unittest.TestLoader()
    
    # 2. Discover all tests
    # This searches the current directory ('tests') for any file 
    # that starts with 'test_' and loads all test classes inside.
    start_dir = 'tests'
    suite = loader.discover(start_dir, pattern='test_*.py')

    # 3. Create a TestRunner and execute the suite
    # verbosity=2 shows the name and result of each test method.
    runner = unittest.TextTestRunner(verbosity=2)
    print("\n--- Running Combined Test Suite ---")
    result = runner.run(suite)

    # 4. Exit with status code based on test results (Important for CI/CD)
    if not result.wasSuccessful():
        sys.exit(1) # Fail build if tests failed

if __name__ == '__main__':
    run_full_suite()