# Imported modules and files
import unittest
from StackArray import ArrayStack

s = ArrayStack

class MyTestCase(unittest.TestCase):

    def test_onlyInteger(self):
        with self.assertRaises(TypeError):
            s.push()

    def test_emptyStack(self):
        self.assertTrue(s.stack_empty())

    def test_popOnEmpty(self):
        with self.assertRaises(IndexError):
            s.pop()

    def test_peekOnEmpty(self):
        with self.assertRaises(IndexError):
           s.top()


if __name__ == '__main__':
    unittest.main()
