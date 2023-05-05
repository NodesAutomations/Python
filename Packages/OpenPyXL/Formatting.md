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
