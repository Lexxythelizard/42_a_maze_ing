#!/usr/bin/python3


# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++
import maze
import maze.cells as cell

# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++

# ---------------------------- initialization ----------------------------


def test_maze_init() -> None:
    test: maze.Maze

    print("test maze init :\t\t\t\t", end='')
    test = maze.Maze((5, 5))
    assert (test.get_width() == 5)
    assert (test.get_height() == 5)
    print("[O.K.]")


# ---------------------------- dimensions ----------------------------


def test_maze_dimensions() -> None:
    test: maze.Maze

    print("test maze dimensions :\t\t\t\t", end='')
    test = maze.Maze((10, 8))
    assert (test.get_width() == 10)
    assert (test.get_height() == 8)
    assert (test.get_size() == (10, 8))
    print("[O.K.]")


# ---------------------------- cell access ----------------------------


def test_maze_cell_access() -> None:
    test: maze.Maze

    print("test maze cell access :\t\t\t\t", end='')
    test = maze.Maze((3, 3))
    assert (isinstance(test._get_cell((0, 0)), cell.RegularCell))
    assert (isinstance(test._get_cell((1, 1)), cell.RegularCell))
    assert (isinstance(test._get_cell((2, 2)), cell.RegularCell))
    assert (test._get_cell((0, 0)) is test._get_grid()[0][0])
    assert (test._get_cell((1, 0)) is test._get_grid()[1][0])
    print("[O.K.]")


# ---------------------------- cell state ----------------------------


def test_maze_cell_state() -> None:
    test: maze.Maze

    print("test maze cell state :\t\t\t\t", end='')
    test = maze.Maze((4, 4))
    assert (bool(test._get_cell((1, 1))) is False)
    test.set_visit((1, 1))
    assert (bool(test._get_cell((1, 1))) is True)
    assert (test.close_wall((1, 1), 0b1000, semipermeable=True) is True)
    assert (int(test._get_cell((1, 1))) == 0b1000)
    test.set_unvisit((1, 1))
    assert (bool(test._get_cell((1, 1))) is False)
    print("[O.K.]")


# ---------------------------- str checking ----------------------------


def test_maze_str() -> None:
    test: maze.Maze

    print("test maze str :\t\t\t\t\t", end='')
    test = maze.Maze((2, 2))
    assert (str(test) == "00\n00")
    test.close_frame()
    assert (str(test) == "93\nc6")
    test = maze.Maze((3, 3))
    assert (str(test) == "000\n000\n000")
    test.close_wall((2, 0), 0b0001, semipermeable=True)
    test.close_wall((2, 0), 0b0010, semipermeable=True)
    test.close_wall((0, 2), 0b0100, semipermeable=True)
    test.close_wall((0, 2), 0b1000, semipermeable=True)
    assert (str(test) == "003\n000\nc00")
    print("[O.K.]")


# ---------------------------- frame checking ----------------------------


def test_maze_frame() -> None:

    test: maze.Maze

    print("test maze frame :\t\t\t\t", end='')
    test = maze.Maze((2, 2))
    test.close_frame()
    assert (str(test) == "93\nc6")
    test = maze.Maze((3, 3))
    test.close_frame()
    assert (str(test) == "913\n802\nc46")
    assert (test.open_wall((0, 0), 0b0001, semipermeable=True) is False)
    assert (test.open_wall((0, 0), 0b1000, semipermeable=True) is False)
    assert (test.open_wall((2, 0), 0b0001, semipermeable=True) is False)
    assert (test.open_wall((2, 0), 0b0010, semipermeable=True) is False)
    assert (test.open_wall((2, 2), 0b0010, semipermeable=True) is False)
    assert (test.open_wall((2, 2), 0b0100, semipermeable=True) is False)
    assert (test.open_wall((0, 2), 0b0100, semipermeable=True) is False)
    assert (test.open_wall((0, 2), 0b1000, semipermeable=True) is False)
    assert (test.close_wall((1, 0), 0b0100, semipermeable=True) is True)
    print("[O.K.]")


