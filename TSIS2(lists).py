"""
List items are ordered, changeable, and allow duplicate values.
List items are indexed, the first item has index [0], the second item has index [1] etc.

""" 
#examples
'''
thislist = ["apple", "banan", "cherry"]
print (thislist)
'''

'''
thislist = ["apple", "banana", "cherry"]
print = (len(thislist))
'''

'''

Result Size: 726 x 585
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#ans: <class 'list'>
'''
'''
thislist = list(("apple", "banana", "cherry")) 
print(thislist)
#ans: ["apple", "banana", "cherry"]
'''

'''
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#ans: here is printed value by its index. banana
'''

'''
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#ans: here is printed value by its inverse or just negative index. cherry
'''

'''
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#ans: here is printed value that starts at index 2 (included) and end at index 5 (not included).
'''

'''
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
'''
 
'''
 #insert()
 thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
#ans:['apple', 'banana', 'watermelon', 'cherry']
 '''

'''
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#ans ['apple', 'banana', 'cherry', 'orange']
'''

'''
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#ans ['apple', 'orange', 'banana', 'cherry']
'''

'''
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#ans:['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']
'''

'''
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) 
#ans ['apple', 'banana', 'cherry', 'kiwi', 'orange']
'''

'''
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#ans ['apple', 'cherry']
'''


'''
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#ans ['apple', 'banana']
'''

'''
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#ans ['apple', 'cherry']
'''

'''
thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) 
#ans there will be an error because "thislist" was deleted.
'''

'''
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
ans ['banana', 'cherry']
'''

'''
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#ans []
'''

'''
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  """
ans  apple
     banana
     cherry
     """
'''

'''
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
"""
ans apple
    banana
    cherry
"""
'''

'''
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist)
  print(thislist[1])
  i = i + 1 
  """
  ans apple
      banana
      cherry
"""
'''

'''
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
"""
ans apple
    banana
    cherry
'''

'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
 if "a" in x:
   newlist.append(x)
print (newlist)
#ans ['apple', 'banana', 'mango']
'''

'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
ans ['apple', 'banana', 'mango']
'''

'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)
#ans ["banana", "cherry", "kiwi", "mango"]
'''

'''
newlist = [x for x in range(10)]
print(newlist)
#ans [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)
#ans ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']
'''

'''
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#ans [23, 50, 65, 82, 100]
'''

'''
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#ans [100, 82, 65, 50, 23]
'''

'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#ans ['Kiwi', 'Orange', 'banana', 'cherry']
'''

'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#ans ['banana', 'cherry', 'Kiwi', 'Orange']
'''

'''
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#ans ['apple', 'banana', 'cherry']
'''

'''
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#ans ['apple', 'banana', 'cherry']
'''

'''
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
#ans ['a', 'b', 'c', 1, 2, 3]
'''

'''
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#ans ['a', 'b', 'c', 1, 2, 3]
'''

'''
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
#ans ['a', 'b', 'c', 1, 2, 3]
'''

#Exercises 
'''
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
'''

'''
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
'''

'''
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
'''
'''
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
'''

'''

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
'''

'''
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
'''

'''
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
'''

'''
fruits = ["apple", "banana", "cherry"]
print(len(fruits))
'''