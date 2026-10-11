#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

# import typing
from maze.ui.cli.styles.base \
    import WallStyleProto, CellStyleProto, MetaStyleProto
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


class StyleSheet:

    default = {'re_color': '', 'ft_color': ''}

    redred = {'re_color': 'red', 'ft_color': 'red'}
    redgren = {'re_color': 'red', 'ft_color': 'green'}
    redblue = {'re_color': 'red', 'ft_color': 'blue'}
    redyellow = {'re_color': 'red', 'ft_color': 'yellow'}

    greenred = {'re_color': 'green', 'ft_color': 'red'}
    greengreen = {'re_color': 'green', 'ft_color': 'green'}
    greenblue = {'re_color': 'green', 'ft_color': 'blue'}
    greenyellow = {'re_color': 'green', 'ft_color': 'yellow'}

    bluered = {'re_color': 'blue', 'ft_color': 'red'}
    bluegreen = {'re_color': 'blue', 'ft_color': 'green'}
    blueblue = {'re_color': 'blue', 'ft_color': 'blue'}
    blueyellow = {'re_color': 'blue', 'ft_color': 'yellow'}

    yellowred = {'re_color': 'yellow', 'ft_color': 'red'}
    yellowgreen = {'re_color': 'yellow', 'ft_color': 'green'}
    yellowblue = {'re_color': 'yellow', 'ft_color': 'blue'}
    yellowyellow = {'re_color': 'yellow', 'ft_color': 'yellow'}

    color_styles = {
        'default': default,
        'redred': redred,
        'redgren': redgren,
        'redblue': redblue,
        'redyellow': redyellow,
        'greenred': greenred,
        'greengreen': greengreen,
        'greenblue': greenblue,
        'greenyellow': greenyellow,
        'bluered': bluered,
        'bluegreen': bluegreen,
        'blueblue': blueblue,
        'blueyellow': blueyellow,
        'yellowred': yellowred,
        'yellowgreen': yellowgreen,
        'yellowblue': yellowblue,
        'yellowyellow': yellowyellow
    }

    un_symbol_default = ' '
    vi_symbol_default = '*'
    tr_symbol_default = 'O'
    ft_symbol_default = 'X'


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class WallStyle(WallStyleProto):

    """
    DOC
    """

    def __init__(self, key: str = 'default') -> None:

        """
        DOC
        """

        name = key if key in StyleSheet.color_styles.keys() else 'default'
        self._set_name(name)
        self._init_values(StyleSheet.color_styles[self.name])


class CellStyle(CellStyleProto):

    """
    DOC
    """

    def __init__(self, key: str = 'default') -> None:

        """
        DOC
        """

        name = key if key in StyleSheet.color_styles.keys() else 'default'
        self._set_name(name)
        self._init_values(StyleSheet.color_styles[self.name])
        self.set_ft_symbol(StyleSheet.ft_symbol_default)
        self.set_un_symbol(StyleSheet.un_symbol_default)
        self.set_vi_symbol(StyleSheet.vi_symbol_default)
        self.set_tr_symbol(StyleSheet.tr_symbol_default)


class MetaStyle(MetaStyleProto):

    """
    DOC
    """

    def __init__(self, key: str = 'default') -> None:

        """
        DOC
        """

        name = key if key in StyleSheet.color_styles.keys() else 'default'
        self._set_name(name)
        self._set_wall(WallStyle(self.name))
        self._set_cell(CellStyle(self.name))
