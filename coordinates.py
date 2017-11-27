#This is how to import Turtle module
'''
import turtle
turtle.forward(90)
turtle.right(120)
turtle.forward(90)
turtle.left(120)
'''



#Example
import turtle
turtle.setup(900,400)
name = turtle.Screen()
name.title("Drawing boxes")
name.bgcolor("blue")
turtle.color("red")


alex =turtle.Turtle()
for i in [0,1,2,3]:
    alex.forward(50)
    alex.left(90)


import turtle
alex = turtle.Turtle()
for i in [0,1,2,3]:
    alex.backward(100)
    alex.right(90)
    
import turtle
alex =turtle.Turtle()
for i in [0,1,2,3]:
    alex.forward(50)
    alex.right(90)

import turtle
alex = turtle.Turtle()
for i in [0,1,2,3]:
    alex.backward(100)
    alex.left(90)
