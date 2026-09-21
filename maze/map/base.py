#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import typing
import abc
import maze.cells as cell
import maze.base as blueprint
import maze.values.constants as const

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------


class StringContainer:

    maze_type_err = "TypeError: expected Maze, got %s instead"


# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class BlueprintRelativeMazeMap(abc.ABC):

    __map: dict[tuple[int, int], int]
    __dom: blueprint.BlueprintMaze
    __coord: tuple[int, int]
    __ftcell: bool

    def __init__(
        self, dom: blueprint.BlueprintMaze, coord: tuple[int, int]
    ) -> None:

        self._guard_maze_type(dom)
        self.__dom = dom

        self.__dom._guard_coord_type(coord)
        self.__dom._guard_coord_val(
            coord,
            self.__dom.width,
            self.__dom.height
        )
        self.__coord = coord

        self.__map = dict()

        self._dim_map()
        self.init_unknown()
        self.init_position()
        self.init_ftcell()
        self.init_42()

    @property
    def map(self) -> dict[tuple[int, int], int]:
        return (self.__map)

    @property
    def coord(self) -> tuple[int, int]:
        return (self.__coord)

    @property
    def ftcell(self) -> bool:
        return (self.__ftcell)

    @property
    def dom(self) -> bool:
        return (self.__dom)

    def set_coord(self, coord: tuple[int, int]) -> None:
        self.__coord = coord

    def init_position(self) -> None:
        self.__map[self.coord] = const.Directions.none

    def init_42(self) -> None:
        for x in range(self.__dom.width):
            for y in range(self.__dom.height):
                if (
                    isinstance(
                        self.__dom.cells[x][y], cell.FourtyTwoCell
                    )
                ):
                    self.__map[(x, y)] = const.Directions.ft_cell

    def init_unknown(self) -> None:
        for x in range(self.__dom.width):
            for y in range(self.__dom.height):
                self.__map[(x, y)] = const.Directions.unknown

    def _dim_map(self) -> None:
        for x in range(self.__dom.width):
            for y in range(self.__dom.height):
                self.__map.update({(x, y): const.Directions.blocked})

    def init_ftcell(self) -> None:

        x: int
        y: int

        x, y = self.__coord
        self.__ftcell = False

        if (
            isinstance(
                self.__dom.cells[x][y], cell.FourtyTwoCell
            )
        ):
            self.__ftcell = True

    @abc.abstractmethod
    def get_neighbours(
        self, restricted: bool = False
    ) -> dict[tuple[int, int], cell.Cell]:
        pass

    @abc.abstractmethod
    def set_map_cell(self, coord: tuple[int, int], key: int) -> None:
        pass

    @staticmethod
    def _guard_maze_type(maze: typing.Any) -> None:
        if (not isinstance(maze, blueprint.BlueprintMaze)):
            raise TypeError(StringContainer.maze_type_err % type(maze))
