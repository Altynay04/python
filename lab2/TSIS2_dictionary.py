#Examples

'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
'''

'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#ans ford
'''

'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#ans Result Size: 659 x 518
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
#ans {'brand': 'Ford', 'model': 'Mustang', 'year': 2020
'''

'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)
#ans Mustang
'''

'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)
#ans will return a list of the keys in dictionary -- dict_keys(['brand', 'model', 'year'])
'''

'''
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change
#ans dict_keys(['brand', 'model', 'year'])
dict_keys(['brand', 'model', 'year', 'color'])
'''

'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
#ans {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}
'''

'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
#ans {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
'''

'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
#ans{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
'''

'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)
#ans {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
'''

'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
#ans {'brand': 'Ford', 'year': 1964}
'''

'''
thisdict = {
"brand" : "Ford",
"model" : "Mustang",
"year" : 1964
}
thisdict.popitem()
print(thisdict)
#ans {'brand': 'Ford', 'model': 'Mustang'}
'''

'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
#ans {'brand': 'Ford', 'year': 1964}. And it also can delete dictionary completly
'''

'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
#ans {}
'''

'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
"""ans brand
       model
       year """
'''

'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])
"""Ans
Ford
Mustang
1964
Printed all key names"""
'''

'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(thisdict[x])
"""
Ford
Mustang
1964
Printed all values in the dictionary"""
'''

'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)
"""ans
Ford
Mustang
1964"""
'''

'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)
"""ans
brand
model
year"""
'''

'''
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
"""ans
brand Ford
model Mustang
year 1964"""
'''

'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
#ans {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
'''

'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
#ans {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
'''

'''
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
#ans {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
'''

'''
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
#ans {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
'''

'''
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])
#Tobias
'''

#Exercises

'''
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
#ans mustang 
'''

'''

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

'''

'''
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
'''

'''
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

'''

'''
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
'''