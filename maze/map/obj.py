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
    RelativeMazeMap is a map which keeps track of each cells coordinate and
    how to reach them, by using the folowing keys:

        - 1: north / up
        - 2: east  / right
        - 4: south / down
        - 8: west  / left

        - 16: unknown
        - 0:  own cell
        - -1: unreachable
        - 42: (unreachable, but ok because) 42 cell

    stats:
        __dom:    the related Maze instance
        __coord:  the own coords (x, y)
        __map:    the map, how to reach each cell from this relative position
                  {(x, y): key-value}

    Takes related maze instance as argument.
    readable with .dom
    automaticly initializes a dict of coord and values {coord: key}
        -> just containing 16: unknown, 42: FourtyTwo, 0: self keys
           at after initialisation
    """

    def get_neighbours(
        self, restricted: bool = True
    ) -> dict[tuple[int, int], cell.Cell]:

        """
        returns a dict with 0 - 4 items:
        relative neighbours {coord: Cell}
        items are sorted in order defined in
        .maze.values.constants.Directions.hierarchy

        filters cells by default:
        just returns reachable items (wall to that direction is open)
        for unfiltered use restricted=False
        """

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

        """
        set Value of cell in .map {coord: key}
        raises Error if coord is invalid or non existing
        raises Error if key is invalid
        valid keys are: [1, 2, 4, 8, 0, -1, 16, 42]
        """

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
    MazeMap is a map which contains as many RealativeMazeMaps
    as the related maze contains cells.

    see help(RelativeMazeMap)

    stats:
        __dom:    the related Maze instance
        __map:    the cluster of RealtiveMazeMap instances
                   {(x, y): RelativeMazeMap}

    Takes related maze instance as argument.
    readable with .dom
    automaticly initializes a cluster of RealtiveMazeMap instances
        -> just containing 16: unknown, 42: FourtyTwo, 0: self keys
           at after initialisation

    Can assign values to cells in each relative maze:
    see: .set_relative_map_cell()

    everything needs to get orchestred by using the object and its methods
    """

    def map_init_unknown(self) -> None:

        """
        basicly just dims a new dict {coord: RelativeMazeMap}
        and inits avery instance of RealtivMazeMap
        should be called automaticly by constructor
        """

        for x in range(self.dom.width):
            for y in range(self.dom.height):
                self.map.update(
                    {(x, y): RelativeMazeMap(self.dom, (x, y))}
                )

    def get_relative_map(
        self, coord: tuple[int, int]
    ) -> base.BlueprintRelativeMazeMap:

        """
        returns the RelativeMazeMap instance at coord
        works like .map[coord] but raises customize TypeError
        if coord is invalid
        """

        self.dom._guard_coord_type(coord)
        self.dom._guard_coord_val(
            coord,
            self.width,
            self.height
        )
        return (self.map[coord])

    def get_relative_neighbours(
        self, coord: tuple[int, int], restricted: bool = True
    ) -> dict[tuple[int, int], cell.Cell]:

        """
        returns a dict with 0 - 4 items:
        relative neighbours {coord: Cell}
        items are sorted in order defined in
        .maze.values.constants.Directions.hierarchy

        filters cells by default:
        just returns reachable items (wall to that direction is open)
        for unfiltered use restricted=False
        """

        self.dom._guard_coord_type(coord)
        self.dom._guard_coord_val(
            coord,
            self.width,
            self.height
        )
        return (self.map[coord].get_neighbours(restricted))

    def set_relative_map_cell(
        self, coord_map: tuple[int, int],
        coord_cell: tuple[int, int],
        key: int
    ) -> None:

        """
        set Value of cell in .map {coord_map: .map {coord_cell: key} }
        coord_map: coord of relativeMazeMap
        coord_cell: coord of cell in .map of relativeMazeMap

        raises Error if coord_* is invalid or non existing
        raises Error if key is invalid
        valid keys are: [1, 2, 4, 8, 0, -1, 16, 42]
        """

        self.dom._guard_coord_type(coord_map)
        self.dom._guard_coord_val(
            coord_map, self.width, self.height
        )
        self.dom._guard_coord_type(coord_cell)
        self.dom._guard_coord_val(
            coord_cell, self.width, self.height
        )
        self.map[coord_map].set_map_cell(coord_cell, key)

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
