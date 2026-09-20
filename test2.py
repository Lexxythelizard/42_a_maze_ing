#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import maze.cells as cell
import maze
from maze.map.obj_1 import RelativeMazeMap as Relative

# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- sniggle ----------------------------

def test_relative_map() -> None:

    test: Relative
    ctrl: cell.RegularCell
    dom: maze.Maze

    dom = maze.Maze((4, 4))
    ctrl = dom.cells[1][1]
    test = Relative(
        dom=dom, coord=(1, 1)
    )

    print("test RelativeMazeMap :\t\t\t", end='')

    assert (test.coord == (1, 1))
    assert (test.ftcell is False)
    assert (test.map.get((0, 0)) == 16)
    assert (test.map.get((1, 1)) == 0)
    dom.cells[2][2] = cell.FourtyTwoCell()
    assert (test.map.get((2, 2)) == 16)
    test.init_42()
    assert (test.map.get((2, 2)) == 42)
    dom.cells[1][1] = cell.FourtyTwoCell()
    assert (test.ftcell is False)
    test.init_ftcell()
    assert (test.ftcell is True)
    assert (test.map.get((1, 1)) == 0)
    test.init_42()
    assert (test.map.get((1, 1)) == 42)
    assert (test.map.get((2, 2)) == 42)
    assert (test.map.get((1, 2)) == 16)
    assert (test.map.get((2, 1)) == 16)

    print("[O.K.]")


def test_relative_get_neighbours() -> None:

    print("test get neighnours :\t\t\t", end='')


    print("[under construction]")


# ---------------------------- utils ----------------------------

# def ...

# ---------------------------- run ----------------------------


def main() -> None:

    print("\n------------------------------------")
    test_relative_map()
    test_relative_get_neighbours()
    print("\n------------------------------------")


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
