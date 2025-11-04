---
title: Enum
---
from enum import Enum
### Sample code
```python
from enum import Enum

class Colors(Enum):
    Red = 0
    Green = 1
    Blue = 2

color1 = Colors.Red
color2 = Colors.Green
color3 = Colors.Blue

print(f"{color1},{color1.name},{color1.value}") 
# print : Colors.Red,Red,0
```
