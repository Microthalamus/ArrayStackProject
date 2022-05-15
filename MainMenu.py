# Imported modules for python
import sys
import os

# Imported StackArray Class
from StackArray import ArrayStack

menu_options = {}
s = ArrayStack()

# Main Menu Options

def main_menu():
    os.system('cls')
    print('Current Stack: ', s._data)
    print('Please choose from the following: ')
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Quit')
    choice = int(input())

main_menu()