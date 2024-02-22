# 2. Write a Python program to print yesterday, today, tomorrow.
import datetime

today = datetime.datetime.now()
sb = datetime.timedelta(days=1)

yesterday = today - sb
tomorrow = today + sb
To = today.strftime("%Y/%m/%d")
Yes = yesterday.strftime("%Y/%m/%d")
T = tomorrow.strftime("%Y/%m/%d")
print (To)
print(Yes)
print (T)
'''
ans: 
2024/02/22
2024/02/21
2024/02/23
'''