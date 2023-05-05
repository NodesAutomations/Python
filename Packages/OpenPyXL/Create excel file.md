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
