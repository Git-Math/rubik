import sys
import print_cube
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
    if len(scramble_move_list) == 0:
        print("<scramble> can't be empty", file=sys.stderr)
        usage()
        sys.exit(1)

    rubiks_cube = cube.Cube()
    rubiks_cube.scramble(scramble_move_list)

    if rubiks_cube.is_solved():
        print("This rubik's cube is already solved")
        sys.exit(0)

    ret = rubiks_cube.search_short_solution(cube.move_list, [], 3)
    if ret[0]:
        print("Short solution:", *ret[1])
        rubiks_cube.reverse_solution(ret[1])
        print_cube.print_cube(rubiks_cube, ret[1], None)
        sys.exit(0)

