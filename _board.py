import turtle
import random
import time
STRING_DISTANCE = 100
turtle_colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink"]
colors = {0: "black"}
it = 2
while it <= 2048:
    colors.update({it: random.choice(turtle_colors)})
    it *= 2


class Logic:
    def __init__(self):
        self.cubs = [[0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0],
                     [0, 0, 0, 0]]
        self.board_height = 4
        self.board_width = 4
        self.tur = turtle.Turtle()
        self.tur.penup()
        self.tur.hideturtle()
        self.tur.goto(0, 0)
        self.generate()

    def print(self):
        self.tur.clear()
        self.tur.goto(-200, 200)
        xcor = -200
        ycor = 200
        for i in range(0, self.board_height):
            for j in range(0, self.board_width):
                key = self.cubs[i][j]
                self.tur.pencolor(colors[key])
                self.tur.write(self.cubs[i][j], align="left", font=("Comic Sans MS", 25, "normal"))
                xcor += STRING_DISTANCE
                self.tur.goto(xcor, ycor)
            xcor -= (4 * STRING_DISTANCE)
            ycor -= STRING_DISTANCE
            self.tur.goto(xcor, ycor)

    def generate(self):
        cors = []
        for i in range(self.board_height):
            for j in range(self.board_width):
                if self.cubs[i][j] == 0:
                    cors.append((i, j))
        choice = random.choice(cors)
        self.cubs[choice[0]][choice[1]] = 2
        self.print()

    def up(self):
        self.move_up()
        for j in range(self.board_width):
            for i in range(self.board_height-1):
                if self.cubs[i][j] != 0:
                    if self.cubs[i][j] == self.cubs[i+1][j]:
                        self.cubs[i][j] += self.cubs[i+1][j]
                        self.cubs[i+1][j] = 0
        self.move_up()
        self.generate()

    def move_up(self):
        for j in range(self.board_width):
            for i in range(self.board_height):
                z = i
                while z > 0 and self.cubs[z-1][j] == 0:
                    self.cubs[z-1][j] = self.cubs[z][j]
                    self.cubs[z][j] = 0
                    z -= 1

    def down(self):
        self.move_down()
        for j in range(self.board_width):
            for i in range(self.board_height-1, 0, -1):
                if self.cubs[i][j] != 0:
                    if self.cubs[i][j] == self.cubs[i-1][j]:
                        self.cubs[i][j] += self.cubs[i-1][j]
                        self.cubs[i-1][j] = 0
        self.move_down()
        self.generate()

    def move_down(self):
        for j in range(self.board_width):
            for i in range(self.board_height-1, -1, -1):
                if self.cubs[i][j] != 0:
                    z = i
                    while z < self.board_height-1 and self.cubs[z + 1][j] == 0:
                        self.cubs[z + 1][j] = self.cubs[z][j]
                        self.cubs[z][j] = 0
                        z += 1

    def left(self):
        self.move_left()
        for i in range(self.board_height):
            for j in range(self.board_width - 1):
                if self.cubs[i][j] != 0:
                    if self.cubs[i][j] == self.cubs[i][j + 1]:
                        self.cubs[i][j] += self.cubs[i][j + 1]
                        self.cubs[i][j + 1] = 0
        self.move_left()
        self.generate()

    def move_left(self):
        for i in range(self.board_height):
            for j in range(self.board_width):
                if self.cubs[i][j] != 0:
                    z = j
                    while z > 0 and self.cubs[i][z-1] == 0:
                        self.cubs[i][z-1] = self.cubs[i][z]
                        self.cubs[i][z] = 0
                        z -= 1

    def right(self):
        self.move_right()
        for i in range(self.board_height):
            for j in range(self.board_width - 1, 0, -1):
                if self.cubs[i][j] != 0:
                    if self.cubs[i][j] == self.cubs[i][j - 1]:
                        self.cubs[i][j] += self.cubs[i][j - 1]
                        self.cubs[i][j - 1] = 0
        self.move_right()
        self.generate()

    def move_right(self):
        for i in range(self.board_height):
            for j in range(self.board_width - 1, -1, -1):
                if self.cubs[i][j] != 0:
                    z = j
                    while z < self.board_width-1 and self.cubs[i][z+1] == 0:
                        self.cubs[i][z+1] = self.cubs[i][z]
                        self.cubs[i][z] = 0
                        z += 1

    def if_win(self):
        for i in range(self.board_height):
            for j in range(self.board_width):
                if self.cubs[i][j] == 2048:
                    return True
        return False

    def print_win(self):
        time.sleep(0.3)
        self.tur.clear()
        win = turtle.Turtle()
        win.color("black")
        win.hideturtle()
        win.goto(0, 0)
        win.write(f"You Won!", align="center", font=("Comic Sans MS", 30, "normal"))

    def if_lose(self):
        for i in range(self.board_height):
            for j in range(self.board_width):
                if self.cubs[i][j] == 0:
                    return False
                if i != 3 and self.cubs[i][j] == self.cubs[i+1][j]:
                    return False
                if i != 0 and self.cubs[i][j] == self.cubs[i-1][j]:
                    return False
                if j != 3 and self.cubs[i][j] == self.cubs[i][j+1]:
                    return False
                if j != 0 and self.cubs[i][j] == self.cubs[i][j-1]:
                    return False
        return True

    def print_lose(self):
        time.sleep(0.3)
        self.tur.clear()
        lose = turtle.Turtle()
        lose.color("black")
        lose.hideturtle()
        lose.goto(0, 0)
        lose.write(f"You Lost!", align="center", font=("Comic Sans MS", 30, "normal"))




class Grid:
    def __init__(self):
        self.grid_d = turtle.Turtle()
        self.grid_d.color("black")
        self.grid_d.hideturtle()
        self.draw_grid()


    def draw_grid(self):
        xcor = -215
        ycor = 240
        for i in range(5):
            self.change_cor(xcor, ycor)
            self.for_10()
            ycor -= STRING_DISTANCE
        self.grid_d.right(90)
        xcor = -215
        ycor = 240
        for i in range(5):
            self.change_cor(xcor, ycor)
            self.for_10()
            xcor += STRING_DISTANCE

    def for_10(self):
        for i in range(20):
            self.grid_d.forward(20)

    def change_cor(self, x, y):
        self.grid_d.penup()
        self.grid_d.goto(x, y)
        self.grid_d.pendown()

    def clear(self):
        self.grid_d.clear()
