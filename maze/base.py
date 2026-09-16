#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import typing
import abc
import maze.cells as cell
from maze.values.constants import Directions

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# TODO: implement get_neighbour

# ---------------------------- strings ----------------------------


class StringContainer:

    coord_err = "Error: Coords must be 0 < x %d; 0 < y < %d; got x: %d, y: %d"
    size_err = "Error: Size (width, height) must be greater than 0"
    size_err += ", got (%d, %d)"
    cell_err = "Error: Expected instance of Cell got %s instead"

    coord_type_err_0 = "Error: Expected tuple[int, int], got %s"
    coord_type_err_1 = "Error: Expected tuple[int, int], got tuple[%s, %s]"


# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class BlueprintMaze(abc.ABC):

    """
    Maze Blueprint
    """

    __cells: list[list[cell.Cell]]
    __height: int
    __width: int

    def __init__(
        self,
        size: tuple[int, int],
    ) -> None:

        width: int
        height: int

        self.__width = 0
        self.__height = 0
        self.__cells = []

        self._guard_coord_type(size)

        width, height = size
        if (width <= 0 or height <= 0):
            raise ValueError(StringContainer.size_err % size)

        self._init_empty(size)

    def __str__(self) -> str:
        field: str

        field = ""
        for y in range(self.__height):
            for x in range(self.__width):
                field += str(self.__cells[x][y])
            field += "\n" if y + 1 < self.__height else ''
        return (field)

    def _get_cell(
        self, coord: tuple[int, int]
    ) -> cell.Cell:

        x: int
        y: int

        self._guard_coord_type(coord)
        self._guard_coord_val(coord, self.get_width(), self.get_height())
        x, y = coord
        return (self.__cells[x][y])

    def _replace_cell(
        self, coord: tuple[int, int], new: cell.Cell
    ) -> cell.Cell:

        x: int
        y: int

        self._guard_coord_type(coord)
        self._guard_coord_val(coord, self.get_width(), self.get_height())

        if (not isinstance(new, cell.Cell)):
            raise TypeError(StringContainer.cell_err % type(new))

        x, y = coord
        self.__cells[x][y] = new
        return (self._get_cell(coord))

    def get_width(self) -> int:
        return (self.__width)

    def get_height(self) -> int:
        return (self.__width)

    def get_size(self) -> tuple[int, int]:
        return (self.__width, self.__height)

    def open_wall(
        self, coord: tuple[int, int], wall: typing.Any
    ) -> bool:
        self._guard_coord_type(coord)
        self._guard_coord_val(coord, self.get_width(), self.get_height())
        return (self._get_cell(coord).open_wall(wall))

    def open_mult_walls(
        self, coord: tuple[int, int], walls: typing.Any
    ) -> bool:
        self._guard_coord_type(coord)
        self._guard_coord_val(coord, self.get_width(), self.get_height())
        return (self._get_cell(coord).open_mult_walls(walls))

    def close_wall(
        self, coord: tuple[int, int], wall: typing.Any
    ) -> bool:
        self._guard_coord_type(coord)
        self._guard_coord_val(coord, self.get_width(), self.get_height())
        return (self._get_cell(coord).close_wall(wall))

    def close_mult_walls(
        self, coord: tuple[int, int], walls: typing.Any
    ) -> bool:
        self._guard_coord_type(coord)
        self._guard_coord_val(coord, self.get_width(), self.get_height())
        return (self._get_cell(coord).close_mult_walls(walls))

    @staticmethod
    def _guard_coord_type(coord: tuple[int, int]) -> None:

        x: int
        y: int

        if (not isinstance(coord, tuple)):
            raise TypeError(StringContainer.coord_type_err_0)
        x, y = coord
        if (not (isinstance(x, int) and isinstance(y, int))):
            raise TypeError(StringContainer.coord_type_err_1)

    @staticmethod
    def _guard_coord_val(
        coord: tuple[int, int], width: int, height: int
    ) -> None:

        x: int
        y: int

        x, y = coord
        if (not ((0 < x < width) and (0 < y < height))):
            raise IndexError(
                StringContainer.coord_err % ((width, height) + coord)
            )

    @staticmethod
    def get_neighbour_coords(
        coord: tuple[int, int], direction: typing.Any
    ) -> tuple[int, int]:

        steps: tuple[int, int]
        x1: int
        y1: int
        x2: int
        y2: int

        steps = Directions.relative_directions.get(direction, (0, 0))
        x1, y1 = coord
        x2, y2 = steps
        return ((x1 + x2, y1 + y2))

    @abc.abstractmethod
    def _init_empty(self, size: tuple[int, int]) -> None:
        pass

    @abc.abstractmethod
    def set_start(self, coord: tuple[int, int]) -> None:
        pass

    @abc.abstractmethod
    def set_goal(self, coord: tuple[int, int]) -> None:
        pass

    @abc.abstractmethod
    def get_start(self) -> tuple[int, int]:
        pass

    @abc.abstractmethod
    def get_goal(self) -> tuple[int, int]:
        pass
