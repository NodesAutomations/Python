Link : [Python Full Tutorial for Beginners - Learn Python Programming in 17 Hours - YouTube](https://www.youtube.com/watch?v=sCOw5y1RQpY)

# Intro

- python is interpreter language which is different from c# complier language
- in compiler language you can’t run program until you solve all errors
- in interpreter language execution happen line by line so even if you have some errors in your program all the lines about errors will gets executed, program will stop when he finds error
- Python also has dynamic semantics which mean data types of each objects are decided on runtime
- This is also different from regular programming language like C# where we decide data type of objects in advance

# Downloads

- [Welcome to Python.org](https://www.python.org/)
- [PyCharm: the Python IDE for Professional Developers by JetBrains](https://www.jetbrains.com/pycharm/)

# Run Python

- We can write python script in notepad file and directly run inside command prompt
    
    ```jsx
    python filePath.py
    ```
    
- We Can User python IDLE which
- We can use Third party IDE like Pycharm to Run and Debut python script

# Commands

## Comments

- Use Can use # to Start Comments

## Print

```python
# Print Normal String
print("HelloWorld")

# Print Using Variables
print(10+10)
```

## Variables

```python
# Basic Variables
a=10
b=5
c=a*2

print(a+b)
print(c)

c="Hello"
print(c)

# You can Start variable name with underscore
_a=10
# but not with any other character This will give errors
@a=10 
```

```python
15
20
Hello
```

## Strings functions

### concatenate

```python
a="Hello"
b="World"
print(a+" "+b)
```

```python
Hello World
```

```python
 a="Hello"
b="World"
print(a,b)
c=30
# This will return error due to difference in datatype
print(a+c)
```

## Operators

### Arithmetic Operators

```python
#Exponent
print(5**2) ## will return 25

#Floor Division
print(10//3) ## will return 3
```

### Assignment Operator

```python
a=10
a+=5
print(a)#prints 15
a-=5
print(a)#prints 10
```

### Comparison Operator

```python
print(a==b)
print(a!=b)
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
```

```python
False
True
True
True
False
False
```

### Logical Operators

```python
a=10
b=5

print(a>5 and b>0)
print(a>5 or b>0)
```

```python
True
True
```

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

# Data Type

## Immutable Data Type

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

```python
10
Hello
4.4
```

## Mutable Data Type

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

### Lenght

```python
l=[10,20,30,40]
print(l)

print(len(l))
```

```python
[10, 20, 30, 40]
4
```

### Delete

```python
l=[10,20,30,40]
print(l)

del l[1]
print(l)
```

```python
[10, 20, 30, 40]
[10, 30, 40]
```

### Pop

Same as delete but also return deleted value

```python
l=[10,20,30,40]
print(l)

print(l.pop(1))
print(l)
```

```python
[10, 20, 30, 40]
20
[10, 30, 40]
```

### Remove

```python
l=[10,20,30,40]
print(l)

l.remove(30)
print(l)
```

```python
[10, 20, 30, 40]
[10, 20, 40]
```

### Clear

```python
l=[10,20,30,40]
print(l)

l.clear()
print(l)
```

```python
[10, 20, 30, 40]
[]
```

### Insert

```python
l=[10,20,30,40]
print(l)

l.insert(0,100)
print(l)
```

```python
[10, 20, 30, 40]
[100, 10, 20, 30, 40]
```

### Append

```python
l=[10,20,30,40]
print(l)

l.append(100)
print(l)
```

```python
[10, 20, 30, 40]
[10, 20, 30, 40, 100]
```

### Extend

```python
l=[10,20,30,40]
print(l)

l.extend([50,60])
print(l)
```

```python
[10, 20, 30, 40]
[10, 20, 30, 40, 50, 60]
```

## List Comprehension

```python
l=[]
for i in range(1,101):
     l.append(i)

print(l)

l=[i for i in range(1,101)]

print(l)
```

```python
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
```

# Getting Inputs

## Input Function

```python
a=input("Enter The Value=")
print("Value:",a)
```

```python
Enter The Value=10
Value: 10
```

```python
a=input("Enter The Value1=")
b=input("Enter The Value2=")
print(a+b)
```

```python
Enter The Value1=10
Enter The Value2=20
1020
```

### Type Casing

```python
a=int(input("Enter The Value1="))
b=int(input("Enter The Value2="))
print(a+b)
```

```python
Enter The Value1=10
Enter The Value2=20
30
```

# Conditional Statements

```python
a=2
if a>5:
    print("A is greater than 5")

if a<5:
    print("A is Less than 5")
```

```python
A is Less than 5
```

```python
a=10
if a>5:
    print("A is greater than 5")
else:
    print("A is Less than 5")
```

# Loops

## For Loop

```python
for n in range(1,11,1):
    print(n)
```

```python
1
2
3
4
5
6
7
8
9
10
```

## While Loop

```python
i=1
while i<=10:
    print(i)
    i=i+1
```

```python
1
2
3
4
5
6
7
8
9
10
```

# String

## Indexing

```python
a="Hello"
print(a[1])
print(a[-1])
```

```python
e
o
```

```python
a="Hello Nodes Automations"
print(a[0:5])
print(a[6:12])
```

```python
Hello
Nodes
```

```python
a="Hello Nodes Automations"
print(a[0:5])
print(a[6:12])
print(a[-1:-11:-1])
print(a[-11:-1])
print(a[-11:])
```

```python
Hello
Nodes
snoitamotu
Automation
Automations
```

## Formatting

```python
a="Hello"
b="Nodes Automations"
print("{0},{1}".format(a,b))
print("{},{}".format(a,b))
```

```python
Hello,Nodes Automations
Hello,Nodes Automations
```

[https://youtu.be/sCOw5y1RQpY?t=20610](https://youtu.be/sCOw5y1RQpY?t=20610)
