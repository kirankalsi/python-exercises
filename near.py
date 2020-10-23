def near(str1, str2):
    for i in range(len(str1)):
        newstr1 = str1[:i] + str1[i+1:]
        if newstr1 == str2:
            return True
    return False

print(near("reset", "rest"))
print(near("dragoon", "dragon"))
print(near("eave", "leave"))
print(near("sleet", "lets"))