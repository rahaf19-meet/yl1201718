from turtle import *
import random
import math

class Ball(Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius)	
		self.color(color)
		self.speed(speed)
ball1=Ball(7,"red",1)
ball2=Ball(4,"blue",1)
x1=ball1.xcor()
x2=ball2.xcor()
y1=ball1.ycor()
y2=ball2.ycor()
posx1=random.randint(0,100)
posx2=random.randint(0,100)
posy1=random.randint(0,100)
posy2=random.randint(0,100)
ball1.goto(posx1,posy1)
ball2.goto(posx2,posy2)
a=False
def check_collision(ball1,ball2):
 	if ball1.shapesize()[0]+ball2.shapesize()[0]>math.sqrt(math.pow((x2-x1),2)+ math.pow((y2-y1),2)):
 		ball1.color("black")	
 		ball2.color("pink")
			


check_collision(ball1,ball2)
mainloop()