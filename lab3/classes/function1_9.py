import math

def volumeOfSphere(radius):
    return (4/3) * math.pi * pow(radius, 3)

radius = int(input())
Volume = volumeOfSphere(radius)
print(Volume)
'''
ans 
1
4.1887902047863905
'''