#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import maze.cells as cell

# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- sniggle ----------------------------

def test_single_42() -> None:

    test: cell.FourtyTwoCell
    test = cell.FourtyTwoCell()
    print("test 42cell single wall :\t\t\t", end='')
    assert (test.close_wall('west') == True)
    assert (int(test) == 0b1000)
    assert (str(test) == '8')
    assert (test.close_wall(0b1000) == True)
    assert (int(test) == 0b1000)
    assert (str(test) == '8')
    test.lock()
    assert (test.close_wall(0b0001) == False)
    assert (int(test) == 0b1000)
    assert (str(test) == '8')
    assert (test.open_wall(0b1000) == False)
    assert (int(test) == 0b1000)
    assert (str(test) == '8')
    test.unlock()
    assert (test.close_wall(0b0001) == True)
    assert (int(test) == 0b1001)
    assert (str(test) == '9')
    assert (test.open_wall('s') == True)
    assert (int(test) == 0b1001)
    assert (str(test) == '9')
    assert (test.open_wall(0b0001) == True)
    assert (int(test) == 0b1000)
    assert (str(test) == '8')
    assert (test.open_wall(0b1000) == True)
    assert (int(test) == 0b0000)
    assert (str(test) == '0')
    assert (test.open_wall(0b0000) == True)
    assert (int(test) == 0b0000)
    assert (str(test) == '0')

    print("[O.K.]")


def test_multiple_42() -> None:

    test: cell.FourtyTwoCell
    test = cell.FourtyTwoCell()
    print("test 42cell multiple walls / arguments :\t", end='')
    assert (test.close_mult_walls(['west', 'w', 'e']) == True)
    assert (int(test) == 10)
    assert (str(test) == 'a')
    assert (test.close_mult_walls(14) == True)
    assert (int(test) == 14)
    assert (str(test) == 'e')
    test.lock()
    assert (test.close_mult_walls(1) == False)
    assert (int(test) == 14)
    assert (str(test) == 'e')
    assert (test.open_mult_walls(1) == False)
    assert (int(test) == 14)
    assert (str(test) == 'e')
    test.unlock()
    assert (test.close_mult_walls(1) == True)
    assert (int(test) == 15)
    assert (str(test) == 'f')
    assert (test.open_mult_walls(['s']) == True)
    assert (int(test) == 11)
    assert (str(test) == 'b')
    assert (test.open_mult_walls(5) == True)
    assert (int(test) == 10)
    assert (str(test) == 'a')
    assert (test.open_mult_walls(0b0111) == True)
    assert (int(test) == 0b1000)
    assert (str(test) == '8')
    assert (test.open_mult_walls(0b0000) == True)
    assert (int(test) == 0b1000)
    assert (str(test) == '8')

    print("[O.K.]")


def test_single_regular() -> None:

    test: cell.RegularCell
    test = cell.RegularCell()
    print("test regular cell single wall :\t\t\t", end='')
    assert (bool(test) == False)
    test.visit()
    assert (bool(test) == True)
    test.unvisit()
    assert (bool(test) == False)
    assert (test.close_wall('west') == True)
    assert (int(test) == 0b1000)
    assert (str(test) == '8')
    assert (test.close_wall(0b1000) == True)
    assert (int(test) == 0b1000)
    assert (str(test) == '8')
    test.lock()
    assert (test.close_wall(0b0001) == True)
    assert (int(test) == 0b1001)
    assert (str(test) == '9')
    assert (test.open_wall(0b1000) == False)
    assert (int(test) == 0b1001)
    assert (str(test) == '9')
    test.unlock()
    assert (test.close_wall(0b0001) == True)
    assert (int(test) == 0b1001)
    assert (str(test) == '9')
    assert (test.open_wall('s') == True)
    assert (int(test) == 0b1001)
    assert (str(test) == '9')
    assert (test.open_wall(0b0001) == True)
    assert (int(test) == 0b1000)
    assert (str(test) == '8')
    assert (test.open_wall(0b1000) == True)
    assert (int(test) == 0b0000)
    assert (str(test) == '0')
    assert (test.open_wall(0b0000) == True)
    assert (int(test) == 0b0000)
    assert (str(test) == '0')

    print("[O.K.]")


def test_multiple_regular() -> None:

    test: cell.RegularCell
    test = cell.RegularCell()
    print("test regular cell multiple walls / arguments :\t", end='')
    assert (test.close_mult_walls(['west', 'w', 'e']) == True)
    assert (int(test) == 0b1010)
    assert (str(test) == 'a')
    assert (test.close_mult_walls(0b1110) == True)
    assert (int(test) == 0b1110)
    assert (str(test) == 'e')
    test.lock()
    assert (test.close_mult_walls(0b0001) == True)
    assert (int(test) == 0b1111)
    assert (str(test) == 'f')
    assert (test.open_mult_walls(0b0001) == True)
    assert (int(test) == 0b1110)
    assert (str(test) == 'e')
    test.unlock()
    assert (test.close_mult_walls(0b0001) == True)
    assert (int(test) == 0b1111)
    assert (str(test) == 'f')
    assert (test.open_mult_walls(['s']) == True)
    assert (int(test) == 0b1011)
    assert (str(test) == 'b')
    assert (test.open_mult_walls(0b0101) == True)
    assert (int(test) == 0b1010)
    assert (str(test) == 'a')
    assert (test.open_mult_walls(0b0111) == True)
    assert (int(test) == 0b1000)
    assert (str(test) == '8')
    assert (test.open_mult_walls(0b0000) == True)
    assert (int(test) == 0b1000)
    assert (str(test) == '8')

    print("[O.K.]")


# ---------------------------- utils ----------------------------

# def ...

# ---------------------------- run ----------------------------


def main() -> None:

    print("\n------------------------------------")
    test_single_42()
    test_multiple_42()
    test_single_regular()
    test_multiple_regular()
    print("\n------------------------------------")


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
