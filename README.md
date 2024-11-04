# Turtle Graphics Control Program

This project is a simple Python program that uses the Turtle graphics library to create an interactive drawing environment. Control the movement of the turtle on the screen using specific keys to draw shapes, move around, and reset the screen.

## Features
- **Move Forwards** - Move the turtle forward by 10 units with the `w` key.
- **Move Backwards** - Move the turtle backward by 10 units with the `s` key.
- **Turn Left** - Rotate the turtle 10 degrees to the left with the `a` key.
- **Turn Right** - Rotate the turtle 10 degrees to the right with the `r` key.
- **Clear Screen** - Clear all drawings and reset the turtle's position with the `c` key.

## Code Overview

### Importing Modules
We use the Turtle and Screen classes from the `turtle` module to create our drawing environment and capture keyboard events.

```python
from turtle import Turtle, Screen
# Setting Up the Turtle and Screen
#  Create a Turtle instance called tim.
#  Create a Screen instance called screen to manage our interactive window.
tim = Turtle()
screen = Screen()

# Each function corresponds to a specific turtle movement or action triggered by key presses.
#  Moves the turtle forward by 10 units.
def move_forwards():
    tim.forward(10)
#  Moves the turtle backward by 10 units.
def move_backwards():
    tim.backward(10)
#  Turns the turtle 10 degrees to the left.
def turn_left():
    newHeading = tim.heading() + 10
    tim.setheading(newHeading)
#  Turns the turtle 10 degrees to the right.
def turn_right():
    newHeading = tim.heading() - 10
    tim.setheading(newHeading)
#  Clears the screen, resets the turtle's position, and puts the pen down.
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# Listening for Key Presses
#  The screen.listen() function enables the screen to detect key presses, and we use screen.onkey() to bind each key to its respective function.
screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "r")
screen.onkey(clear, "c")


# Exit on Click
#  The program will keep the screen open until a mouse click closes it.
screen.exitonclick()
```

## Requirements
- Python 3.x
- Turtle graphics library (standard in Python)

## How to Run
1. Clone the repository or download the script.
2. Run the program using:
```bash
python your_script_name.py
```
3. Use the keys w, s, a, r, and c to control the turtle!

## License
This project is open-source and available under the MIT License.



Enjoy exploring Turtle graphics with this interactive program!
