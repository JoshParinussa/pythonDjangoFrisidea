
def printFileContents(file_name):
    with open(file_name, 'r') as text:
        print(text.read())

# Excution
printFileContents('file_text.txt')