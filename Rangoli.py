# Simple Rangoli using Turtle

import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)
t.pensize(2)

colors = ["red", "blue", "green", "orange", "purple"]

# Draw circles in flower style
for i in range(36):
    t.color(colors[i % 5])
    t.circle(100)
    t.left(10)

# Center dot
t.penup()
t.goto(0, 0)
t.dot(20, "gold")

t.hideturtle()
turtle.done()