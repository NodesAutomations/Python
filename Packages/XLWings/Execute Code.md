### To Run excel macro from python
```python
wb=xw.Book("Sample.xlsx")

# Macro without input
macro=wb.macro("ModuleName.SubName")
macro()

# macro with input
macroWithInput=wb.macro("ModuleName.SubName2")
macroWithInput("InputPara")
```
