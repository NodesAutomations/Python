---
title: Packages
nav_order: 4
---

### Explore python packages
- https://anaconda.org/anaconda/repo
- https://anaconda.cloud/package-categories

### Install PIP
- use `pip --version` to check for current pip version
- use `python -m ensurepip --default-pip` to install pip
- use `python.exe -m pip install --upgrade pip` to update pip
- you can find your install python packages @`C:\Users\Ryzen2600x\AppData\Local\Programs\Python\Python311\Lib\site-packages`

### Install new Python package
- use `pip install pybrot` to install new packages, you need name of package to use this command
- Local python package Directory : `C:\Users\Ryzen2600x\AppData\Local\Programs\Python\Python311\Lib\site-packages`
- when you use any python package, you can double click on any class to explore it's code, you'll also able to see it's file location on vscode

### Uninstall python package
- use `pip uninstall pybrot` to remove any package you don't like

### Sample code to use pybrot library
- this also require numpy and matplotlib package
```python
from pybrot.Mandelbrot import Mandelbrot

m=Mandelbrot()
m.show()
```