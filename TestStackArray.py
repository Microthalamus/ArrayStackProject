# Imported modules and files
import unittest
from StackArray import ArrayStack

s = ArrayStack

class MyTestCase(unittest.TestCase):

    def test_onlyInteger(self):
        # Test to determine if an input that is not an integer throws an exception
        with self.assertRaises(TypeError):
            s.push()

    def test_emptyStack(self):
        # Test to determine if stack is empty
        self.assertTrue(s.stack_empty())

    def test_popOnEmpty(self):
        # Test to determine if IndexError is thrown if array is empty and pop is selected
        with self.assertRaises(IndexError):
            s.pop()

    def test_peekOnEmpty(self):
        # Test to determine if IndexError is thrown if array is empty and peek is selected
        with self.assertRaises(IndexError):
           s.top()


if __name__ == '__main__':
    unittest.main()
