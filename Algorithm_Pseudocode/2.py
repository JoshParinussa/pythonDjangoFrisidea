
def countFileCapitalLetters(filename):
    with open(filename) as countletter:
        count = 0
        text = countletter.read()
        for character in text:
            if character.isupper():
                count += 1
    print(count)

# Excution
countFileCapitalLetters('file_text.txt')