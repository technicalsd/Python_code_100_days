from turtle import Turtle, Screen

my_turtle = Turtle()
# for _ in range(15):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()


# another solution
for _ in range(15):
    my_turtle.forward(10)
    my_turtle.pencolor("white")
    my_turtle.forward(10)
    my_turtle.pencolor('black')







screen =Screen()
screen.exitonclick()