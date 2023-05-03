### Simple Error handling
```python
user_input=input("Enter a number :")
try:
    user_input=int(user_input)
except :
    print("Invalid input")
```

### Error Handling with specific exception
```python
user_input=input("Enter a number :")
try:
    user_input=int(user_input)
except ValueError :
    print("Invalid number")
except :
    print("Invalid input")
```