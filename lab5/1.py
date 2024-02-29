#Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.
import re

def pattern(str):
    p = r'ab*' # for searching a pattern, "a, ab, abbb ..., " 
    # here ab* means that after 'a' there must be 0 or more 'b'
    if re.match(p, str):
        return True
    else:
        return False

str = str(input())
print(pattern(str))
'''
ans: 
ab
True
or
b
False
'''