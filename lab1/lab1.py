import turtle
print("Rahaf "*100)
number1=10
print(number1)
number2=0.5*number1
print(number2)
list=[15,12,6]
n=0
for i in range(3):
	print(list[n])
	print(list[n]*2)
	n=n+1
print(list[0]+list[1]+list[2])
turtle.penup()
turtle.goto(100,0)
turtle.pendown()
turtle.goto(100,200)
turtle.goto(200,200)
turtle.goto(200,0)
turtle.goto(100,0)
turtle.mainloop()
