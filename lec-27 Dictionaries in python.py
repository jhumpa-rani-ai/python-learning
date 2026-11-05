#  dictionaris is used for mapping of any types.

info ={'name':'karan','age':19,'eligible':True}
print(info)
print(info.keys())
print(info.values())
for key in info.keys():
    print(f"The value corresponding to the {key} is {info[key]}")

print(info.itmes())
for key,value in info.items():
    print(f"the value corresponding to the {key} is {info[key]}")