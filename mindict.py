#Minimum Value in a Dictionary
my_dict={"a":34,"c":1,"d":341,"2":23}
if not my_dict:
    print("Empty Dict")
else:
    print(min(set(my_dict.values())))
#1
