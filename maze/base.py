#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import typing
import abc
import maze.cells as cell
# from maze.values.constants import Directions

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

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
        self.__width = width
        self.__height = height

    def __str__(self) -> str:
        field: str

        field = ""
        for y in range(self.__height):
            for x in range(self.__width):
                field += str(self.__cells[x][y])
            field += "\n" if y + 1 < self.__height else ''
        return (field)

    @property
    def cells(self) -> list[list[cell.Cell]]:
        return (self.__cells)

    @property
    def width(self) -> int:
        return (self.__width)

    @property
    def height(self) -> int:
        return (self.__height)

    def _get_cell(
        self, coord: tuple[int, int]
    ) -> cell.Cell:

        x: int
        y: int

        self._guard_coord_type(coord)
        self._guard_coord_val(coord, self.get_width(), self.get_height())
        x, y = coord
        return (self.__cells[x][y])

    def _get_grid(self) -> list[list[cell.Cell]]:
        return (self.__cells)

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
        return (self.__height)

    def get_size(self) -> tuple[int, int]:
        return (self.__width, self.__height)

    def validate_coord(self, coord: tuple[int, int]) -> bool:

        x: int
        y: int

        if (not isinstance(coord, tuple)):
            return (False)
        if (len(coord) != 2):
            return (False)

        x, y = coord
        if (not (isinstance(x, int) and isinstance(y, int))):
            return (False)
        if (not ((0 <= x < self.__width) and (0 <= y < self.__height))):
            return (False)
        return (True)

    @abc.abstractmethod
    def open_wall(
        self,
        coord: tuple[int, int],
        wall: typing.Any,
        semipermeable: bool = False
    ) -> bool:
        pass

    @abc.abstractmethod
    def open_mult_walls(
        self,
        coord: tuple[int, int],
        walls: typing.Any,
        semipermeable: bool = False
    ) -> bool:
        pass

    @abc.abstractmethod
    def close_wall(
        self,
        coord: tuple[int, int],
        wall: typing.Any,
        semipermeable: bool = False
    ) -> bool:
        pass

    @abc.abstractmethod
    def close_mult_walls(
        self,
        coord: tuple[int, int],
        walls: typing.Any,
        semipermeable: bool = False
    ) -> bool:
        pass

    @staticmethod
    def _guard_coord_type(coord: tuple[int, int]) -> None:

        x: int
        y: int

        if (not isinstance(coord, tuple)):
            raise TypeError(StringContainer.coord_type_err_0)
        if (len(coord) != 2):
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
        if (not ((0 <= x < width) and (0 <= y < height))):
            raise IndexError(
                StringContainer.coord_err % ((width, height) + coord)
            )

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
