n = int(input())
b = int(input())
if n>b:
    for i in range(n, b-1, -1):
        if i%2==1:
            print(i)