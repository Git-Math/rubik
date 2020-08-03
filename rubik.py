import sys
import print_cube
import cube
import solve

def usage():
    print("usage: %s [-q] <scramble>\n\
-q: quiet, the cube is not printed\n\
<scramble>: scramble to solve" % sys.argv[0])

if __name__ == '__main__':
    quiet_mode = False
    i_scramble = 1
    if len(sys.argv) == 3:
        if sys.argv[1] != "-q":
            print("Invalid argument: %s" % sys.argv[1], file=sys.stderr)
            usage()
            sys.exit(1)
        quiet_mode = True
        i_scramble = 2
    elif len(sys.argv) != 2:
        print("Invalid argument number", file=sys.stderr)
        usage()
        sys.exit(1)
    elif len(sys.argv[i_scramble]) > 10000:
        print("scramble too long", file=sys.stderr)
        usage()
        sys.exit(1)

    scramble_move_list = sys.argv[i_scramble].split()
    if len(scramble_move_list) == 0:
        print("<scramble> can't be empty", file=sys.stderr)
        usage()
        sys.exit(1)

    rubiks_cube = cube.Cube()
    rubiks_cube.move_sequence(scramble_move_list)

    if rubiks_cube.is_solved():
        print("This rubik's cube is already solved")
        sys.exit(0)

    _, solution = rubiks_cube.search_short_solution(cube.move_list, [], 3)
    step = None

    if not solution:
        solution, step = solve.solve(rubiks_cube)

    print(*solution, sep=" ")
    if not quiet_mode:
        rubiks_cube.reverse_solution(solution)
        print_cube.print_cube(rubiks_cube, solution, step)
