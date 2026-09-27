#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import maze
from maze.ui.cli.obj import Output

# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


def test_cell_interface_no_colors() -> None:

    test: Output
    dom: maze.Maze

    dom = maze.Maze((4, 4))
    test = Output(
        dom=dom
    )

    print("test CellInterface no colors :\t\t\t", end='')

    assert (test.dom == dom)

    print("[Implement]")


def test_cell_interface_colors() -> None:

    test: Output
    dom: maze.Maze

    dom = maze.Maze((4, 4))
    test = Output(
        dom=dom
    )

    print("test CellInterface with colors :\t\t", end='')

    assert (test.dom == dom)

    print("[Implement]")


def test_frame_interface_no_colors() -> None:

    test: Output
    dom: maze.Maze

    dom = maze.Maze((4, 4))
    test = Output(
        dom=dom
    )

    print("test FrameInterface no colors :\t\t\t", end='')

    assert (test.dom == dom)

    print("[Implement]")


def test_frame_interface_colors() -> None:

    test: Output
    dom: maze.Maze

    dom = maze.Maze((4, 4))
    test = Output(
        dom=dom
    )

    print("test FrameInterface with colors :\t\t", end='')

    assert (test.dom == dom)

    print("[Implement]")


def test_maze_interface_no_colors() -> None:

    test: Output
    dom: maze.Maze

    dom = maze.Maze((4, 4))
    test = Output(
        dom=dom
    )

    print("test MazeInterface no colors :\t\t\t", end='')

    assert (test.dom == dom)

    print("[Implement]")


# ---------------------------- utils ----------------------------

# def ...

# ---------------------------- run ----------------------------


def main() -> None:

    print("\n------------------------------------\n")
    test_cell_interface_no_colors()
    test_cell_interface_colors()
    test_frame_interface_no_colors()
    test_frame_interface_colors()
    test_maze_interface_no_colors()
    print("\n------------------------------------")


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
