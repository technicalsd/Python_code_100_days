# Draw a traingle,square,pentagon,hexagon,heptagon,octagon,nanogon and decagon amd so on
from turtle import Turtle,Screen
import random
my_turtle = Turtle()

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(0,num_sides):
        my_turtle.forward(40)
        my_turtle.right(angle)

color = ["red","blue","green","yellow","purple","orange","grey","deeppink"]
for shape_side_n in range(3,360):
    my_turtle.pencolor(random.choice(color))
    draw_shape(shape_side_n)








screen = Screen()
screen.exitonclick()