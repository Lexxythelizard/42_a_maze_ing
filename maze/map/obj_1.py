#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import typing
import maze.map.base as base
import maze.cells as cell
import maze.base as blueprint
import maze.values.constants as const
from maze.move.base import Orientation

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------


class StringContainer:

    maze_type_err = "TypeError: expected Maze, got %s instead"


# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class RelativeMazeMap(base.BlueprintRelativeMazeMap, Orientation):


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
