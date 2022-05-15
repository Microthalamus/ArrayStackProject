import unittest
from StackArray import ArrayStack

s = ArrayStack()

class MyTestCase(unittest.TestCase):
    def test_emptyStack(self):
        self.assertFalse(s, 0)  # Test to see if stack is empty


if __name__ == '__main__':
    unittest.main()
