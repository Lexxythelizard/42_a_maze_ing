#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import abc

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------


class StringContainer:

    coord_err = "Error: Coords must be 0 < x %d; 0 < y < %d; got x: %d, y: %d"
    size_err = "Error: Size (width, height) must be greater than 0"
    size_err += ", got (%d, %d)"
    cell_err = "Error: Expected instance of Cell got %s instead"
    str_err = "Error: Expected str got %s instead"

    coord_type_err_0 = "Error: Expected tuple[int, int], got %s"
    coord_type_err_1 = "Error: Expected tuple[int, int], got tuple[%s, %s]"


# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class ColorCodes:

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


class WallStyleProto(abc.ABC):

    """
    Blueprint for Wall style
    """

    __name: str
    __ft_color: str
    __re_color: str

    @abc.abstractmethod
    def __init__(self, key: str) -> None:
        pass

    @property
    def name(self) -> str:
        return (self.__name)

    @property
    def re_color(self) -> str:
        return (self.__re_color)

    @property
    def ft_color(self) -> str:
        return (self.__ft_color)

    @property
    def re_code(self) -> str:
        return (
            '' if not self.__re_color else ColorCodes.colors[self.__re_color]
        )

    @property
    def ft_code(self) -> str:
        return (
            '' if not self.__ft_color else ColorCodes.colors[self.__ft_color]
        )

    def _set_name(self, key: str) -> None:
        """
        DOC
        """
        if (not isinstance(key, str)):
            raise TypeError(StringContainer.str_err % type(key))
        self.__name = key

    def _init_values(self, values: dict[str, str]) -> None:
        """
        DOC
        """
        self.__re_color = values['re_color']
        self.__ft_color = values['ft_color']


class CellStyleProto(abc.ABC):

    """
    Blueprint Cell style
    """

    __name: str
    __ft_color: str
    __re_color: str
    __ft_symbol: str
    __un_symbol: str
    __vi_siymbol: str
    __tr_symbol: str

    @abc.abstractmethod
    def __init__(self, key: str) -> None:
        pass

    @property
    def name(self) -> str:
        return (self.__name)

    @property
    def re_color(self) -> str:
        return (self.__re_color)

    @property
    def ft_color(self) -> str:
        return (self.__ft_color)

    @property
    def re_code(self) -> str:
        return (
            '' if not self.__re_color else ColorCodes.colors[self.__re_color]
        )

    @property
    def ft_code(self) -> str:
        return (
            '' if not self.__ft_color else ColorCodes.colors[self.__ft_color]
        )

    @property
    def ft_symbol(self) -> str:
        return (self.__ft_symbol)

    @property
    def un_symbol(self) -> str:
        return (self.__un_symbol)

    @property
    def vi_symbol(self) -> str:
        return (self.__vi_symbol)

    @property
    def tr_symbol(self) -> str:
        return (self.__tr_symbol)

    def set_ft_symbol(self, symbol: str) -> None:
        """
        DOC
        """
        if (not isinstance(symbol, str)):
            raise TypeError(StringContainer.str_err % type(symbol))
        if (len(symbol) != 1):
            raise ValueError("[Spaceholder]")

        self.__ft_symbol = symbol

    def set_un_symbol(self, symbol: str) -> None:
        """
        DOC
        """
        if (not isinstance(symbol, str)):
            raise TypeError(StringContainer.str_err % type(symbol))
        if (len(symbol) != 1):
            raise ValueError("[Spaceholder]")

        self.__un_symbol = symbol

    def set_vi_symbol(self, symbol: str) -> None:
        """
        DOC
        """
        if (not isinstance(symbol, str)):
            raise TypeError(StringContainer.str_err % type(symbol))
        if (len(symbol) != 1):
            raise ValueError("[Spaceholder]")

        self.__vi_symbol = symbol

    def set_tr_symbol(self, symbol: str) -> None:
        """
        DOC
        """
        if (not isinstance(symbol, str)):
            raise TypeError(StringContainer.str_err % type(symbol))
        if (len(symbol) != 1):
            raise ValueError("[Spaceholder]")

        self.__tr_symbol = symbol

    def _set_name(self, key: str) -> None:
        """
        DOC
        """
        if (not isinstance(key, str)):
            raise TypeError(StringContainer.str_err % type(key))
        self.__name = key

    def _init_values(self, values: dict[str, str]) -> None:
        """
        DOC
        """
        self.__re_color = values['re_color']
        self.__ft_color = values['ft_color']


class MetaStyleProto(abc.ABC):

    """
    Blueprint for Style

    stats:

        __dom:              related Maze
        __frame_interface:  Utility Class see FrameInterface
        __frame:            the concatinated frame string with specifier %s
                            in the middle of each cell
        __settings:         container for settings

    """

    __name: str
    __wall: WallStyleProto
    __cell: CellStyleProto

    @property
    def name(self) -> str:
        return (self.__name)

    @property
    def wall(self) -> WallStyleProto:
        return (self.__wall)

    @property
    def cell(self) -> CellStyleProto:
        return (self.__cell)

    @abc.abstractmethod
    def __init__(
        self, wall_style: str, cell_style: str
    ) -> None:
        pass

    def _set_name(self, key: str) -> None:
        """
        DOC
        """
        if (not isinstance(key, str)):
            raise TypeError(StringContainer.str_err % type(key))
        self.__name = key

    def _set_wall(self, wall_style: WallStyleProto) -> None:
        # TODO: implement guard
        self.__wall = wall_style

    def _set_cell(self, cell_style: CellStyleProto) -> None:
        # TODO: implement guard
        self.__celll = cell_style
