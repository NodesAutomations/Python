### Simple List
```python
a=["way of kings","words or radiant","Oathbringer","Rhythm of War"]
# print all items
print(a)
# print first item
print(a[0])
# change first item
a[0]="Vivek"
# print first item
print(a[0])
```

### Using List of multiple types
```python
a=["way of kings",1,bool]
print(a)
```

### Using Slicing with List 
```python
a=["way of kings","words or radiant","Oathbringer","Rhythm of War"]
# Print First two items
print(a[0:2])
# Print Last two items
print(a[-2:])
```
### List Functions
```python
a=[5,2,6,3,7]
# print numbers in ascending order
a.sort()
print(a)
# print numbers in descending order
a.reverse()
print(a)
# Add new number at end
a.append(8)
print(a)
# Add number at 3rd position
a.insert(2,4)
print(a)
# remove element from 3rd position
a.pop(2)
print(a)
# remove specific element from list
a.remove(2)
print(a)
```