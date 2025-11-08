### Tkinter tutorial
- https://www.youtube.com/watch?v=mop6g-c5HEY

### Simple Message box to show info, warning, error
```python
from tkinter import messagebox

messagebox.showinfo(title="Info", message="Hey this is info message")
messagebox.showwarning(title="Warning", message="Hey this is warning message")
messagebox.showerror(title="Error", message="Hey this is error message")
```
### Simple Message box to get feedback from user
```python
import tkinter as tk
from tkinter import messagebox

# this will retun yes/no as string
result = messagebox.askquestion("askquestion", "Are you sure?")
print(result)

# this will retun True/Falue as bool
result = messagebox.askokcancel("askokcancel", "Want to continue?")
print(result)

# this will retun True/Falue as bool
result = messagebox.askyesno("askyesno", "Find the value?")
print(result)

# this will retun True/Falue as bool
result = messagebox.askretrycancel("askretrycancel", "Try again?")
print(result)
```

### Simple Window with message
```python
import tkinter

# Create new window
# nothing will happen when you run this code
# we need somethign to keep our window running
window = tkinter.Tk()

# Code for GUI
window.title("Results")
window.minsize(width=500, height=150)

label = tkinter.Label(
    text="Hey, you've successfully completed this test", font=("Arial", 12, "bold"))
label.pack(side="left")
label.pack(anchor="nw")

# this is require to keep window running
window.mainloop()
```
### UI with button
```python
import tkinter as tk


def SayHello():
    print("Hellow")


# Create new window
# nothing will happen when you run this code
# we need somethign to keep our window running
window = tk.Tk()

# Code for GUI
window.title("Results")
window.minsize(width=500, height=70)

label = tk.Label(text="Hey, you've successfully completed this test")
label.pack(side="left")
label.pack(anchor="nw")
label.pack(padx=10, pady=10)

ok_button = tk.Button(window, text="OK", command=SayHello)
ok_button.pack(side="bottom")
ok_button.pack(anchor="se")
ok_button.pack(padx=10, pady=10)


# this is require to keep window running
window.mainloop()
```

### Script
```python
import json
import requests # pip install requests
from tkinter import *

def get_fun_fact():
    url ="https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
    response = requests.request("GET", url)
    data = json.loads(response.text)
    useless_fact = data['text']
    print(useless_fact)
    lbl.configure(text=useless_fact)

window=Tk()
window.title("Fun Fact Generator")
window.geometry("800x80")

btn=Button(window,text="Click Me",command=get_fun_fact)
btn.pack()

lbl=Label(window,text="Click the button to get random fact")
lbl.pack()

window.mainloop()
```
