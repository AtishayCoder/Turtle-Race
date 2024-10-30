from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "orange", "yellow", "purple"]
y_positions = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for i in range(0, 6):
    t = Turtle("turtle")
    t.color(colors[i])
    t.penup()
    t.goto(-230, y_positions[i])
    all_turtles.append(t)

game_is_on = True
while game_is_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(1, 10))

        if turtle.xcor() > 225:
            if user_bet == turtle.color()[0]:
                print(f"You won! The {turtle.color()[0]} turtle is the winner.")
                game_is_on = False
            else:
                print(f"You lost. The {turtle.color()[0]} turtle is the winner.")
                game_is_on = False

screen.exitonclick()
