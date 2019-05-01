
points=[]
c=0
infile=open('a.txt','r')
for i in infile:
	points.append([])
	points[c].append((list(map(int,i.rstrip().split(",")))))
	points[c].append(c)
	c+=1

print(points)


		
