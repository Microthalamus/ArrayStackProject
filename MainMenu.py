# Imported modules for python
import sys
import os

menu_options = {}

# Main Menu Options

def main_menu():
    os.system('cls')
    print('Please choose from the following: ')
    print('1. Push')
    print('2. Pop')
    print('3. Peek')
    print('4. Quit')
    choice = int(input())