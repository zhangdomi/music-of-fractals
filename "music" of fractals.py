import math
import turtle
import numpy as np
from scipy.io import wavfile


k = 0
N = 700.0
samplingFrequency = 44100

xpos = [0 for i in range(20000)]
ypos = [0 for i in range(20000)]
audio_xpos = [0 for i in range(200000000)]
audio_ypos = [0 for i in range(200000000)]


def triangle(turtle, size, depth):
    global k
    if depth == 0:
        turtle.forward(size)
        xpos[k] = turtle.pos()[0] / N
        ypos[k] = turtle.pos()[1] / N
        k = k + 1

    else:
        triangle(turtle, size / 3, depth - 1)
        #xpos[k] = turtle.pos()[0] / N
        #ypos[k] = turtle.pos()[1] / N
        turtle.right(60)
        triangle(turtle, size / 3, depth - 1)
        turtle.left(120)
        triangle(turtle, size / 3, depth - 1)
        turtle.right(60)
        triangle(turtle, size / 3, depth - 1)

turtle.speed(0)
x_start = -0.5                               # center of the coordinate system
y_start = -1/(math.sqrt(3) * 2)

phi = 0
phi_step = 4

for phi_k in range(15):
    x_st = x_start * math.cos(phi * math.pi/180) - y_start * math.sin(phi * math.pi/180)
    y_st = x_start * math.sin(phi * math.pi/180) + y_start * math.cos(phi * math.pi/180)
    turtle.setheading(phi)

    turtle.penup()
    turtle.goto(x_st * N, y_st * N)
    xpos[k] = turtle.pos()[0]/N
    ypos[k] = turtle.pos()[1]/N
    k = k + 1

    for i in range(3):
        triangle(turtle, N, 3)
        turtle.left(120)

    phi = phi + phi_step
    turtle.clear()
    print(phi)

N_fr_p = k  # Number of fractal points
samplingFrequency = 44100

print(N_fr_p)

def HoldOff(T, N_holdoff):  # Time in sec, Number of holdoff
    N_points = T * samplingFrequency  # Number of points
    N_rep = round(N_points / (N_fr_p * N_holdoff))  # Number of repetitions
    for i in range(N_rep):
        for j in range(N_fr_p):
            for l in range(N_holdoff):
                audio_xpos[i * N_fr_p * N_holdoff + j * N_holdoff + l] = xpos[j]
                audio_ypos[i * N_fr_p * N_holdoff + j * N_holdoff + l] = ypos[j]


HoldOff(200, 15)

audio_pos = np.vstack((audio_xpos, audio_ypos))

audio_pos = audio_pos.transpose()
wavfile.write('Sirpinski_No_Turtle_rotate_5_level_3_HO_15_4_15.wav', samplingFrequency, audio_pos)
