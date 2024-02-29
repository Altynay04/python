#Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re

text = "This apple, is. golden"
replacedText = re.sub(r'[ ,.]', ':', text)
print(replacedText)
'''
ans
This:apple::is::golden
'''