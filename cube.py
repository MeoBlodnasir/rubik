class Square(object):
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return "{0}".format(self.color)

class Face(object):
    def __init__(self, color):
        self.squares = [color, color, color, color, color, color, color, color, color]
        self.up_row = None
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
    def link(self, up_row, bot_row, left_row, right_row):
        self.up_row = up_row
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

    def __str__(self):
        return "FRONT\n{0}\nLEFT\n{1}\nRIGHT\n{2}\nTOP\n{3}\nBOTTOM\n{4}\nBACK\n{5}\n___________________________".format(self.front, self.left, self.right, self.top, self.bot, self.back)
