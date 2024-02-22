# 1. Write a Python program to subtract five days from current date.
import datetime

Current_date = datetime.datetime.now()
substr = datetime.timedelta(days = 5)
H = Current_date - substr 
K = H.strftime("%Y/%m/%d")
print(Current_date)# ans 2024-02-22 03:39:50.694156
print(K)
#ans 2024/02/17