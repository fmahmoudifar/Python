# from turtle import Turtle, Screen

# timmy_the_turtle = Turtle()

# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("RED")


# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)



# screen = Screen()
# screen.exitonclick()

import turtle as t
import random

tim = t.Turtle()

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
        
for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)