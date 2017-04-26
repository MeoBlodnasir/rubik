import copy

class Face:
    def __init__(self, color, up, down, left, right):
        self.squares = [color,color,color,color,color,color,color,color,color]
        self.upface = up
        self.downface = down
        self.rightface = right
        self.leftface = left
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

class Cube:
    def __init__(self):
        self.front_face = None
        self.left_face = None
        self.right_face = None
        self.top_face = None
        self.bottom_face = None
        self.back_face = None
        self.front_face = Face("G", self.top_face, self.bottom_face, self.left_face, self.right_face)
        self.left_face = Face("R", self.top_face, self.bottom_face, self.back_face, self.front_face)
        self.right_face = Face("O", self.top_face, self.bottom_face, self.front_face, self.back_face)
        self.top_face = Face("Y", self.back_face, self.front_face, self.left_face, self.right_face)
        self.bottom_face = Face("W", self.back_face, self.front_face, self.right_face, self.left_face)
        self.back_face = Face("B", self.top_face, self.bottom_face, self.right_face, self.left_face)

    def __str__(self):
        return "FRONT\n{0}\nLEFT\n{1}\nRIGHT\n{2}\nTOP\n{3}\nBOTTOM\n{4}\nBACK\n{5}\n___________________________".format(self.front_face, self.left_face, self.right_face, self.top_face, self.bottom_face, self.back_face)
    







