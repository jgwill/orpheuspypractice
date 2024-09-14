import unittest
from io import StringIO
import sys
from orpheuspypractice import say_hello

class TestSayHello(unittest.TestCase):
  def test_say_hello(self):
    # Redirect stdout to capture print statements
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Call the function
    say_hello()
    
    # Reset redirect.
    sys.stdout = sys.__stdout__
    
    # Check if the output is as expected
    self.assertEqual(captured_output.getvalue().strip(), "Hello, World!")

if __name__ == '__main__':
  unittest.main()