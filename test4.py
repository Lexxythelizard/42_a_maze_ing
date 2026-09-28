#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import maze
from maze.ui.cli.obj import Output
from maze.cells.obj import Cell
# import maze.ui.cli.base as sniggle

# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


def test_cell_interface_no_colors() -> None:

    test: Output
    dom: maze.Maze
    cell: cells.Cell

    dom = maze.Maze((4, 4))
    test = Output(
        dom=dom
    )
    cell = dom.cells[0][0]

    print("test CellInterface no colors :\t\t\t", end='')

    assert (test.dom == dom)
    assert (
        test.frame_interface.cell_interface.get_cell_top(cell) == "+   +"
    )
    assert (
        test.frame_interface.cell_interface.get_cell_middle(cell) == "  %s  "
    )
    assert (
        test.frame_interface.cell_interface.get_cell_bottom(cell) == "+   +"
    )
    dom.close_frame()
    assert (
        test.frame_interface.cell_interface.get_cell_top(cell) == "+ – +"
    )
    assert (
        test.frame_interface.cell_interface.get_cell_middle(cell) == "| %s  "
    )
    assert (
        test.frame_interface.cell_interface.get_cell_bottom(cell) == "+   +"
    )
    dom.close_wall((0, 0), 'east')
    dom.close_wall((0, 0), 'south')
    assert (
        test.frame_interface.cell_interface.get_cell_top(cell) == "+ – +"
    )
    assert (
        test.frame_interface.cell_interface.get_cell_middle(cell) == "| %s |"
    )
    assert (
        test.frame_interface.cell_interface.get_cell_bottom(cell) == "+ – +"
    )
    cell = dom.cells[0][1]
    assert (
        test.frame_interface.cell_interface.get_cell_top(cell) == "+ – +"
    )
    assert (
        test.frame_interface.cell_interface.get_cell_middle(cell) == "| %s  "
    )
    assert (
        test.frame_interface.cell_interface.get_cell_bottom(cell) == "+   +"
    )
    print("[O.K.]")


def test_cell_interface_colors() -> None:

    test: Output
    dom: maze.Maze
    cell: cells.Cell

    dom = maze.Maze((4, 4))
    test = Output(
        dom=dom
    )
    cell = dom.cells[0][0]

    print("test CellInterface with colors :\t\t", end='')

    assert (test.dom == dom)
    assert (
        test.frame_interface.cell_interface.get_cell_top(cell, 'green') ==
        "\033[32m+   +\033[0m"
    )
    assert (
        test.frame_interface.cell_interface.get_cell_middle(cell, 'green') ==
        "\033[32m \033[0m %s \033[32m \033[0m"
    )
    assert (
        test.frame_interface.cell_interface.get_cell_bottom(cell, 'green') ==
        "\033[32m+   +\033[0m"
    )

    dom.close_frame()
    assert (
        test.frame_interface.cell_interface.get_cell_top(cell, 'green') ==
        "\033[32m+ – +\033[0m"
    )
    assert (
        test.frame_interface.cell_interface.get_cell_middle(cell, 'green') ==
        "\033[32m|\033[0m %s \033[32m \033[0m"
    )
    assert (
        test.frame_interface.cell_interface.get_cell_bottom(cell, 'green') ==
        "\033[32m+   +\033[0m"
    )

    dom.close_wall((0, 0), 'east')
    dom.close_wall((0, 0), 'south')
    assert (
        test.frame_interface.cell_interface.get_cell_top(cell, 'green') ==
        "\033[32m+ – +\033[0m"
    )
    assert (
        test.frame_interface.cell_interface.get_cell_middle(cell, 'green') ==
        "\033[32m|\033[0m %s \033[32m|\033[0m"
    )
    assert (
        test.frame_interface.cell_interface.get_cell_bottom(cell, 'green') ==
        "\033[32m+ – +\033[0m"
    )
    print("[O.K.]")


def test_frame_interface_no_colors() -> None:

    test: Output
    dom: maze.Maze

    dom = maze.Maze((4, 4))
    test = Output(
        dom=dom
    )

    print("test FrameInterface no colors :\t\t\t", end='')

    assert (test.dom == dom)
    assert (
        test.frame_interface.get_row_top(dom, 0) ==
        "+   + +   + +   + +   +\n"
    )
    assert (
        test.frame_interface.get_row_middle(dom, 0) ==
        "  %s     %s     %s     %s  \n"
    )
    assert (
        test.frame_interface.get_row_bottom(dom, 0) ==
        "+   + +   + +   + +   +\n"
    )
    assert (
        test.frame_interface.get_row_bottom(dom, 3) ==
        "+   + +   + +   + +   +"
    )
    dom.close_frame()
    assert (
        test.frame_interface.get_row_top(dom, 0) ==
        "+ – + + – + + – + + – +\n"
    )
    assert (
        test.frame_interface.get_row_middle(dom, 0) ==
        "| %s     %s     %s     %s |\n"
    )
    assert (
        test.frame_interface.get_row_bottom(dom, 0) ==
        "+   + +   + +   + +   +\n"
    )
    assert (
        test.frame_interface.get_row_bottom(dom, 3) ==
        "+ – + + – + + – + + – +"
    )
    dom.close_wall((1, 1), 'west')
    assert (
        test.frame_interface.get_row_middle(dom, 1) ==
        "| %s | | %s     %s     %s |\n"
    )
    print("[O.K.]")


