#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import typing
import abc
import maze.cells as cell
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


class BlueprintMazeGen(abc.ABC):

    """
    Maze Blueprint
    """

    __width: int
    __height: int
    __entry_coord: tuple[int, int]
    __exit_coord: tuple[int, int]
    __outputfile_name: str
    __is_perfect: bool


    @property
    def is_perfect(self) -> bool:
        return (self.__is_perfect)

    def __init__(
        self,
        width: int,
        height: int,
        entry_coord: tuple[int, int],
        exit_coord: tuple[int, int],
        outputfile_name: str,
        is_perfect: bool
    ) -> None:

        """
        DOC
        """

        # TODO: implement guard

        __width = width
        __height = height
        __entry_coord = entry_coord
        __exit_coord = exit_coord
        __outputfile_name = outputfile_name
        __is_perfect = is_perfect

    def validate(self) -> bool:
        raise NotImplementedError(".validate not implemented yet")
        return True
        if width

    def ingest(inputfile_name: str) -> None:

        """
        DOC
        """

        lines: list[str]

        lines = []
        if (not isinstance(inputfile_name, str)):
            raise TypeError

        # TODO: implement guard: file not found and file forbidden, 
        # TODO: call class for reading and parsing inputfile_name


class MazeGenInputValidator(abc.ABC):

    
    required_keys = [
        'WIDTH',
        'HEIGHT',
        'ENTRY',
        'EXIT',
        'OUTPUT_FILE',
        'PERFECT'
    ]

    def ingest


    def validate(filename: str) -> bool:

        lines: list[str]
        param_dict: dict[str, str]

        lines = []
        param_dict = dict()

        # TODO: implement readline

        # filter for hash
        lines = [el for el in lines if el]
        lines = [el for el in lines if el[0] = '#']

        if (len(lines) < 6):
            return (False)

        # count =
        for el in lines:
            if (el.count('=' != 1):
                return (False)

        for el in lines:
            temp = el.split('=')
            if (not (temp[0] and temp[1])):
                return (False)

        for el in lines:
            temp = el.split('=')

            if (param_dict.get(temp[0], '')):
                return (False)

            if (temp[0] == 'WIDTH' or temp[0] == 'HEIGHT'):
                for c in temp[1]:
                    if c not in '0123456789':
                        return (False)
                param_dict.update({temp[0]: int(temp[1])})

            # TODO: if temp[0] ENTRY or EXIT temp[1] should be x, y

            if (temp[0] == 'PERFECT'):
                if (temp[0] not in ["True", "False"]):
                    return (False)

        for key in required_keys:
            if (key not in param_dict.keys()):
                return (False)
