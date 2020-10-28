def times_tables():
    tt=""
    for first_num in range(1,11):
        for second_num in range(1,11):
            num = first_num*second_num
            tt = tt + str(num) + " "
        tt = tt + "\n"
    return tt

print(times_tables())