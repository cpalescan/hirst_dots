import colorgram
import turtle
import random


screen = turtle.Screen()
screen.screensize(300, 300)


# color extraction
colors = colorgram.extract("hirst.jpg", 25)
swaps = []
for color in colors:
    rgb = color.rgb
    for values in rgb:
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        my_swap = (r, g, b)
        swaps.append(my_swap)

# turtle creation

turtle.colormode(255)


# setting world coordinates
x = 10
y = 10
turtle.setworldcoordinates(-x, -y, x, y)

# placing the turtle in the bottom left corner
turtle.teleport(-x, -y)


# left to right
def left_to_right():
    """prints dots from - x to x"""
    n = 1
    while n < (2 * x):
        new_x = - x + n
        turtle.teleport(new_x)
        color = random.choice(swaps)
        turtle.dot(10,color)
        n += 1

# bottom to top + left to right
b = 1
turtle.hideturtle()
while b < (2 * y):
    new_y = -y + b
    turtle.teleport(-x, new_y)
    b += 1
    left_to_right()


screen.exitonclick()
