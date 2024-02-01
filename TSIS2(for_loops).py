#Examples

'''
for x in "banana":
  print(x)
"""
ans 
b
a
n
a
n
a
"""
'''

'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#ans apple
    # banana
'''

'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
#ans apple
'''

'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#ans apple
    # cherry
  '''

'''
for x in range(6):
  print(x)
"""
ans 
0
1
2
3
4
5
"""
'''

'''
for x in range(2, 6):
  print(x) 
"""

for x in range(2, 6):
  print(x) 

for x in range(2, 6):
  print(x) 
"""ans 
2
3
4
5
"""
'''

'''
for x in range(2, 30, 3):
  print(x) 
"""ans 
2
5
8
11
14
17
20
23
26
29
"""
'''

'''
for x in range(6):
  print(x)
else:
  print("Finally finished!")
"""ans
0
1
2
3
4
5
Finally finished!
"""
'''

'''
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
""" ans
0
1
2
"""
'''

'''
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
"""ans
red apple
red banana
red cherry
big apple
big banana
big cherry
tasty apple
tasty banana
tasty cherry"""
'''

'''
for x in [0, 1, 2]:
  pass
#ans because empty for loop, would raise an error without the pass statement

'''

'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
'''

'''

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
'''

'''

for x in range(6):
  print(x)
'''

'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
'''