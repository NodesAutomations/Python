### Sample Code to create new excel file
```python
from openpyxl import Workbook

wb=Workbook()
wb.create_sheet("Test")

ws=wb["Test"]

for i in range(1,11):
    ws.cell(i,1).value=i
    ws.cell(i,2).value="=A"+str(i)+ "*2"

wb.save(filename="output.xlsx")
```

### Sample code to add new sheet to exising one
```python
import openpyxl

# Load Excel file
wb=openpyxl.load_workbook("Sample.xlsx")

# Write new sheet
wb.create_sheet("Test")

# Save workbook, you can overwrite existing file if you want to
wb.save("New File.xlsx")
```
```python
# Write new sheet with Specific Position, 0=first sheet
wb.create_sheet("Test",0)
```
### Overwrite specific Cell
```python
# Overwrite data in existing sheet
ws=wb["Sheet1"]
ws["A1"].value="Test"
ws.cell(1,2).value="cool book names"
```

### Cell formatting
```python
import openpyxl
from openpyxl.styles import Font,Color

wb=openpyxl.load_workbook("Sample.xlsx")
ws=wb["Sheet1"]

# Font style
style=Font("Daytona",size=14,color="DC143C",underline="single",strikethrough=True)

for i in range(2,10):
    ws.cell(i,2).font=style

wb.save("Sample.xlsx")
```
### number type
```python
import openpyxl
from openpyxl.styles import numbers

wb=openpyxl.load_workbook("Sample.xlsx")
ws=wb["Sheet1"]

# pattern
ws.cell(2,1).number_format=numbers.FORMAT_CURRENCY_USD
```
### Background color
```python
import openpyxl
from openpyxl.styles import PatternFill

wb=openpyxl.load_workbook("Sample.xlsx")
ws=wb["Sheet1"]

# pattern
pattern=PatternFill(patternType="solid",fgColor="c64747")

ws.cell(1,2).fill=pattern
wb.save("Sample.xlsx")
```
