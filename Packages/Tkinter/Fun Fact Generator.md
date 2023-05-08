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
