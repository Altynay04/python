n = int(input())
b = int(input())
c = int(input())
if n==b & b==c & c==n:
    print("Equireterial")
elif n==b or b==c or c==n:
    print("Isoceles")
else:
    print("Versatible")