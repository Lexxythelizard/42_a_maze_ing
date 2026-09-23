#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import maze.cells as cell
import maze
from maze.map.obj import RelativeMazeMap as Relative
from maze.map.obj import MazeMap as Map

# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- sniggle ----------------------------

def test_relative_map() -> None:

    test: Relative
    dom: maze.Maze

    dom = maze.Maze((4, 4))
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

    test: Relative
    ctrl_1: dict[tuple[int, int], cell.Cell]
    ctrl_2: dict[tuple[int, int], cell.Cell]
    dom: maze.Maze

    dom = maze.Maze((4, 4))
    ctrl_1 = {
        (2, 1): dom.cells[2][1],
        (1, 2): dom.cells[1][2],
        (0, 1): dom.cells[0][1],
        (1, 0): dom.cells[1][0]
    }
    ctrl_2 = {
        (2, 1): dom.cells[2][1],
        (1, 2): dom.cells[1][2]
    }
    test = Relative(
        dom=dom, coord=(1, 1)
    )

    print("test get neighnours :\t\t\t", end='')

    assert (test.coord == (1, 1))
    assert (test.ftcell is False)
    assert (test.get_neighbours(restricted=False) == ctrl_1)
    assert (test.get_neighbours() == ctrl_1)
    dom.cells[1][1].close_mult_walls(0b1001)
    assert (test.get_neighbours(restricted=False) == ctrl_1)
    assert (test.get_neighbours() == ctrl_2)

    print("[O.K.]")


def test_set_cell() -> None:

    test: Relative
    ctrl_1: str
    ctrl_2: str
    dom: maze.Maze

    dom = maze.Maze((4, 4))
    test = Relative(
        dom=dom, coord=(1, 1)
    )
    ctrl_1 = "ValueError: Invalid map key! expected one of "
    ctrl_1 += "[1, 2, 4, 8, 0, 16, -1, 42] got 3"

    print("test set map cell :\t\t\t", end='')

    assert (test.coord == (1, 1))
    assert (test.ftcell is False)
    test.set_map_cell((0, 0), 2)
    assert (test.map[(0, 0)] == 2)
    test.set_map_cell((0, 1), 4)
    assert (test.map[(0, 1)] == 4)
    test.set_map_cell((1, 2), 1)
    assert (test.map[(1, 2)] == 1)
    test.set_map_cell((2, 1), 8)
    assert (test.map[(2, 1)] == 8)
    test.set_map_cell((2, 2), 42)
    assert (test.map[(2, 2)] == 42)
    test.set_map_cell((1, 1), 0)
    assert (test.map[(1, 1)] == 0)
    test.set_map_cell((3, 3), -1)
    assert (test.map[(3, 3)] == -1)
    try:
        test.set_map_cell((2, 2), 3)
    except ValueError as err:
        ctrl_2 = str(err)
    assert (ctrl_1 == ctrl_2)
    print("[O.K.]")


def test_meta_map() -> None:

    test: Map
    ctrl_1: dict[tuple[int, int], cell.Cell]
    ctrl_2: dict[tuple[int, int], cell.Cell]
    dom: maze.Maze

    dom = maze.Maze((4, 4))

    ctrl_1 = {
        (2, 1): dom.cells[2][1],
        (1, 2): dom.cells[1][2],
        (0, 1): dom.cells[0][1],
        (1, 0): dom.cells[1][0]
    }
    ctrl_2 = {
        (2, 1): dom.cells[2][1],
        (1, 2): dom.cells[1][2]
    }
    test = Map(dom=dom)

    print("test (meta) MazeMap :\t\t\t", end='')

    assert (test.dom == dom)
    assert (test.map[(1, 1)].dom == dom)
    assert (test.width == 4)
    assert (test.height == 4)
    assert (test.map[(1, 1)].map[(1, 1)] == 0)
    assert (test.map[(1, 1)].map[(2, 2)] == 16)
    assert (test.map[(1, 1)] == test.get_relative_map((1, 1)))
    assert (
        test.map[(1, 1)].map[(2, 2)] ==
        test.get_relative_map((1, 1)).map[(2, 2)]
    )
    assert (test.map[(1, 1)].get_neighbours(restricted=False) == ctrl_1)
    assert (test.get_relative_map((1, 1)).get_neighbours() == ctrl_1)
    assert (test.get_relative_neighbours((1, 1)) == ctrl_1)
    dom.cells[1][1].close_mult_walls(0b1001)
    assert (test.map[(1, 1)].get_neighbours() == ctrl_2)
    assert (test.get_relative_map((1, 1)).get_neighbours() == ctrl_2)
    assert (test.get_relative_neighbours((1, 1)) == ctrl_2)
    assert (
        test.get_relative_neighbours((1, 1), restricted=False) == ctrl_1
    )

    print("[O.K.]")


def test_set_relative_map_cell() -> None:

    test: Map
    dom: maze.Maze

    dom = maze.Maze((4, 4))
    test = Map(dom=dom)

    print("test set_relative_map_cell :\t\t", end='')

    assert (test.dom == dom)
    assert (test.map[(1, 1)].dom == dom)
    test.set_relative_map_cell(
        coord_map=(1, 1), coord_cell=(2, 2), key=4
    )
    assert (test.map[(1, 1)].map[(2, 2)] == 4)
    assert (test.map[(1, 1)].map[(1, 1)] == 0)
    assert (test.map[(0, 0)].map[(2, 2)] == 16)
    assert (test.map[(0, 0)].map[(1, 1)] == 16)
    assert (test.map[(2, 2)].map[(2, 2)] == 0)

    print("[O.K.]")


# ---------------------------- utils ----------------------------

# def ...

# ---------------------------- run ----------------------------


def main() -> None:

    print("\n------------------------------------\n")
    test_relative_map()
    test_relative_get_neighbours()
    test_set_cell()
    test_meta_map()
    test_set_relative_map_cell()
    print("\n------------------------------------")


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
