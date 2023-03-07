import colorgram
import turtle as turtle_module
import random

# Extract 10 colors from a Hirst image
colors = colorgram.extract('image.jpg', 30)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]


turtle = turtle_module.Turtle()
turtle_module.colormode(255)
turtle.speed('fast')

turtle.hideturtle()
turtle.setheading(218)
turtle.penup()
turtle.forward(300)
turtle.setheading(0)


number_of_dots = 100


def change_position():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(500)
    turtle.setheading(0)


for dot_count in range(1, number_of_dots + 1):
    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)
    if dot_count % 10 == 0:
        change_position()


screen = turtle_module.Screen()
screen.exitonclick()