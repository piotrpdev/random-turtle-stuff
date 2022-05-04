from time import sleep
import turtle

s = turtle.getscreen()
t = turtle.Turtle()

def setup():
    turtle.mode("logo")
    t.speed('fastest')
    turtle.hideturtle()
    t.hideturtle()
    turtle.tracer(0, 0)

def createClock():
    t.up()
    t.rt(90)
    t.fd(100)
    t.lt(90)
    t.down()
    t.circle(100)
    t.up()
    t.lt(90)
    t.fd(100)
    t.down()

def createHands(degrees):
    t.seth(degrees)
    t.fd(80)

setup()
createClock()

i = 0

while True:
    createHands(i * 6)
    turtle.update()
    if i == 59:
        i = 0
    else:
        i += 1
    sleep(1)
    t.undo()