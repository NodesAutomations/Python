# Function with Error Handling
from logging import exception


def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(0))


# Code to Raise and Catch Exception in program
def printNumbers(number):
    if number==0 :
        raise Exception("Zero Not allowed")
    else :
        print(number)

try:
    print(printNumbers(0))
except Exception as err:
    print("Something went Wrong :" + str(err))
