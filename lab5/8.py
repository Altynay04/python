#Write a Python program to split a string at uppercase letters.
import re

text = "TheAppleIsGolden"

words = re.findall(r'[A-Z][^A-Z]*', text)
print(words)
'''
['The', 'Apple', 'Is', 'Golden']
'''