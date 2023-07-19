from turtle import Turtle, Screen, circle

my_turtle = Turtle()
my_turtle.speed("slow")

def move_forward():
    my_turtle.forward(10)
def move_backward():
    my_turtle.backward(10)

def clock_wise():
    new_heading  = my_turtle.heading() + 20
    my_turtle.setheading(new_heading) # or just use left() instead of heading andset heading

def anti_clock_wise():
    new_heading = my_turtle.heading() - 20
    my_turtle.setheading(new_heading)
def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()
screen =  Screen()
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward,"s")
screen.onkey(clock_wise, "d")
screen.onkey(anti_clock_wise,"a")
screen.onkey(clear, "c")
screen.exitonclick()



