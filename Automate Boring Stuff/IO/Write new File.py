StaadFilePath="C:\\Users\\Ryzen2600x\\source\\repos\\Python\\NewFolder\\Model.std"

# So Here we are opening new staad file for writing
# if file didn't exist then python will create new file for us
# If file already Exist then write mode overwrite exiting file
stdFile=open(StaadFilePath,"w")
stdFile.write("Hey, This is my first file creation using python.\n");
stdFile.close()

# Now ReOpen file to add new line using append mode
stdFile=open(StaadFilePath,"a")
stdFile.write("I am really good at this\n");
stdFile.close()

# Print file to console
stdFile=open(StaadFilePath)
contents=stdFile.read()
print(contents)
