# Imported modules and files
import unittest
from StackArray import ArrayStack

s = ArrayStack()
def pop_error():
    raise Exception('Array is empty')

class MyTestCase(unittest.TestCase):

    def test_emptyStack(self):  # Test to see if stack is empty
        self.assertIs(s.stack_empty(),True)
    def test_pushcomplete(self):    # Test to see if stack has an integer from push
        self.assertIs(s.stack_empty(),False)
    def test_pop(self): # Test to make sure exception is thrown is for attempts to pop empty array
        with self.assertRaises(Exception) as context:
            pop_error()
        self.assertTrue('Array is empty' in context.exception)



if __name__ == '__main__':
    unittest.main()
