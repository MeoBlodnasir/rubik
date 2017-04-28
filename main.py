import sys
import getopt
from cube import Cube

def usage():
    print("Usage:")
    print("     -h: print this help")
    print("     -d: step by step")
    print("     -r: randomize")
    print("     -i <moves>: mix the cube with <moves>")

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hdi:r')
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    if len(opts) == 0 or len(args) > 0:
        usage()
        sys.exit(1)

    debug = False
    randomize = False
    mix = False
    mix_moves = ""

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt == '-i':
            mix = True
            mix_moves = arg
        elif opt == '-r':
            randomize = True
        elif opt == '-d':
            debug = True

    cube = Cube()

    if mix:
        try:
            cube.mix(mix_moves)
        except Exception as e:
            print("Invalid format")
            sys.exit(1)
    elif randomize:
        cube.randomize()
    else:
        usage()
        sys.exit(1)

    if debug:
        cube.debug = True
    else:
        print(cube)

    cube.solve()
    print(cube)
