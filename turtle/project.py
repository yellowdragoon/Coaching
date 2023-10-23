import turtle as t
import time
import random

"""
Create two turtles that will represent the players.
Each turtle should be a different color.
The turtles should be the turtle shape.
Move the turtles to their starting positions without leaving a trace.
The second turtle should be directly below the first one.

Make a finish circle for each turtle/finish line.
Make a die by creating a list of integers 1-6.
Figure out how to use the random library in python to choose a random number from the list you have created.
"""
die_numbers = [1, 2, 3, 4, 5, 6]

t.color("red")
t.shape("turtle")

distance = 750

t.penup()
t.goto(-400, 300)
t.forward(distance)
t.pendown()
t.dot(50)
t.penup()
t.back(distance)

t2 = t.clone()
t2.goto(-400, 100)
t2.color("blue")
t2.forward(distance)
t2.pendown()
t2.dot(50)
t2.penup()
t2.back(distance)

steps_left_1 = distance
steps_left_2 = distance
speed = 30

while True:
    # For turtle 1, pick a random number from the list
    # Move that turtle forward by that number of steps
    # Use the time library to wait 0.5 seconds
    # Do the same for the second turtle
    steps = speed * random.choice(die_numbers)
    steps_left_1 -= steps

    if steps_left_1 <= 0:
        print("Turtle 1 won!")
        break

    t.forward(steps)
    time.sleep(0.5)

    steps = speed * random.choice(die_numbers)
    steps_left_2 -= steps

    if steps_left_2 <= 0:
        print("Turtle 2 won!")
        break

    t2.forward(steps)
    time.sleep(0.5)

t.mainloop()