import sys
from cube import Cube

if __name__ == "__main__":
    cube = Cube()
    if len(sys.argv) == 1:
        cube.randomize()
    elif len(sys.argv) == 2:
        try:
            cube.mix(sys.argv[1])
        except Exception as e:
            print("Invalid format")
            sys.exit(1)
    else:
        print("Invalid format")
        sys.exit(1)
    cube.solve()
    print(cube)
