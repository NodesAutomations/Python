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
