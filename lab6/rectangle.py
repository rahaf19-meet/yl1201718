from turtle import *
import random
import math

class square (Turtle):
	def __init__(self,height,color,speed):
		Turtle.__init__(self)
		self.shape("square")
		self.shapesize(height)
		self.color(color)
		self.speed(speed)
rec1=square(7,"red",1)
rec2=square(7,"blue",1)
x1=rec1.xcor()
x2=rec2.xcor()
y1=rec1.ycor()
y2=rec2.ycor()

rec1_top=y1+(rec1.shapesize()[0]/2)
rec1_right=x1+(rec1.shapesize()[0]/2)
rec1_bottom=y1-(rec1.shapesize()[0]/2)
rec1_left=x1-(rec1.shapesize()[0]/2)

rec2_top=y2-(rec2.shapesize()[0]/2)
rec2_right=x2+(rec2.shapesize()[0]/2)
rec2_bottom=y2-(rec2.shapesize()[0]/2)
rec2_left=x2-(rec2.shapesize()[0]/2)

posx1=random.randint(0,100)
posx2=random.randint(0,100)
posy1=random.randint(0,100)
posy2=random.randint(0,100)
rec1.goto(posx1,posy1)
rec2.goto(posx2,posy2)

def check_collision(rec1,rec2):
 	if (rec1_top >= rec2_bottom and rec1_right>=rec2_left and rec1_bottom <=rec2_top and rec1_left <= rec2_right):
 		rec1.color("black")	
 		rec2.color("pink")
			


check_collision(rec1,rec2)
mainloop()