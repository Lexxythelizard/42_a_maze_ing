#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

# import typing
from maze.ui.cli.base import MazeInterface
# import maze.cells as cells
# from maze.obj import Maze
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
    Output
        ...under construction

    stats:

        __dom:              related Maze
        __frame_interface:  Utility Class see FrameInterface
        __frame:            the concatinated frame string with specifier %s
                            in the middle of each cell
        __settings:         container for settings

    ...

    -----------------------------------------------------------------------

    examples on a 4 x 4 Maze

    .frame

    <open and empty>                    <closed frame>

    '+   + +   + +   + +   +\\n'        '+ – + + – + + – + + – +\\n'
    '  %s     %s     %s     %s  \\n'    '| %s     %s     %s     %s |\\n'
    '+   + +   + +   + +   +\\n'        '+ – + + – + + – + + – +\\n'
    '+   + +   + +   + +   +\\n'        '+ – + + – + + – + + – +\\n'
    '  %s     %s     %s     %s  \\n'    '| %s     %s     %s     %s |\\n'
    '+   + +   + +   + +   +\\n'        '+ – + + – + + – + + – +\\n'
    '+   + +   + +   + +   +\\n'        '+ – + + – + + – + + – +\\n'
    '  %s     %s     %s     %s  \\n'    '| %s     %s     %s     %s |\\n'
    '+   + +   + +   + +   +\\n'        '+ – + + – + + – + + – +\\n'
    '+   + +   + +   + +   +\\n'        '+ – + + – + + – + + – +\\n'
    '  %s     %s     %s     %s  \\n'    '| %s     %s     %s     %s |\\n'
    '+   + +   + +   + +   +'           '+ – + + – + + – + + – +'

    <all cells closed>                  <etc>

    '+ – + + – + + – + + – +\\n'        ...
    '| %s | | %s | | %s | | %s |\\n'    ...
    '+ – + + – + + – + + – +\\n'        ...
    '+ – + + – + + – + + – +\\n'        ...
    '| %s | | %s | | %s | | %s |\\n'    ...
    '+ – + + – + + – + + – +\\n'        ...
    '+ – + + – + + – + + – +\\n'        ...
    '| %s | | %s | | %s | | %s |\\n'    ...
    '+ – + + – + + – + + – +\\n'        ...
    '+ – + + – + + – + + – +\\n'        ...
    '| %s | | %s | | %s | | %s |\\n'    ...
    '+ – + + – + + – + + – +'           ...

    -----------------------------------------------------------------------
    """

    def sniggle(self) -> None:
        pass
