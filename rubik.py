import sys
import cube

def usage():
    print("usage: %s <scramble>\n\
<scramble>: scramble to solve" % sys.argv[0])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Invalid argument number", file=sys.stderr)
        usage()
        sys.exit(1)
    elif len(sys.argv[1]) > 10000:
        print("scramble too long", file=sys.stderr)
        usage()
        sys.exit(1)
    scramble_move_list = sys.argv[1].split()
    cube = cube.Cube()

