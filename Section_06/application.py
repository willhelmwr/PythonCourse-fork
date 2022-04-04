import os

for dirpath, dirnames, filenames in os.walk("/<YOUR DIRECTORY STRUCTURE>/myfolder"):
    # print(dirpath)
    # print(dirnames)
    # print(filenames)
    # print(" ----------------- ")
    pass

# Get basename.. that's the file at the directory location given
print(os.path.basename("/bin/tools/myfile.txt"))

# Get the directory name only, not the file
print(os.path.dirname("/bin/tools/hello/balbala/myfile.txt"))

# Will give directory name and basename in a tuple
print(os.path.split("/bin/tools/hello/balbala/myfile.txt"))

# Check if the path exists on the computer
print(os.path.exists("/bin/tools/hello/balbala/myfile.txt"))

# used to check if file exists in the specified path
os.path.isfile("/bin/tools/hello/balbala/myfile.txt")

# used to check if directory exists in the specified path
os.path.isdir("/bin/tools/hello/balbala/myfile.txt")

# Get file with path and file extension in a tuple
print(os.path.splitext("/bin/tools/hello/balbala/myfile.txt"))
