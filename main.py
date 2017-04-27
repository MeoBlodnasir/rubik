from cube import Cube

if __name__ == "__main__":
    cube = Cube()
    #print(cube)
    #print("Rotate U")
    #cube.rotate("U")
    #print(cube)
    cube.randomize()
    cube.solve()
    print(cube)
