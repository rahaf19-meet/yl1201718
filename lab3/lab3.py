import turtle
turtle.speed(50)
turtle.pensize(5)
turtle.color("green")

howmanysides=6
sidelength=120
degree=60
angle=20
howmanysquares=360/angle

for i in range(howmanysquares):
	turtle.left(angle)
	for i in range(howmanysides):
		turtle.forward(sidelength)
		turtle.left(degree)

turtle.mainloop()