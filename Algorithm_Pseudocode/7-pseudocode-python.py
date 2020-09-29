# PSEUDOCODE

# string = "katak"
# reverse_string = string.reverse    # reorder string from right to left
# if string == reverse_string:       # compare if original string is same with the reverse_string then it is Palindrome
#     print 'Palindrome'



# Script Python

def palindromeChecker(word):
    if word == word[::-1]:
        print("Word is Palindrome")
    else:
        print("Word is not Palindrome")

# Excution
palindromeChecker('bebek')