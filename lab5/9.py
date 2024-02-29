#Write a Python program to insert spaces between words starting with capital letters.

import re

text = "HelloMyNameIsAlseitAndIamAStudentOfKbtu"
words = re.findall(r'[A-Z][^A-Z]*', text)
spaced = ' '.join(words)
print(spaced)