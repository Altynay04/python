# 4. Write a Python program to calculate two date difference in seconds
 
from datetime import datetime
date1 = datetime(2024, 2, 13, 12, 0, 0)  # Example date 1
date2 = datetime(2024, 2, 12, 12, 0, 0)  # Example date 2

difference_in_seconds = abs((date1 - date2).total_seconds())
print(difference_in_seconds)
#ans 86400.0