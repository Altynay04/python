#Examples

'''
thisset = {"apple", "banana", "cherry"}
print(thisset)
#ans 1time {'apple', 'banana', 'cherry'}
#ans 2time {'banana', 'cherry', 'apple'}
#ans 3time {'cherry', 'banana', 'apple'}
'''

'''
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
#ans {'banana', 'cherry', 'apple'}
'''

'''
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)
#ans {True, 2, 'banana', 'cherry', 'apple'} there no 1, because true and 1 are cinsidered the same value, so they are duplicates
'''

'''
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)
#ans {False, True, 'cherry', 'apple', 'banana'} there no 0, because false and 0 are cinsidered the same value, so they are duplicates
'''

'''
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#ans cherry
     apple
     banana
'''

''''
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
#ans true
'''

'''
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
#ans {'orange', 'cherry', 'apple', 'banana'}
'''

'''
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#ans{'apple', 'mango', 'cherry', 'pineapple', 'banana', 'papaya'}
'''

'''
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
#ans{'banana', 'cherry', 'apple', 'orange', 'kiwi'}
'''

'''
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#nas {"apple", "cherry"}
'''

'''
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#nas {"apple", "cherry"}
'''

'''
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
#ans {'c', 3, 'a', 'b', 1, 2}
'''

'''
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
#ans {1, 2, 'a', 'c', 3, 'b'}
'''

'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
#ans apple
'''

'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
#ans apple
'''

'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)
#ans {banana", "cherry", "google", "microsoft"}
'''

#Exercises

'''

fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!") 
'''

'''
fruits = {"apple", "banana", "cherry"}
fruit.add("orange")
'''

'''
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
friuts.update(more_fruits)
'''
'''
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
'''

'''
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
'''
