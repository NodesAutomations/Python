### Python Installation
- Install latest version of python from python.org
- Install python with installer, make sure to check "Add Python x.x.x to PATH" 
- Adding this will help you to run python from command line
- you can check out this python path go to settings>system>About>Advance System settings>Advance Tab> environmental variables

### Check Python installation
- Open command Prompt and type `python` to start python script
- you should able to see your python version in next line
- Now Just type `print("Hello")`
- This will print hello world to next line
- congratulation you just manage to run your hello world on python
- This is also call python  REPL (Read-Eval-Print Loop), allows you to run Python code interactively
- use can use `exit()` to come out of REPL mode
- You can use `python --version` to check out your python version without starting python Execution
- To run specific python script you can use following command
```
python "c:/Users/Ryzen2600x/source/repos/Python/Sample Code/Test.py"
```
- You can also run python interactively using IDLE, just search for IDLE after installation, you can create new script from IDLE and Run that script by pressing `F5`


### Visual Studio Code setup for python
- you can install visual studio Code from it's website
- Just proceed with it's installer, during selection options make sure to check all checkboxes, this is require for `Open with Code` option in windows context menu
- After visual studio code installation you can install python extension for visual studio code, this will let us run and debug python directly from visual studio code plus provide syntax highlight and intellisense for python functions
- Also Install mypy for type annotation check Refer : https://github.com/NodesAutomations/Python/blob/master/Docs/Static%20Type%20checking%20with%20Mypy.md
- To setup startup script in visual studio code edit `launch.json` file in `.vscode` folder, set variable  `"program": "Python\\StartUp.py"` 

### Visual Studio setup for python
- From Visual studio installer make sure to check for python development 
- Proceed with installation, it will allow you to create new python application from visual studio create new project window
- You can choose Python Application for basic python project, this will automatically create simple python file that you can directly run inside visual studio with all functionality
