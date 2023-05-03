### Read Text file
```python
file=open("input.txt","r")
data=file.read()
print(data)
file.Close()
```
### Read Text file line by line
```python
file=open("input.txt")
print(file.readline())
```
### Write Text file
```python
file=open("out.txt","w")
file.write("Hello")
file.close
```
### Add new text to existing file
```python
file=open("out.txt","a")
file.write("this is new line")
file.close
```