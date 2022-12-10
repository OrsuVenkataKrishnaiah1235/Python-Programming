#Check if All Values are Equal
my_dict={"a":3,"b":3,"c":3}
value=len(set(my_dict.values()))
if value==0:
	print("Dict is Empty")
elif value==1:
	print("True")
else:
	print("False")
#true
