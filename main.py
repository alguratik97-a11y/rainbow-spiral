# Program to draw a rainbow spiral using Turtle graphics

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Rainbow Spiral")

# Create a turtle instance
pen = turtle.Turtle()
pen.speed("fastest")
pen.width(2)

# List of rainbow colors
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Loop to draw the spiral
for i in range(100):
    # Select color dynamically using the modulo operator
    pen.color(colors[i % len(colors)])
    
    # Move forward and turn to create the spiral effect
    pen.forward(i * 2)
    pen.left(59)

# Keep the window open
turtle.done()
