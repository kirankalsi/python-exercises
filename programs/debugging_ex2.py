def product(n):
    total = 1
    for i in n:
        total *= i
    return total

print(product([4,4,5]))

'''
Bugged Code:
def product(n):
    total == 1
    for n in n:
        total *= i
return total

print(product([4,4,5]))
'''