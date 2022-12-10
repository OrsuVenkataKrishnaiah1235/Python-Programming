#Make a Dictionary from Nested Lists
l=[["a",1],["b",2],["c",3],["d",4]]
my_dict={}
for i in l:
    key=i[0]
    value=i[1]
    my_dict[key]=value
print(my_dict)

#{'a': 1, 'b': 2, 'c': 3, 'd': 4}

