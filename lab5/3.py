#Write a Python program to find sequences of lowercase letters joined with a underscore.

import re

pattern = re.compile(r"[a-z]+_[a-z]+")
print(pattern.findall("apple_golden_"))
'''
ans 
if a is lowercase['apple_golden']
if A is uppercase ['pple_golden']
'''