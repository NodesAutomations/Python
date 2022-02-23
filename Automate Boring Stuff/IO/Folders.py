import os

# Create New Folder
if not os.path.exists("C:\\Users\\Ryzen2600x\\source\\repos\\Python\\NewFolder") :
    os.makedirs("C:\\Users\\Ryzen2600x\\source\\repos\\Python\\NewFolder")
    print("New Folder Created")
else:
    print("Folder Already Exist")
