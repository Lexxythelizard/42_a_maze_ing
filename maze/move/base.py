#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import typing
from typing import cast
import abc
import maze.cells as cell
import maze.base as blueprint
import maze.values.constants as const

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------


class StringContainer:

    maze_type_err = "TypeError: expected Maze, got %s instead"


# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class Orientation(abc.ABC):

    """
    The Blueprint for orientation and movement in the maze
    """

    @staticmethod
    def get_neighbours_coord(
        coord: tuple[int, int],
        maze: blueprint.BlueprintMaze,
        raw: bool = False
    ) -> list[tuple[int, int]]:

        """
        gets a list of all neighbours coords according to the hierarchy
        defined in .maze.values.constants.Directions.hierarchy
        by default nonexisting (cell) coords got filtered out
        if raw=True return unfiltered list
        """

        neighbours: list[tuple[int, int]]
        x1: int
        y1: int
        x2: int
        y2: int
        width: int
        height: int
        x_ctrl: int
        y_ctrl: int
        catch: tuple[int, int]

        neighbours = list()
        x1, y1 = coord
        for direction in const.Directions.hierarchy:
            x2, y2 = const.Directions.relative_directions[direction]
            neighbours.append((x1 + x2, y1 + y2))

        if (raw):
            return (neighbours)
        width = maze.width
        height = maze.height
        catch = (-1, -1)
        for idx, el in enumerate(neighbours):
            x_ctrl, y_ctrl = el
            if (not ((0 <= x_ctrl < width) and (0 <= y_ctrl < height))):
                catch = neighbours.pop(idx)
        del catch
        return (neighbours)

    @staticmethod
    def get_neighbour_by_direction(
        coord: tuple[int, int],
        maze: blueprint.BlueprintMaze,
        direction: typing.Any
    ) -> list[tuple[int, int]]:

        """
        takes a direction and return the neighbour in [direction]
        if neighbour exists
        valid directions are:
        [1, 2, 4, 8, 'n', 'e', 's', 'w', "north", "east", "south", "west"]
        if invalid input: raise error
        """

        x1: int
        y1: int
        x2: int
        y2: int
        neighbours: list[tuple[int, int]]
        neighbour_coord: tuple[int, int]

        neighbours = list()

        x1, y1 = coord
        x2, y2 = const.Directions.relative_directions[direction]
        neighbour_coord = (x1 + x2, y1 + y2)
        if (maze.validate_coord(neighbour_coord)):
            neighbours.append(neighbour_coord)
        return (neighbours)

    @staticmethod
    def get_opposite_direction(direction: typing.Any) -> int:

        """
        takes any direction and return the power-of-two-key of its opposite
        valid directions are:
        [1, 2, 4, 8, 'n', 'e', 's', 'w', "north", "east", "south", "west"]
        if invalid input: return 0
        if valid input: return 1 / 2 / 4 / 8
        """

        return (
            const.Directions.opposite_directions.get(
                const.Directions.directions.get(direction, 0), 0
            )
        )

    @staticmethod
    def is_neighbour_east(
        coord: tuple[int, int],
        maze: blueprint.BlueprintMaze
    ) -> bool:

        """
        takes coords (x, y) and an instance of Maze
        checks if neighbour cell/coords (x + 1, y) exists
        """

        x: int
        y: int

        x, y = coord
        return ((0 <= x < (maze.width - 1)) and (0 <= y < maze.height))

    @staticmethod
    def is_neighbour_south(
        coord: tuple[int, int],
        maze: blueprint.BlueprintMaze
    ) -> bool:

        """
        takes coords (x, y) and an instance of Maze
        checks if neighbour cell/coords (x, y + 1) exists
        """

        x: int
        y: int

        x, y = coord
        return ((0 <= x < maze.width) and (0 <= y < (maze.height - 1)))

    @staticmethod
    def is_neighbour_west(
        coord: tuple[int, int],
        maze: blueprint.BlueprintMaze
    ) -> bool:

        """
        takes coords (x, y) and an instance of Maze
        checks if neighbour cell/coords (x - 1, y) exists
        """

        x: int
        y: int

        x, y = coord
        return ((1 <= x < maze.width) and (0 <= y < maze.height))

    @staticmethod
    def is_neighbour_north(
        coord: tuple[int, int],
        maze: blueprint.BlueprintMaze
    ) -> bool:

        """
        takes coords (x, y) and an instance of Maze
        checks if neighbour cell/coords (x, y - 1) exists
        """

        x: int
        y: int

        x, y = coord
        return ((0 <= x < maze.width) and (1 <= y < maze.height))

    @staticmethod
    def get_neighbour_coord_east(coord: tuple[int, int]) -> tuple[int, int]:

        """
        takes coords (x, y) and returns the coords of its hypothetical
        neighbour to the east indepentently from their existence
        return -> (x + 1, y)
        """

        relative_direction: tuple[int, int]
        neighbour_coord: tuple[int, int]

        relative_direction = const.Directions.relative_directions['east']
        neighbour_coord = cast(
            tuple[int, int],
            tuple(map(sum, zip(coord, relative_direction)))
        )
        return (neighbour_coord)

    @staticmethod
    def get_neighbour_coord_south(coord: tuple[int, int]) -> tuple[int, int]:

        """
        takes coords (x, y) and returns the coords of its hypothetical
        neighbour to the south indepentently from their existence
        return -> (x, y + 1)
        """

        relative_direction: tuple[int, int]
        neighbour_coord: tuple[int, int]

        relative_direction = const.Directions.relative_directions['south']
        neighbour_coord = cast(
            tuple[int, int],
            tuple(map(sum, zip(coord, relative_direction)))
        )
        return (neighbour_coord)

    @staticmethod
    def get_neighbour_coord_west(coord: tuple[int, int]) -> tuple[int, int]:

        """
        takes coords (x, y) and returns the coords of its hypothetical
        neighbour to the west indepentently from their existence
        return -> (x - 1, y)
        """

        relative_direction: tuple[int, int]
        neighbour_coord: tuple[int, int]

        relative_direction = const.Directions.relative_directions['west']
        neighbour_coord = cast(
            tuple[int, int],
            tuple(map(sum, zip(coord, relative_direction)))
        )
        return (neighbour_coord)

    @staticmethod
    def get_neighbour_coord_north(coord: tuple[int, int]) -> tuple[int, int]:

        """
        takes coords (x, y) and returns the coords of its hypothetical
        neighbour to the north indepentently from their existence
        return -> (x, y - 1)
        """

        relative_direction: tuple[int, int]
        neighbour_coord: tuple[int, int]

        relative_direction = const.Directions.relative_directions['north']
        neighbour_coord = cast(
            tuple[int, int],
            tuple(map(sum, zip(coord, relative_direction)))
        )
        return (neighbour_coord)


