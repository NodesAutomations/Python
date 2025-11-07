### For Loop
```python
numbers=[1,2,3]
for number in numbers:
    print(number)
```

### for loop using Range
```python
# Print number 0-9
for i in range(10):
    print(i)

# print number 1-10
for i in range(1,11):
    print(i)

# print number 2,4,6,8,10
for i in range(2,11,2):
    print(i)
```
### Loop with  enumerate
```python
names = ["Vivek", "Deven", "Dhruv"]

for index, name in enumerate(names):
    print(index, names)
```
### For loop with else
- else statement executed after all iterations are completed successfully
- if for loop is interupted with break then else won't get executed
- same concept with while loop
```python
for i in range(11):
    print(i)

else:
    print("Sorry no i")
```
### while Loop
```python
i=0
while i<10:
    print(i)
    i=i+1
```
### while loop with else
```python
i=0
while i<10:
    print(i)
    i=i+1
else:
    print("Loop ended")
```
