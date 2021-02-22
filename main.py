from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()  # creates a Screen object
screen.setup(width=500, height=400)  # sets the size of the screen
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y_positions = [-70, -40, -10, 20, 50, 80]  # lists stores the different y-positions for the start line
all_turtles = []  # list for all our turtle instances


for index in range(0, 6):  # generates six turtles to be positioned on the same x-coordinate in a start position
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(-230, y_positions[index])
    new_turtle.color(colors[index])
    all_turtles.append(new_turtle)

if user_bet:  # if the user has chose which turtle will win
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False  # stops the race
            winning_color = turtle.pencolor()  # stores the color of the winning turtle
            if winning_color == user_bet:
                print(f"You have won, the {winning_color} is the winner!")
            else:
                print(f"You have lost, the {winning_color} is the winner!")

        random_distance = random.randint(0, 10)  # generates a random distance
        turtle.forward(random_distance)  # move each of the turtles by a random distance
















screen.exitonclick()
