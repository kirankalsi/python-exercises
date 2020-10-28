#import pdb
#pdb.set_trace()

item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
    for i in item_list:
        print(item_list[n])
        n += 1

print(item_list[0])

'''
Bugged Code:

item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
    for i in item_list:
        print(item_list[i])

print item_list[5]
'''