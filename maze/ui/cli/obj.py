#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import typing
from maze.ui.cli.base import MazeInterface
import maze.cells as cells
from maze.obj import Maze
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


class Output(MazeInterface):

    """
    ...Name...here
    """
    def sniggle(self) -> None:
        pass
