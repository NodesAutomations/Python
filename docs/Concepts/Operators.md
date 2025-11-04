---
title: Operators
---

### Basic operators
- Arithmetic operators : `+`,`-`,`*`,`/`
- Assignment operators : `=`,`+=`,`-=`
- Comparison operators : `==`,`>`,`<`,`>=`,`<=`,`!=`
- Logical operators : `and`,`or`,`not`


### Membership Operator

```python
a="Hello"
print('H' in a)# Retrun True
print('h' in a)# Retrun False
```

```python
a=[10,20,30]
print(50 in a)#return False
print(20 in a)#return True
print(40 not in a)#return True
```

### Identity Operator

```python
a=10
b=10
c=5
print(a is b)#Returns True
print(a is c)#Returns False
print(a is not c)#Returns True
```

### Bitwise Operator

```python
a=True
b=False

#AND
print(a&b)#Returns False
#OR
print(a|b)#Returns True
#XOR
print(a^b)#Returns True
```