import os

def removeFile(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    else:
        print("The file does not exist")

# Excution
removeFile('fileremove.txt')