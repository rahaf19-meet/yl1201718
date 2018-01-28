from turtle import *
import random
import math
import time
colormode(255)
tracer(1)
hideturtle()

class Ball(Turtle):
	def __init__(self,x,y,dx,dy,radius,color):
		Turtle.__init__(self)
		self.pu()
		self.goto(x,y)
		self.dx=dx
		self.dy=dy
		self.shape("circle")
		self.radius=radius
		self.shapesize(radius/10)
		self.color(color)

	def move(self,screen_width,screen_height):
		current_x=self.xcor()
		current_y=self.ycor()
		new_x=current_x+self.dx
		new_y=current_y+self.dy
		right_side_ball=new_x+self.radius
		left_side_ball=new_x-self.radius
		top_side_ball=new_y+self.radius
		buttom_side_ball=new_y-self.radius
		self.goto(new_x,new_y)
		screen_width_right=screen_width
		screen_width_left= -screen_width
		screen_height_up=screen_height
		screen_height_down=-screen_height
		if right_side_ball>screen_width_right or left_side_ball<screen_width_left or top_side_ball>screen_height_up or buttom_side_ball<screen_height_down:
			self.dx=-self.dx
			self.dy=-self.dy
		



# ball1=Ball(0,0,1,2,20,"red")
# ball2=Ball(100,100,2,1,40,"pink")
# while True:
# 	ball1.move(400,400)
# 	ball2.move(400,400)
# 	getscreen().update()
# 	time.sleep(0.01)

# #def check_collision(ball1,ball2):
# #	ball1.move(200,200)
# #	if right_side_ball>screen_height or left_side_ball<screen_height or top_side_ball>screen_width or buttom_side_ball<screen_width:
# #		ball1.dx=(-ball1.dx)
# #		ball1.dy=(-ball1.dy)
# #	ball2.move(200,200)
# #	if right_side_ball>screen_height or left_side_ball<screen_height or top_side_ball>screen_width or buttom_side_ball<screen_width:
# #		ball2.dx=(-ball2.dx)
# #		ball2.dy=(-ball2.dy)


# mainloop()








