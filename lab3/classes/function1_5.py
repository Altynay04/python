from itertools import permutations
def print_permutations():
    s = input("String : ")
    perms = permutations(s) 
    
    print("All permutations : ")
    for perm in perms:
        print(''.join(perm))
print_permutations()
'''
String : hello
All permutations : 
hello
helol
hello
helol
heoll
heoll
hlelo
hleol
hlleo
hlloe
hloel
hlole
hlelo
hleol
hlleo
hlloe
hloel
hlole
hoell
hoell
holel
holle
holel
holle
ehllo
ehlol
ehllo
ehlol
eholl
eholl
elhlo
elhol
ellho
elloh
elohl
elolh
elhlo
elhol
ellho
elloh
elohl
elolh
eohll
eohll
eolhl
eollh
eolhl
eollh
lhelo
lheol
lhleo
lhloe
lhoel
lhole
lehlo
lehol
lelho
leloh
leohl
leolh
llheo
llhoe
lleho
lleoh
llohe
lloeh
lohel
lohle
loehl
loelh
lolhe
loleh
lhelo
lheol
lhleo
lhloe
lhoel
lhole
lehlo
lehol
lelho
leloh
leohl
leolh
llheo
llhoe
lleho
lleoh
llohe
lloeh
lohel
lohle
loehl
loelh
lolhe
loleh
ohell
ohell
ohlel
ohlle
ohlel
ohlle
oehll
oehll
oelhl
oellh
oelhl
oellh
olhel
olhle
olehl
olelh
ollhe
olleh
olhel
olhle
olehl
olelh
ollhe
olleh
'''