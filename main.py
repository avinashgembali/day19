from turtle import Turtle,Screen

t = Turtle()
s = Screen()
def move():
    t.forward(10)
def back():
    t.backward(10)
def aclock():
    t.right(-10)
    # setheading method also can be used in the way t.setheading(t.heading()+10)
def clock():
    t.right(10)
    # setheading method also can be used in the way t.setheading(t.heading()-10)
def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
s.listen()
s.onkey(move, "w")
s.onkey(back, "s")
s.onkey(aclock, "a")
s.onkey(clock, "d")
s.onkey(clear,"c")
s.exitonclick()