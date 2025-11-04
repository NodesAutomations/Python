---
title: Type Check
nav_order: 6
---

### What is it?
- python is dynamic typed language so we can't always specify our variable time at compile time. python decide variable type at runtime.
- but newer version of python has feature call `type hints`
- refer : https://docs.python.org/3/library/typing.html
- using type hints we can specify our variable types at compile time, this won't affect our python code but this will help a lot for documentation, code autocomplete and find out type error at compile time
- so to help with our type checking python has separate library called `mypy` 
- refer : https://pypi.org/project/mypy/

### how to install and use
- `pip install mypy`
- use `mypy pythonfile.py` command to run type check using command prompt
- with visual studio you can automatically run it live, open command tool and type `python linter` this will allow you to set mypy as python linter
- after doing that you will be able to see problems related to types in vs code problem tab
