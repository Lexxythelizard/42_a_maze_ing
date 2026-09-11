#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import typing
from maze.cells.base import Cell

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------


# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class FourtyTwoCell(Cell):

    """
    Unvisitable 42 maze Cell
    """

    __locked: bool

    def __init__(self, walls: int = 0b0) -> None:

        super().__init__(walls)
        self.__locked = False

    def close_wall(self, wall: typing.Any) -> bool:

        wall = self.parse_wall_param(wall)
        self.value_guard_wall(wall)

        if (self.__locked):
            return (False)
        self._set_walls(self._get_walls() | wall)
        return (True)

    def open_wall(self, wall: typing.Any) -> bool:

        wall = self.parse_wall_param(wall)
        self.value_guard_wall(wall)

        if (self.__locked):
            return (False)
        self._set_walls((self._get_walls() ^ wall) & self._get_walls())
        return (True)

    def close_mult_walls(self, walls: typing.Any) -> bool:

        walls = self.parse_walls_param(walls)
        self.value_guard_walls(walls)

        if (self.__locked):
            return (False)
        self._set_walls(self._get_walls() | walls)
        return (True)

    def open_mult_walls(self, walls: typing.Any) -> bool:

        walls = self.parse_walls_param(walls)
        self.value_guard_walls(walls)

        if (self.__locked):
            return (False)
        self._set_walls((self._get_walls() ^ walls) & self._get_walls())
        return (True)

    def lock(self) -> None:
        self.__locked = True

    def unlock(self) -> None:
        self.__locked = False


class RegularCell(Cell):

    """
    Generic maze Cell
    """

    __walls: int
    __constant_walls: int
    __visited: bool

    def __init__(self, walls: int = 0b0) -> None:

        super().__init__(walls)
        self.__visited = False

    def __bool__(self) -> bool:
        return (self.__visited)

    def close_wall(self, wall: typing.Any) -> bool:

        wall = self.parse_wall_param(wall)
        self.value_guard_wall(wall)

        self._set_walls(self._get_walls() | wall)
        return (True)

    def open_wall(self, wall: typing.Any) -> bool:

        wall = self.parse_wall_param(wall)
        self.value_guard_wall(wall)

        if (self.__constant_walls & wall):
            return (False)
        self._set_walls(
            (
                (
                    self._get_walls() ^ wall
                ) & self._get_walls()) | self.__constant_walls
        )
        return (True)

    def close_mult_walls(self, walls: typing.Any) -> bool:

        walls = self.parse_walls_param(walls)
        self.value_guard_walls(walls)

        self._set_walls(self._get_walls() | walls)
        return (True)

    def open_mult_walls(self, walls: typing.Any) -> bool:

        walls = self.parse_walls_param(walls)
        self.value_guard_walls(walls)

        if (self.__constant_walls & walls):
            return (False)
        self._set_walls(
            (
                (
                    self._get_walls() ^ walls
                ) & self._get_walls()) | self.__constant_walls
        )
        return (True)

    def lock(self) -> None:
        self.__constant_walls = self._get_walls()

    def unlock(self) -> None:
        self.__constant_walls &= 0b0

    def visit(self) -> None:
        self.__visited = True

    def unvisit(self) -> None:
        self.__visited = False


# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- sniggle ----------------------------

# def ...

# ---------------------------- utils ----------------------------

# def ...

# ---------------------------- run ----------------------------


def main() -> None:
    pass


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
