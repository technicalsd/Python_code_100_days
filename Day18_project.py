import turtle
import random
import colorgram
from turtle import Turtle,Screen,color
# colors = colorgram.extract("1234567.jpg",30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tuple = (r,g,b)
#     rgb_colors.append(tuple)

color_list = [(249, 248, 244), (250, 246, 248), (240, 245, 250), (241, 248, 245), (235, 225, 83), (200, 6, 70), (197, 164, 12), (233, 52, 130), (205, 75, 13), (110, 179, 217), (218, 162, 103), (32, 187, 109), (26, 105, 171), (14, 23, 63), (234, 224, 7), (18, 29, 172), (212, 136, 176), (11, 184, 213), (204, 30, 138), (229, 168, 197), (125, 189, 161), (9, 48, 28), (39, 132, 73), (126, 219, 233), (68, 22, 8), (113, 90, 209), (144, 216, 200), (63, 10, 25), (187, 16, 6), (235, 64, 33)]
turtle.colormode(255)
my_turtle = Turtle()
my_turtle.hideturtle()
my_turtle.setheading(225)
my_turtle.penup()
my_turtle.forward(300)
my_turtle.setheading(0)
number_of_dots = 100
my_turtle.speed('fastest')
for dot_count in range(1,number_of_dots+1):
        my_turtle.dot(20, random.choice(color_list))
        my_turtle.penup()
        my_turtle.forward(50)
        if dot_count %10 == 0:
                my_turtle.setheading(90)
                my_turtle.forward(50)
                my_turtle.setheading(180)
                my_turtle.forward(500)
                my_turtle.setheading(0)



screen = Screen()
screen.exitonclick()
