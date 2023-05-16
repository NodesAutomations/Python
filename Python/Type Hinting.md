### Reference
- https://www.youtube.com/watch?v=QORvB-_mbZ0
- https://www.youtube.com/watch?v=9gNnhNxra3E

### Type Hinting for any variable declaration
basic variables
```python
value1: int
value2: float
value3: bool
value4: str
```
list
```python
data1:list[int]
data2:list[float]
data3:list[str]
data4:list[list[int]]
```
Dictionary
```python
data1:dict[int,str]
data2:dict[int,bool]
```
### Type Hinting with function
```python
def add_num(num1: int, num2: int) -> int:
    return num1+num2
sum = add_num(1, 2)
```
