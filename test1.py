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
    #assert (len(test.cells) == 25)
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
    assert (bool(test._get_cell((1, 1))) == False)
    assert (test.set_visit((1, 1)) == None)
    assert (bool(test._get_cell((1, 1))) == True)
    assert (test.close_wall((1, 1), 0b1000) == True)
    assert (int(test._get_cell((1, 1))) == 0b1000)
    assert (test.set_unvisit((1, 1)) == None)
    assert (bool(test._get_cell((1, 1))) == False)
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
    test.close_wall((2, 0), 0b0001)
    test.close_wall((2, 0), 0b0010)
    test.close_wall((0, 2), 0b0100)
    test.close_wall((0, 2), 0b1000)
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
    assert (test.open_wall((0, 0), 0b0001) == False)
    assert (test.open_wall((0, 0), 0b1000) == False)
    assert (test.open_wall((2, 0), 0b0001) == False)
    assert (test.open_wall((2, 0), 0b0010) == False)
    assert (test.open_wall((2, 2), 0b0010) == False)
    assert (test.open_wall((2, 2), 0b0100) == False)
    assert (test.open_wall((0, 2), 0b0100) == False)
    assert (test.open_wall((0, 2), 0b1000) == False)
    assert (test.close_wall((1, 0), 0b0100) == True)
    print("[O.K.]")

# ---------------------------- neighbors ----------------------------

# follows

# ---------------------------- utils ----------------------------

# def ...

# ---------------------------- run ----------------------------

def main() -> None:
    print("\n------------------------------------")
    test_maze_init()
    test_maze_dimensions()
    test_maze_cell_access()
    test_maze_cell_state()
    test_maze_str()
    test_maze_frame()
    print("\n------------------------------------")

# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':
    main()

