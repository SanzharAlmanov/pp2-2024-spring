def san(a):
    for item in range(1, a+1):
        yield item**2

n = int(input("Enter a number: "))
squares = san(n)
print(" ,".join(map(str, squares)))