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
    exec_menu(choice)

# Function for execute menu

def exec_menu(choice):
    os.system('cls')
    if choice == 1:
        print("Please Enter an Integer")
        integer = int(input())
        s.push(integer)
        main_menu()
    else:
        print('Invalid option, please try again')
        main_menu()

main_menu()