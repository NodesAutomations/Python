### Sample Code to generate word report by populating template
- Template file: `Hello, my name is {{ name }}.`
```python
import os,sys # standard python lib
from docxtpl import DocxTemplate # pip install docxtpl

# Change path to current working directory
os.chdir(sys.path[0])

# Get word template
doc=DocxTemplate("Template.docx")
context={"name":"Vivek"}

doc.render(context)
doc.save("Report.docx")
```
