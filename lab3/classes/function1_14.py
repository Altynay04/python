def isPalindrom(word):
    reversed_word = word[::-1]
    if(reversed_word == word):
        print("is palindrom")
    else:
        print("is not palindrom")

mystring = input()
isPalindrom(mystring)