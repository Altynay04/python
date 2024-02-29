#Write a python program to convert snake case string to camel case string.

import re

def snakeToCamel(text):
    words = text.split('_')
    CamelString= words[0]
    for char in words[1:]:
        CamelString += char.capitalize()
    return CamelString

text = "the_snake_case_string"
print(snakeToCamel(text))
'''
ans 
theSnakeCaseString
'''

    