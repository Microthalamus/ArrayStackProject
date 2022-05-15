import unittest
from StackArray import ArrayStack

s = ArrayStack()

class MyTestCase(unittest.TestCase):
    def test_emptyStack(self):
        self.assertFalse(s, 0)  # Test to see if stack is empty
    def test_pushcomplete(self):
        self.assertFalse(s,0) #Test to see if stack is integer


if __name__ == '__main__':
    unittest.main()
