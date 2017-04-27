from cube import Cube

if __name__ == "__main__":
    cube = Cube()
    cube.randomize()
    cube.solve()
    print(cube)
