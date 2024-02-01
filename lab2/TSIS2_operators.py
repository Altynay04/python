"""
Python Operators
Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators

"""

'''
#Example with + operator
print (10+5)
#ans: 15
'''

#Ex for Arithmetic "+"; "-"; "*"; "/"; "% - moduls"; "** - exponentiation"; "// - floor division"
'''
x = 5
y = 3
print (x+y)
#ans: 8
''' 

'''
x = 8
y = 5
print (x - y)
#asn: 3
'''

'''
x = 5
y = 3
print (x*y)
#ans: 15
'''

'''
x = 15
y = 3
print (x/y)
#ans:5 
'''

'''
x = 5
y = 2
print(x % y)
#ans: 1
'''

'''
x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2
ans: 32
'''

'''
x = 15
y = 2
print(x // y)
#the floor division // rounds the result down to the nearest whole number
#ans: 7
'''
"""
Python Assignment Operators
"""
'''
#ex:   =	x = 5	x = 5 
x = 5
print(x)
#ans: 5
'''

'''
#ex: +=	x += 3	x = x + 3
x = 5
x += 3
print(x)
#ans: 8
'''

'''
#ex: -=	x -= 3	x = x - 3
x = 5
x -= 3
print(x)
#ans: 2
'''

'''
#ex: *=	x *= 3	x = x * 3
x = 5
x *= 3
print(x)
#ans: 15
'''

'''
#ex: /=	x /= 3	x = x / 3
x = 5
x /= 3
print(x)
#ans:1.6666666666666667
'''

'''
%=	x %= 3	x = x % 3
x = 5
x%=3
print(x)
#ans: 2
'''

'''
#ex: //=	x //= 3	x = x // 3
x = 5
x//=3
print(x)
#ans: 1
'''
'''
#ex: **=	x **= 3	x = x ** 3
x = 5
x **= 3
print(x)
##ans:125
'''

'''
#ex: &=	x &= 3	x = x & 3
x = 5
x &= 3
print(x)
#ans: 1
'''
'''
#ex: |=	x |= 3	x = x | 3
x = 5
x |= 3
print(x)
#ans:7
'''

'''
#xe: ^=	x ^= 3	x = x ^ 3
x = 5
x ^= 3
print(x)
#ans:6
'''
'''
#ex: >>=	x >>= 3	x = x >> 3
x = 5
x >>= 3
print(x)
#ans: 0
'''

'''
#ex:>=	Greater than or equal to	x >= y
x = 5
y = 3
print(x >= y)
# returns True because five is greater, or equal, to 3

'''

'''
#ex:<=	Less than or equal to	x <= y
x = 5
y = 3
print(x <= y)
# returns False because 5 is neither less than or equal to 3
#ans: Falls
'''

"""
Python Logical Operators
"""
'''
#ex: and 	Returns True if both statements are true	x < 5 and  x < 10
x = 5
print(x > 3 and x < 10)
# returns True because 5 is greater than 3 AND 5 is less than 10
#ans: 10
'''

'''
#ex:or	Returns True if one of the statements is true	x < 5 or x < 4
x = 5
print(x > 3 or x < 4)
# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)
#ans: True
'''

'''
#ex:not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
x = 5
print(not(x > 3 and x < 10))
# returns False because not is used to reverse the result
#ans: False
'''

"""
Python Identity Operators
"""

'''
#ex:is 	Returns True if both variables are the same object	x is y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content\
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
#ans:True False True
'''

'''
#ex: is not	Returns True if both variables are not the same object	x is not y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
# returns False because z is the same object as x
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content
print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y
#ans:False True False
'''

"""
Python Membership Operators
"""

'''
#ex: in 	Returns True if a sequence with the specified value is present in the object	x in y
x = ["apple", "banana"]
print("banana" in x)
# returns True because a sequence with the value "banana" is in the list
#ans:True
'''

'''
#ex: not in	Returns True if a sequence with the specified value is not present in the object	x not in y
x = ["apple", "banana"]
print("pineapple" not in x)
# returns True because a sequence with the value "pineapple" is not in the list
#ans: True
'''

"""
Python Bitwise Operators
"""

'''
#ex: & 	AND	Sets each bit to 1 if both bits are 1	x & y
print(6 & 3)



"""
The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""
#ans: 2
'''
'''
#ex:
|	OR	Sets each bit to 1 if one of two bits is 1	x | y
print(6 | 3)



"""
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""
#ans: 7
'''
'''
#ex:^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y
print(6 ^ 3)



"""
The ^ operator compares each bit and set it to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101
====================

Decimal numbers and their binary values:
0 = 0000000000000000
1 = 0000000000000001
2 = 0000000000000010
3 = 0000000000000011
4 = 0000000000000100
5 = 0000000000000101
6 = 0000000000000110
7 = 0000000000000111
"""
#ans: 5
'''

'''
#ex: ~	NOT	Inverts all the bits	~x
print(~3)



"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100

Decimal numbers and their binary values:
 4 = 0000000000000100
 3 = 0000000000000011
 2 = 0000000000000010
 1 = 0000000000000001
 0 = 0000000000000000
-1 = 1111111111111111
-2 = 1111111111111110
-3 = 1111111111111101
-4 = 1111111111111100
"""
#ans: -4
'''

'''
#ex:<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2
print(3 << 2)



"""
The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""
#ans:12
'''

'''
#ex:  >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
print(8 >> 2)



"""
The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000000000001000
becomes
 2 = 0000000000000010

Decimal numbers and their binary values:
 0 = 0000000000000000
 1 = 0000000000000001
 2 = 0000000000000010
 3 = 0000000000000011
 4 = 0000000000000100
 5 = 0000000000000101
 6 = 0000000000000110
 7 = 0000000000000111
 8 = 0000000000001000
 9 = 0000000000001001
10 = 0000000000001010
11 = 0000000000001011
12 = 0000000000001100
"""
#ans:2
'''

"""
Operator Precedence
"""
'''
#ex: Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:
print((6 + 3) - (6 + 3))
#ans: 0
'''

'''
#ex: Multiplication * has higher precedence than addition +, and therefor multiplications are evaluated before additions:
print(100 + 5 * 3)
#ans: 115
'''
#Exersizes:

'''
#1
print(10 * 5)
#ans: 50
'''

'''
#2
print(10 /2)
 #ans: 5
'''

'''
#3

fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")
'''

'''
#4:
if 5 != 10:
  print("5 and 10 is not equal")
'''

'''
#5:
if 5 == 10 or 4 == 4:
  print("At least one of the statements is true")
'''

