#Write a Python program that matches a string that has an 'a' followed by two to three 'b'.
import re

def search_pattern(string):
    p = r'ab{2,3}' #here are looking for a pattern where after 'a' comes 2 or 3 'b'
    if re.match(p, string):
        return True
    else:
        return False

string = str(input())
print(search_pattern(string))
'''
ans 
ab
False
or 
abb
True
'''