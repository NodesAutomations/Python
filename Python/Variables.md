### Basic Variable types syntax
- python automatically detect our variable type depending on value assigned
- Also variable names are case sensitive so `a` and `A` is considered as two separate variables

```python
# string
a = "Vivek"
# integer
b = 105
# float
c = 10.23
# boolen
d=True
# null
e=None

# printing variables
print(a)
print(b)
print(c)
print(d)
print(e)

# printing variable types
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
```

### Type Casting
- Type casting is method to check for type of input
- so in below code id you assign `a="vivek"` then it will throw run time error 
- we can use `int()`,`str()`,`float()`,`bool()` for this
```python
# string
a="100"
print(type(a))

# typecast string as integer
b=int(a)
print(type(b))
```