def isPrime(num):
    if(num == 1):
        return False
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
print([x for x in list if isPrime(x)])
#ans [2, 3, 5, 7, 11, 13, 17]