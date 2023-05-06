### Read Excel file
```python
import xlwings as xw

# Get workbook
wb = xw.Book("sample.xlsx")

# Get worksheet
sheet = wb.sheets['Sheet1']

# Get Cell/Range
print("Value of A1 cell : " + sheet["A1"].value)

rng=sheet["A1:C5"]
print(f"Number of Cells in range {rng.address} : {rng.count}")

for i in range(1,rng.rows.count+1):
    for j in range(1,rng.columns.count+1):
         print(rng[(i-1)*rng.columns.count+j-1].value)
```

### Read Name Range and table range
```python
import xlwings as xw

# Get workbook
wb = xw.Book("sample.xlsx")

# Get active worksheet
sheet = wb.sheets.active

# Get Specific Name range
print(sheet["Category"].value)
print(sheet["Author"].value)

# Get Table
rng=sheet["BookTable"]

for i in range(1,rng.rows.count+1):
    for j in range(1,rng.columns.count+1):
         print(rng[(i-1)*rng.columns.count+j-1].value)
###
