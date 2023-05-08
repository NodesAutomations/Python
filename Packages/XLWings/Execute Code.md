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

### To Run python script from excel
```python
Sub RunPythonScript(PythonScriptPath As String)

Dim objShell As Object
Dim PythonExePath As String
ActiveWorkbook.Save
ChDir ActiveWorkbook.path

    Set objShell = VBA.CreateObject("Wscript.Shell")
    
    PythonExePath = """C:\Users\Ryzen2600x\AppData\Local\Programs\Python\Python311\python.exe"""
 
    objShell.Run PythonExePath & PythonScriptPath
End Sub
```
