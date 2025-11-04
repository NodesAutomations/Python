---
title: Decorator
parent: Code
---
## Function Decorator
- it's method to modify behavior of existing functions
- also make sure that passing funciton argument matches with decorator functions

### Sample Code
```python
def greet(fx):
    def mfx():
        print("Good Morning.")
        fx()
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello")

hello()
```
```
Good Morning.
Hello
Thanks for using this function
```
