import re

class Square(object):
    def __init__(self, color):
        self.color = color
    def set(self, color):
        self.color = color
    def __str__(self):
        return "{0}".format(self.color)

class Face(object):
    def __init__(self, color):
        self.squares = [Square(color), Square(color), Square(color), Square(color), Square(color), Square(color), Square(color), Square(color), Square(color)]
        self.top_row = None
        self.bot_row = None
        self.left_row = None
        self.right_row = None

    def top_border(self):
        return [self.squares[0], self.squares[1], self.squares[2]]
    def bot_border(self):
        return [self.squares[6], self.squares[7], self.squares[8]]
    def left_border(self):
        return [self.squares[0], self.squares[3], self.squares[6]]
    def right_border(self):
        return [self.squares[2], self.squares[5], self.squares[8]]

    def link(self, top_row, bot_row, left_row, right_row):
        self.top_row = top_row
        self.bot_row = bot_row
        self.left_row = left_row
        self.right_row = right_row

    def rotate(self):
        switch = [self.squares[0].color, self.squares[1].color, self.squares[2].color]
        self.squares[0].set(self.squares[6].color)
        self.squares[1].set(self.squares[3].color)
        self.squares[2].set(switch[0])
        self.squares[3].set(self.squares[7].color)
        self.squares[6].set(self.squares[8].color)
        self.squares[7].set(self.squares[5].color)
        self.squares[8].set(switch[2])
        self.squares[5].set(switch[1])
        switch = [self.top_row[0].color, self.top_row[1].color, self.top_row[2].color]
        self.top_row[0].set(self.left_row[0].color)
        self.top_row[1].set(self.left_row[1].color)
        self.top_row[2].set(self.left_row[2].color)
        self.left_row[0].set(self.bot_row[0].color)
        self.left_row[1].set(self.bot_row[1].color)
        self.left_row[2].set(self.bot_row[2].color)
        self.bot_row[0].set(self.right_row[0].color)
        self.bot_row[1].set(self.right_row[1].color)
        self.bot_row[2].set(self.right_row[2].color)
        self.right_row[0].set(switch[0])
        self.right_row[1].set(switch[1])
        self.right_row[2].set(switch[2])

    def __str__(self):
        return ("{0} {1} {2}\n{3} {4} {5}\n{6} {7} {8}\n".format(self.squares[0],
            self.squares[1],
            self.squares[2],
            self.squares[3],
            self.squares[4],
            self.squares[5],
            self.squares[6],
            self.squares[7],
            self.squares[8]))

class Cube(object):
    def __init__(self):
        self.front = Face("G")
        self.left = Face("R")
        self.right = Face("O")
        self.top = Face("Y")
        self.bot = Face("W")
        self.back = Face("B")
        self.front.link(
            self.top.bot_border(),
            self.bot.top_border(),
            self.left.right_border(),
            self.right.left_border()
        )
        self.back.link(
            self.top.top_border(),
            self.bot.bot_border(),
            self.right.right_border(),
            self.left.left_border()
        )
        self.left.link(
            self.top.left_border(),
            self.bot.right_border(),
            self.back.right_border(),
            self.front.left_border()
        )
        self.right.link(
            self.top.right_border(),
            self.bot.left_border(),
            self.front.right_border(),
            self.back.left_border()
        )
        self.top.link(
            self.back.top_border(),
            self.front.top_border(),
            self.left.top_border(),
            self.right.top_border()
        )
        self.bot.link(
            self.front.bot_border(),
            self.back.bot_border(),
            self.right.bot_border(),
            self.left.bot_border()
        )

    def rotate_up(self):
        switch = self.front
        self.front = self.bot
        self.bot = self.back
        self.back = self.top
        self.top = switch

    def rotate_down(self):
        switch = self.front
        self.front = self.top
        self.top = self.back
        self.back = self.bot
        self.bot = switch

    def rotate_left(self):
        switch = self.front
        self.front = self.right
        self.right = self.back
        self.back = self.left
        self.left = switch

    def rotate_right(self):
        switch = self.front
        self.front = self.left
        self.left = self.back
        self.back = self.right
        self.right = switch

    def rotate_u(self):
        self.top.rotate()

    def __str__(self):
        def line(c, n):
            return c[n*5:n*5+5]

        empty = "     "
        front = re.sub('\n', '', self.front.__str__())
        back = re.sub('\n', '', self.back.__str__())
        left = re.sub('\n', '', self.left.__str__())
        right = re.sub('\n', '', self.right.__str__())
        top = re.sub('\n', '', self.top.__str__())
        bot = re.sub('\n', '', self.bot.__str__())
        string = ("Cube:\n" +
            empty         + " " + line(top, 0)   + " " +  empty          + "\n" +
            empty         + " " + line(top, 1)   + " " +  empty          + "\n" +
            empty         + " " + line(top, 2)   + " " +  empty          + "\n" +
            line(left, 0) + " " + line(front, 0) + " " +  line(right, 0) + "\n" +
            line(left, 1) + " " + line(front, 1) + " " +  line(right, 1) + "\n" +
            line(left, 2) + " " + line(front, 2) + " " +  line(right, 2) + "\n" +
            empty         + " " + line(bot, 0)   + " " +  empty          + "\n" +
            empty         + " " + line(bot, 1)   + " " +  empty          + "\n" +
            empty         + " " + line(bot, 2)   + " " +  empty          + "\n" +
            empty         + " " + line(back, 0)  + " " +  empty          + "\n" +
            empty         + " " + line(back, 1)  + " " +  empty          + "\n" +
            empty         + " " + line(back, 2)  + " " +  empty          + "\n")
        return string

    def isTopWhiteEdges(self):
        if self.top.squares[1] == "W"\
        and self.top.squares[3] == "W"\
        and self.top.squares[5] == "W"\
        and self.top.squares[7] == "W":
            return True
        return False
    def moveWhiteEdgeToTop(self):
        if self.front.squares[5] == "W":
            self.rotate("R")
        elif self.bottom.squares[5] == "W":
            self.rotate("R2")
        elif self.back.squares[3] == "W":
            self.rotate("R'")
    def getTopWhiteEdges(self):
        while not self.isTopWhiteEdges():
            self.moveWhiteEdgeToTop()
            while not self.top.squares[5] == "W":
                self.rotate("U'")
                self.rotatecube("Right")
                self.rotate("R")
                self.moveWhiteEdgeToTop()
            self.rotatecube("Right")

    def solve(self):
        self.getTopWhiteEdges()

