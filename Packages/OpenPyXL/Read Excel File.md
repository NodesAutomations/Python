### Load Excel file to read
```python
import openpyxl

# Load Excel file
wb=openpyxl.load_workbook("Sample.xlsx")
```
### Get Access to specific sheet
```python
# Print All sheet names
print(wb.sheetnames)

# Print Sheet 1 Data
ws=wb["Sheet1"]
print(ws)
```

### Get Access to specific cell
```python
# Print Sheet 1 Data
ws=wb["Sheet1"]
print(ws)

# Print value of cell using cell Address
print(ws["A1"].value)
print(ws["B1"].value)
```
### Read specific Range
```python
import openpyxl

# Get workbook
wb=openpyxl.load_workbook("Sample.xlsx")

# Get worksheet
ws=wb["Sheet1"]

# Print Data
range=ws["A1:B5"]
for cell1,cell2 in range:
    print(cell1.value,cell2.value)
```
