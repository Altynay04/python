# 3. Write a Python program to drop microseconds from datetime.
import datetime
time = datetime.datetime.now()
T = time.strftime("%d/%m/%Y,%H:%M:%S")
print(T)
#ans 22/02/2024,08:56:58