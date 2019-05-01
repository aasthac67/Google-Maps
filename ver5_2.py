#---------------------NEAREST NEIGHBOURS USING KD-TREES---------------------- 

#Imported modules and files
import math
import matplotlib.pyplot as plt
import time
from kd_tree import KDTree


def find_places(tree,d,pts):

	x,y=[],[]
	x_all,y_all=[],[]

	for i in pts[0] :
		x_all.append(i[0][0])
		y_all.append(i[0][1])

	#print(x_all,"--",y_all)

	print("Do you want to find the closest ",pts[1],"\n\t1) Enter the no. closest points\n\t2) In a given radius")
		
	t=int(input())

	start_time=time.time()
	if t==1:
		l=int(input("Enter no. of closest points required : "))
		print("\n\n---- CLOSEST ",l," ",pts[1]," ----")

		
		best=tree.nearest_neighbor(d,t,l)

		for i in range(l):
			x.append(best[i][0][0])
			y.append(best[i][0][1])
			print("mindistance :",math.sqrt(best[i][2]))
			print("label:",best[i][1])
			print("closest point",best[i][0])
			print("counter of recursive_search:",tree.returncounter())
			print("- - - - - - - - - - - - - - - ")
		
		print("-------",time.time()-start_time,"-------")
		patch=plt.Circle((d[0],d[1]),radius=math.sqrt(best[0][2]),color="#98ffff",alpha=0.2)
		ax=plt.gca()
		ax.add_patch(patch)
		
#		plt.axis('scaled')
		plt.scatter(d[0], d[1], label="My Location", color= "black",marker= "^", s=140)
#		plt.scatter(x, y, label= pts[1], color= "green",marker= "*", s=30) 
		plt.scatter(x_all, y_all, label= pts[1], color= pts[2],marker= "*", s=30) 
		plt.scatter(x,y,s=80,facecolors='none',edgecolors='b')  
#		plt.xlabel('x - axis') 
#		plt.ylabel('y - axis') 
#		plt.title("CLOSEST ", pts[1])
		plt.legend() 
		plt.show() 
	
	if t==2:
		#l=int(input("Enter no. of closest points required : "))
		print(" ---- CLOSEST ",pts[1]," ----")
		
		r=float(input("\nEnter search radius :"))
		
		
		best=tree.nearest_neighbor(d,t,0,r)


		for i in range(len(best)):
			x.append(best[i][0][0])
			y.append(best[i][0][1])
			print("mindistance :",math.sqrt(best[i][2]))
			print("label:",best[i][1])
			print("closest point",best[i][0])
			print("counter of recursive_search:",tree.returncounter())
			print("- - - - - - - - - - - - - - - ")


		
		
		patch=plt.Circle((d[0],d[1]),radius=r,color="#98ffff",alpha=0.2)
		ax=plt.gca()
		ax.add_patch(patch)
#		plt.axis('scaled')
		plt.scatter(d[0], d[1], label="My Location", color= "black",marker= "^", s=140)
#		plt.scatter(x, y, label= pts[1], color= "green",marker= "*", s=30) 
		plt.scatter(x_all, y_all, label= pts[1], color= pts[2],marker= "*", s=30) 
		plt.scatter(x,y,s=80,facecolors='none',edgecolors='b')  
#		plt.xlabel('x - axis') 
#		plt.ylabel('y - axis') 
#		plt.title("CLOSEST ", pts[1])
		plt.axis('scaled')
		plt.legend() 
		plt.show() 

	

def plotgraph(*args):
	for arg in args:
		x=[]
		y=[]
		for i in arg[0] :
			x.append(i[0][0])
			y.append(i[0][1])

		plt.scatter(x, y, label= arg[1], color=arg[2], marker= "*", s=80) 
		  
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

	#Entering own location : 
	print("Enter your location ( x y ): ")
	d=list(map(float,input().split()))

	#defining python lists to store attributes of a type of place
	hotel_list   =[None,"hotels","green"]
	police_list  =[None,"police","yellow"]
	hospital_list=[None,"hospitals","red"]
	petrol_list  =[None,"petrol_bunk","cyan"]
	school_list  =[None,"schools","blue"]

	#making respective trees of differents places   
	police_tree , police_list[0]   = police()
	hotel_tree ,  hotel_list[0]    = hotels()
	school_tree , school_list[0]   = schools()
	petrol_tree , petrol_list[0]   = petrol_bunk()
	hospital_tree,hospital_list[0] = hospitals()

	#plotting graph
	plotgraph(police_list,hotel_list,school_list,petrol_list,hospital_list)

	# my location
	plt.scatter(d[0], d[1], label="My_Location", color="black", marker= "^", s=140)
	plt.legend() 

	# function to show the plot 
	plt.show() 
	#clear graph for future use
	plt.clf()


	print("Which closest place do you wanna find?",
		   "\n\t1.Police Station",
		   "\n\t2.Hotels",
		   "\n\t3.Schools",
		   "\n\t4.Petrol Bunk",
		   "\n\t5.Hospitals")
	choice=int(input())

	if choice==1:
		find_places(police_tree,d,police_list)
	elif choice==2:
		find_places(hotel_tree,d,hotel_list)
	elif choice==3:
		find_places(school_tree,d,school_list)
	elif choice==4:
		find_places(petrol_tree,d,petrol_list)
	elif choice==5:
		find_places(hospital_tree,d,hospital_list)
	else:
		print("Wrong choice!")






if __name__ == '__main__':
	main()
