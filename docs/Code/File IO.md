---
title: File IO
parent: Code
---

### Read Text file
```python
file=open("input.txt","r")
data=file.read()
print(data)

# ReadLines Method of File object returns list
lines=file.readlines()
print(lines[0])
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
### Sample code for staad file
```python
staadFilePath="C:\\Users\\Ryzen2600x\\source\\repos\\Python\\NewFolder\\Model.std"

# So Here we are opening new staad file for writing
# if file didn't exist then python will create new file for us
# If file already Exist then write mode overwrite exiting file
stdFile=open(StaadFilePath,"w")
stdFile.write("Hey, This is my first file creation using python.\n");
stdFile.close()

# Now ReOpen file to add new line using append mode
stdFile=open(StaadFilePath,"a")
stdFile.write("I am really good at this\n");
stdFile.close()

# Print file to console
stdFile=open(StaadFilePath)
contents=stdFile.read()
print(contents)
```