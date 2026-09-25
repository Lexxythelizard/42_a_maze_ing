#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import abc
import typing
from maze.values.constants import Directions

# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------


# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++

# ---------------------------- abstr/par ----------------------------

class Cell(abc.ABC):

    """
    Generic maze Cell
    """

    __walls: int
    __visited: bool
    __locked: bool

    def __init__(self, walls: int = 0b0) -> None:
        self.__walls = walls
        self.__visited = False
        self.__locked = False

    def __int__(self) -> int:
        return (self.__walls)

    def __str__(self) -> str:
        return (str(hex(self.__walls))[-1])

    def _get_walls(self) -> int:
        return (self.__walls)

    def _set_walls(self, walls: int) -> None:
        self.__walls = walls

    def _set_visited(self, arg: typing.Any) -> None:
        if (arg):
            self.__visited = True
        else:
            self.__visited = False

    def _set_locked(self, arg: typing.Any) -> None:
        if (arg):
            self.__locked = True
        else:
            self.__locked = False

    @property
    def walls(self) -> int:
        return (self.__walls)

    @property
    def locked(self) -> bool:
        return (self.__locked)

    @property
    def visited(self) -> bool:
        return (self.__visited)

    @property
    def east_wall(self) -> bool:
        return (self.__walls & Directions.east)

    @property
    def south_wall(self) -> bool:
        return (self.__walls & Directions.south)

    @property
    def west_wall(self) -> bool:
        return (self.__walls & Directions.west)

    @property
    def north_wall(self) -> bool:
        return (self.__walls & Directions.north)

    @abc.abstractmethod
    def close_wall(self, wall: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def close_mult_walls(self, wall: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def open_wall(self, wall: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def open_mult_walls(self, wall: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def visit(self) -> None:
        pass

    @abc.abstractmethod
    def unvisit(self) -> None:
        pass

    @abc.abstractmethod
    def lock(self) -> None:
        pass

    @abc.abstractmethod
    def unlock(self) -> None:
        pass

    @staticmethod
    def parse_wall_param(wall: typing.Any) -> int:

        if (not isinstance(wall, (str, int))):
            raise TypeError("[spaceholder]")

        if (isinstance(wall, str)):
            return (Directions.directions.get(wall.strip().lower(), -1))

        return (wall)

    @staticmethod
    def value_guard_wall(wall: int) -> None:

        if (wall == 0):
            return
        if (wall in Directions.directions.values()):
            return
        raise ValueError("[Spaceholder]")

    @staticmethod
    def parse_walls_param(walls: typing.Any) -> int:

        if (isinstance(walls, int)):
            return (walls)

        if (not isinstance(walls, list)):
            raise TypeError("[Spaceholder]")

        walls = list(set(walls))
        walls = [Cell.parse_wall_param(wall) for wall in walls]
        walls = list(set(walls))
        if (-1 in walls):
            return (-1)
        return (sum(walls))

    @staticmethod
    def value_guard_walls(wall: int) -> None:

        if (wall < 0 or wall > 15):
            raise ValueError("[Spaceholder]")
