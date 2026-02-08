import turtle

# Set up the screen and turtle
t = turtle.Turtle()
t.speed(3)  # Moderate speed to see the drawing process
t.pensize(5)
#body figure
def draw_boy():
    # Head
    t.circle(40)  # Draws a circle for the head
    
    # Body
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.right(90)
    t.forward(100)  # Main vertical line for the body
    
    # Legs
    t.left(45)
    t.forward(60)   # Left leg
    t.backward(60)
    t.right(90)
    t.forward(60)   # Right leg
    t.backward(60)
    
    # Arms
    t.left(45)
    t.penup()
    t.goto(0, -30)  # Move to the "chest" area
    t.pendown()
    t.left(90)
    t.forward(50)   # Left arm
    t.backward(100) # Right arm
    
    # Hide turtle and keep window open
    t.hideturtle()
    turtle.done()

draw_boy()

