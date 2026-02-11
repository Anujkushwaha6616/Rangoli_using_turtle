# Random hart shape print
import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Black background makes colors pop
t = turtle.Turtle()
t.speed(0) # Fastest speed

def draw_heart(color, size, x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.pendown()
    t.color(color)
    t.begin_fill()
    
    # Heart drawing logic
    t.left(140)
    t.forward(size)
    t.circle(-size/2, 200) # Left lobe
    t.left(120)
    t.circle(-size/2, 200) # Right lobe
    t.forward(size)
    
    t.end_fill()

# List of vibrant colors
colors = ["red", "pink", "purple", "gold", "cyan", "magenta", "orange"]

# Draw 15 hearts in random locations
for _ in range(15):
    random_color = random.choice(colors)
    random_size = random.randint(20, 60)
    random_x = random.randint(-250, 250)
    random_y = random.randint(-200, 200)
    
    draw_heart(random_color, random_size, random_x, random_y)

t.hideturtle()
turtle.done()

