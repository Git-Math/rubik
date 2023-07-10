# rubik
Rubik's cube solver with 2D modelisation of the solution. The algorithm is optimized to always find a solution in less than 2 seonds with a small amount of moves.  
We use the classic [notation](https://solvethecube.com/notation) to describe the initial scramble and the solution.

## Solver

### How to run
```
python3 rubik.py [-q] <scramble>
-q: quiet, the cube is not printed
<scramble>: scramble to solve
```

### Example
```
$ python3 rubik.py "R B2 D' R2 U2 F2 B' U' D2 L' U' L D2 L B R U' B L' B R2 F2 B' F L2 U R' L R D' L' R D' L R U' L2 U F2 U2 B2 L' B F2 R2 D' R' U2 R' D"
B' D' B' L' D' B' U2 B U2 R U R' U R U' R' L U' L' U2 R' U' R U2 R' U' R U R' U' R B' U2 B U' L U L' U F U F' U2 F U F' U' F U F' L2 D L' U2 L D' L' U2 L' U R' U L' U2 R U' R' U2 R L U'
```

https://github.com/Git-Math/rubik/assets/11985913/13197c0e-9e12-465f-b6e0-0a444a8f86c1

## Generate random scramble

### How to run
```
python3 rubik_scramble.py <number> <length>
<number>: number of scramble (must be a number between 1 and 99)
<length>: length of one scramble (must be a number between 1 and 999)
```

### Example
```
$ python3 rubik_scramble.py 5 10
R B' U B2 U2 R' B2 D2 B2 D'
F2 U B2 D2 R D' R U F2 D
F' D U B R' B2 F' D' L' D'
L R2 U R2 U2 L B D F R'
F2 L' R2 D2 U' B2 U2 L2 B F2
```
