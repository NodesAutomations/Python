### Get File / Folder Path
```python
from pathlib import Path

# Get home directory
folderPath=Path.home()
print(folderPath)

# Get Current working folder path
folderPath=Path.cwd()
print(folderPath)

# Get Current Python file path
filePath=Path(__file__)
print(filePath)

# Get first parent folder path
folderPath=Path.cwd().parent
print(folderPath)

# Get nth Parent folder path
folderPath=Path.cwd().parents[2]
print(folderPath)
```

### Path manipulation
```python
from pathlib import Path

# Get Current working folder path
folderPath=Path.cwd()
print(folderPath)

# Get Current Python file path
filePath=Path(__file__)
print(filePath)

# Join path
folderPath=folderPath /"Test"
print(folderPath)

# Create directory if it does not exist
folderPath.mkdir(exist_ok=True)
# exist_ok: to ignore "FileExistsError" if the target direcotry already exist

# Check path is folder
result=folderPath.is_dir()

# Check if path is file
result=filePath.is_file()

```
### File name manipulation
```python
from pathlib import Path

# Get Current Python file path
filePath=Path(__file__)
print(filePath)

#Get file Name
fileName=filePath.name
print(fileName)

# Get file Name without extension
fileName=filePath.stem
print(fileName)
```
### Loop through files and folder
```python
from pathlib import Path

# Get Current working folder path
folderPath=Path.cwd()
print(folderPath)

# Iterate over files in directory
for file in folderPath.iterdir():
    print(file)

# Iterate over files with specific extension
for file in folderPath.iterdir():
    if file.suffix==".md":
        print(file)

# Iterate over files including files in subfolder
for file in folderPath.rglob("*"):
    print(file)
```
