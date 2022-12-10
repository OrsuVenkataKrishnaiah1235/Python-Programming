#Add a Key-Value Pair Only if the Key is Not in the Dictionary
my_dict={}
for i in range(1,11,2):
	my_dict[i]=i**2
new_key=12
new_value=144
if new_key not in my_dict:
	my_dict[12]=144
print(my_dict)

#{1: 1, 3: 9, 5: 25, 7: 49, 9: 81, 12: 144}

