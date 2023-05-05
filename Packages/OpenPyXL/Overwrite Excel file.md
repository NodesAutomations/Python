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
