import sys
import io
import os

def mathfunction ():
    #mathfunction1='n'
    firstNumber = int(input('Please enter first number: '))
    secondNumber = int(input('Please enter second number: '))

    while True:
        operation = input('Do you want to multiply (m ) or divide(d) or both(b): ')
        if operation == 'y':
           print(f"Result: {firstNumber * secondNumber}")
           break
        elif operation == 'n':
            print(f"Result: {firstNumber / secondNumber}")
            break
        elif operation == 'b':
            print(f"Result Multiplication: {firstNumber * secondNumber}")
            print(f"Result Division: {firstNumber / secondNumber}")
            break
        else:
            print('Invalid Selection. Please enter y or n only')


mathfunction ()