## Function Decorator
- it's method to modify behavior of existing functions

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
