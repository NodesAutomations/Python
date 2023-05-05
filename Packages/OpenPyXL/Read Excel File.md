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
    
# Print data with row and column number
range=ws.iter_rows(min_row=1,max_row=5,min_col=1,max_col=2)
for cell1,cell2 in range:
    print(cell1.value,cell2.value)
```
### Read Name Range
```python
import openpyxl

# Get workbook
wb=openpyxl.load_workbook("Sample.xlsx")
ws=wb.active

# Getting Category Range
nameRange=wb.defined_names['Category']
Sheet=list(nameRange.destinations)[0][0]
address=list(nameRange.destinations)[0][1].replace('$','')

print(Sheet,":", ws[address].value)

# Getting Author Range
nameRange=wb.defined_names['Author']
Sheet=list(nameRange.destinations)[0][0]
address=list(nameRange.destinations)[0][1].replace('$','')

print(Sheet,":", ws[address].value)
```

### Read table
```python
import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo

# Get workbook
wb=openpyxl.load_workbook("Sample.xlsx")
ws=wb.active

# Get the table object by name
table_range = ws.tables["BookTable"]
data = ws[table_range.ref]

for row in data:
    for cell in row:
        print(cell.value, end=" ")
    print()
```
