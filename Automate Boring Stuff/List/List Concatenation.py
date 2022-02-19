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