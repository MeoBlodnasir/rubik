import sys
import getopt
from cube import Cube

def usage():
    print("Usage:")
    print("     -h: print this help")
    print("     -v: show inital state and final state")
    print("     -d: step by step")
    print("     -r: randomize")
    print("     -i <moves>: mix the cube with <moves>")

if __name__ == "__main__":
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hvdi:r')
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    if len(opts) == 0 or len(args) > 0:
        usage()
        sys.exit(1)

    verbose = False
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
        elif opt == '-v':
            verbose = True

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

    if verbose:
        print(cube)

    cube.solve()

    if debug:
        print("\033[F",end="")

    if verbose:
        print(cube)

