import unittest
class ArrayStack:
    def __init__(self):
        self._data = []

    def stack_empty(self): # Function for checking if stack is empty
        return len(self._data) == 0

    def push(self, e):
        try:
            self._data.append(e)
            if not isinstance(e, int):
                raise TypeError('TypeError: Stack only take integers')
        except TypeError:
            if not isinstance(e, int):
                print('Please Enter an integer to add.')
                integer = int(input())
                self.push(integer)

    def pop(self):
        try:
            return self._data.pop()

        except IndexError:
           if self.stack_empty():
            print('IndexError: Stack is Empty')
            print('Please Enter an integer to add.')
            integer = int(input())
            self.push(integer)

    def top(self):
        try:
            return self._data[0]
            print('The top is :', self._data[0])

        except IndexError:
            if self.stack_empty():
                print('IndexError: Stack is Empty')
                print('Please Enter an integer to add.')
                integer = int(input())
                self.push(integer)


