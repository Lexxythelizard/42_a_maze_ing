#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

# import typing
from maze.ui.cli.base import MazeInterface
import maze.cells as cells
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

    def get_blank_maze_output(self) -> str:

        """
        just gets a maze output colored walls but empty cells
        """

        self.set_frame()
        return (self.frame % ((' ') * (self.dom.width * self.dom.height)))

    def get_maze_output(
        self
    ) -> str:

        """
        get maze output:
        walls according to style
        symbols according to style
        """

        filling: list[str]

        filling = list()

        if (not self.frame):
            self.set_frame()

        # iterates through the whole array of cells
        for y in range(self.dom.height):
            for x in range(self.dom.width):

                # append visited symbol, if cell was visited
                if (self.dom.cells[x][y].visited):
                    filling.append(
                        self.settings.cell.vi_symbol
                    )

                # append ft symbol symbol, if cell was visited
                elif (isinstance(self.dom.cells[x][y], cells.FourtyTwoCell)):
                    filling.append(
                        self.settings.cell.ft_symbol
                    )

                # append unvisited symbol in any other case
                else:
                    filling.append(
                        self.settings.cell.un_symbol
                    )

        return (self.frame % tuple(filling))
