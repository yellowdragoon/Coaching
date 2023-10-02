import turtle as t
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

t.penup()
t.goto(-400, 300)

t2 = t.clone()
t2.goto(-400, 100)

t.color("red")
t2.color("blue")

t.shape("turtle")
t2.shape("turtle")

t.mainloop()