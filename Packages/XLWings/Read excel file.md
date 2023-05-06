### Read Excel file
```python
import xlwings as xw

# Get workbook
wb = xw.Book("sample.xlsx")

# Get worksheet
sheet = wb.sheets['Sheet1']

# Get Single Cell
print("Value of A1 cell : " + sheet["A1"].value)
print("Value of A1 cell : " + sheet[0,0].value)

# Get Table/Range
rng=sheet["A1:C5"]
print(f"Number of Cells in range {rng.address} : {rng.count}")

for i in range(0,rng.rows.count):
    for j in range(0,rng.columns.count):
         print(sheet[i,j].value)
```

### Read Name Range and table range
```python
import xlwings as xw

# Get workbook
wb = xw.Book("sample.xlsx")

# Get active worksheet
sheet = wb.sheets["Inputs"]

# Get Specific Name range
print(sheet["Category"].value)
print(sheet["Author"].value)

# Get Table
rng=sheet["BookTable"]

for i in range(0,rng.rows.count):
    for j in range(0,rng.columns.count):
         print(rng[i,j].value)
```
