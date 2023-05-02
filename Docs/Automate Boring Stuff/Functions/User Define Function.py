# Regular Function
def Hello():
    print("Hey, I'm vivek from Nodes Automations.")

# Function with input parameter
def SayHello(name):
    print("Hey, I'm " + name + " from Nodes Automations.")
 
# Function with return value
def CalculateSquare(number):
    return number*number

# Function with Error Handling
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(0))