#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import typing
import abc
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


class CLIContainer:

    """
    DOCSTRING

    sniggle...

    ...valid colors:

        - red
        - green
        - blue
        - yellow
    """

    colors = {
        'red': '\033[31m',
        'green': '\033[32m',
        'blue': '\033[34m',
        'yellow': '\033[33m',
        'reset': '\033[0m'
    }

    space = ' '
    wall_corner = '+'
    wall_vertical = '|'
    wall_horizontal = '–'
    wall_none = ' '

    wall_hori = "+ – +"
    prot_vert = "| x |"

    horizontal = "%s %s %s" % (wall_corner, "%s", wall_corner)
    vertical = "%s %s %s"


class CellInterface(abc.ABC):

    """
    CellInterface is not intended to be initalized and made as an
    utility class for CellInterface

    Cell could be colored or blank (default setting)
    specifier in the middle is always blank and made to be assinged/replaced
    or colored in a second step.

    for valid colors see: CLIContainer
    ------------------------------------------------------------
    Cell gets ASCII rendered in 3 lines:

    line\\cell   open cell:            close cell:

    top:         +   +$                + – +$
    middle:        %s  $               | %s |$
    bottom:      +   +$                + – +$
    ------------------------------------------------------------
    the specifier in the middle is meant to be used to fill it with
    any single character incl space which symbolized visited/unvisited/42
    """

    @staticmethod
    def get_cell_top(cell: cells.Cell, color: str = '') -> str:

        """
        gets the cell top as string, by default blank

        TOP:
        open:   +   +

        closed: + – +
        """

        wall_chr: str
        wall_str: str

        wall_chr = \
            CLIContainer.wall_horizontal \
            if cell.north_wall else CLIContainer.wall_none
        wall_str = CLIContainer.colors[color] if color else ''
        wall_str += CLIContainer.horizontal % wall_chr
        wall_str += CLIContainer.colors['reset'] if color else ''

        return (wall_str)

    @staticmethod
    def get_cell_middle(cell: cells.Cell, color: str = '') -> str:

        """
        DOCSTRING
        gets the cell middle as string, by default blank
        specifier is always blank

        MIDDLE:
        open:     %s  $

        closed: | %s  $    /  $ %s |    /  | %s |
        """

        wall_chr_left: str
        wall_chr_right: str
        wall_str: str

        wall_chr_right = CLIContainer.colors[color] if color else ''
        wall_chr_right += \
            CLIContainer.wall_vertical \
            if cell.east_wall else CLIContainer.wall_none
        wall_chr_right += CLIContainer.colors['reset'] if color else ''

        wall_chr_left = CLIContainer.colors[color] if color else ''
        wall_chr_left += \
            CLIContainer.wall_vertical \
            if cell.west_wall else CLIContainer.wall_none
        wall_chr_left += CLIContainer.colors['reset'] if color else ''

        wall_str = \
            CLIContainer.vertical % (wall_chr_left, "%s", wall_chr_right)
        return (wall_str)

    @staticmethod
    def get_cell_bottom(cell: cells.Cell, color: str = '') -> str:

        """
        gets the cell bottom as string, by default blank

        BOTTOM:
        open:   +   +

        closed: + – +
        """

        wall_chr: str
        wall_str: str

        wall_chr = \
            CLIContainer.wall_horizontal \
            if cell.south_wall else CLIContainer.wall_none
        wall_str = CLIContainer.colors[color] if color else ''
        wall_str += CLIContainer.horizontal % wall_chr
        wall_str += CLIContainer.colors['reset'] if color else ''

        return (wall_str)


