#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

# import maze
# import maze.ui as ui
# from maze.cells import Cell
import typing
from maze.construct.base import MazeDrill
from maze.move import MazeRunner
# from maze.values.constants import Directions

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class ConstructionWorker(MazeRunner, MazeDrill):

    """
    DOCSTRING
    """

    sniggle: typing.Any
