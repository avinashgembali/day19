from turtle import Turtle,Screen
import random
is_race_on = False
s = Screen()
s.setup(width=500, height=400)
user_input = s.textinput(title = "make your bet",prompt = "which turtle will win the race ? enter a color : ")
colors = ["red","orange","yellow","green","blue","purple"]
xc = -230
yc = -30
list = []
for col in colors:
    t = Turtle("turtle")
    t.color(col)
    t.penup()
    t.goto(x=xc, y=yc)
    yc += 28
    list.append(t)

if user_input:
    is_race_on = True
while is_race_on:
    for t in list:
        if t.xcor() > 230:
            is_race_on = False
            if t.fillcolor() == user_input:
                print(f"{t.fillcolor()} has won the race you are correct!")
            else:
                print(f"{t.fillcolor()} has won the race you lost!")
        move = random.randint(0,10)
        t.forward(move)
s.exitonclick()