import turtle
import random

s = turtle.getscreen()
t = turtle.Turtle()

x_len = 800
data_min = 10
data_max = 50
data = random.sample(range(data_min, data_max), 40)
spacer = x_len / ((len(data) * 2) - 1) # -1 for leaving out the initial spacer

def setup():
    t.speed('fastest')
    turtle.hideturtle()
    t.hideturtle()
    turtle.tracer(0, 0)

    t.penup()
    t.backward(x_len / 2)
    t.pendown()

def generateGraph():
    for idx, step in enumerate(data):
        step *= 2
        t.fillcolor(((1 - step / (data_max * 2),) * 3))
        if not idx == 0:
            t.forward(spacer)
        t.left(90)
        t.begin_fill()
        t.forward(step)
        t.right(90)
        t.forward(spacer)
        t.right(90)
        t.forward(step)
        t.end_fill()
        t.left(90)

def finish():
    turtle.update()
    s.exitonclick()

setup()
generateGraph()
finish()
