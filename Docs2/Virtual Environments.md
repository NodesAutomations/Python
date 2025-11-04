### Overview
- A virtual environment is a tool used to isolate specific Python environments on a single machine, allowing you to work on multiple projects with different dependencies and packages without conflicts. This can be especially useful when working on projects that have conflicting package versions or packages that are not compatible with each other.
- use `python -m venv myenv` to create new virtual environment
- use `myenv/Scripts/activate.bat` to active virtual environment
- use `deactivate` to deactivate virtual environment

### Crete requirement text file
- use `pip freeze>requirements.txt` to crete requirement text file
- use `pip install -r requirements.tet` to use this file to install packages on another computer