class FrameInterface(abc.ABC):

    """
    FrameInterface is not intended to be initalized and made as an
    utility class for MazeInterface

    Cells could be colored or blank (default setting)
    depends on function passed as argument
        --> under construction
    specifier in the middle of each cell is always blank and
    made to be assinged/replaced or colored in a second step.

    for utility class CellInterface see: CellInterface
    ------------------------------------------------------------
    Row gets ASCII rendered in 3 lines:

    top:         get_cell_top()       of row y    x times
    middle:      get_cell_middle()    of row y    x times
    bottom:      get_cell_bottom()    of row y    x times
    ------------------------------------------------------------
    the specifier in the middle is meant to be used to fill it with
    any single character incl space which symbolized visited/unvisited/42
    """

    cell_interface: type[CellInterface] = CellInterface

    @classmethod
    def get_row_top(
        cls, maze: Maze, row: int, function: typing.Any = None
    ) -> str:

        """
        gets the row top as string, by default blank

        concatinates output of .cell_interface.get_cell_top()
        separated by space; line ended with newline

        param function:
            ...under construction
        """

        line: str

        line = ''
        for x in range(maze.width):
            cell = maze.cells[x][row]
            line += cls.cell_interface.get_cell_top(cell)
            line += CLIContainer.space if ((x + 1) < maze.width) else '\n'

        return (line)

    @classmethod
    def get_row_middle(
        cls, maze: Maze, row: int, function: typing.Any = None
    ) -> str:

        """
        gets the row middle as string, by default blank
        specifier is always blank

        concatinates output of .cell_interface.get_cell_middle()
        separated by space; line ended with newline

        param function:
            ...under construction
        """

        line: str

        line = ''
        for x in range(maze.width):
            cell = maze.cells[x][row]
            line += cls.cell_interface.get_cell_middle(cell)
            line += CLIContainer.space if ((x + 1) < maze.width) else '\n'

        return (line)

    @classmethod
    def get_row_bottom(
        cls, maze: Maze, row: int, function: typing.Any = None
    ) -> str:

        """
        gets the row bottom as string, by default blank

        concatinates output of .cell_interface.get_cell_bottom()
        separated by space; line ended with newline if not last row

        param function:
            ...under construction
        """

        line: str

        line = ''
        for x in range(maze.width):
            cell = maze.cells[x][row]
            line += cls.cell_interface.get_cell_bottom(cell)
            line += CLIContainer.space if ((x + 1) < maze.width) else ''
        if (maze.height):
            line += '\n' if ((row + 1) < maze.height) else ''

        return (line)

    @classmethod
    def get_frame_one_color(cls, maze: Maze, color: str = '') -> str:

        """
        gets a uni-colored frame - blank by default
        specifiers are always blank

        param color:
        ... under construction
        ... depends on function in .get_row_*()
        """

        frame: str

        frame = ''
        for y in range(maze.height):
            frame += cls.get_row_top(maze=maze, row=y)
            frame += cls.get_row_middle(maze=maze, row=y)
            frame += cls.get_row_bottom(maze=maze, row=y)

        return (frame)


class MazeInterface(abc.ABC):

    """
    MazeInterface is the Blueprint for Output

    stats:

        __dom:              related Maze
        __frame_interface:  Utility Class see FrameInterface
        __frame:            the concatinated frame string with specifier %s
                            in the middle of each cell
        __settings:         container for settings

    """

    __dom: Maze
    __frame_interface: type[FrameInterface] = FrameInterface
    __frame: str
    __settings: typing.Any

    def __init__(
        self,
        dom: Maze,
    ) -> None:

        # TODO: Implementguard dom
        self.__dom = dom
        self.__frame = ''
        self.__settings = None

    @property
    def dom(self) -> Maze:
        return (self.__dom)

    @property
    def frame_interface(self) -> type[FrameInterface]:
        return (self.__frame_interface)

    @property
    def frame(self) -> str:
        return (self.__frame)

    @property
    def width(self) -> int:
        return (self.__dom.width)

    @property
    def height(self) -> int:
        return (self.__dom.height)

    @property
    def size(self) -> tuple[int, int]:
        return (self.__dom.width, self.__dom.height)

    def set_frame_blank(self) -> None:

        """
        gets a blank frame and assign it to .frame
        use .set_frame_blank() then use .frame to work with it
        """

        self.__frame = \
            self.__frame_interface.get_frame_one_color(maze=self.dom)
