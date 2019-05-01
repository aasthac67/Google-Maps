import collections
import math
import matplotlib.pyplot as plt
import time

def square_distance(a, b):
	s = 0
	for x, y in zip(a, b):
		d = x - y
		s += d * d

	return s

#Node = collections.namedtuple("Node", 'point axis label left right')

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
		

		def recursive_search(here):
			
			if here is None:
				return
			cnt()
			point, axis, label, left, right = here.point,here.axis,here.label,here.left,here.right

			here_sd = square_distance(point, destination)
			

			if here_sd < best[2] and label not in x:
				best[0] = point
				best[1] = label
				best[2] = here_sd

			if axis==0:
				plt.axvline(point[0])
			else:
				plt.axhline(point[1])

			diff = destination[axis] - point[axis]
			close, away = (left, right) if diff <= 0 else (right, left)

			recursive_search(close)

			if diff ** 2 < best[2]:
				recursive_search(away)

		recursive_search(self.root)
		
		return best[0], best[1], math.sqrt(best[2])


if __name__ == '__main__':

	from random import random

		
	points = [((1,0),0),((2,0),1),((0,1),2),((2,2),3),((2,4),4),((8,3),5),((7,1),6),((9,4),7),((2,9),8),((2,6),9),((3,4),10),((3,3),11),((5,4),12),((6,4),13),((6,7),14),((4,2),15),((6,1.8),16),((8,2.5),17),((4,6.5),18),((6,6.3),19),((4.5,6),20),((4.3,7.1),21),((8.1,7.3),22),((8.4,8.4),23),((0.5,5),24),((1.2,6.3),25),((1.6,2.7),26),((1.1,7.5),27),((6.5,4.5),28),((8.1,5.5),29)]

	x=[]
	y=[]
	for i in points :
		x.append(i[0][0])
		y.append(i[0][1])

	plt.scatter(x, y, label=points, color='r', marker= "*", s=30)
	plt.show()

	tree = KDTree(points)
 
	destination = [4,5]
	prevlabel=[]
	
	l=int(input("Enter no. of closest points required : "))
	start=time.time()

	for i in range (l):
		
		closest, label, mindistance = tree.nearest_neighbor(destination,prevlabel)
			

		print("mindistance :",mindistance)

		print("label:",label)
		print("closest point",closest)
		print("counter of recursive_search:",cnt.count)

		prevlabel.append(label)

	print("--------------",time.time()-start)

	plt.scatter(x, y, label=points, color='r', marker= "*", s=30)
	plt.scatter(destination[0],destination[1],label="loc", color= 'b',marker= "^", s=30) 
	plt.axis('scaled')
	plt.show()