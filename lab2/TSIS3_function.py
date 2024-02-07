"""
In python a function is defined using the def keyword 
"""

#Examples 

'''
def my_function():
  print ("Hello from a function!")
#ans Hello from a function!
'''

'''
def mu_function (fname):
  print (nfame + "Refsnes")
my_function ("Emil")
my_function ("Tobias")
my_function ("Linus")
"""
ans Emil Refsnes
    Tobias Refsnes
    Linus Refsnes
"""
'''

'''
def funct(fname, lname):
  print (fname + " " + lname)
funct("Emil", "Refsnes")
#ans Emil Refsnes
'''

'''
def funct(*kids):
  print ("The youngest child is + kids[2]")
funct("Emil", "Tobias", "Linus")
#ans The youngest child is Linus 
'''

'''
def funct(child1, child2, child3):
  print ("The youngest child is + child3")
funct(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
#nas The youngest child is Linus
'''

'''
def funct(**kid):
  print ("HIs name is" + kid[lname])
funct(fname = "Tobias", lname = "Refsnes")
'''

'''
def funct(country= "Norway"):
  print("I an from" + country)
funct ("Sweden")
funct ("India")
funct ()
funct ("Brazil)
"""ans
I am from Sweden
I am from India
I am from Norway
I am from Brazil """
'''

'''
def funct(food):
 for in x in food:
   print (x)
fruits = ["apple", "banana", "cherry"]
funct (fruits)
"""ans 
apple
banana
cherry
'''

'''
def funct(x):
  return *5
print (fuct(3))
print (fuct(5))
print (fuct(10))
"""ans
15
25
50"""
'''

'''
def funct():
  pass
#ans will be error without pass statement, because the function is empty 
'''

"""
for functions that can have only positional arguments, or only have keyword arguments
"""
'''
def funct(x, /):
  print (x)
funct(3)
#ans 3
  '''

'''
def funct(x):
  print (x)
funct(x = 3)
#ans 3
'''

'''
def funct (x, /):
  print (x)
fucnt(x = 3)
#ans there will be error, because there should be only "x,/" or "x = 3" 
'''

"""
for functions than can have only reyword arguments
"""

'''
def funct(*, x):
  print (x)
funct(x = 3)
#ans 3
'''

'''
def funct(x)
  print (x)
funct(x)
#ans 3
'''

'''
def funct (*, x)
  print (3)
#ans there will be mistake 
'''
