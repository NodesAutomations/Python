### Basic 
```python
# Create Dictionary
a={"1":"Way of Kings","2":"Words of Radiance","3":"Oathbringer","4":"Rhythm of War","0":{"Book":"The Stormlight Archive"}}
# Access item using key
print(a["2"])
# printing nested item
print(a["0"])
print(a["0"]["Book"])
# Add new item
items={"5":"New Book","6":"book6"}
a.update(items)
print(a)
```

### Code to loop through dictionary
```python
books = {"1": "Way of Kings", "2": "Words of Radiance",
         "3": "Oathbringer", "4": "Rhythm of War"}

# Loop through the dictionary items
for key, value in books.items():
    # Print the key and value on separate lines
    print(f"Key: {key}")
    print(f"Value: {value}")
    print()  # Add a blank line for readability
```
### Dictionary Method
```python
a = {"1": "Way of Kings", "2": "Words of Radiance",
     "3": "Oathbringer", "4": "Rhythm of War"}
# Print all keys of dictionary
print(a.keys())
# print all values of dictionary
print(a.values())
# print all items
print(a.items())
```
