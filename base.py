#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

# import typing
import abc
# import maze.cells as cell
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

        self.__width = width
        self.__height = height
        self.__entry_coord = entry_coord
        self.__exit_coord = exit_coord
        self.__outputfile_name = outputfile_name
        self.__is_perfect = is_perfect
        self.__seed = 42

    def validate(self) -> bool:
        raise NotImplementedError(".validate not implemented yet")
        return True

    def ingest(inputfile_name: str) -> None:

        """
        DOC
        """

        # lines: list[str]

        # lines = []
        if (not isinstance(inputfile_name, str)):
            raise TypeError

        # TODO: implement guard: file not found and file forbidden,
        # TODO: call class for reading and parsing inputfile_name


class MazeGenInputValidator(abc.ABC):

    """
    DOC
    """

    required_keys = [
        'WIDTH',
        'HEIGHT',
        'ENTRY',
        'EXIT',
        'OUTPUT_FILE',
        'PERFECT'
    ]

    @staticmethod
    def validate_file(filename: str) -> bool:

        """
        DOC
        """

        try:
            open(filename, 'r')

        except (FileNotFoundError, PermissionError):
            return (False)

        return (True)

    @classmethod
    def validate_format(cls, filename: str) -> bool:

        """
        DOC

        NOTE:
        call .validate_file() before passing filename to method
        """

        lines: list[str]
        param_dict: dict[str, str]

        lines = []
        param_dict = dict()

        lines = cls.read_lines(filename)

        # filter for hash
        lines = [el for el in lines if el]
        lines = [el for el in lines if el[0] != '#']

        print('test 0')
        if (len(lines) < 6):
            return (False)

        print('test 1')
        # count =
        for el in lines:
            if (el.count('=') != 1):
                return (False)

        print('test 2')
        for el in lines:
            temp = el.split('=')
            if (not (temp[0] and temp[1])):
                return (False)

        print('test 3')
        for el in lines:
            temp = el.split('=')

            print('test 3.a')
            if (param_dict.get(temp[0], '')):
                return (False)

            print('test 3.b')
            # checks if value of WIDTH and HEIGHT was integer
            if (temp[0] == 'WIDTH' or temp[0] == 'HEIGHT'):
                for c in temp[1]:
                    if c not in '0123456789':
                        return (False)
                param_dict.update({temp[0]: int(temp[1])})

            print('test 3.c')
            if (temp[0] == "ENTRY" or temp[0] == "EXIT"):
                # print('test 3.c.1 %d' % temp[1].count(','))
                if (temp[1].count(',') != 1):
                    return (False)
                # print('test 3.c.2')
                for c in temp[1]:
                    if (c not in "0123456789" and c != ','):
                        return (False)
                param_dict.update({temp[0]: temp[1]})

            print('test 3.d')
            if (temp[0] == 'PERFECT'):
                if (temp[1] not in ["True", "False"]):
                    return (False)
                param_dict.update({temp[0]: temp[1]})

            # TODO: delete thhis block
            if (temp[0] == 'OUTPUT_FILE'):
                param_dict.update({temp[0]: temp[1]})

        print('test 4')
        # checks if every required key was used
        for key in cls.required_keys:
            print(key)
            if (key not in param_dict.keys()):
                return (False)

        return (True)

    @classmethod
    def validate_values(cls, filename: str) -> bool:

        """
        DOC

        NOTE:
        call .validate_format() before passing filename to method
        """

        lines: list[str]
        param_dict: dict[str, str]

        lines = []
        param_dict = dict()

        lines = cls.read_lines(filename)

        for el in lines:
            temp = el.split('=')

            if (temp[0] == 'WIDTH' or temp[0] == 'HEIGHT'):
                param_dict.update({temp[0]: int(temp[1])})

            # TODO: if temp[0] ENTRY or EXIT temp[1] should be x, y

            elif (temp[0] == 'PERFECT'):
                if (temp[1] == "True"):
                    param_dict.update({temp[0]: True})
                else:
                    param_dict.update({temp[0]: False})

            else:
                param_dict.update({temp[0]: temp[1]})

        if (param_dict["WIDTH"] <= 0 or param_dict["HEIGTH"] <= 0):
            return (False)

        # checks if coords of ENTRY and EXIT are in frame

        temp_x, temp_y = param_dict["ENTRY"]
        if (temp_x <= 0 or temp_x >= param_dict["WIDTH"]):
            return (False)
        if (temp_y <= 0 or temp_y >= param_dict["HEIGHT"]):
            return (False)

        temp_x, temp_y = param_dict["EXIT"]
        if (temp_x <= 0 or temp_x >= param_dict["WIDTH"]):
            return (False)
        if (temp_y <= 0 or temp_y >= param_dict["HEIGHT"]):
            return (False)

        return (True)

    @staticmethod
    def read_lines(filename: str) -> list[str]:

        """
        Reads the file 'filename' line by line and return its content as list

        NOTE:
        please make sure file exists and you have the permission to open it
        """

        lines: list[str]

        with open(filename, 'r') as f:
            lines = f.readlines()

        lines = [
            line[:-1] if line[-1] == '\n' else line for line in lines
        ]

        return (lines)
