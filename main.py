from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for i in range(6):
    y_coordinate = -100 + i * 40
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.goto(x=-230, y=y_coordinate)
    timmy.color(colors[i])

screen.exitonclick()