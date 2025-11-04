---
title: String
---
### Three ways to define strings
- single quoted strings 
```
`vivek`
``` 
- Double quoted strings 
```
"Vivek"
``` 
- Triple quoted strings  
```
```Vivek```
``` 
Benifit of this system is that you can use separate system depending on your string. If your string contain double quote then you can define string with single quote, if you string contain double and single quote both you can use triple quote.

### String Concate
```python
a="Vivek"
b="Patel"
c=a + " " + b
print(c)
```

### String Splicing
```python
a="Vivek"
b="Patel"
c=a + " " + b
print("Original String : " + c)
# Print third character from string
print("Third Character: " + c[2])
# Print First 4 character from string
print(c[0:4])
print(c[:4])
# Skip First 3 characters
print(c[3:])
# Print Last 4 character from string
print(c[-4:])
```

### String Functions
```python
a="Vivek"
b="Patel"
c=a + " " + b
print("String Length: " + str(len(c)))
print ("String Endwith : " + str(c.endswith("Patel")))
print ("String Count : " + str(c.count("e")))
print ("String Capitalize : " + c.capitalize())
print("String Find index : " + str(c.find("P")))
print("String Replace : " + c.replace("Vivek", "Bunty"))
```

### String formatting

```python
a="Hello"
b="Nodes Automations"
print("{0},{1}".format(a,b))
print("{},{}".format(a,b))
print(f"{a},{b}")
```

```python
Hello,Nodes Automations
Hello,Nodes Automations
```