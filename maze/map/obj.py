#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

# import typing
import maze.map.base as base
import maze.cells as cell
# import maze.base as blueprint
import maze.values.constants as const
from maze.move.base import Orientation

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------


class StringContainer:

    maze_type_err = "TypeError: expected Maze, got %s instead"


# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class RelativeMazeMap(base.BlueprintRelativeMazeMap, Orientation):

    """
    Blueprint for Relative Maze Map
    """

    def get_neighbours(
        self, restricted: bool = True
    ) -> dict[tuple[int, int], cell.Cell]:

        coord_list: list[tuple[int, int]]
        out: dict[tuple[int, int], cell.Cell]
        out_cpy: dict[tuple[int, int], cell.Cell]

        coord_list = self.get_neighbours_coord(
            coord=self.coord,
            maze=self.dom
        )
        out = {}

        for el in coord_list:
            x, y = el
            out.update({el: self.dom.cells[x][y]})

        if (restricted):

            out_cpy = {}
            x, y = self.coord
            for key, val in out.items():
                compare = const.Directions.get_direction_by_coord(
                    self.coord, key
                )
                if (compare & int(self.dom.cells[x][y]) == 0b0000):
                    out_cpy.update({key: val})
            return (out_cpy)

        return (out)

    def set_map_cell(self, coord: tuple[int, int], key: int) -> None:
        self.dom._guard_coord_type(coord)
        self.dom._guard_coord_val(
            coord,
            self.dom.width,
            self.dom.height
        )
        const.Directions.guard_map_key(key)
        x, y = coord
        self.map[(x, y)] = key


class MazeMap(base.BlueprintMazeMap):

    """
    MazeMap
    """

    def map_init_unknown(self) -> None:
        for x in range(self.__dom.width):
            for y in range(self.__dom.height):
                self.__map.update(
                    {(x, y): RelativeMazeMap(self.__dom, (x, y))}
                )

    def get_relative_map(
        self, coord: tuple[int, int]
    ) -> base.BlueprintRelativeMazeMap:

        self.dom._guard_coord_type(coord)
        self.dom._guard_coord_val(
            coord,
            self.width,
            self.height
        )
        return (self.map[coord])

    def get_relative_neighbours(
        self, coord: tuple[int, int], restricted: bool = False
    ) -> dict[tuple[int, int], cell.Cell]:

        self.dom._guard_coord_type(coord)
        self.dom._guard_coord_val(
            coord,
            self.width,
            self.height
        )
        return (self.map[coord].get_neighbours(restricted))

    def dev_print_relative_map(
        self, coord: tuple[int, int]
    ) -> None:

        """
        For development, print Realtive maze map
        """

        self.dom._guard_coord_type(coord)
        self.dom._guard_coord_val(
            coord,
            self.width,
            self.height
        )
        print(self.map[coord])
