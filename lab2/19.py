n = int(input())
b = int(input())
if n<b:
    for i in range (n, b+1):
        print (i)
elif n>b:
    for i in range (n, b-1, -1):
        print (i)
elif n==b:
    print(n)