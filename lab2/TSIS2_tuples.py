#Examples

'''
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#ans <class 'typle'>
'''

'''
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#ans ('apple', 'banana', 'cherry', 'apple', 'cherry')
'''

'''
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(tuple1)
print(tuple2)
print(tuple3)
#ans ('apple', 'banana', 'cherry')
(1, 5, 7, 9, 3)
(True, False, False)
'''

'''
tuple1 = ("abc", 34, True, 40, "male")
#ans ('abc', 34, True, 40, 'male')
'''

'''
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#ans ('orange', 'kiwi', 'melon')
'''

'''
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
#ans ("apple", "kiwi", "cherry")/ since tulple is unchangeable, to change it, we firstly 
#need to convert it in list, after that change list, and again convert it back into tuple 
'''

'''
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
#ans ('apple', 'banana', 'cherry', 'orange')
'''

'''
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#ans ('banana', 'cherry')
'''

'''
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)
#ans this will raise an error because the tuple no longer exists
'''

'''
fruits = ("apple", "banana", "cherry")
print(fruits)
#ans ('apple', 'banana', 'cherry')
'''

'''
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
#ans apple
     banana
     cherry
'''

'''
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#ans apple
banana
['cherry', 'strawberry', 'raspberry']
'''

'''
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)
#ans apple
['mango', 'papaya', 'pineapple']
cherry
'''

'''
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#ans apple
     banana
     cherry
'''

'''
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
#ans apple
     banana
     cherry
'''

'''
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
#ans apple
     banana
     cherry
'''

'''
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#ans ('a', 'b', 'c', 1, 2, 3)
'''

'''
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
#ans ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
'''

#Exersices

'''
fruits = ("apple", "banana", "cherry")
print(fruits[0])
#ans apple
'''

'''
fruits = ("apple", "banana", "cherry")
print(len(fruits))
#ans 3
'''

'''
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
#ans cherry
'''

'''
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])
#ans ('cherry', 'orange', 'kiwi')
'''

