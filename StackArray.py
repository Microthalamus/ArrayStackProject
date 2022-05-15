
class ArrayStack:
    def __init__(self):
        self._data = []
    def __len__(self):
        return len(self._data)
    def stack_empty(self): # Function for checking if stack is empty
        return len(self._data) == 0
    def push(self, e):
        self._data.append(e)