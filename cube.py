import copy
class Square:
    def __init__(self):
        self.colour = "X"
    def __str__(self):
        return self.colour

class Row:
    def __init__(self):
        self.left_square = Square()
        self.middle_square = Square()
        self.right_square = Square()
    def __str__(self):
        return ("{0} {1} {2}".format(self.left_square, self.middle_square, self.right_square))

class Face:
    def __init__(self):
        self.top_row = Row()
        self.middle_row = Row()
        self.bottom_row = Row()
    def __str__(self):
        return ("{0}\n{1}\n{2}".format(self.top_row, self.middle_row, self.bottom_row))

class Cube:
    def __init__(self):
        self.front_face = Face()
        self.left_face = Face()
        self.right_face = Face()
        self.top_face = Face()
        self.bottom_face = Face()
        self.back_face = Face()
        self.front_face.top_row.left_square.colour = "G"
        self.front_face.top_row.middle_square.colour = "G"
        self.front_face.top_row.right_square.colour = "G"
        self.front_face.middle_row.left_square.colour = "G"
        self.front_face.middle_row.middle_square.colour = "G"
        self.front_face.middle_row.right_square.colour = "G"
        self.front_face.bottom_row.left_square.colour = "G"
        self.front_face.bottom_row.middle_square.colour = "G"
        self.front_face.bottom_row.right_square.colour = "G"

        self.left_face.top_row.left_square.colour = "R"
        self.left_face.top_row.middle_square.colour = "R"
        self.left_face.top_row.right_square.colour = "R"
        self.left_face.middle_row.left_square.colour = "R"
        self.left_face.middle_row.middle_square.colour = "R"
        self.left_face.middle_row.right_square.colour = "R"
        self.left_face.bottom_row.left_square.colour = "R"
        self.left_face.bottom_row.middle_square.colour = "R"
        self.left_face.bottom_row.right_square.colour = "R"

        self.right_face.top_row.left_square.colour = "O"
        self.right_face.top_row.middle_square.colour = "O"
        self.right_face.top_row.right_square.colour = "O"
        self.right_face.middle_row.left_square.colour = "O"
        self.right_face.middle_row.middle_square.colour = "O"
        self.right_face.middle_row.right_square.colour = "O"
        self.right_face.bottom_row.left_square.colour = "O"
        self.right_face.bottom_row.middle_square.colour = "O"
        self.right_face.bottom_row.right_square.colour = "O"

        self.top_face.top_row.left_square.colour = "Y"
        self.top_face.top_row.middle_square.colour = "Y"
        self.top_face.top_row.right_square.colour = "Y"
        self.top_face.middle_row.left_square.colour = "Y"
        self.top_face.middle_row.middle_square.colour = "Y"
        self.top_face.middle_row.right_square.colour = "Y"
        self.top_face.bottom_row.left_square.colour = "Y"
        self.top_face.bottom_row.middle_square.colour = "Y"
        self.top_face.bottom_row.right_square.colour = "Y"

        self.bottom_face.top_row.left_square.colour = "W"
        self.bottom_face.top_row.middle_square.colour = "W"
        self.bottom_face.top_row.right_square.colour = "W"
        self.bottom_face.middle_row.left_square.colour = "W"
        self.bottom_face.middle_row.middle_square.colour = "W"
        self.bottom_face.middle_row.right_square.colour = "W"
        self.bottom_face.bottom_row.left_square.colour = "W"
        self.bottom_face.bottom_row.middle_square.colour = "W"
        self.bottom_face.bottom_row.right_square.colour = "W"

        self.back_face.top_row.left_square.colour = "B"
        self.back_face.top_row.middle_square.colour = "B"
        self.back_face.top_row.right_square.colour = "B"
        self.back_face.middle_row.left_square.colour = "B"
        self.back_face.middle_row.middle_square.colour = "B"
        self.back_face.middle_row.right_square.colour = "B"
        self.back_face.bottom_row.left_square.colour = "B"
        self.back_face.bottom_row.middle_square.colour = "B"
        self.back_face.bottom_row.right_square.colour = "B"

    def __str__(self):
        return "FRONT\n{0}\nLEFT\n{1}\nRIGHT\n{2}\nTOP\n{3}\nBOTTOM\n{4}\nBACK\n{5}\n___________________________".format(self.front_face, self.left_face, self.right_face, self.top_face, self.bottom_face, self.back_face)
    
    def copyrow(row):
        ret = Row()
        ret.left_square.colour = row.left_square.colour
        ret.middle_square.colour = row.middle_square.colour
        ret.right_square.colour = row.right_square.colour

    def rotate(self,face):
        if "'" not in face:
            if face == "U":
                f = self.top_face
                tmp = f.top_row
                # CHANGED ON OTHERS
                tmp2 = copy.deepcopy(self.front_face.top_row)
                self.front_face.top_row = copy.deepcopy(self.right_face.top_row)
                self.right_face.top_row = copy.deepcopy(self.back_face.top_row)
                self.back_face.top_row = copy.deepcopy(self.left_face.top_row)
                self.left_face.top_row = copy.deepcopy(tmp2)
            elif face == "D":
                f = self.bottom_face
                tmp = f.bottom_row
                # CHANGED ON OTHERS
                tmp2 = copy.deepcopy(self.front_face.bottom_row)
                self.front_face.bottom_row = copy.deepcopy(self.left_face.top_row)
                self.left_face.bottom_row = copy.deepcopy(self.back_face.top_row)
                self.back_face.bottom_row = copy.deepcopy(self.right_face.top_row)
                self.right_face.bottom_row = copy.deepcopy(tmp2)
            elif face == "R":
                f = self.right_face
                tmp = f.bottom_row
                # CHANGED ON OTHERS
                col1 = self.top_face.top_row.right_square.colour
                col2 = self.top_face.middle_row.right_square.colour
                col3 = self.top_face.bottom_row.right_square.colour
                self.top_face.bottom_row.right_square.colour = self.front_face.bottom_row.right_square.colour
                self.top_face.middle_row.right_square.colour = self.front_face.middle_row.right_square.colour
                self.top_face.top_row.right_square.colour = self.front_face.top_row.right_square.colour


                self.front_face.bottom_row.right_square.colour = self.bottom_face.top_row.right_square.colour
                self.front_face.middle_row.right_square.colour = self.bottom_face.middle_row.right_square.colour
                self.front_face.top_row.right_square.colour = self.bottom_face.bottom_row.right_square.colour

                
                self.bottom_face.bottom_row.right_square.colour = self.back_face.bottom_row.left_square.colour
                self.bottom_face.middle_row.right_square.colour = self.back_face.middle_row.left_square.colour
                self.bottom_face.top_row.right_square.colour = self.back_face.top_row.left_square.colour

                self.back_face.bottom_row.left_square.colour = col1
                self.back_face.middle_row.left_square.colour = col2
                self.back_face.top_row.left_square.colour = col3
            elif face == "L":
                f = self.left_face
                tmp = f.bottom_row
                # CHANGED ON OTHERS
                col1 = self.top_face.top_row.left_square.colour
                col2 = self.top_face.middle_row.left_square.colour
                col3 = self.top_face.bottom_row.left_square.colour
                self.top_face.bottom_row.left_square.colour = self.back_face.top_row.right_square.colour
                self.top_face.middle_row.left_square.colour = self.back_face.middle_row.right_square.colour
                self.top_face.top_row.right_square.colour = self.front_face.top_row.right_square.colour


                self.front_face.bottom_row.right_square.colour = self.bottom_face.top_row.right_square.colour
                self.front_face.middle_row.right_square.colour = self.bottom_face.middle_row.right_square.colour
                self.front_face.top_row.right_square.colour = self.bottom_face.bottom_row.right_square.colour

                
                self.bottom_face.bottom_row.right_square.colour = self.back_face.bottom_row.left_square.colour
                self.bottom_face.middle_row.right_square.colour = self.back_face.middle_row.left_square.colour
                self.bottom_face.top_row.right_square.colour = self.back_face.top_row.left_square.colour

                self.back_face.bottom_row.left_square.colour = col1
                self.back_face.middle_row.left_square.colour = col2
                self.back_face.top_row.left_square.colour = col3


            # CHANGES ON THE ROTATING FACE 
            f.top_row.left_square.colour = f.bottom_row.left_square.colour
            f.top_row.middle_square.colour = f.middle_row.left_square.colour
            f.top_row.right_square.colour = tmp.left_square.colour

            f.middle_row.left_square.colour = f.bottom_row.middle_square.colour
            f.bottom_row.left_square.colour = f.bottom_row.right_square.colour

            f.bottom_row.middle_square.colour = f.middle_row.right_square.colour
            f.bottom_row.right_square.colour = tmp.right_square.colour

            f.middle_row.right_square.colour = tmp.middle_square.colour
        else:
            if face == "U'":
                f = self.top_face
                tmp = f.top_row
                # CHANGED ON OTHERS
                tmp2 = copy.deepcopy(self.front_face.top_row)
                self.front_face.top_row = copy.deepcopy(self.left_face.top_row)
                self.left_face.top_row = copy.deepcopy(self.back_face.top_row)
                self.back_face.top_row = copy.deepcopy(self.right_face.top_row)
                self.right_face.top_row = copy.deepcopy(tmp2)
            elif face == "D'":
                f = self.bottom_face
                tmp = f.bottom_row
                # CHANGED ON OTHERS
                tmp2 = copy.deepcopy(self.front_face.bottom_row)
                self.front_face.bottom_row = copy.deepcopy(self.right_face.bottom_row)
                self.right_face.bottom_row = copy.deepcopy(self.back_face.bottom_row)
                self.back_face.bottom_row = copy.deepcopy(self.left_face.bottom_row)
                self.left_face.bottom_row = copy.deepcopy(tmp2)
            elif face == "R'":
                f = self.right_face
                tmp = f.bottom_row
                # CHANGED ON OTHERS
                col1 = self.top_face.top_row.right_square.colour
                col2 = self.top_face.middle_row.right_square.colour
                col3 = self.top_face.bottom_row.right_square.colour
                self.top_face.bottom_row.right_square.colour = self.back_face.top_row.left_square.colour
                self.top_face.middle_row.right_square.colour = self.back_face.middle_row.left_square.colour
                self.top_face.top_row.right_square.colour = self.back_face.bottom_row.left_square.colour

                self.back_face.bottom_row.left_square.colour = self.bottom_face.bottom_row.right_square.colour
                self.back_face.middle_row.left_square.colour = self.bottom_face.middle_row.right_square.colour
                self.back_face.top_row.left_square.colour = self.bottom_face.top_row.right_square.colour

                self.bottom_face.bottom_row.right_square.colour = self.front_face.top_row.right_square.colour
                self.bottom_face.middle_row.right_square.colour = self.front_face.middle_row.right_square.colour
                self.bottom_face.top_row.right_square.colour = self.front_face.bottom_row.right_square.colour


                self.front_face.bottom_row.right_square.colour = col3
                self.front_face.middle_row.right_square.colour = col2
                self.front_face.top_row.right_square.colour = col1

                
            # CHANGES ON THE ROTATING FACE 
            f.top_row.left_square.colour = tmp.right_square.colour
            f.top_row.middle_square.colour = f.middle_row.right_square.colour
            f.top_row.right_square.colour = f.bottom_row.right_square.colour
            
            
            f.middle_row.right_square.colour = f.bottom_row.middle_square.colour
            f.bottom_row.right_square.colour = f.bottom_row.left_square.colour
            f.bottom_row.middle_square.colour = f.middle_row.left_square.colour
            f.bottom_row.left_square.colour = tmp.left_square.colour
            
            f.middle_row.left_square.colour = tmp.middle_square.colour







