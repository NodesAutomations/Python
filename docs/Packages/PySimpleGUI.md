### Sample code
```python
import PySimpleGUI as gui # pip install pysimplegui

layout=[
    [gui.Text("First Name"),gui.Input(key="First_Name")],
    [gui.Text("Last Name"),gui.Input(key="Last_Name")],
    [gui.Button("Read"),gui.Exit()]
]

form=gui.Window("My First GUI using python",layout)

while True:
    event,values=form.read()
    if event==gui.WIN_CLOSED or event=="Exit":
        break
    if event=="Read":
        print(event,values)

form.close()
```
![image](https://github.com/NodesAutomations/Python/assets/60865708/56e0b607-18c8-4d34-9de9-f7b96e2d2885)
