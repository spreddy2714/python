import turtle

def drawSquare(t, sz):
    """Drawing a square"""
    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
drawSquare(alex, 50)

wn.exitonclick()
