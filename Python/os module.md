### Get Current working directory
```python
import os
 print(os.getcwd())
```
### Get File name , folder name
```python
path='C:\\Users\\Ryzen2600x\\source\\repos\\Python'

# Get file name
fileName=os.path.basename(path)

# Get folder name
folder=os.path.dirname(path)

# Get All Folder Content in List
files=os.listdir(path)
```

### Create new folder
```python
import os

# Create New Folder
if not os.path.exists("C:\\Users\\Ryzen2600x\\source\\repos\\Python\\NewFolder") :
    os.makedirs("C:\\Users\\Ryzen2600x\\source\\repos\\Python\\NewFolder")
    print("New Folder Created")
else:
    print("Folder Already Exist")
```