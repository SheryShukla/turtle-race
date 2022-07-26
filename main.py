from turtle import*
import random

sc = Screen()
sc.setup(width=500, height=400)
sc.bgcolor("Black")
sc.title("THE TURTLE RACE")

# Making a bet
user_bet = sc.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ").lower()

colors = ["Red", "Green", "Blue", "Yellow", "Pink"]
y_p = [ -60, -30, 0, 30, 60]

is_race_on = False
all_turtles = []

# Turtles are designed
for turtle_index in range(0, 5):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.speed(10)
    all_turtles.append(tim)
    tim.goto(x=-230,y=y_p[turtle_index])

# bet
if user_bet:
    is_race_on=True
    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor()>250:
                is_race_on = False
                winner = turtle.pencolor()
                if winner == user_bet:
                    print("You won!!!!! :)")
                else:
                    print("You lose :(")
                    print(f"The winner is {winner}")

            r_distance = random.randint(0, 10)
            turtle.forward(r_distance)

sc.exitonclick()

