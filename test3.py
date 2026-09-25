#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import maze.cells as cell
import maze
from maze.move.obj import MazeRunner as MazeRunner

# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- sniggle ----------------------------

def test_maze_runner_basics() -> None:

    test: MazeRunner
    dom: maze.Maze

    dom = maze.Maze((4, 4))
    test = MazeRunner(
        dom=dom, position=(3, 0)
    )

    print("test MazeRunner basics :\t\t\t", end='')

    assert (test.dom == dom)
    assert (test.cell == dom._get_cell((3, 0)))
    assert (test.position == (3, 0))
    assert (bool(test.cell) is True)

    print("[O.K.]")


def test_maze_runner_move_empty() -> None:

    test: MazeRunner
    dom: maze.Maze

    dom = maze.Maze((4, 4))
    test = MazeRunner(
        dom=dom, position=(3, 0)
    )

    print("test MazeRunner move - no walls :\t\t", end='')

    assert (test.dom == dom)
    assert (test.cell == dom._get_cell((3, 0)))
    assert (test.position == (3, 0))
    assert (bool(test.cell) is True)

    print("[Implement]")


def test_maze_runner_check_walls() -> None:

    test: MazeRunner
    dom: maze.Maze

    dom = maze.Maze((4, 4))
    test = MazeRunner(
        dom=dom, position=(3, 0)
    )

    print("test MazeRunner.is_open() :\t\t\t", end='')

    assert (test.dom == dom)
    assert (test.cell == dom._get_cell((3, 0)))
    assert (test.position == (3, 0))
    assert (bool(test.cell) is True)

    print("[Implement]")


def test_maze_runner_check_visited() -> None:

    test: MazeRunner
    dom: maze.Maze

    dom = maze.Maze((4, 4))
    test = MazeRunner(
        dom=dom, position=(3, 0)
    )

    print("test MazeRunner.is_visited() :\t\t\t", end='')

    assert (test.dom == dom)
    assert (test.cell == dom._get_cell((3, 0)))
    assert (test.position == (3, 0))
    assert (bool(test.cell) is True)

    print("[Implement]")


def test_maze_runner_move_with_walls() -> None:

    test: MazeRunner
    dom: maze.Maze

    dom = maze.Maze((4, 4))
    test = MazeRunner(
        dom=dom, position=(3, 0)
    )

    print("test MazeRunner move - walls:\t\t\t", end='')

    assert (test.dom == dom)
    assert (test.cell == dom._get_cell((3, 0)))
    assert (test.position == (3, 0))
    assert (bool(test.cell) is True)

    print("[Implement]")




# ---------------------------- utils ----------------------------

# def ...

# ---------------------------- run ----------------------------


def main() -> None:

    print("\n------------------------------------\n")
    test_maze_runner_basics()
    test_maze_runner_move_empty()
    test_maze_runner_check_walls()
    test_maze_runner_check_visited()
    test_maze_runner_move_with_walls()
    print("\n------------------------------------")


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
