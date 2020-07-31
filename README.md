# rubik3000

Minimum moves rubik's cube solver.

## Install:
* To run a classic 'pip install' of the project, you can just do:
```shell
make
```
* If you want an editable version (dev), run:
```shell
make dev
```
* This will also install dev dependencies, such as linter/tester. You can trigger them all with:
```shell
# this is actually an alias to: make lint flake test todo
make check
```


## Usage:
* The script accept one argument, which is a list of moves to scramble the cube. It will then solve the cube, with an amazing UI poping up. For instance:
```shell
./rubik "F R U2 B' L' D'"
```
