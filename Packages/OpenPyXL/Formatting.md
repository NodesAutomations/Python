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
