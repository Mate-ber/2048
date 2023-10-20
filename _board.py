import turtle
import random
STRING_DISTANCE = 100


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
                self.tur.write(self.cubs[i][j], align="left", font=("Courier", 20, "normal"))
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
        for j in range(self.board_width):
            for i in range(self.board_height-1, 0, -1):
                if self.cubs[i][j] != 0:
                    if self.cubs[i-1][j] == 0:
                        self.cubs[i-1][j] = self.cubs[i][j]
                        self.cubs[i][j] = 0

        for j in range(self.board_width):
            for i in range(self.board_height-1):
                if self.cubs[i][j] != 0:
                    if self.cubs[i][j] == self.cubs[i+1][j]:
                        self.cubs[i][j] += self.cubs[i+1][j]
                        self.cubs[i+1][j] = 0

        for j in range(self.board_width):
            for i in range(self.board_height - 1, 0, -1):
                if self.cubs[i][j] != 0:
                    if self.cubs[i - 1][j] == 0:
                        self.cubs[i - 1][j] = self.cubs[i][j]
                        self.cubs[i][j] = 0
        self.generate()

    def down(self):
        for j in range(self.board_width):
            for i in range(self.board_height-1):
                if self.cubs[i][j] != 0:
                    if self.cubs[i+1][j] == 0:
                        self.cubs[i+1][j] = self.cubs[i][j]
                        self.cubs[i][j] = 0

        for j in range(self.board_width):
            for i in range(self.board_height-1, 0, -1):
                if self.cubs[i][j] != 0:
                    if self.cubs[i][j] == self.cubs[i-1][j]:
                        self.cubs[i][j] += self.cubs[i-1][j]
                        self.cubs[i-1][j] = 0
        for j in range(self.board_width):
            for i in range(self.board_height-1):
                if self.cubs[i][j] != 0:
                    if self.cubs[i+1][j] == 0:
                        self.cubs[i+1][j] = self.cubs[i][j]
                        self.cubs[i][j] = 0
        self.generate()

    def left(self):
        for i in range(self.board_height):
            for j in range(self.board_width - 1, 0, -1):
                if self.cubs[i][j] != 0:
                    if self.cubs[i][j - 1] == 0:
                        self.cubs[i][j - 1] = self.cubs[i][j]
                        self.cubs[i][j] = 0

        for i in range(self.board_height):
            for j in range(self.board_width - 1):
                if self.cubs[i][j] != 0:
                    if self.cubs[i][j] == self.cubs[i][j + 1]:
                        self.cubs[i][j] += self.cubs[i][j + 1]
                        self.cubs[i][j + 1] = 0

        for i in range(self.board_height):
            for j in range(self.board_width - 1, 0, -1):
                if self.cubs[i][j] != 0:
                    if self.cubs[i][j - 1] == 0:
                        self.cubs[i][j - 1] = self.cubs[i][j]
                        self.cubs[i][j] = 0
        self.generate()

    def right(self):
        for i in range(self.board_height):
            for j in range(self.board_width - 1):
                if self.cubs[i][j] != 0:
                    if self.cubs[i][j + 1] == 0:
                        self.cubs[i][j + 1] = self.cubs[i][j]
                        self.cubs[i][j] = 0

        for i in range(self.board_height):
            for j in range(self.board_width - 1, 0, -1):
                if self.cubs[i][j] != 0:
                    if self.cubs[i][j] == self.cubs[i][j - 1]:
                        self.cubs[i][j] += self.cubs[i][j - 1]
                        self.cubs[i][j - 1] = 0

        for i in range(self.board_height):
            for j in range(self.board_width - 1):
                if self.cubs[i][j] != 0:
                    if self.cubs[i][j + 1] == 0:
                        self.cubs[i][j + 1] = self.cubs[i][j]
                        self.cubs[i][j] = 0
        self.generate()

    def if_win(self):
        for i in range(self.board_height):
            for j in range(self.board_width):
                if self.cubs[i][j] == 2048:
                    return True
        return False

    def print_win(self):
        self.tur.clear()
        win = turtle.Turtle()
        win.color("black")
        win.hideturtle()
        win.goto(0, 0)
        win.write(f"You Won!", align="center", font=("Courier", 30, "normal"))

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
        self.tur.clear()
        lose = turtle.Turtle()
        lose.color("black")
        lose.hideturtle()
        lose.goto(0, 0)
        lose.write(f"You Lost!", align="center", font=("Courier", 30, "normal"))








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
