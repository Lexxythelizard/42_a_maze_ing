#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import typing
import maze.cells as cell
import maze.base as blueprint

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------


class StringContainer:

    maze_type_err = "TypeError: expected Maze, got %s instead"


# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class MazeMap:

    """
    maze
    """

    _map: list[list[dict]]
    _related_maze: blueprint.Maze
    _related_grid: list[list[cells.Cell]]

    def __init__(
        self,
        related: blueprint.Maze,
        empty: bool = False
    ) -> None:

        self._realted_maze = related
        self._related_grid = None

        self.map_init_unkknown()

    def map_init_unknown(self) -> None:
        pass
