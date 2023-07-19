import turtle
import turtle as t
from turtle import Turtle,Screen,circle
import random
screen = Screen()
screen.bgcolor("black")
my_turtle = Turtle()
turtle.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tuple = (r, g, b)
    return tuple

my_turtle.speed('fastest')
a = 0
while a<72:
    my_turtle.color(random_color())
    my_turtle.circle(100)
    my_turtle.right(5)
    a +=1
#      another method
#   current_heading = my_turtle.heading()
#   my_turtle.setheading(current_heading+10)




screen.exitonclick()