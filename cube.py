import re

class Square(object):
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return "{0}".format(self.color)

class Face(object):
    def __init__(self, color):
        self.squares = [color, color, color, color, color, color, color, color, color]
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

    def __str__(self):

        def line(c, n):
            return c[n*5:n*5+5]

        empty = "     "
        front = re.sub('\n', '', self.front.__str__())
        back = re.sub('\n', '', self.back.__str__())
        left = re.sub('\n', '', self.back.__str__())
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
