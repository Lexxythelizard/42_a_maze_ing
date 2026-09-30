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
    42 maze Cell is a special Cell which is not made for being
    visited or entered.
    Yet it could get visited.

    stats:

        __walls:    representing the four walls by the powers of two
                    int: 0 <= walls <= 15
        __visted:   bool
        __locked:   bool: if True no changes in walls are possible

    if Cell is locked open or close walls is not possible.
    set their walls once:
    recommended in Orchestering MazeObject, then lock Cell
    """

    def close_wall(self, wall: typing.Any) -> bool:

        """
        closes [direction] wall if cell is not locked
        if success: return True else return False

        valid directions-args are:
        [1, 2, 4, 8, 'n', 'e', 's', 'w', "north", "east", "south", "west"]
        raise Error if invalid argument was passed
        """

        wall = self.parse_wall_param(wall)
        self.value_guard_wall(wall)

        if (self.locked):
            return (False)
        self._set_walls(self._get_walls() | wall)
        return (True)

    def open_wall(self, wall: typing.Any) -> bool:

        """
        opens [direction] wall if cell is not locked
        if success: return True else return False

        valid directions-args are:
        [1, 2, 4, 8, 'n', 'e', 's', 'w', "north", "east", "south", "west"]
        raise Error if invalid argument was passed
        """

        wall = self.parse_wall_param(wall)
        self.value_guard_wall(wall)

        if (self.locked):
            return (False)
        self._set_walls((self._get_walls() ^ wall) & self._get_walls())
        return (True)

    def close_mult_walls(self, walls: typing.Any) -> bool:

        """
        closess [direction, ...] walls if cell is not locked
        if success: return True else return False

        valid direction-args a a list containig arbitary amount of
        valid directions:
        [1, 2, 4, 8, 'n', 'e', 's', 'w', "north", "east", "south", "west"]
        or any integer in (closed) intervall 0 and 15
        raise Error if invalid argument was passed
        """

        walls = self.parse_walls_param(walls)
        self.value_guard_walls(walls)

        if (self.locked):
            return (False)
        self._set_walls(self._get_walls() | walls)
        return (True)

    def open_mult_walls(self, walls: typing.Any) -> bool:

        """
        opens [direction, ...] walls if cell is not locked
        if success: return True else return False

        valid direction-args a a list containig arbitary amount of
        valid directions:
        [1, 2, 4, 8, 'n', 'e', 's', 'w', "north", "east", "south", "west"]
        or any integer in (closed) intervall 0 and 15
        raise Error if invalid argument was passed
        """

        walls = self.parse_walls_param(walls)
        self.value_guard_walls(walls)

        if (self.locked):
            return (False)
        self._set_walls((self._get_walls() ^ walls) & self._get_walls())
        return (True)

    def lock(self) -> None:
        """
        sets .locked to True
        """
        self._set_locked(True)

    def unlock(self) -> None:
        """
        sets .unlocked to False
        """
        self._set_locked(False)

    def visit(self) -> None:
        """
        sets .visited to True
        """
        self._set_visited(True)

    def unvisit(self) -> None:
        """
        sets .visited to False
        """
        self._set_visited(False)


class RegularCell(Cell):

    """
    42 maze Cell is a special Cell which is not made for being
    visited or entered.
    Yet it could get visited.

    stats:

        __walls:    representing the four walls by the powers of two
                    int: 0 <= walls <= 15
        __visted:   bool
        __locked:   bool: if True no changes in walls are possible

    if Cell is locked open or close walls is not possible.
    set their walls once:
    recommended in Orchestering MazeObject, then lock Cell
    """

    __constant_walls: int

    @property
    def constant_walls(self) -> int:
        return (self.__constant_walls)

    def __init__(self, walls: int = 0b0) -> None:

        super().__init__(walls)
        self.__constant_walls = 0b0000

    def __bool__(self) -> bool:
        return (self.visited)

    def close_wall(self, wall: typing.Any) -> bool:

        """
        closes [direction] wall
        returns allways True

        valid directions-args are:
        [1, 2, 4, 8, 'n', 'e', 's', 'w', "north", "east", "south", "west"]
        raise Error if invalid argument was passed
        """

        wall = self.parse_wall_param(wall)
        self.value_guard_wall(wall)

        self._set_walls(self._get_walls() | wall)
        return (True)

    def open_wall(self, wall: typing.Any) -> bool:

        """
        opens [direction] wall if wall [direction] is not constant
        if success: return True else return False

        valid directions-args are:
        [1, 2, 4, 8, 'n', 'e', 's', 'w', "north", "east", "south", "west"]
        raise Error if invalid argument was passed
        """

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

        """
        closes [direction, ...] walls
        returns allways True

        valid direction-args a a list containig arbitary amount of
        valid directions:
        [1, 2, 4, 8, 'n', 'e', 's', 'w', "north", "east", "south", "west"]
        or any integer in (closed) intervall 0 and 15
        raise Error if invalid argument was passed
        """

        walls = self.parse_walls_param(walls)
        self.value_guard_walls(walls)

        self._set_walls(self._get_walls() | walls)
        return (True)

    def open_mult_walls(self, walls: typing.Any) -> bool:

        """
        opens [direction, ...] walls if cell is none of them is constant
        if success: return True else return False

        valid direction-args a a list containig arbitary amount of
        valid directions:
        [1, 2, 4, 8, 'n', 'e', 's', 'w', "north", "east", "south", "west"]
        or any integer in (closed) intervall 0 and 15
        raise Error if invalid argument was passed
        """

        walls = self.parse_walls_param(walls)
        self.value_guard_walls(walls)

        if (self.__constant_walls & walls):
            return (False)
        self._set_walls(
            (
                (
                    self.walls ^ walls
                ) & self.walls) | self.__constant_walls
        )
        return (True)

    def lock(self) -> None:
        """
        sets .locked to True
        and make closed walls constant
        """
        self.__constant_walls = self.walls
        self._set_locked(self.walls)

    def unlock(self) -> None:
        """
        sets .lockeded to False
        and make closed unconstant
        """
        self.__constant_walls &= 0b0
        self._set_locked(0b0)

    def visit(self) -> None:
        """
        sets .visited to True
        """
        self._set_visited(True)

    def unvisit(self) -> None:
        """
        sets .visited to False
        """
        self._set_visited(False)
