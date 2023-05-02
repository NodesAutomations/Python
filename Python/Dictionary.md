### Basic 
```python
# Create Dictionary
a={"1":"Way of Kings","2":"Words of Radiance","3":"Oathbringer","4":"Rhythm of War","0":{"Book":"The Stormlight Archive"}}
# Access item using key
print(a["2"])
# printing nested item
print(a["0"])
print(a["0"]["Book"])
```
### Dictionary Method
```python
a={"1":"Way of Kings","2":"Words of Radiance","3":"Oathbringer","4":"Rhythm of War"}
# Print all keys of dictionary
print(a.values())
# print all values of dictionary
print(a.items())
```