from turtle import *
from random import randint
import turtle
import sys
timcontrols = "CONTROLS: \n \n 'shift + q' = Pen Down,\n 'q' = Pen Up,\n 'r' = Custom Colour Changing,\n 'shift + e' = Show,\n 'e' = Hide,\n 'delete' = kill.\n To make Tim write on the screen, press 'tab' then input what Tim should say\n when prompted! :)'"
garycontrols = "CONTROLS: \n \n 'shift + o' = Pen Down,\n 'o' = Pen Up,\n 'l' = Custom Colour Changing,\n 'shift + p' = Show,\n 'p' = Hide,\n 'delete' = kill.\n To make Gary write on the screen, press 'Return (Enter)' then input what Gary should say\n when prompted! :)'"
def up():
    tim.forward(20)
def right():
    tim.right(10)
def left():
    tim.left(20)
def down():
    tim.backward(20)
def kill():
    quit()
def pen_up():
    print("Pen Up")
    tim.penup()
def pen_down():
    print("Pen Down")
    tim.pendown()
def color_change():
    colour = input('What colour shall Tim be? ')
    tim.color(colour)
def color_change2():
    tim.color("Tomato")
def show():
    print("Tim is Visible")
    tim.showturtle()
def hide():
    print("Tim is Hidden")
    tim.hideturtle()
def write_():
    txt = input("What shall Tim write? ")
    tim.write(txt)
    print("Tim has said,", txt)
def write_undo():
    tim.undo()
def tim_control():
    print(timcontrols)

def clear_():
    turtle.clear()


pg = Screen()
pg.title('Turtle Adventure')
penup()
speed(0)
goto(10000,0)

#Tim
tim = Turtle()
tim.color("tomato")
tim.shape('turtle')
tim.speed(0.5)
tim.width(5)
tim.setheading(0)

#Gary:
gary = Turtle()
gary.color("black")
gary.shape('turtle')
gary.speed(0.5)
gary.width(5)
gary.setheading(0)
gary.hideturtle()
def up2():
    gary.forward(20)
def right2():
    gary.right(10)
def left2():
    gary.left(20)
def down2():
    gary.backward(20)
def pen_up2():
    print("Gary.Pen Up")
    gary.penup()
def pen_down2():
    print("Gary.Pen Down")
    gary.pendown()
def color_change2():
    colour_gary = input('What colour shall Gary be? ')
    gary.color(colour_gary)
def show2():
    print("Gary is Visible")
    gary.showturtle()
def hide2():
    print("Gary is Hidden")
    gary.hideturtle()
def write_2():
    txt_gary = input("What shall Gary write? ")
    gary.write(txt_gary)
    print("Gary has said,", txt_gary)
def Gary_control():
    print(garycontrols)
def Multiplayer():
    gary.showturtle()
    print("yay friends")
    print('')
    print(garycontrols)
def Singleplayer():
    gary.hideturtle()
    print("Goodbye")
def x():
    tim.write('X')
def o():
    gary.write('O')

print(timcontrols)
turtle.listen()

turtle.onkey(up, 'w')
turtle.onkey(down, 's')
turtle.onkey(right, 'd')
turtle.onkey(left, 'a')
turtle.onkey(kill, 'Delete')
turtle.onkey(pen_up, 'q')
turtle.onkey(pen_down, 'Q')
turtle.onkey(color_change, 'r')
turtle.onkey(hide, 'e')
turtle.onkey(show, 'E')
turtle.onkey(write_, 'Tab')
turtle.onkey(clear_, '1')
turtle.onkey(x, 'x')
#Gary
turtle.onkey(up2, 'Up')
turtle.onkey(down2, 'Down')
turtle.onkey(right2, 'Right')
turtle.onkey(left2, 'Left')
turtle.onkey(pen_up2, 'o')
turtle.onkey(pen_down2, 'O')
turtle.onkey(color_change2, 'l')
turtle.onkey(hide2, 'p')
turtle.onkey(show2, 'P')
turtle.onkey(write_2, 'Return')
turtle.onkey(o, 'c')

#Tic Tac Toe
def tic_tac_toe():
    tim.penup()
    gary.penup()
    gary.color('white')
    # draw board 
    pieces = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    turn = "X"

    turtle.clear()
    turtle.setup(600, 600)
    turtle.bgcolor("black")

    turtle.color("white")
    turtle.hideturtle()
    turtle.speed('fastest')
    turtle.width(10)
    turtle.up()
    
    # Horizontal bars
    turtle.goto(-300, 100)
    turtle.down()
    turtle.forward(600)
    turtle.up()
    turtle.goto(-300, -100)
    turtle.down()
    turtle.forward(600)
    turtle.up()

    # Vertical bars
    turtle.goto(-100, 300)
    turtle.setheading(-90)
    turtle.down()
    turtle.forward(600)
    turtle.up()
    turtle.goto(100, 300)
    turtle.down()
    turtle.forward(600)
    turtle.up()

    print("'x' = draw an X and 'c' = draw a C \n \n Gary is 'O' and Tim is 'X'")