def test_opposite_direction() -> None:

    test: maze.Maze

    print("test opposite_direction :\t\t\t", end='')
    test = maze.Maze((3, 3))
    assert (test.get_opposite_direction(0b1111) == 0)
    assert (test.get_opposite_direction(0b0000) == 0)
    assert (test.get_opposite_direction(1) == 4)
    assert (test.get_opposite_direction(4) == 1)
    assert (test.get_opposite_direction(2) == 8)
    assert (test.get_opposite_direction(8) == 2)
    assert (test.get_opposite_direction("north") == 4)
    assert (test.get_opposite_direction("south") == 1)
    assert (test.get_opposite_direction("east") == 8)
    assert (test.get_opposite_direction("west") == 2)
    assert (test.get_opposite_direction(0b0001) == 0b0100)
    assert (test.get_opposite_direction(0b0100) == 0b0001)
    assert (test.get_opposite_direction(0b0010) == 0b1000)
    assert (test.get_opposite_direction(0b1000) == 0b0010)
    print("[O.K.]")


def test_maze_open_default_setting() -> None:

    test: maze.Maze

    print("test maze_open_wall no semipermeable :\t\t", end='')
    test = maze.Maze((3, 3))
    assert (test.open_wall((0, 0), 0b0001) is True)
    assert (test.open_wall((1, 1), 0b0001) is True)
    assert (int(test._get_cell((0, 0))) == 0b0000)
    assert (int(test._get_cell((1, 1))) == 0b0000)
    test.close_frame()
    assert (int(test._get_cell((0, 0))) == 0b1001)
    assert (test.open_wall((0, 0), 0b0001) is False)
    assert (test.open_wall((0, 1), 0b0001) is True)
    assert (test.open_wall((1, 1), 0b0001) is True)
    assert (int(test._get_cell((0, 0))) == 0b1001)
    assert (int(test._get_cell((0, 1))) == 0b1000)
    assert (int(test._get_cell((1, 1))) == 0b0000)
    test._get_cell((1, 0)).close_wall(0b0100)
    assert (int(test._get_cell((1, 0))) == 0b0101)
    assert (int(test._get_cell((1, 1))) == 0b0000)
    assert (test.open_wall((1, 0), 0b0001) is False)
    assert (test.open_wall((1, 1), 0b0001) is True)
    assert (int(test._get_cell((1, 0))) == 0b0001)
    assert (int(test._get_cell((1, 1))) == 0b0000)

    test._get_cell((1, 0)).close_wall(0b0100)
    test._get_cell((1, 0)).lock()
    assert (int(test._get_cell((1, 0))) == 0b0101)
    assert (int(test._get_cell((1, 1))) == 0b0000)
    assert (test.open_wall((1, 0), 0b0001) is False)
    assert (test.open_wall((1, 1), 0b0001) is False)
    assert (int(test._get_cell((1, 0))) == 0b0101)
    assert (int(test._get_cell((1, 1))) == 0b0000)

    print("[O.K.]")


def test_maze_close_default_setting() -> None:

    test: maze.Maze

    print("test maze_close_wall no semipermeable :\t\t", end='')
    test = maze.Maze((3, 3))
    assert (test.close_wall((1, 0), 0b0001) is True)
    assert (int(test._get_cell((1, 0))) == 0b0001)
    assert (int(test._get_cell((1, 1))) == 0b0000)
    assert (test.close_wall((1, 1), 0b0001) is True)
    assert (int(test._get_cell((1, 0))) == 0b0101)
    assert (int(test._get_cell((1, 1))) == 0b0001)
    test.close_frame()
    assert (int(test._get_cell((0, 0))) == 0b1001)
    assert (int(test._get_cell((1, 0))) == 0b0101)
    assert (int(test._get_cell((1, 1))) == 0b0001)

    assert (test.close_wall((0, 1), 0b1000) is True)
    assert (int(test._get_cell((0, 1))) == 0b1000)
    assert (int(test._get_cell((1, 1))) == 0b0001)

    assert (test.close_wall((0, 1), 0b0010) is True)
    assert (int(test._get_cell((0, 1))) == 0b1010)
    assert (int(test._get_cell((1, 1))) == 0b1001)
    assert (int(test._get_cell((0, 0))) == 0b1001)

    assert (str(test) == "953\na92\nc46")
    print("[O.K.]")


# ---------------------------- utils ----------------------------

# def ...

# ---------------------------- run ----------------------------


def main() -> None:

    print("\n------------------------------------\n")
    test_maze_init()
    test_maze_dimensions()
    test_maze_cell_access()
    test_maze_cell_state()
    test_maze_str()
    test_maze_frame()
    test_opposite_direction()
    test_maze_open_default_setting()
    test_maze_close_default_setting()
    print("\n------------------------------------")

# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++


if __name__ == '__main__':
    main()
