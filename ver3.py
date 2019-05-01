import math
import matplotlib.pyplot as plt


def square_distance(a, b):
	s = 0
	for x, y in zip(a, b):
		d = x - y
		s += d * d

	return s



class Node:
	def __init__(self,pt,ax,l,lt,rt):
		self.point=pt
		self.axis=ax
		self.label=l
		self.left=lt
		self.right=rt


def cnt():
	cnt.count+=1

cnt.count=0


class KDTree(object):
	
	def __init__(self,objects=[]):
		

		def build_tree(objects, axis=0):

			if not objects:
				return None


			objects.sort(key=lambda o: o[0][axis])
			median_idx = len(objects) // 2
			median_point, median_label = objects[median_idx]

			next_axis = (axis + 1) % 2

			return Node(median_point, axis, median_label,
						build_tree(objects[:median_idx], next_axis),
						build_tree(objects[median_idx + 1:], next_axis))

		self.root = build_tree(list(objects))


	def nearest_neighbor(self, destination,x=None):

		best = [None, None, float('inf')]
		# state of search: best point found, its label,
		# lowest squared distance
		

		def rec_search(here):
			
			if here is None:
				return
			cnt()
			point, axis, label, left, right = here.point,here.axis,here.label,here.left,here.right

			here_sd = square_distance(point, destination)
			

			if here_sd < best[2] and label not in x :
				best[0] = point
				best[1] = label
				best[2] = here_sd

			diff = destination[axis] - point[axis]
			close, away = (left, right) if diff <= 0 else (right, left)

			rec_search(close)

			if diff ** 2 < best[2]:
				rec_search(away)

		rec_search(self.root)
		
		return best[0], best[1], math.sqrt(best[2])

	def rad_neighbor(self, destination,r,x=None):

		best = [None, None, float('inf')]
		# state of search: best point found, its label,
		# lowest squared distance
		

		def recursive_search(here):
			
			if here is None:
				return
			cnt()
			point, axis, label, left, right = here.point,here.axis,here.label,here.left,here.right

			here_sd = square_distance(point, destination)
			

			if here_sd < best[2] and here_sd <= r*r and label not in x :
				best[0] = point
				best[1] = label
				best[2] = here_sd

			diff = destination[axis] - point[axis]
			close, away = (left, right) if diff <= 0 else (right, left)

			recursive_search(close)

			if diff ** 2 < best[2]:
				recursive_search(away)

		recursive_search(self.root)
		
		return best[0], best[1], math.sqrt(best[2])


def find_places(tree,name,d,pts):

	prevlabel=[]
	x=[]
	y=[]

	x_all=[]
	y_all=[]
	for i in pts[0] :
		x_all.append(i[0][0])
		y_all.append(i[0][1])

	print(x_all,"--",y_all)

	print("Do you want to fine the closest ",name,"\n\t1) In a given radius\n\t2) Enter the no. closest points")
	
	t=int(input())
	if t==2:
		l=int(input("Enter no. of closest points required : "))
		print(" ---- CLOSEST ",l," ",name," ----")


		for i in range (l):
			closest, label, mindistance = tree.nearest_neighbor(d,prevlabel)
			
			print("mindistance :",mindistance)
			print("label:",label)
			print("closest point",closest)
			print("counter of recursive_search:",cnt.count)
			print()
			x.append(closest[0])
			y.append(closest[1])
			prevlabel.append(label)
			plt.clf()
		plt.scatter(d[0], d[1], label="My Location", color= "black",marker= "^", s=80)
		plt.scatter(x_all, y_all, label= name, color= pts[2],marker= "*", s=30) 
		plt.scatter(x,y,s=80,facecolors='none',edgecolors='b')  
#		plt.xlabel('x - axis') 
#		plt.ylabel('y - axis') 
#		plt.title("CLOSEST ", name) 
		plt.legend() 
		plt.show() 
	
	if t==1:
		#l=int(input("Enter no. of closest points required : "))
		r=float(input("\nEnter search radius :"))
		
		print(" ---- CLOSEST ",name," ----")
		
		
		prevlabel=[]
		
		while True:
			closest, label, mindistance = tree.rad_neighbor(d,r,prevlabel)
			if mindistance==float('inf'):
				break
			print("mindistance :",mindistance)
			print("label:",label)
			print("closest point",closest)
			print("counter of recursive_search:",cnt.count)
			print()
			x.append(closest[0])
			y.append(closest[1])
			prevlabel.append(label)


		plt.clf()
		
		patch=plt.Circle((d[0],d[1]),radius=r,color="#98ffff",alpha=0.2)
		ax=plt.gca()
		ax.add_patch(patch)
