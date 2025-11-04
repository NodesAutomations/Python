---
title: List
parent: Code
---
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
list to store unlimited inputs from user
```python
names=[]
while True:
    print("Enter New Name")
    name=input()
    if name=="":
        break
    names=names + [name]
print("Names Are:")
for name in names:
    print(name)
```
### Using List of multiple types
```python
a=["way of kings",1,bool]
print(a)
```

### List with multiple Index
```python
#multy Index List
names=[["Kaledin","Dalenar"],["Navani","Yashnah"]]
print(names[0])
print(names[0][1])
```
```python
data = [
    [0, 12, 6],
    [57, 69, 68],
    [19, 21, -1],
    [1, 18, 19],
    [16, 9, 10],
    [-1, -1, -1]
]

for i in range(len(data)):
    for j in range(len(data[0])):
        print(data[i][j])

print()
```
### using  list as 2D array for custom class
```python
from node import Node

n1 = Node(1, 0, 0, 0)
n2 = Node(2, 10, 0, 0)
n3 = Node(3, 20, 0, 0)

n4 = Node(4, 0, 10, 0)
n5 = Node(5, 10, 10, 0)
n6 = Node(6, 20, 10, 0)

n7 = Node(7, 0, 20, 0)
n8 = Node(8, 10, 20, 0)
n9 = Node(9, 20, 20, 0)

nodesRow1 = []
nodesRow1.append(n1)
nodesRow1.append(n2)
nodesRow1.append(n3)

nodesRow2 = []
nodesRow2.append(n4)
nodesRow2.append(n5)
nodesRow2.append(n6)

nodesRow3 = []
nodesRow3.append(n7)
nodesRow3.append(n8)
nodesRow3.append(n9)

nodes = []
nodes.append(nodesRow1)
nodes.append(nodesRow2)
nodes.append(nodesRow3)

for i, rowNodes in enumerate(nodes):
    for j, node in enumerate(rowNodes):
        print(i, j, node)

print("")
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
