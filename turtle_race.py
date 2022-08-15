import tkinter.messagebox
from turtle import Turtle, Screen
from tkinter import messagebox
import random

screen = Screen()

def turtle_race():
    screen.clear()
    color = ["black",  "green", "violet", "orange", "yellow", "red", "blue",
             "gray"]
    starting_place = [-30,33,-95,100,-165,160,-225,227,]
    screen.bgpic("turtle_race.gif")
    screen.setup(width=850,height=650)
    turtle_list = []

    guess = screen.textinput("Guess the Color of the wining Turtle",f"Choose a Color "
     f"{color[0].title()},{color[1].title()},{color[2].title()},{color[3].title()},{color[4].title()},{color[5].title()},"
                                                                    f"{color[6].title()},{color[7].title()}").lower()

    for x in range(len(starting_place)):
        tummy = Turtle()
        tummy.shape("turtle")
        tummy.shapesize(2)
        tummy.color(color[x])
        tummy.penup()
        tummy.speed("fastest")
        tummy.goto(x=-355, y=starting_place[x])
        turtle_list.append(tummy)

    reach_not_the_end = True
    while reach_not_the_end:
        for tummy in turtle_list:
            tummy.forward(random.randint(10,20))
            tummy.speed(0)
            if tummy.xcor() >= 292:
                reach_not_the_end = False
                winner = tummy.fillcolor()
                if len(tummy.color()) < 3:
                    if winner == guess.lower():
                        messagebox.showinfo("Congratulation! ",f"You are the winner,You guessed {guess.title()}")
                    else:
                        messagebox.showinfo("Sorry",f"You guess Wrong, You guessed {guess.title()},But The winner is {winner.title()}")

                break

turtle_race()
while screen.textinput("Do you want to play the game again?","Enter 'y' to continue 'n' to finish ").lower() == "y":
    turtle_race()

screen.exitonclick()
