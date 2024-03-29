from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []

for i in range(6):
    y_coordinate = -100 + i * 40
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinate)
    new_turtle.color(colors[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            is_race_on = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

if winner == user_bet:
    print(f"You've won! The {winner} turtle is the winner!")
else:
    print(f"You've lost! The {winner} turtle is the winner!")

screen.exitonclick()