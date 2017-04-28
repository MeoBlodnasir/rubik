import random
import time

class Square(object):
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return "{0}".format(self.color)
    def __eq__(self, other):
        return self.color == other.color

class Face(object):
    def __init__(self, name, color):
        self.name = name
        self.squares = [Square(color), Square(color), Square(color), Square(color), Square(color), Square(color), Square(color), Square(color), Square(color)]
        self.top_row = None
        self.bot_row = None
        self.left_row = None
        self.right_row = None

    def top_border(self):
        return [self.squares[0], self.squares[1], self.squares[2]]
    def right_border(self):
        return [self.squares[2], self.squares[5], self.squares[8]]
    def bot_border(self):
        return [self.squares[8], self.squares[7], self.squares[6]]
    def left_border(self):
        return [self.squares[6], self.squares[3], self.squares[0]]

    def link(self, top_row, bot_row, left_row, right_row):
        self.top_row = top_row
        self.right_row = right_row
        self.bot_row = bot_row
        self.left_row = left_row

    def rotate_borders(self):
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

    def rev_rotate_borders(self):
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
        self.left_row[0].color = (switch[0])
        self.left_row[1].color = (switch[1])
        self.left_row[2].color = (switch[2])

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

    def rotate_with_borders(self):
        self.rotate()
        self.rotate_borders()
        return self.name

    def rev_rotate_with_borders(self):
        self.rev_rotate()
        self.rev_rotate_borders()
        return self.name

    def __str__(self):
        return ("{0} {1} {2}{3} {4} {5}{6} {7} {8}".format(
            self.squares[0],
            self.squares[1],
            self.squares[2],
            self.squares[3],
            self.squares[4],
            self.squares[5],
            self.squares[6],
            self.squares[7],
            self.squares[8]))

