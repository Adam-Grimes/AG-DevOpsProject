# Import the 'unittest' framework for creating and running tests
import unittest
# Import 'sys' to control the script's exit status
import sys

# Define a function to find and run all tests
def run_full_suite():
    """
    Automatically discovers and runs all tests in the project.
    """
    # 1. Create a TestLoader
    # The TestLoader object is used to find tests
    loader = unittest.TestLoader()
    
    # 2. Discover all tests
    # 'discover' searches a directory for test files
    start_dir = '.' # Start searching in the current directory
    # Find all files matching the pattern 'test_*.py'
    suite = loader.discover(start_dir, pattern='test_*.py')

    # 3. Create a TestRunner and execute the suite
    # 'TextTestRunner' runs the tests and prints results to the console
    # verbosity=2 provides more detailed output (shows each test name)
    runner = unittest.TextTestRunner(verbosity=2)
    
    print("\n--- Running Combined Test Suite ---")
    # Run all the tests found in the 'suite'
    result = runner.run(suite)

    # 4. Exit with status code based on test results (Important for CI/CD)
    # Check if the 'run' was *not* successful (i.e., any test failed)
    if not result.wasSuccessful():
        # Exit the script with a status code of 1, indicating failure
        # This tells CI tools (like GitHub Actions) that the build failed
        sys.exit(1)

# This standard 'if' block runs only when the script is executed directly
if __name__ == '__main__':
    # Call the main function to start the test discovery and run
    run_full_suite()