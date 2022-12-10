#Sort Lists in Ascending Order ()
my_dict={"a":[3,1,3,212,1],"b":[23,3,2,1,1,2],"c":[232,32,3,2,122,1]}
for value in my_dict.values():
    value.sort()
print(my_dict)

#{'a': [1, 1, 3, 3, 212], 'b': [1, 1, 2, 2, 3, 23], 'c': [1, 2, 3, 32, 122, 232]}
