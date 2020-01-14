triangle_var = 2

def triangleAlgorithm(n):
	"""
	print a triangle
	
	parameter pada dasarnya adalah variable yang didefinisikan kedalam sebuah method.
	tidak seperti variable persis, karena parameter dapat didefiniskan tanpa default value,
	  yang berarti parameter tersebut diwajibkan diberikan nilai ketika kita memanggil function tsb.
	
	this will be a docstring
	"""
	for i in range(1,n+1):
		print("{:^30}".format(' '.join(str('*')*i)))
		
def privateTriangleAlgo():
	print("this is private")
