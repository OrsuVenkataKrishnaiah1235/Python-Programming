#Frequency of the Values in a Dictionary
my_dict={"a":4,"b":5,"c":2,"d":4}
m_dict={}
for value in my_dict.values():
    if value in m_dict:
        m_dict[value]+=1
    else:
        m_dict[value]=1
print(m_dict)

#{4: 2, 5: 1, 2: 1}

