from turtle import *
import random
import math
import time
from ball import Ball

colormode(255)
tracer(1)
hideturtle()

RUNNING=True

SLEEP=0.0077
SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

MY_BALL=Ball(100,100,2,1,40,"black")
NUMBER_OF_BALLS=5.
MINIMUM_BALL_RADIUS =10.
MAXIMUM_BALL_RADIUS =100.
MINIMUM_BALL_DX =-5.
MAXIMUM_BALL_DX =5.
MINIMUM_BALL_DY =-5.
MAXIMUM_BALL_DY =5.

BALLS=[]
for i in range(NUMBER_OF_BALLS):
	x=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS ,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
	y=random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
	dx=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	while dx==0:
		dx=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
	dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
	while dy==0:
		dy=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY) 
	raduis=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color=(random.random(), random.random(), random.random())
	ball5=Ball(x,y,dx,dy,radius,color)
	ball5.append(BALLS)
for i in BALLS:
	i.move(SCREEN_WIDTH,SCREEN_HEIGHT)

def collide(ball_a,ball_b):
	if ball_a==ball_b:
		return False
	DISTANCE_BETWEEN_CORES=int(ball_a.pos())-int(ball_b.pos())
	if DISTANCE_BETWEEN_CORES+10<=ball_a.radius+ball_b.radius:
		return True
	else:
		return False
def check_all_balls_collision():
	for ball_a in BALLS:
		for ball_b in BALLS:
			if collide(ball_a,ball_b)==True:
				raduis_a=ball_a.radius
				raduis_b=ball_b.radius	
				x_coordinate=random.randint(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS ,SCREEN_WIDTH - MAXIMUM_BALL_RADIUS)
				y_coordinate=random.randint(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS , SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS)
				x_axis_speed=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				while x_axis_speed==0:
					x_axis_speed=random.randint(MINIMUM_BALL_DX, MAXIMUM_BALL_DX)
				y_axis_speed=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				while y_axis_speed==0:
					y_axis_speed=random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY) 
				raduis=random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				r=random.randint(0,225)
				g=random.randint(0,225)
				b=random.randint(0,225)
				color=(r,g,b)
				if ball_a<ball_b:
					ball_a=Ball(x_coordinate,y_coordinate,x_axis_speed,y_axis_speed,radius,color)
					raduis_b=+raduis_b
				else:
					ball_b=Ball(x_coordinate,y_coordinate,x_axis_speed,y_axis_speed,radius,color)
					raduis_a=+raduis_a
collide(ball_a,ball_b)
check_all_balls_collision()



mainloop()