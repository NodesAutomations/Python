### Simple Error handling
- finally is optional
- finally block is always executed
```python
user_input=input("Enter a number :")
try:
    user_input=int(user_input)
except :
    print("Invalid input")
finally:
    print("end of program")
```

### Error Handling with specific exception
```python
user_input=input("Enter a number :")
try:
    user_input=int(user_input)
except ValueError :
    print("Invalid number")
except :
    print("Invalid input")
```
```python
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(0))
```

### Raise Exception
```python
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
```
