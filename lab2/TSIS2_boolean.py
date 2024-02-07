"""
The bool() function allows you to evaluate any value, and give you True or False

Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones.
"""

#Examples with True statement:

'''
print(10>9)
print(10==9)
print(10<9) 
#ans: True; False; False
'''

'''
print (bool("Hello"))
print (bool(15))
#ans: True; True
'''

'''
x = "Hello"
y = 15
print (bool(x))
print (bool(y))
#ans: True; True
'''

'''
print (bool("abs"))
print (bool(123))
print (bool(["apple", "orange", "banan"]))
#ans: True; True; True
'''

"""
There are not many values that evaluate to False, except empty values, such as (), [], {}, "", the number 0, and 
the value None. And of course the value False evaluates to False
"""

#Examples with False statement:

'''
print (bool(False))
print (bool(None))
print (bool(0))
print (bool(()))
print (bool([]))
print (bool({}))
#ans: False; False; False; False; False; False
'''

'''
class myclass():
    def __len__(self):
        return 0
myobj = myclass()
print (bool(myobj))    
#ans: FaLse
'''

"""
Functions can Return a Boolean
You can create functions that returns a Boolean Value.
"""

'''
def myFunction():
    return True
print (myFunction())
#ans: True
'''

'''
#Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction():
    return True
if myFunction():
    print ("YES")
else:
    print ("NO")
#ans: YES
'''

"""
Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to
determine if an object is of a certain data type

Check if an object is an integer or not:
"""

'''
x = 200
print (isinstance(x, int))
#ans: True
'''
#Exercise
'''
#Ex The statement below would print a Boolean value, which one?
print (10>9)
#ans: True
'''

'''
#Ex The statement below would print a Boolean value, which one?
print (10==9)
#ans: False
'''

'''
#Ex The statement below would print a Boolean value, which one?
print (10<9)
#ans: False
'''

'''
#Ex The statement below would print a Boolean value, which one?
print (bool("abs"))
'''

'''
#Ex the statement below would print a Boolean value, which one?
print (bool(0))
#ans: False
'''