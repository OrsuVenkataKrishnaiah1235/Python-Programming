#Make a Frequency Dictionary from the Elements of a List ()
l=["a","b","a","c","a","b"]
dic={}
for elem in l:
	if elem not in dic:
		dic[elem]=1
	else:
		dic[elem]+=1
print(dic)

'''
{'a': 3, 'b': 2, 'c': 1}
'''