def test_frame_interface_colors() -> None:

    test: Output
    dom: maze.Maze

    dom = maze.Maze((4, 4))
    test = Output(
        dom=dom
    )

    print("test FrameInterface with colors :\t\t", end='')

    assert (test.dom == dom)

    print("[Implement; expand method]")


def test_maze_interface_no_colors() -> None:

    test: Output
    dom: maze.Maze
    ctrl_1: str
    ctrl_2: str
    ctrl_3: str

    dom = maze.Maze((4, 4))
    test = Output(
        dom=dom
    )
    ctrl_1 = "+   + +   + +   + +   +\n"
    ctrl_1 += "  %s     %s     %s     %s  \n"
    ctrl_1 += "+   + +   + +   + +   +\n"
    ctrl_1 += "+   + +   + +   + +   +\n"
    ctrl_1 += "  %s     %s     %s     %s  \n"
    ctrl_1 += "+   + +   + +   + +   +\n"
    ctrl_1 += "+   + +   + +   + +   +\n"
    ctrl_1 += "  %s     %s     %s     %s  \n"
    ctrl_1 += "+   + +   + +   + +   +\n"
    ctrl_1 += "+   + +   + +   + +   +\n"
    ctrl_1 += "  %s     %s     %s     %s  \n"
    ctrl_1 += "+   + +   + +   + +   +"

    ctrl_2 = "+ – + + – + + – + + – +\n"
    ctrl_2 += "| %s     %s     %s     %s |\n"
    ctrl_2 += "+   + +   + +   + +   +\n"
    ctrl_2 += "+   + +   + +   + +   +\n"
    ctrl_2 += "| %s     %s     %s     %s |\n"
    ctrl_2 += "+   + +   + +   + +   +\n"
    ctrl_2 += "+   + +   + +   + +   +\n"
    ctrl_2 += "| %s     %s     %s     %s |\n"
    ctrl_2 += "+   + +   + +   + +   +\n"
    ctrl_2 += "+   + +   + +   + +   +\n"
    ctrl_2 += "| %s     %s     %s     %s |\n"
    ctrl_2 += "+ – + + – + + – + + – +"

    ctrl_3 = "+ – + + – + + – + + – +\n"
    ctrl_3 += "| %s     %s     %s     %s |\n"
    ctrl_3 += "+ – + +   + +   + +   +\n"
    ctrl_3 += "+ – + +   + +   + +   +\n"
    ctrl_3 += "| %s | | %s     %s     %s |\n"
    ctrl_3 += "+   + + – + + – + +   +\n"
    ctrl_3 += "+   + + – + + – + +   +\n"
    ctrl_3 += "| %s     %s     %s     %s |\n"
    ctrl_3 += "+   + +   + +   + +   +\n"
    ctrl_3 += "+   + +   + +   + +   +\n"
    ctrl_3 += "| %s     %s     %s     %s |\n"
    ctrl_3 += "+ – + + – + + – + + – +"

    print("test MazeInterface no colors :\t\t\t", end='')

    assert (test.dom == dom)
    test.set_frame_blank()
    assert(test.frame == ctrl_1)
    dom.close_frame()
    assert(test.frame == ctrl_1)
    test.set_frame_blank()
    assert(test.frame == ctrl_2)
    dom.close_wall((0, 0), 'south')
    dom.close_wall((1, 1), 'west')
    dom.close_wall((1, 1), 'south')
    dom.close_wall((2, 2), 'north')
    assert(test.frame == ctrl_2)
    test.set_frame_blank()
    assert(test.frame == ctrl_3)

    print("[O.K.]")

    print(
        test.frame_interface.cell_interface.get_cell_top(dom.cells[0][0])
    )
    print(
        test.frame_interface.cell_interface.get_cell_middle(dom.cells[0][0])
    )
    print(
        test.frame_interface.cell_interface.get_cell_bottom(dom.cells[0][0])
    )
    dom.close_frame()
    print(
        test.frame_interface.cell_interface.get_cell_top(dom.cells[0][0])
    )
    print(
        test.frame_interface.cell_interface.get_cell_middle(dom.cells[0][0])
    )
    print(
        test.frame_interface.cell_interface.get_cell_bottom(dom.cells[0][0])
    )
    print(
        test.frame_interface.cell_interface.get_cell_top(
            dom.cells[0][0],
            color='green'
        )
    )
    print(
        test.frame_interface.cell_interface.get_cell_middle(
            dom.cells[0][0],
            color='green'
        )
    )
    print(
        test.frame_interface.cell_interface.get_cell_bottom(
            dom.cells[0][0],
            color='green')
    )


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
