import turtle
import time

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Name Pulse Rangoli")

# Create turtle
t = turtle.Turtle()
t.speed(0)
t.width(2)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw rangoli pattern
for i in range(72):
    t.color(colors[i % 6])
    t.circle(100)
    t.left(5)

# Create name pulse
name = screen.textinput("Your Name", "Enter your name:")
pulse = turtle.Turtle()
pulse.color("white")
pulse.hideturtle()
pulse.penup()
pulse.goto(0, -20)

# Animate pulsing name
for size in range(10, 30):
    pulse.clear()
    pulse.write(name, align="center", font=("Arial", size, "bold"))
    time.sleep(0.1)

for size in range(30, 10, -1):
    pulse.clear()
    pulse.write(name, align="center", font=("Arial", size, "bold"))
    time.sleep(0.1)

# Keep window open
turtle.done()