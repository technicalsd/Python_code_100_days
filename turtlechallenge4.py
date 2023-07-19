from turtle import *
import random
import turtle as t
my_turtle = Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tuple = (r, g, b)
    return tuple

directions = [0,90,90,180,180,270,270]
my_turtle.speed("fast")
my_turtle.pensize(5)
for _ in range(0,200):
    my_turtle.color(random_color())
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(directions))




screen = Screen()
screen.exitonclick()
