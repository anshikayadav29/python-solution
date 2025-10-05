# 🎨 Random AI-like Abstract Art Generator
import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.width(2)
t.hideturtle()

colors = ["#FF007F", "#7FFF00", "#00FFFF", "#FFD700", "#FF4500", "#8A2BE2"]

# Draw random abstract art
for i in range(150):
    t.color(random.choice(colors))
    t.pensize(random.randint(1, 4))
    t.forward(random.randint(20, 100))
    t.right(random.randint(45, 180))
    t.circle(random.randint(10, 80))
    t.left(random.randint(20, 170))
    if i % 10 == 0:
        t.penup()
        t.goto(random.randint(-200, 200), random.randint(-200, 200))
        t.pendown()

turtle.done()
