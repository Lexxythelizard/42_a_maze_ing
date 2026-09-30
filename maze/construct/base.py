#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import maze.base as maze
# import maze.ui as ui
# from maze.cells import Cell
import abc
import typing
# from maze.values.constants import Directions

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class MazeDrill(abc.ABC):

    """
    DOCSTRING
    """

    # dom: maze.BlueprintMaze
    # position: tuple[int, int]

    @property
    @abc.abstractmethod
    def dom(self) -> maze.BlueprintMaze:
        pass

    @property
    @abc.abstractmethod
    def position(self) -> tuple[int, int]:
        pass

    @abc.abstractmethod
    def move_east(self) -> bool:
        pass

    @abc.abstractmethod
    def move_south(self) -> bool:
        pass

    @abc.abstractmethod
    def move_west(self) -> bool:
        pass

    @abc.abstractmethod
    def move_north(self) -> bool:
        pass

    @abc.abstractmethod
    def move(self, direction: typing.Any) -> bool:
        pass

    @staticmethod
    @abc.abstractmethod
    def get_neighbour_coord_east(coord: tuple[int, int]) -> tuple[int, int]:
        pass

    @staticmethod
    @abc.abstractmethod
    def get_neighbour_coord_south(coord: tuple[int, int]) -> tuple[int, int]:
        pass

    @staticmethod
    @abc.abstractmethod
    def get_neighbour_coord_west(coord: tuple[int, int]) -> tuple[int, int]:
        pass

    @staticmethod
    @abc.abstractmethod
    def get_neighbour_coord_north(coord: tuple[int, int]) -> tuple[int, int]:
        pass

    @staticmethod
    @abc.abstractmethod
    def get_neighbour_coord(
        coord: tuple[int, int], direction: typing.Any
    ) -> tuple[int, int]:
        pass

    def carve_passage_east(self) -> bool:
        """
        Doesn't check if neighbour cell exists.
        Just carves a passage to the east if wall is openable
        Success: --> True;        else: --> False
        """
        return (
            self.dom.open_wall(self.position, "east")
        )

    def carve_passage_south(self) -> bool:
        """
        Doesn't check if neighbour cell exists.
        Just carves a passage to the south if wall is openable
        Success: --> True;        else: --> False
        """
        return (self.dom.open_wall(self.position, "south"))

    def carve_passage_west(self) -> bool:
        """
        Doesn't check if neighbour cell exists.
        Just carves a passage to the west if wall is openable
        Success: --> True;        else: --> False
        """
        return (self.dom.open_wall(self.position, "west"))

    def carve_passage_north(self) -> bool:
        """
        Doesn't check if neighbour cell exists.
        Just carves a passage to the north if wall is openable
        Success: --> True;        else: --> False
        """
        return (self.dom.open_wall(self.position, "north"))

    def carve_passage(self, direction: typing.Any) -> bool:
        """
        Doesn't check if neighbour cell exists.
        Just carves a passage to the direction if wall is openable
        Success: --> True;        else: --> False
        """
        return (self.dom.open_wall(self.position, direction))

    def traverse_east(self) -> bool:

        """
        gets the hypothetical neighbour coord to the east
        checks the existance of neighbour cell
        if neighbour exists and if wall is openable:
            --> carve passage ang move through; return True
        else:
            do nothing and return False
        """

        neighbour_coord: tuple[int, int]

        neighbour_coord = self.get_neighbour_coord_east(self.position)
        if (self.dom.validate_coord(neighbour_coord)):
            if (self.carve_passage_east()):
                return (self.move_east())
            return (False)
        return (False)

    def traverse_south(self) -> bool:

        """
        gets the hypothetical neighbour coord to the south
        checks the existance of neighbour cell
        if neighbour exists and if wall is openable:
            --> carve passage ang move through; return True
        else:
            do nothing and return False
        """

        neighbour_coord: tuple[int, int]

        neighbour_coord = self.get_neighbour_coord_south(self.position)
        if (self.dom.validate_coord(neighbour_coord)):
            if (self.carve_passage_south()):
                return (self.move_south())
            return (False)
        return (False)

    def traverse_west(self) -> bool:

        """
        gets the hypothetical neighbour coord to the west
        checks the existance of neighbour cell
        if neighbour exists and if wall is openable:
            --> carve passage ang move through; return True
        else:
            do nothing and return False
        """

        neighbour_coord: tuple[int, int]

        neighbour_coord = self.get_neighbour_coord_west(self.position)
        if (self.dom.validate_coord(neighbour_coord)):
            if (self.carve_passage_west()):
                return (self.move_west())
            return (False)
        return (False)

    def traverse_north(self) -> bool:

        """
        gets the hypothetical neighbour coord to the north
        checks the existance of neighbour cell
        if neighbour exists and if wall is openable:
            --> carve passage ang move through; return True
        else:
            do nothing and return False
        """

        neighbour_coord: tuple[int, int]

        neighbour_coord = self.get_neighbour_coord_north(self.position)
        if (self.dom.validate_coord(neighbour_coord)):
            if (self.carve_passage_north()):
                return (self.move_north())
            return (False)
        return (False)

    def traverse(self, direction: typing.Any) -> bool:

        """
        gets the hypothetical neighbour coord to the [direction]
        checks the existance of neighbour cell
        if neighbour exists and if wall is openable:
            --> carve passage ang move through; return True
        else:
            do nothing and return False

        valid directions are:
        [1, 2, 4, 8, 'n', 'e', 's', 'w', "north", "east", "south", "west"]
        if invalid input: raise error
        """

        neighbour_coord: tuple[int, int]

        neighbour_coord = self.get_neighbour_coord_east(self.position)
        if (self.dom.validate_coord(neighbour_coord)):
            if (self.carve_passage(direction)):
                return (self.move(direction))
            return (False)
        return (False)
