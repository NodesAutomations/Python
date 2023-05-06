### Sample code to create new excel file
```python
import xlwings as xw

# Get workbook
wb = xw.Book()

# Get first worksheet
ws=wb.sheets[0]

# Write data to this sheet
ws["A1"].value="Hey this string  is comming from python"

#Save workbook
wb.save("output.xlsx")
```
