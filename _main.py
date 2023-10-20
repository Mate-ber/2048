import time
from turtle import Screen
from _board import Logic
from _board import Grid

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

logic = Logic()
grid = Grid()

screen.listen()
screen.onkeypress(logic.up, "Up")
screen.onkeypress(logic.down, "Down")
screen.onkeypress(logic.right, "Right")
screen.onkeypress(logic.left, "Left")

while True:
    if logic.if_win():
        grid.clear()
        logic.print_win()
    if logic.if_lose():
        grid.clear()
        logic.print_lose()

    time.sleep(.1)
    screen.update()

screen.exitonclick()
