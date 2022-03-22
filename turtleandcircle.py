import turtle
t = turtle.Pen()
t.color('pink')
t.shape('turtle')


def Rectangle():
    for i in range(4):
        t.forward(100)
        t.left(90)
        t.circle(90)

def Go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

Rectangle()
Go(10,10)
Rectangle()
Go(20,20)
Rectangle()
Go(30,30)
Rectangle()
Go(40,40)