class Cube(object):

    def link_all(self):
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
            self.bot.left_border(),
            self.back.right_border(),
            self.front.left_border()
        )
        self.right.link(
            self.top.right_border(),
            self.bot.right_border(),
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
            self.left.bot_border(),
            self.right.bot_border()
        )

    def __init__(self):
        self.display = False
        self.debug = False
        self.front = Face("F", "G")
        self.left = Face("L", "R")
        self.right = Face("R", "O")
        self.top = Face("U", "Y")
        self.bot = Face("D", "W")
        self.back = Face("B", "B")
        self.link_all()

    def rotate_up(self):
        switch = self.front
        self.front = self.bot
        self.bot = self.back
        self.bot.rotate()
        self.bot.rotate()
        self.back = self.top
        self.back.rotate()
        self.back.rotate()
        self.top = switch
        self.right.rotate()
        self.left.rev_rotate()
        self.link_all()

    def rotate_down(self):
        switch = self.front
        self.front = self.top
        self.top = self.back
        self.top.rotate()
        self.top.rotate()
        self.back = self.bot
        self.back.rotate()
        self.back.rotate()
        self.bot = switch
        self.right.rev_rotate()
        self.left.rotate()
        self.link_all()

    def rotate_right(self):
        switch = self.front
        self.front = self.right
        self.right = self.back
        self.back = self.left
        self.left = switch
        self.top.rotate()
        self.bot.rev_rotate()
        self.link_all()

    def rotate_left(self):
        switch = self.front
        self.front = self.left
        self.left = self.back
        self.back = self.right
        self.right = switch
        self.top.rev_rotate()
        self.bot.rotate()
        self.link_all()

    def rotate(self, rotate_str):
        count = 1
        if "'2" in rotate_str:
            raise "Invalid format: '2"

        if "2" in rotate_str:
            rotate_str = rotate_str[:-1]
            count = 2

        switch = {
            "U": self.top.rotate_with_borders,
            "D": self.bot.rotate_with_borders,
            "R": self.right.rotate_with_borders,
            "L": self.left.rotate_with_borders,
            "F": self.front.rotate_with_borders,
            "B": self.back.rotate_with_borders,
            "U'": self.top.rev_rotate_with_borders,
            "D'": self.bot.rev_rotate_with_borders,
            "R'": self.right.rev_rotate_with_borders,
            "L'": self.left.rev_rotate_with_borders,
            "F'": self.front.rev_rotate_with_borders,
            "B'": self.back.rev_rotate_with_borders
        }
        func = switch.get(rotate_str)

        move_name = ""
        for i in range(count):
            move_name = func()

        if self.display:
            if self.debug:
                print(self)
                time.sleep(1/100.0)
                for i in range(10):
                    print("\033[F",end="")
            else:
                if len(rotate_str) > 1:
                    move_name += rotate_str[1:]
                if count == 2:
                    move_name += "2"
                print(move_name, end = " ")

    def __str__(self):
        def line(cube_str, nline):
            return cube_str[nline*5:nline*5+5]

        empty = "     "
        front = self.front.__str__()
        back = self.back.__str__()
        left = self.left.__str__()
        right = self.right.__str__()
        top = self.top.__str__()
        bot = self.bot.__str__()
        string = (
            empty         + " " + line(top, 0)   + " " +  empty          + "\n" +
            empty         + " " + line(top, 1)   + " " +  empty          + "\n" +
            empty         + " " + line(top, 2)   + " " +  empty          + "\n" +
            line(left, 0) + " " + line(front, 0) + " " +  line(right, 0) + " " + line(back, 0)  +  "\n" +
            line(left, 1) + " " + line(front, 1) + " " +  line(right, 1) + " " + line(back, 1)  +  "\n" +
            line(left, 2) + " " + line(front, 2) + " " +  line(right, 2) + " " + line(back, 2)  +  "\n" +
            empty         + " " + line(bot, 0)   + " " +  empty          + "\n" +
            empty         + " " + line(bot, 1)   + " " +  empty          + "\n" +
            empty         + " " + line(bot, 2)   + " " +  empty          + "\n")
        string = string.replace("Y", "\033[33mY\033[0m")
        string = string.replace("B", "\033[34mB\033[0m")
        string = string.replace("G", "\033[32mG\033[0m")
        string = string.replace("R", "\033[31mR\033[0m")
        string = string.replace("O", "\033[35mO\033[0m")
        return string

    def moveWhiteEdgeToTop(self):
        if self.front.squares[5].color == "W":
            self.rotate("R")
        elif self.bot.squares[5].color == "W":
            self.rotate("R2")
        elif self.back.squares[3].color == "W":
            self.rotate("R'")


    def getTopWhiteEdges(self):
        i = 0
        while i < 4:
            self.moveWhiteEdgeToTop()
            while not self.top.squares[5].color == "W":
                self.rotate("U")
                self.rotate_left()
                self.rotate("R")
                self.moveWhiteEdgeToTop()
            self.rotate_left()
            i += 1
    
    def moveOneWhiteEdgeToBottom(self):
        if self.right.squares[1] == self.right.squares[4]:
            self.rotate("R2")
            return True
        return False

    def moveWhiteEdgesToBottom(self):
        i = 0
        while i < 4:
            while not self.moveOneWhiteEdgeToBottom():
                self.rotate("U")
                self.rotate_left()
            self.rotate_left()
            i += 1

    def getCorrectCornerinTopLayer(self, col1, col2):
        i = 0
        while i < 4:
            if (self.front.squares[8].color == "W" or self.front.squares[8].color == col1 or self.front.squares[8].color == col2)\
                    and (self.right.squares[6].color == "W" or self.right.squares[6].color == col1 or self.right.squares[6].color == col2)\
                    and (self.bot.squares[2].color == "W" or self.bot.squares[2].color == col1 or self.bot.squares[2].color == col2):
                        self.rotate("R")
                        self.rotate("U")
                        self.rotate("R'")
                        self.rotate("U'")
            self.rotate_left()
            i += 1

    def positionYellowToTop(self):
        if self.front.squares[4].color == "Y":
            self.rotate_up()
        elif self.back.squares[4].color == "Y":
            self.rotate_down()
        elif self.left.squares[4].color == "Y":
            self.rotate_right()
            self.rotate_down()
        elif self.right.squares[4].color == "Y":
            self.rotate_left()
            self.rotate_down()
        elif self.bot.squares[4].color == "Y":
            self.rotate_down()
            self.rotate_down()

                    
    def repositionCube(self):
        self.positionYellowToTop()
        while not self.right.squares[4].color == "O":
            self.rotate_left()

    def positionWhiteCornerOnTopRight(self, col1, col2):
        while not ((self.front.squares[2].color == "W" or self.front.squares[2].color == col1 or self.front.squares[2].color == col2)\
                and (self.right.squares[0].color == "W" or self.right.squares[0].color == col1 or self.right.squares[0].color == col2)\
                and (self.top.squares[8].color == "W" or self.top.squares[8].color == col1 or self.top.squares[8].color == col2)):
                    self.rotate("U")
    def isBottomRightCornerCorrect(self, col1, col2):
        return self.front.squares[8].color == col1\
                and self.right.squares[6].color == col2\
                and self.bot.squares[2].color == "W"

    def getBottomWhiteCorners(self):
        i = 0
        while i < 4:
            col1 = self.front.squares[4].color
            col2 = self.right.squares[4].color
            self.getCorrectCornerinTopLayer(col1, col2)
            self.positionWhiteCornerOnTopRight(col1, col2)
            while not self.isBottomRightCornerCorrect(col1, col2):
                self.rotate("R")
                self.rotate("U")
                self.rotate("R'")
                self.rotate("U'")
            i += 1
            self.rotate_left()

    def isAllSecondLayerEdgesOk(self):
        return self.front.squares[3] == self.front.squares[4] and self.front.squares[5] == self.front.squares[4]\
                and self.right.squares[3] == self.right.squares[4] and self.right.squares[5] == self.right.squares[4]\
                and self.left.squares[3] == self.left.squares[4] and self.left.squares[5] == self.left.squares[4]\
                and self.back.squares[3] == self.back.squares[4] and self.back.squares[5] == self.back.squares[4]

    def switchToRight(self):
        self.rotate("U")
        self.rotate("R")
        self.rotate("U")
        self.rotate("R'")
        self.rotate("U'")
        self.rotate_right()
        self.rotate("L'")
        self.rotate("U'")
        self.rotate("L")
        self.rotate("U")

    def switchToLeft(self):
        self.rotate("U'")
        self.rotate("L'")
        self.rotate("U'")
        self.rotate("L")
        self.rotate("U")
        self.rotate_left()
        self.rotate("R")
        self.rotate("U")
        self.rotate("R'")
        self.rotate("U'")

    def tryPlaceEdge(self):
        if self.front.squares[1] == self.front.squares[4]:
            if self.top.squares[7] == self.left.squares[4]:
                self.switchToLeft()
            elif self.top.squares[7] == self.right.squares[4]:
                self.switchToRight()
            else:
                self.rotate("U")
        else:
            self.rotate("U")

    def kickEdge(self):
        if ((self.front.squares[3] != self.front.squares[4]
            or self.left.squares[5] != self.left.squares[4])
        and not (self.front.squares[3].color == "Y"
            or self.left.squares[5].color == "Y")):
            self.switchToLeft()
        elif ((self.front.squares[5] != self.front.squares[4]
            or self.right.squares[3] != self.right.squares[4])
        and not (self.front.squares[5].color == "Y"
            or self.right.squares[3].color == "Y")):
            self.switchToRight()

    def getSecondLayerEdges(self):
        while not self.isAllSecondLayerEdgesOk():
            for i in range (4):
                self.kickEdge()
                self.tryPlaceEdge()
                self.kickEdge()
            self.rotate_left()


    def YellowLine(self, pos):
        if pos:
            while not (self.top.squares[3].color == "Y" and self.top.squares[5].color == "Y"):
                self.rotate_left()
        self.rotate('F')
        self.rotate("R")
        self.rotate("U")
        self.rotate("R'")
        self.rotate("U'")
        self.rotate("F'")

    def YellowAngle(self):
        while not (self.top.squares[5].color == "Y" and self.top.squares[7].color == "Y"):
            self.rotate_left()
        self.rotate("B")
        self.rotate_right()
        self.rotate_down()
        self.rotate_left()
        self.rotate("R")
        self.rotate("U")
        self.rotate("R'")
        self.rotate("U'")
        self.rotate("B'")
        self.rotate_left()
        self.rotate_down()
        self.rotate_right()

    def YellowDot(self):
        self.YellowLine(False)
        self.YellowAngle()

    

    def getYellowCross(self):
       if self.top.squares[1].color == "Y" and self.top.squares[3].color == "Y"\
               and self.top.squares[5].color == "Y" and self.top.squares[7].color == "Y":
                   return
       if (self.top.squares[1].color == "Y" and self.top.squares[7].color == "Y")\
               or (self.top.squares[3].color == "Y" and self.top.squares[5].color == "Y"):
                   self.YellowLine(True)
       elif (self.top.squares[1].color == "Y" and self.top.squares[5].color == "Y")\
            or (self.top.squares[5].color == "Y" and self.top.squares[7].color == "Y")\
            or (self.top.squares[7].color == "Y" and self.top.squares[3].color == "Y")\
            or (self.top.squares[3].color == "Y" and self.top.squares[1].color == "Y"):
                   self.YellowAngle()
       else:
           self.YellowDot()


    def RightyAlg(self):
        self.rotate("R")
        self.rotate("U")
        self.rotate("R'")
        self.rotate("U'")

    def LeftyAlg(self):
        self.rotate("L'")
        self.rotate("U'")
        self.rotate("L")
        self.rotate("U")

    def AdjacentSwap(self):
        for i in range(4):
            if ((self.top.squares[0].color == "Y"
                or self.top.squares[0] == self.back.squares[4]
                or self.top.squares[0] == self.left.squares[4])\
                    and (self.back.squares[2].color == "Y"
                        or self.back.squares[2] == self.back.squares[4]
                        or self.back.squares[2] == self.left.squares[4])\
                    and (self.left.squares[0].color == "Y"
                        or self.left.squares[0] == self.back.squares[4]
                        or self.left.squares[0] == self.left.squares[4]))\
                    and ((self.top.squares[6].color == "Y"
                        or self.top.squares[6] == self.front.squares[4]
                        or self.top.squares[6] == self.left.squares[4])\
                    and (self.front.squares[0].color == "Y"
                        or self.front.squares[0] == self.front.squares[4]
                        or self.front.squares[0] == self.left.squares[4])\
                    and (self.left.squares[2].color == "Y"
                        or self.left.squares[2] == self.front.squares[4]
                        or self.left.squares[2] == self.left.squares[4]))\
                    and not ((self.top.squares[2].color == "Y"
                        or self.top.squares[2] == self.back.squares[4]
                        or self.top.squares[2] == self.right.squares[4])\
                    and (self.back.squares[0].color == "Y"
                        or self.back.squares[0] == self.back.squares[4]
                        or self.back.squares[0] == self.right.squares[4])\
                    and (self.right.squares[2].color == "Y"
                        or self.right.squares[2] == self.back.squares[4]
                        or self.right.squares[2] == self.right.squares[4])):
                self.RightyAlg()
                self.RightyAlg()
                self.RightyAlg()
                self.rotate_right()
                self.LeftyAlg()
                self.LeftyAlg()
                self.LeftyAlg()
                while not ((self.top.squares[0].color == "Y"
                    or self.top.squares[0] == self.back.squares[4]
                    or self.top.squares[0] == self.left.squares[4])\
                        and (self.back.squares[2].color == "Y"
                            or self.back.squares[2] == self.back.squares[4]
                            or self.back.squares[2] == self.left.squares[4])\
                        and (self.left.squares[0].color == "Y"
                            or self.left.squares[0] == self.back.squares[4]
                            or self.left.squares[0] == self.left.squares[4])):
                    self.rotate("U")
                return True
            self.rotate_left()
        return False

    def DiagonalSwap(self):
                self.RightyAlg()
                self.RightyAlg()
                self.RightyAlg()
                self.rotate_right()
                self.LeftyAlg()
                self.LeftyAlg()
                self.LeftyAlg()


    def positionYellowCorners(self):
        while True:
            if self.AdjacentSwap():
                return
            self.DiagonalSwap()
            if self.AdjacentSwap():
                return
            self.rotate("U")


    def twistYellowCorners(self):
        self.rotate_up()
        self.rotate_up()
        for i in range(4):
            while not self.bot.squares[2].color == "Y":
                self.RightyAlg()
            self.rotate("D")



    def isCubeSolved(self):
        self.repositionCube()
        for i in self.front.squares:
            if not i.color == "G":
                return False
        for i in self.left.squares:
            if not i.color == "R":
                return False
        for i in self.right.squares:
            if not i.color == "O":
                return False
        for i in self.top.squares:
            if not i.color == "Y":
                return False
        for i in self.bot.squares:
            if not i.color == "W":
                return False
        for i in self.back.squares:
            if not i.color == "B":
                return False
        return True

    def finalSequence(self):
        self.RightyAlg()
        self.LeftyAlg()
        for i in range(5):
            self.RightyAlg()
        for i in range(5):
            self.LeftyAlg()

    def isFrontFaceDone(self):
        col = self.front.squares[0]
        for i in self.front.squares:
            if not i == col:
                return False
        return True


    def oneRowDone(self):
        while not self.isFrontFaceDone():
            self.rotate("U")
            self.rotate_left()
        self.finalSequence()
        if not self.isCubeSolved():
            while not (self.front.squares[0] == self.front.squares[1] and self.front.squares[1] == self.front.squares[2]):
                self.rotate_left()
            self.finalSequence()


    def finalLayer(self):
        if (self.isCubeSolved()):
            return
        else:
            for i in range(4):
                if self.front.squares[0] == self.front.squares[1] and self.front.squares[1] == self.front.squares[2]:
                    self.oneRowDone()
                    return
                self.rotate("U")
            self.finalSequence()
            self.finalLayer()



    def solve(self):
        self.display = True
        self.repositionCube()
        self.getTopWhiteEdges()
        self.repositionCube()
        self.moveWhiteEdgesToBottom()
        self.repositionCube()
        self.getBottomWhiteCorners()
        self.getSecondLayerEdges()
        self.repositionCube()
        self.getYellowCross()
        self.positionYellowCorners()
        self.twistYellowCorners()
        self.finalLayer()
        print("")

    def mix(self, move_list):
        for move in move_list.split():
            self.rotate(move)

    def randomize(self):
        l = ["R", "R'", "R2","U", "U'", "U2", "L", "L'","L2", "D", "D'","D2", "B", "B'","B2", "F", "F'","F2"]
        i = 0
        while i < 100:
            a = random.choice(l)
            self.rotate(a)
            f = [
                self.rotate_left,
                self.rotate_right,
                self.rotate_down,
                self.rotate_up
            ]
            func = random.choice(f)
            func()
            i += 1

