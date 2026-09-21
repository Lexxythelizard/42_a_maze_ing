#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import typing
import maze.cells as cell
import maze.base as blueprint
import maze.values.constants as const

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------


class StringContainer:

    maze_type_err = "TypeError: expected Maze, got %s instead"


# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class RelativeMazeMap:

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

    def set_coord(self, coord: tuple[int, int]) -> None:
        self.__coord = coord

    def init_position(self) -> None:
        self.__map[self.coord] = 0

    def init_42(self) -> None:
        for x in range(self.__dom.width):
            for y in range(self.__dom.height):
                if (
                    isinstance(
                        self.__dom.cells[x][y], cell.FourtyTwoCell
                    )
                ):
                    self.__map[(x, y)] = 42

    def init_unknown(self) -> None:
        for x in range(self.__dom.width):
            for y in range(self.__dom.height):
                self.__map[(x, y)] = 16

    def _dim_map(self) -> None:
        for x in range(self.__dom.width):
            for y in range(self.__dom.height):
                self.__map.update({(x, y): -1})

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

    def get_neighbours(
        self, restricted: bool = False
    ) -> dict[tuple[int, int], cell.Cell]:

        coord_list: list[tuple[int, int]]
        out = dict[tuple[int, int], cell.Cell]
        out_cpy = dict[tuple[int, int], cell.Cell]

        coord_list = self.get_neighbours_coord(
            coord=self.__coord,
            maze=self.__dom
        )
        out = dict()

        for el in coord_list:
            x, y = el
            out.update({el: self.__dom.cells[x][y]})

        if (restricted):

            out_cpy = dict()
            x, y = self.__coord
            for key, val in out.items():
                compare = const.Directions.get_direction_by_coord(
                    self.__coord, key
                )
                if (compare & int(self.__dom.cells[x][y]) == 0b0000):
                    out_cpy.update({key: val})
            out = out_cpy

        return (out)

    @staticmethod
    def get_neighbours_coord(
        coord: tuple[int, int],
        maze: blueprint.BlueprintMaze,
        raw: bool = False
    ) -> list[tuple[int, int]]:

        neighbours: list[tuple[int, int]]
        x1: int
        y1: int
        x2: int
        y2: int
        width: int
        height: int
        x_ctrl: int
        y_ctrl: int
        catch: tuple[int, int]

        neighbours = list()
        x1, y1 = coord
        for direction in const.Directions.hierarchy:
            x2, y2 = const.Directions.relative_directions[direction]
            neighbours.append((x1 + x2, y1 + y2))

        if (raw):
            return (neighbours)
        width = maze.width
        height = maze.height
        catch = (-1, -1)
        for idx, el in enumerate(neighbours):
            x_ctrl, y_ctrl = el
            if (not ((0 <= x_ctrl < width) and (0 <= y_ctrl < height))):
                catch = neighbours.pop(idx)
        del catch
        return (neighbours)

    @staticmethod
    def get_neighbours_directions(
        coord: tuple[int, int],
        maze: blueprint.BlueprintMaze
    ) -> list[tuple[int, int]]:

        neighbours = list()
        x1, y1 = coord
        for direction in const.Directions.hierarchy:
            x2, y2 = const.Directions.relative_directions[direction]
            neighbours.append((x1 + x2, y1 + y2))

    @staticmethod
    def _guard_maze_type(maze: typing.Any) -> None:
        if (not isinstance(maze, blueprint.BlueprintMaze)):
            raise TypeError(StringContainer.maze_type_err % type(maze))
