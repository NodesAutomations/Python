
path="C:\\Users\\Ryzen2600x\\source\\repos\\Python\\NewFolder\\Test.txt"

#Open file in Read Mode,"r" is optional argument
testfile=open(path,"r")

#Read The Contents of Files
# Read Method of File object returns String
# print(testfile.read())

# ReadLines Method of File object returns list
lines=testfile.readlines()
print(lines[0])