class BlueprintMazeRunner(abc.ABC):

    """
    The Blueprint for orientation and movement in the maze
    """

    __dom: blueprint.BlueprintMaze
    __position: tuple[int, int]

    def __init__(
        self,
        dom: blueprint.BlueprintMaze,
        position: tuple[int, int] = (0, 0)
    ) -> None:

        # TODO: implement dom guard
        # TODO: implement coord guard

        self.__dom = dom
        self.__position = position
        self.__dom._get_cell(self.__position).visit()

    @property
    def dom(self) -> blueprint.BlueprintMaze:
        return (self.__dom)

    @property
    def position(self) -> tuple[int, int]:
        return (self.__position)

    @property
    def cell(self) -> cell.Cell:
        return (self.dom._get_cell(self.__position))

    def _set_position(self, coord: tuple[int, int]) -> None:
        # TODO: implement guard
        self.__position = coord

    def is_open_east(self) -> bool:

        """
        Checks if wall to the east (in related cell) is open
        indepentendly of neighbours existence
        returns True if open False if closed
        """

        return (not self.cell.east_wall)

    def is_open_south(self) -> bool:

        """
        Checks if wall to the south (in related cell) is open
        indepentendly of neighbours existence
        returns True if open False if closed
        """

        return (not self.cell.south_wall)

    def is_open_west(self) -> bool:

        """
        Checks if wall to the west (in related cell) is open
        indepentendly of neighbours existence
        returns True if open False if closed
        """

        return (not self.cell.west_wall)

    def is_open_north(self) -> bool:

        """
        Checks if wall to the north (in related cell) is open
        indepentendly of neighbours existence
        returns True if open False if closed
        """

        return (not self.cell.north_wall)

    def is_open(self, direction: typing.Any) -> bool:

        """
        Checks if wall to the direction (in related cell) is open
        indepentendly of neighbours existence
        returns True if open False if closed

        direction have to be:
        [1, 2, 4, 8, 'n', 'e', 's', 'w', "north", "east", "south", "west"]
        raises Error if unvalid direction: ...under construction
        """

        side: int

        # TODO: implement guard
        side = const.Directions.directions[direction]
        return (bool((int(self.cell) ^ side) & int(self.cell)))

    @abc.abstractmethod
    def is_visited_east(self) -> bool:
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
