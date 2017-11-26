from turtle import *
import random
colormode(255)

class Rectangle(Turtle):
	def __init__(self,width,height):
		Turtle.__init__(self)
		self.width=width
		self.height=height

		register_shape("rectangle",((0,self.height),(self.width,self.height),(self.width,0),(0,0)))
		self.shape("rectangle")
		self.setheading(90)


class Square(Rectangle):
	
	def __init__(self,size):
		Rectangle.__init__(self,size,size)

		
		#size=width*height
		#self.shapesize(size)
		# self.shape('square')

	#def random_color(self):
		#r=random.randint(0,225)
		#g=random.randint(0,225)
		#b=random.randint(0,225)
		#self.color(r,g,b)

#s=Square(10)
#s.random_color()
r=Square(200)

mainloop()





