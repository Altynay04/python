#Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

import re

pattern = re.compile(r'a.*b$')
print(pattern.findall("asljnln, dfodtursdiytugb, ab, luygfluyb"))
'''
ans 
['asljnln, dfodtursdiytugb, ab, luygfluyb']
'''