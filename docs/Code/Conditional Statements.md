---
title: Conditional Statements
parent: Code
---
### If else
```python
a=0
if (a==0):
    print("a is 0")
elif(a>0):
    print("a is greater than 0")
else:
    print("a is less then 0")
```
### Match Case 
```python
# Get the input value from the user
value = int(input("Enter a value: "))

# Use match case to check the value
match value:
    case 0:
        print("The value is zero.")
    case _ if value > 0:
        print("The value is positive.")
    case _:
        print("The value is negative.")
```
