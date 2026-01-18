import sys
import io
import os

def mathfunction ():
    #mathfunction1='n'
    firstNumber = int(input('Please enter first number: '))
    secondNumber = int(input('Please enter second number: '))

    while True:
        operation = input('Do you want to add (a ) or subtract(s) or both(b): ')
        if operation == 'a':
           print(f"Result: {firstNumber + secondNumber}")
           break
        elif operation == 's':
            print(f"Result: {firstNumber - secondNumber}")
            break
        elif operation == 'b':
            print(f"Result Add: {firstNumber + secondNumber}")
            print(f"Result Add: {firstNumber - secondNumber}")
            break
        else:
            print('Invalid Selection. Please enter y or n only')


mathfunction ()





