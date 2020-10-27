#import pdb

def is_prime(x):
    #pdb.set_trace()
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
            return True

'''
Bugged Code:

def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n = 0:
                return False
            return True
'''