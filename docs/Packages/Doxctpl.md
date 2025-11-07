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
### Code to insert images at placeholder
- contents in word file
```
Hello, my name is {{ name }}.
{{ placeholder_1}}
{{ placeholder_2}}
```
```python
import os,sys # standard python lib
from docxtpl import DocxTemplate, InlineImage # pip install docxtpl
from docx.shared import Cm,Inches,Mm,Emu

# Change path to current working directory
os.chdir(sys.path[0])

# Get word template
doc=DocxTemplate("Template.docx")
# Cm(5) represent length of image
placeholder1=InlineImage(doc,"Placeholders/Placeholder_1.png",Cm(5))
placeholder2=InlineImage(doc,"Placeholders/Placeholder_2.png",Cm(5))


context={"name":"Vivek",
         "placeholder_1":placeholder1,
         "placeholder_2":placeholder2,
         }

# to replace place holder image use following code
# doc.replace_pic("originalfile1.png","newfile.png")

doc.render(context)
doc.save("Report.docx")
```
