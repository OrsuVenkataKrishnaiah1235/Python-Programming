#Distance Between Two 3D Points
pointsA=[3,4,5,6]
pointsB=[0,1,2,3]
distance=0
for i in range(len(pointsA) or len(pointsB)):
	distance+=(pointsA[i]-pointsB[i])**2
print(distance**(1/2))

#6.0

