# Whenever your program stuck in infinite loop just press CTRL + C to send KeyboardInterrupt Error and Break Execution
# while True:
#     print("Hello")

while True:
    print("Who are you?")
    name=input()
    if name!="vivek":
        continue
    print("Hello vivek, Enter your password:")
    password=input()
    if password=="test":
        break
        ("Access Granted")