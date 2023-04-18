import turtle

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle.speed(0)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

for i in range(30, 330, 30):
    for j, color in enumerate(colors):
        turtle.penup()
        turtle.goto(0, -i)
        turtle.setheading(j*60)
        turtle.pendown()
        turtle.color(color)
        turtle.circle(i, 60)

turtle.hideturtle()
turtle.done()
