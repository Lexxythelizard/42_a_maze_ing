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


class CellInterface:

    """
    DOCSTRING
    """

    @staticmethod
    def get_cell_top(cell: cells.Cell, color: str = '') -> str:

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

        wall_chr_left: str
        wall_chr_right: str
        wall_str: str

        wall_chr_right = CLIContainer.colors[color] if color else ''
        wall_chr_right += \
            CLIContainer.wall_vertical \
            if cell.east_wall else CLIContainer.wall_none
        wall_chr_right = CLIContainer.colors['reset'] if color else ''

        wall_chr_left = CLIContainer.colors[color] if color else ''
        wall_chr_left += \
            CLIContainer.wall_vertical \
            if cell.west_wall else CLIContainer.wall_none
        wall_chr_left = CLIContainer.colors['reset'] if color else ''

        wall_str = \
            CLIContainer.vertical % (wall_chr_left, "%s", wall_chr_right)
        return (wall_str)

    @staticmethod
    def get_cell_bottom(cell: cells.Cell, color: str = '') -> str:

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
    ...Name...here
    """

    __cell_interface: type[CellInterface] = CellInterface

    @property
    def cell_interface(self) -> type[CellInterface]:
        return (self.__cell_interface)

    @classmethod
    def get_row_top(
        cls, maze: Maze, row: int, function: typing.Any = None
    ) -> str:

        line: str

        line = ''
        for x in range(maze.width):
            cell = maze.cells[x][row]
            line += cls.__cell_interface.get_cell_top(cell)
            line += CLIContainer.space if ((x + 1) < maze.width) else '\n'

        return (line)

    @classmethod
    def get_row_middle(
        cls, maze: Maze, row: int, function: typing.Any = None
    ) -> str:

        line: str

        line = ''
        for x in range(maze.width):
            cell = maze.cells[x][row]
            line += cls.__cell_interface.get_cell_middle(cell)
            line += CLIContainer.space if ((x + 1) < maze.width) else '\n'

        return (line)

    @classmethod
    def get_row_bottom(
        cls, maze: Maze, row: int, function: typing.Any = None
    ) -> str:

        line: str

        line = ''
        for x in range(maze.width):
            cell = maze.cells[x][row]
            line += cls.__cell_interface.get_cell_bottom(cell)
            line += CLIContainer.space if ((x + 1) < maze.width) else ''
            line += '\n' if ((row + 1) < maze.height) else ''

        return (line)

    @classmethod
    def get_frame_one_color(cls, maze: Maze, color: str = '') -> str:

        frame: str

        frame = ''
        for y in range(maze.height):
            frame += cls.get_row_top(maze=maze, row=y)
            frame += cls.get_row_middle(maze=maze, row=y)
            frame += cls.get_row_bottom(maze=maze, row=y)

        return (frame)


class MazeInterface(abc.ABC):

    """
    ...Name...here
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
        self.__frame = \
            self.__frame_interface.get_frame_one_color(maze=self.dom)
