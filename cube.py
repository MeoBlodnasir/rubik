import copy

class Row:
    def __init__(self, color):
        self.left_square = color
        self.middle_square = color
        self.right_square = color
    def __str__(self):
        return ("{0} {1} {2}".format(self.left_square, self.middle_square, self.right_square))

class Face:
    def __init__(self, color):
        self.top_row = Row(color)
        self.middle_row = Row(color)
        self.bottom_row = Row(color)
    def __str__(self):
        return ("{0}\n{1}\n{2}".format(self.top_row, self.middle_row, self.bottom_row))

class Cube:
    def __init__(self):
        self.front_face = Face("G")
        self.left_face = Face("R")
        self.right_face = Face("O")
        self.top_face = Face("Y")
        self.bottom_face = Face("W")
        self.back_face = Face("B")

    def __str__(self):
        return "FRONT\n{0}\nLEFT\n{1}\nRIGHT\n{2}\nTOP\n{3}\nBOTTOM\n{4}\nBACK\n{5}\n___________________________".format(self.front_face, self.left_face, self.right_face, self.top_face, self.bottom_face, self.back_face)
    
    def copyrow(row):
        ret = Row()
        ret.left_square = row.left_square
        ret.middle_square = row.middle_square
        ret.right_square = row.right_square

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
                col1 = self.top_face.top_row.right_square
                col2 = self.top_face.middle_row.right_square
                col3 = self.top_face.bottom_row.right_square
                self.top_face.bottom_row.right_square = self.front_face.bottom_row.right_square
                self.top_face.middle_row.right_square = self.front_face.middle_row.right_square
                self.top_face.top_row.right_square = self.front_face.top_row.right_square


                self.front_face.bottom_row.right_square = self.bottom_face.top_row.right_square
                self.front_face.middle_row.right_square = self.bottom_face.middle_row.right_square
                self.front_face.top_row.right_square = self.bottom_face.bottom_row.right_square

                
                self.bottom_face.bottom_row.right_square = self.back_face.bottom_row.left_square
                self.bottom_face.middle_row.right_square = self.back_face.middle_row.left_square
                self.bottom_face.top_row.right_square = self.back_face.top_row.left_square

                self.back_face.bottom_row.left_square = col1
                self.back_face.middle_row.left_square = col2
                self.back_face.top_row.left_square = col3
            elif face == "L":
                f = self.left_face
                tmp = f.bottom_row
                # CHANGED ON OTHERS
                col1 = self.top_face.top_row.left_square
                col2 = self.top_face.middle_row.left_square
                col3 = self.top_face.bottom_row.left_square
                self.top_face.bottom_row.left_square = self.back_face.top_row.right_square
                self.top_face.middle_row.left_square = self.back_face.middle_row.right_square
                self.top_face.top_row.right_square = self.front_face.top_row.right_square


                self.front_face.bottom_row.right_square = self.bottom_face.top_row.right_square
                self.front_face.middle_row.right_square = self.bottom_face.middle_row.right_square
                self.front_face.top_row.right_square = self.bottom_face.bottom_row.right_square

                
                self.bottom_face.bottom_row.right_square = self.back_face.bottom_row.left_square
                self.bottom_face.middle_row.right_square = self.back_face.middle_row.left_square
                self.bottom_face.top_row.right_square = self.back_face.top_row.left_square

                self.back_face.bottom_row.left_square = col1
                self.back_face.middle_row.left_square = col2
                self.back_face.top_row.left_square = col3


            # CHANGES ON THE ROTATING FACE 
            f.top_row.left_square = f.bottom_row.left_square
            f.top_row.middle_square = f.middle_row.left_square
            f.top_row.right_square = tmp.left_square

            f.middle_row.left_square = f.bottom_row.middle_square
            f.bottom_row.left_square = f.bottom_row.right_square

            f.bottom_row.middle_square = f.middle_row.right_square
            f.bottom_row.right_square = tmp.right_square

            f.middle_row.right_square = tmp.middle_square
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
                col1 = self.top_face.top_row.right_square
                col2 = self.top_face.middle_row.right_square
                col3 = self.top_face.bottom_row.right_square
                self.top_face.bottom_row.right_square = self.back_face.top_row.left_square
                self.top_face.middle_row.right_square = self.back_face.middle_row.left_square
                self.top_face.top_row.right_square = self.back_face.bottom_row.left_square

                self.back_face.bottom_row.left_square = self.bottom_face.bottom_row.right_square
                self.back_face.middle_row.left_square = self.bottom_face.middle_row.right_square
                self.back_face.top_row.left_square = self.bottom_face.top_row.right_square

                self.bottom_face.bottom_row.right_square = self.front_face.top_row.right_square
                self.bottom_face.middle_row.right_square = self.front_face.middle_row.right_square
                self.bottom_face.top_row.right_square = self.front_face.bottom_row.right_square


                self.front_face.bottom_row.right_square = col3
                self.front_face.middle_row.right_square = col2
                self.front_face.top_row.right_square = col1

                
            # CHANGES ON THE ROTATING FACE 
            f.top_row.left_square = tmp.right_square
            f.top_row.middle_square = f.middle_row.right_square
            f.top_row.right_square = f.bottom_row.right_square
            
            
            f.middle_row.right_square = f.bottom_row.middle_square
            f.bottom_row.right_square = f.bottom_row.left_square
            f.bottom_row.middle_square = f.middle_row.left_square
            f.bottom_row.left_square = tmp.left_square
            
            f.middle_row.left_square = tmp.middle_square







