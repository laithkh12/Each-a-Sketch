from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    newHeading = tim.heading() + 10
    tim.setheading(newHeading)

def turn_right():
    newHeading = tim.heading() - 10
    tim.setheading(newHeading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "r")
screen.onkey(clear, "c")
screen.exitonclick()
