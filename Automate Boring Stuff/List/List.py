from unicodedata import name

# regular List
names=["vivek","Deven","Dhruv","Yogesh"]
#positive index go from left to right start with 0
print(names[1])
#negative index go from right to left start with -1
print(names[-1]) 
#slices in list aka list range
#list range include value from starting index and one less than end index
print(names[1:3])
print(names[1:-1])
print(names[2:]) # Leving blank index will just use index to end of list

#multy Index List
names=[["Kaledin","Dalenar"],["Navani","Yashnah"]]
print(names[0])
print(names[0][1])