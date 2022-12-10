#Make a Frequency Dictionary for the Characters in a String ()
string="Hello My World"
my_dict={}
for char in string:
    if char in my_dict:
        my_dict[char]+=1
    else:
        my_dict[char]=1
print(my_dict)

#{'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 2, 'M': 1, 'y': 1, 'W': 1, 'r': 1, 'd': 1}
