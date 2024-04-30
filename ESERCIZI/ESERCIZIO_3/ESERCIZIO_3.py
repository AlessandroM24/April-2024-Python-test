# ESERCIZIO 3

import turtle
from turtle import Turtle, Screen
import random

WIDTH = 500
HEIGHT = 500

turtle.colormode(255)
screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
tim = Turtle()
tim.speed(5)


def colore_casuale_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colore = (r, g, b)
    return colore


def disegna_quadrati(num):
    lato_quadrato = WIDTH // num
    tim.penup()
    x_pos = WIDTH // 2 * -1
    y_pos = HEIGHT // 2
    tim.goto(x_pos, y_pos)  # Posizione iniziale
    tim.pendown()

    for quadrato in range(num):
        tim.color(colore_casuale_rgb())
        tim.begin_fill()
        for _ in range(6):
            tim.forward(lato_quadrato)
            tim.right(90)
        tim.end_fill()
        tim.setheading(0)


disegna_quadrati(5)

screen.exitonclick()
