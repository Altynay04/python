n = int(input())
list_num =[]
for i in range (0, n):
    k = input()
    k = int(k)
    list_num.append(k)
    i = i+1
sum = 0
for i in list_num:
    sum = sum+i
print (sum)
#input:  3 
# output :4
# 5
# 6
# 15