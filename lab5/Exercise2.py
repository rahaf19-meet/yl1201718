import turtle
from turtle import *
class Hexagon(Turtle):
	begin_poly()

	for i in range(6):
		turtle.forward(100)
		turtle.left(60)
	end_poly()
	get_poly()


# class Hexagon(Turtle):
# 	def __init__():