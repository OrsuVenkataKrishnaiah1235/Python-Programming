#Convert Dictionary into a List of Lists ()
my_dict={"a":1,"b":2,"c":3,"d":4}
l=[]
for key,value in my_dict.items():
    l.append([key,value])
print(l)

#[['a', 1], ['b', 2], ['c', 3], ['d', 4]]

