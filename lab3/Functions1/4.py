def IsPrime(a):
    for x in range (a-1, 1, -1):
        if a == 1:
            return False
        elif a == 2:
            return True
        elif a % x == 0:
            return False
    return True

lis2 = []
lis = [1, 5, 3, 87, 7, 11, 6, 43, 9, 10]
for item in lis:
    if IsPrime(item):
        lis2.append(item)
print(lis2)