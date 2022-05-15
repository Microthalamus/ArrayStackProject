# Imported modules and files
import unittest
from StackArray import ArrayStack

s = ArrayStack()

class MyTestCase(unittest.TestCase):

    def test_emptyStack(self):
        self.assertIs(s.stack_empty(),True)  # Test to see if stack is empty
    def test_pushcomplete(self):
        self.assertIs(s.stack_empty(),False) #Test to see if stack has an integer from push



if __name__ == '__main__':
    unittest.main()