#		plt.axis('scaled')
		plt.scatter(d[0], d[1], label="My Location", color= "black",marker= "^", s=80)
#		plt.scatter(x, y, label= name, color= "green",marker= "*", s=30) 
		plt.scatter(x_all, y_all, label= name, color= pts[2],marker= "*", s=30) 
		plt.scatter(x,y,s=80,facecolors='none',edgecolors='b')  
#		plt.xlabel('x - axis') 
#		plt.ylabel('y - axis') 
#		plt.title("CLOSEST ", name)
		plt.legend() 
		plt.show() 

	

def plotgraph(*args):
	for arg in args:
		x=[]
		y=[]
		for i in arg[0] :
			x.append(i[0][0])
			y.append(i[0][1])

		plt.scatter(x, y, label= arg[1], color=arg[2], marker= "*", s=30) 
		  
	# x-axis label 
	plt.xlabel('x - axis') 
	# frequency label 
	plt.ylabel('y - axis') 
	# plot title 
	plt.title('CITY') 
	# showing legend 
		  





def hotels():
	
	points=[]
	c=0
	infile=open('hotels.txt','r')
	for i in infile:
		points.append([])
		points[c].append((list(map(float,i.rstrip().split(",")))))
		points[c].append(c)
		c+=1


	return KDTree(points),points



def schools():
	
	points=[]
	c=0
	infile=open('schools.txt','r')
	for i in infile:
		points.append([])
		points[c].append((list(map(float,i.rstrip().split(",")))))
		points[c].append(c)
		c+=1


	return KDTree(points),points



def police():
	
	points=[]
	c=0
	infile=open('police.txt','r')
	for i in infile:
		points.append([])
		points[c].append((list(map(float,i.rstrip().split(",")))))
		points[c].append(c)
		c+=1


	return KDTree(points),points


def hospitals():
	
	points=[]
	c=0
	infile=open('hospitals.txt','r')
	for i in infile:
		points.append([])
		points[c].append((list(map(float,i.rstrip().split(",")))))
		points[c].append(c)
		c+=1


	return KDTree(points),points


def petrol_bunk():
	
	points=[]
	c=0
	infile=open('petrol_bunk.txt','r')
	for i in infile:
		points.append([])
		points[c].append((list(map(float,i.rstrip().split(",")))))
		points[c].append(c)
		c+=1


	return KDTree(points),points



def main():

	 
	print("Enter your location ( x y ): ")
	d=list(map(float,input().split()))

	h =[None,"hotels","green"]
	p =[None,"police","yellow"]
	ho=[None,"hospitals","red"]
	pe=[None,"petrol_bunk","cyan"]
	s =[None,"schools","blue"]

	h_tree ,h[0]  =hotels()   
	p_tree ,p[0]  =police()
	ho_tree,ho[0] =hospitals()
	pe_tree,pe[0] =petrol_bunk()
	s_tree ,s[0]  =schools()

	plotgraph(h,p,ho,pe,s)

	# my location
	plt.scatter(d[0], d[1], label="MY_location", color="black", marker= "^", s=80)
	plt.legend() 


	# function to show the plot 
	plt.show() 


	print("Which closest place do you wanna find?\n\t1.Police Station \n\t2.hotels \n\t3.Schools \n\t4.Petrol Bunk \n\t5.Hospitals")
	choice=int(input())

	

	if choice==1:
		find_places(p_tree,"police_stations",d,p)
	elif choice==2:
		find_places(h_tree,"hotels",d,h)
	elif choice==3:
		find_places(s_tree,"school",d,s)
	elif choice==4:
		find_places(pe_tree,"petrol_bunks",d,pe)
	elif choice==5:
		find_places(ho_tree,"hospitals",d,ho)
	else:
		print("wrong choice!")






if __name__ == '__main__':
	main()
