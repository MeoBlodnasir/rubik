class Square(object):
    def __init__(self, color):
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
        self.squares[0].color = (self.squares[6].color)
        self.squares[1].color = (self.squares[3].color)
        self.squares[2].color = (switch[0])
        self.squares[3].color = (self.squares[7].color)
        self.squares[6].color = (self.squares[8].color)
        self.squares[7].color = (self.squares[5].color)
        self.squares[8].color = (switch[2])
        self.squares[5].color = (switch[1])

        switch = [self.top_row[0].color, self.top_row[1].color, self.top_row[2].color]
        self.top_row[0].color = (self.left_row[0].color)
        self.top_row[1].color = (self.left_row[1].color)
        self.top_row[2].color = (self.left_row[2].color)
        self.left_row[0].color = (self.bot_row[0].color)
        self.left_row[1].color = (self.bot_row[1].color)
        self.left_row[2].color = (self.bot_row[2].color)
        self.bot_row[0].color = (self.right_row[0].color)
        self.bot_row[1].color = (self.right_row[1].color)
        self.bot_row[2].color = (self.right_row[2].color)
        self.right_row[0].color = (switch[0])
        self.right_row[1].color = (switch[1])
        self.right_row[2].color = (switch[2])

    def rev_rotate(self):
        switch = [self.squares[0].color, self.squares[1].color, self.squares[2].color]
        self.squares[0].color = switch[2]
        self.squares[1].color = self.squares[5].color
        self.squares[2].color = self.squares[8].color
        self.squares[5].color = self.squares[7].color
        self.squares[8].color = self.squares[6].color
        self.squares[7].color = self.squares[3].color
        self.squares[6].color = switch[0]
        self.squares[3].color = switch[1]

        switch = [self.top_row[0].color, self.top_row[1].color, self.top_row[2].color]
        self.top_row[0].color = (self.right_row[0].color)
        self.top_row[1].color = (self.right_row[1].color)
        self.top_row[2].color = (self.right_row[2].color)
        self.right_row[0].color = (self.bot_row[0].color)
        self.right_row[1].color = (self.bot_row[1].color)
        self.right_row[2].color = (self.bot_row[2].color)
        self.bot_row[0].color = (self.left_row[0].color)
        self.bot_row[1].color = (self.left_row[1].color)
        self.bot_row[2].color = (self.left_row[2].color)
        self.left_row[0].color = (switch[0].color)
        self.left_row[1].color = (switch[1].color)
        self.left_row[2].color = (switch[2].color)

    def __str__(self):
        return ("{0} {1} {2}{3} {4} {5}{6} {7} {8}".format(self.squares[0],
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

    def rotate(self, rotate_str):
        switch = {
            "U": self.top.rotate,
            "D": self.bot.rotate,
            "R": self.right.rotate,
            "L": self.left.rotate,
            "F": self.front.rotate,
            "B": self.back.rotate,
            "U'": self.top.rev_rotate,
            "D'": self.bot.rev_rotate,
            "R'": self.right.rev_rotate,
            "L'": self.left.rev_rotate,
            "F'": self.front.rev_rotate,
            "B'": self.back.rev_rotate
        }
        func = switch.get(rotate_str)
        func()

    def __str__(self):
        def line(c, n):
            return c[n*5:n*5+5]

        empty = "     "
        front = self.front.__str__()
        back = self.back.__str__()
        left = self.left.__str__()
        right = self.right.__str__()
        top = self.top.__str__()
        bot = self.bot.__str__()
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

    def isBottomWhiteEdges(self):
        if self.bottom.squares[1] == "W"\
        and self.bottom.squares[3] == "W"\
        and self.bottom.squares[5] == "W"\
        and self.bottom.squares[7] == "W":
            return true
        return false

    def moveWhiteEdgeToTop(self):
        if self.front.squares[5] == "W":
            self.rotate("R")
        elif self.bottom.squares[5] == "W":
            self.rotate("R2")
        elif self.back.squares[3] == "W":
            self.rotate("R'")

    def moveWhiteEdgestoBottom(self):
        if self.right.squares[1] == self.right.squares[4]:
            self.rotate("R2")

    def getTopWhiteEdges(self):
        while not self.isTopWhiteEdges():
            self.moveWhiteEdgeToTop()
            while not self.top.squares[5] == "W":
                self.rotate("U'")
                self.rotate_right()
                self.rotate("R")
                self.moveWhiteEdgeToTop()
            self.rotate_right()

    def moveWhiteEdgesToBottom(self):
        while not self.isBottomWhiteEdges():
            self.moveWhiteEdgesToBottom()
            while not self.right.squares[1] == self.right.squares[4]:
                self.rotate("U")
                self.rotate_right()
                self.moveWhiteEdgesToBottom()
            self.rotate_right()

    def getCorrectCornerinTopLayer(self, col1, col2):
        i = 0
        while i < 4:
            if (self.front.squares[8] == "W" or self.front.squares[8] == col1 or self.front.squares[8] == col2)\
                    and (self.right.squares[6] == "W" or self.right.squares[6] == col1 or self.right.squares[6] == col2)\
                    and (self.bottom.squares[6] == "W" or self.bottom.squares[6] == col1 or self.bottom.squares[6] == col2):
                        self.rotate("R")
                        self.rotate("U")
                        self.rotate("R'")
                        self.rotate("U'")
                        return
            self.rotate_right()
            i += 1
                    
    def repositionCube(self):
        while not self.front.squares[4] == "G":
            self.rotate_right()

    def positionWhiteCornerOnTopRight(self, col1, col2):
        self.repositionCube()
        while not (self.front.squares[2] == "W" or self.front.squares[2] == col1 or self.front.squares[2] == col2)\
                and (self.right.squares[0] == "W" or self.right.squares[0] == col1 or self.right.squares[0] == col2)\
                and (self.top.squares[8] == "W" or self.top.squares[8] == col1 or self.bottom.squares[8] == col2):
                    self.rotate("U")
    def isBottomRightCornerCorrect(self, col1, col2):
        return self.front.squares[8] == self.front.squares[4]\
                and self.right.squares[6] == self.left.squares[4]\
                and self.bottom.squares[6] == "W"

    def getBottomWhiteCorners(self):
        i = 0
        while i < 4:
            self.getCorrectCornerinTopLayer(self.front.squares[4], self.left.squares[4])
            self.positionWhiteCornerOnTopRight(self.front.squares[4], self.left.squares[4])
            while not isBottomRightCornerCorrect(self.front.squares[4], self.left.squares[4]):
                self.rotate("R")
                self.rotate("U")
                self.rotate("R'")
                self.rotate("U'")
            i += 1
            self.rotate_right()
        

    def solve(self):
        self.getTopWhiteEdges()
        self.moveWhiteEdgesToBottom()
        self.getBottomWhiteCorners()

