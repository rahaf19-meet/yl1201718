import turtle

turtle.speed(100000000000000000000000000000000)
turtleslides=361



a=1
for i in range(turtleslides):
	turtle.forward(200)
	turtle.right(30)
	turtle.forward(100)
	turtle.right(90)
	turtle.forward(70)
	turtle.home()
	turtle.right(a)
	a=a+1






turtle.mainloop()