---
title: Variables
---
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

### Immutable Data Type

- Immutable Object can’t change it’s state
- types
    - int
    - float
    - complex
    - string
    - tuple set

### Tuple

```python
a=(10,"Hello",4.4)
print(a[0])
print(a[1])
print(a[2])
```

### Mutable Data Type

- Mutable Object Can Change its state
- Types
    - List
    - Dictionary
    - byte array

### List

```python
a=[10,"Hello",4.4]
print(a[0])
print(a[1])
print(a[2])
```

```python
10
Hello
4.4
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

