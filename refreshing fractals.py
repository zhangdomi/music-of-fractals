import math
import turtle
import time

sign= -1          # 1 facing outwards, -1 facing inwards

def triangle(turtle, size, depth):
    if depth==0:
        turtle.forward(size)
    else:
        triangle(turtle, size/3, depth-1)
        turtle.right(60*sign)
        triangle(turtle, size/3, depth - 1)
        turtle.left(120*sign)
        triangle(turtle, size/3, depth - 1)
        turtle.right(60*sign)
        triangle(turtle, size/3, depth - 1)

N= 600            #controls the size of the fractal
x_start = -0.5
y_start = -1 / (math.sqrt(3) * 2)
turtle.speed(0)

wn = turtle.Screen()

for level in range(6):                  #controls the deepness of levels
    turtle.clear()
    wn.tracer(0)
    #turtle.hideturtle()
    turtle.penup()
    turtle.goto(x_start * N, y_start * N)
    turtle.pendown()

    for i in range(3):
        triangle(turtle, N, level)
        turtle.left(120)
    wn.update()

    time.sleep(1)

#ts = turtle.getscreen()
ts = turtle.Screen()
ts.getcanvas().postscript(file="d:\fractal.eps")

turtle.done()
