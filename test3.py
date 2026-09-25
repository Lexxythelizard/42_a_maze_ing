#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

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
    assert (test.cell.visited is True)

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
    assert (test.cell.visited is True)

    assert (test.move_east() is False)
    assert (test.move_north() is False)
    assert (test.move_south() is True)
    assert (test.position == (3, 1))
    assert (test.cell.visited is True)
    assert (test.move_west() is True)
    assert (test.position == (2, 1))
    assert (test.cell.visited is True)
    assert (test.move_west() is True)
    assert (test.position == (1, 1))
    assert (test.cell.visited is True)
    assert (test.move_north() is True)
    assert (test.position == (1, 0))
    assert (test.cell.visited is True)
    assert (test.move_north() is False)

    print("[O.K.]")


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
    assert (test.cell.visited is True)

    assert (test.is_open_east() is True)
    assert (test.is_open_north() is True)
    assert (test.is_open_west() is True)
    assert (test.is_open_south() is True)
    dom.close_frame()
    assert (test.is_open_east() is False)
    assert (test.is_open_north() is False)
    assert (test.is_open_west() is True)
    assert (test.is_open_south() is True)
    dom.close_wall((3, 0), 'west')
    assert (test.is_open_east() is False)
    assert (test.is_open_north() is False)
    assert (test.is_open_west() is False)
    assert (test.is_open_south() is True)
    assert (test.move_south() is True)
    assert (test.position == (3, 1))
    assert (test.is_open_east() is False)
    assert (test.is_open_north() is True)
    assert (test.is_open_west() is True)
    assert (test.is_open_south() is True)
    dom.close_wall((3, 1), 'south')
    assert (test.is_open_east() is False)
    assert (test.is_open_north() is True)
    assert (test.is_open_west() is True)
    assert (test.is_open_south() is False)
    assert (test.move_west() is True)
    assert (test.position == (2, 1))
    assert (test.is_open_east() is True)
    assert (test.is_open_north() is True)
    assert (test.is_open_west() is True)
    assert (test.is_open_south() is True)
    assert (test.move_north() is True)
    assert (test.position == (2, 0))
    assert (test.is_open_east() is False)
    assert (test.is_open_north() is False)
    assert (test.is_open_west() is True)
    assert (test.is_open_south() is True)

    print("[O.K.]")


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
    assert (test.cell.visited is True)

    assert (test.is_visited_north() is False)
    assert (test.is_visited_east() is False)
    assert (test.is_visited_south() is False)
    assert (test.is_visited_west() is False)

    dom.close_frame()
    assert (test.is_visited_north() is False)
    assert (test.is_visited_east() is False)
    assert (test.is_visited_south() is False)
    assert (test.is_visited_west() is False)

    assert (test.move_west() is True)
    assert (test.position == (2, 0))
    assert (test.is_visited_north() is False)
    assert (test.is_visited_east() is True)
    assert (test.is_visited_south() is False)
    assert (test.is_visited_west() is False)

    assert (test.move_south() is True)
    assert (test.position == (2, 1))
    assert (test.is_visited_north() is True)
    assert (test.is_visited_east() is False)
    assert (test.is_visited_south() is False)
    assert (test.is_visited_west() is False)

    assert (dom.close_wall((2, 1), "north") is True)
    assert (test.position == (2, 1))
    assert (test.is_visited_north() is True)
    assert (test.is_visited_east() is False)
    assert (test.is_visited_south() is False)
    assert (test.is_visited_west() is False)

    dom = maze.Maze((4, 4))
    test = MazeRunner(
        dom=dom, position=(2, 2)
    )
    assert (test.cell == dom._get_cell((2, 2)))
    assert (test.position == (2, 2))
    assert (test.cell.visited is True)

    assert (test.is_visited_north() is False)
    assert (test.is_visited_east() is False)
    assert (test.is_visited_south() is False)
    assert (test.is_visited_west() is False)

    assert (dom.close_wall((2, 2), "east") is True)
    assert (dom.close_wall((2, 2), "south") is True)
    assert (dom.close_wall((2, 2), "west") is True)
    assert (dom.close_wall((2, 2), "north") is True)
    assert (test.is_visited_north() is False)
    assert (test.is_visited_east() is False)
    assert (test.is_visited_south() is False)
    assert (test.is_visited_west() is False)

    dom._get_cell((3, 2)).visit()
    dom._get_cell((2, 3)).visit()
    dom._get_cell((1, 2)).visit()
    dom._get_cell((2, 1)).visit()
    assert (test.is_visited_north() is True)
    assert (test.is_visited_east() is True)
    assert (test.is_visited_south() is True)
    assert (test.is_visited_west() is True)

    assert (dom.open_wall((2, 2), "east") is True)
    assert (dom.open_wall((2, 2), "south") is True)
    assert (dom.open_wall((2, 2), "west") is True)
    assert (dom.open_wall((2, 2), "north") is True)
    assert (test.is_visited_north() is True)
    assert (test.is_visited_east() is True)
    assert (test.is_visited_south() is True)
    assert (test.is_visited_west() is True)

    print("[O.K.]")


def test_maze_runner_move_with_walls() -> None:

    test: MazeRunner
    dom: maze.Maze

    dom = maze.Maze((4, 4))
    test = MazeRunner(
        dom=dom, position=(3, 0)
    )

    print("test MazeRunner move - walls :\t\t\t", end='')

    assert (test.dom == dom)
    assert (test.cell == dom._get_cell((3, 0)))
    assert (test.position == (3, 0))
    assert (test.cell.visited is True)
    dom.close_frame()
    assert (dom.close_wall((3, 0), "west") is True)
    assert (dom.close_wall((3, 1), "south") is True)
    assert (dom.close_wall((2, 1), "west") is True)
    assert (dom.close_wall((2, 1), "south") is True)
    assert (dom.close_wall((1, 0), "west") is True)
    assert (dom.close_wall((1, 1), "west") is True)

    assert (test.move_north() is False)
    assert (test.move_west() is False)
    assert (test.move_east() is False)
    assert (test.move_south() is True)
    assert (test.position == (3, 1))
    assert (test.move_east() is False)
    assert (test.move_south() is False)
    assert (test.move_west() is True)
    assert (test.position == (2, 1))
    assert (test.move_west() is False)
    assert (test.move_south() is False)
    assert (test.move_north() is True)
    assert (test.position == (2, 0))
    assert (test.move_north() is False)
    assert (test.move_east() is False)
    assert (test.move_west() is True)
    assert (test.position == (1, 0))
    assert (test.move_north() is False)
    assert (test.move_west() is False)
    assert (test.move_south() is True)
    assert (test.position == (1, 1))
    assert (test.move_west() is False)
    assert (test.move_east() is False)
    assert (test.move_south() is True)
    assert (test.position == (1, 2))
    assert (test.move_west() is True)
    assert (test.position == (0, 2))
    assert (test.move_west() is False)
    assert (test.move_north() is True)
    assert (test.position == (0, 1))
    assert (test.move_west() is False)
    assert (test.move_east() is False)
    assert (test.move_north() is True)
    assert (test.position == (0, 0))

    print("[O.K.]")


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
