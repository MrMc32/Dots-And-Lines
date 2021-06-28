import turtle, random, os

screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("black")

List_Of_Dots = []
Turtle_Dots = []

def CreateDot(x, y):
	Info_Of_Dot = []
	dot = turtle.Turtle()
	dot.hideturtle()
	dot.penup()
	dot.shape("circle")
	dot.shapesize(0.25, 0.25)
	dot.color("red")
	dot.goto(x, y)
	dot.showturtle()
	Info_Of_Dot.append(x)
	Info_Of_Dot.append(y)
	List_Of_Dots.append(Info_Of_Dot)
	Turtle_Dots.append(dot)

os.system("cls")
ran = int(input("\nHOW MANY RANDOM DOTS: "))

for i in range(ran):
	CreateDot(random.randint(-250, 250), random.randint(-250, 250))

arrow = turtle.Turtle()
arrow.hideturtle()
arrow.color("blue")
First_Dot = List_Of_Dots[0]
List_Of_Dots.append(First_Dot)
arrow.penup()
arrow.goto(First_Dot[0], First_Dot[1])
arrow.pendown()

Dot = 1
do = 1

while True:
	arrow.speed(0)
	if do == 1:
		Next_Dot = List_Of_Dots[Dot]
		Turtle_Dot = Turtle_Dots[Dot - 1]
		
		arrow.setheading(arrow.towards(Next_Dot[0], Next_Dot[1]))
		if(arrow.distance(Next_Dot[0], Next_Dot[1]) > 3.0):
			arrow.forward(arrow.distance(Next_Dot[0], Next_Dot[1]))

		xplace = Next_Dot[0] - 1
		xplacep = Next_Dot[0] + 1

		yplace = Next_Dot[1] - 1
		yplacep = Next_Dot[1] + 1

		if arrow.distance(Next_Dot[0], Next_Dot[1]) <= 3.0:
			Turtle_Dot.color("green")
			Dot = Dot + 1
			if Dot >= len(List_Of_Dots):
				do = 0
			
	screen.update()
	print(arrow.distance(Next_Dot[0], Next_Dot[1]))