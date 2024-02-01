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

'''