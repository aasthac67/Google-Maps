#------------------------MODULE TO IMPLEMENT KD-TREE------------------------------


#import math for math functions
import math

#counter function to count no. of recursive search queries
def cnt():
	cnt.count+=1

cnt.count=0

#function to calculate square distance between two points 'a' and 'b'
def square_distance(a, b):
	s = math.pow((a[0]-b[0]),2)+math.pow((a[1]-b[1]),2)
	return s

#Defining a KDTree Node and it's attributes
class Node:
	def __init__(self,pt,ax,l,lt,rt):
		self.point=pt
		self.axis=ax
		self.label=l
		self.left=lt
		self.right=rt
#Implementing KDTree 
class KDTree:
#Initialization using __init__
	
	def __init__(self,objects=[]):
		
#Building the Tree
		def build_tree(objects, axis=0):

			if not objects:
				return None


			objects.sort(key=lambda o: o[0][axis])    #Sorting the coordinates to find the median
			median_idx = len(objects) // 2
			median_point, median_label = objects[median_idx]

			next_axis = (axis + 1) % 2                #Axis: x=0 and y=1 for splitting 

			return Node(median_point, axis, median_label,
						build_tree(objects[:median_idx], next_axis),
						build_tree(objects[median_idx + 1:], next_axis))

		self.root = build_tree(list(objects))



	def nearest_neighbor(self,destination,t,n=0,r=None): 


		# state of search: best point found, its label,
		# lowest squared distance
		if t==1:
			best=[[None, -1, float('inf')] for _ in range(n)]
		elif t==2:
			best=[]

		

		def recursive_search(here):
			
			if here is None:
				return

			cnt()                                      #Updating Counter                 
			point, axis, label, left, right = here.point,here.axis,here.label,here.left,here.right

			here_sd = square_distance(point, destination)
		
# if t=1 find k nearest neighbours
			if t==1:
				if best[n-1][1]==-1:
					best[n-1]=[point,label,here_sd]
					k=n-1
					while k>0 and (best[k][2]>best[k-1][2] or best[k-1][2]==float('inf')):
						best[k],best[k-1]=best[k-1],best[k] 
						k-=1

				elif here_sd < best[0][2] and best[n-1][1]==-1:
					best[n-1]=[point,label,here_sd]
					k=n-1
					while k>0 and (best[k][2]>best[k-1][2] or best[k-1][2]==float('inf') ):
						best[k],best[k-1]=best[k-1],best[k] 
						k-=1

				elif here_sd < best[0][2] and best[n-1][1]!=-1:
					best[0][1],best[0][2]=-1,float('inf')
					k=1
					while k<n and best[k][1]!=-1:
						best[k-1],best[k]=best[k],best[k-1]
						k+=1
					
					best[n-1]=[point,label,here_sd]
					k=n-1
					while best[k][2]>best[k-1][2] and k>0:
						best[k],best[k-1]=best[k-1],best[k] 
						k-=1

#If t=2 find neighbours within a radius of r units

			if t==2:
				if here_sd < r*r:
					best.append([point,label,here_sd])

			

			diff = destination[axis] - point[axis]
			close, away = (left, right) if diff <= 0 else (right, left)

			recursive_search(close)
			
			flag=0
			if t==1:
				for i in range(n):
					if diff**2<best[i][2]:
						flag=1
			if t==2:
				if diff<r:
					flag=1
			
			if flag==1:
				recursive_search(away)

		recursive_search(self.root)
		
		return best	

#Method for returning the count of recursive search queries
	def returncounter(self):
		return cnt.count


