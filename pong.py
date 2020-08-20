#!/usr/bin/env python3

import turtle, os

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Paleta A
paleta_a = turtle.Turtle()
paleta_a.speed(0)
paleta_a.shape("square")
paleta_a.color("white")
paleta_a.shapesize(stretch_wid=5, stretch_len=1)
paleta_a.penup()
paleta_a.goto(-350,0)

# Paleta B
paleta_b = turtle.Turtle()
paleta_b.speed(0)
paleta_b.shape("square")
paleta_b.color("white")
paleta_b.shapesize(stretch_wid=5, stretch_len=1)
paleta_b.penup()
paleta_b.goto(350,0)

# Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)
pelota.dx = 2
pelota.dy = -2

# Puntuaciones
puntos_a = 0
puntos_b = 0

# Marcador
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(puntos_a, puntos_b), align="center", font=("Courier", 24, "normal"))

def paleta_a_arriba():
    y = paleta_a.ycor()
    if y < 230:
        y += 20
        paleta_a.sety(y)

def paleta_a_abajo():
    y = paleta_a.ycor()
    if y > -230:   
        y -= 20
        paleta_a.sety(y)


def paleta_b_arriba():
    y = paleta_b.ycor()
    y += 20
    paleta_b.sety(y)

def paleta_b_abajo():
    y = paleta_b.ycor()
    y -= 20
    paleta_b.sety(y)

# Teclado
wn.onkeypress(paleta_a_arriba, "Up")
wn.onkeypress(paleta_a_abajo, "Down")
wn.onkeypress(paleta_b_arriba, "s")
wn.onkeypress(paleta_b_abajo, "x")
wn.listen()

while True:
    wn.update()

    pelota.sety(pelota.ycor() + pelota.dy)
    pelota.setx(pelota.xcor() + pelota.dx)

    if pelota.ycor() > 290:
        pelota.sety(290)
        pelota.dy *= -1

    if pelota.ycor() < -290:
        pelota.sety(-290)
        pelota.dy *= -1

    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
        puntos_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(puntos_a, puntos_b), align="center", font=("Courier", 24, "normal"))

    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1
        puntos_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(puntos_a, puntos_b), align="center", font=("Courier", 24, "normal"))

    if pelota.xcor() < -340 and pelota.ycor() < paleta_a.ycor() + 50 and pelota.ycor() > paleta_a.ycor() - 50:
        pelota.dx *= -1 
        os.system("afplay bounce.wav&")
    
    elif pelota.xcor() > 340 and pelota.ycor() < paleta_b.ycor() + 50 and pelota.ycor() > paleta_b.ycor() - 50:
        pelota.dx *= -1
        os.system("afplay bounce.wav&")
