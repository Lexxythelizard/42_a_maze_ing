#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import typing
import maze.move.base as base

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------


class StringContainer:

    maze_type_err = "TypeError: expected Maze, got %s instead"
    spaceholder = "[Spaceholder]"


# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class MazeRunner(base.BlueprintMazeRunner, base.Orientation):

    """
    MazeRunner simulates an object with can move inside the maze
    stats:
        __dom: the related Maze instance
        __position: the current position as tuple

    Sets current cell to visited automaticly when initialised
    and when successfully executed a move
    Checks direct neighbour cells have been visited
    Checks if walls in current cell are open or closed
    move_[direction] is protected:
        can't get out of bounce
        can't move through walls (except if semipermeable)
    """

    __ignore_walls: bool = False

    def move_east(self) -> bool:

        """
        Moves east if neighbour exist and wall is open
        then updates the current position and set related cell to visited
        returns True if success, else returns False
        """

        if (self.is_open_east()):
            if (not self.is_neighbour_east(self.position, self.dom)):
                return (False)
            neighbour_coord = self.get_neighbour_coord_east(self.position)
            self._set_position(neighbour_coord)
            self.cell.visit()
            return (True)
        return (False)

    def move_south(self) -> bool:

        """
        Moves south if neighbour exist and wall is open
        then updates the current position and set related cell to visited
        returns True if success, else returns False
        """

        if (self.is_open_south()):
            if (not self.is_neighbour_south(self.position, self.dom)):
                return (False)
            neighbour_coord = self.get_neighbour_coord_south(self.position)
            self._set_position(neighbour_coord)
            self.cell.visit()
            return (True)
        return (False)

    def move_west(self) -> bool:

        """
        Moves west if neighbour exist and wall is open
        then updates the current position and set related cell to visited
        returns True if success, else returns False
        """

        if (self.is_open_west()):
            if (not self.is_neighbour_west(self.position, self.dom)):
                return (False)
            neighbour_coord = self.get_neighbour_coord_west(self.position)
            self._set_position(neighbour_coord)
            self.cell.visit()
            return (True)
        return (False)

    def move_north(self) -> bool:

        """
        Moves north if neighbour exist and wall is open
        then updates the current position and set related cell to visited
        returns True if success, else returns False
        """

        if (self.is_open_north()):
            if (not self.is_neighbour_north(self.position, self.dom)):
                return (False)
            neighbour_coord = self.get_neighbour_coord_north(self.position)
            self._set_position(neighbour_coord)
            self.cell.visit()
            return (True)
        return (False)

    def move(self, direction: typing.Any) -> bool:

        """
        DOC
        Moves in [direction] if neighbour exist and wall is open
        then updates the current position and set related cell to visited
        returns True if success, else returns False
        valid direction:
        [1, 2, 4, 8, 'n', 'e', 's', 'w', "north", "east", "south", "west"]
        raises error if unvalid direction: ...under vonstruction
        """

        # TODO: Implement Guard
        if (self.is_open(direction)):
            neighbour_coord = self.get_neighbour_by_direction(
                    maze=self.dom, coord=self.position, direction=direction
                )[0]
            self._set_position(neighbour_coord)
            self.cell.visit()
        return (False)

    def is_visited_east(self) -> bool:

        """
        Checks if neighbour to the east was visited
        if (neighbour) cell.visited is True return True else return False
        """

        if (not self.is_neighbour_east(coord=self.position, maze=self.dom)):
            return (False)

        return (
            self.dom._get_cell(
                self.get_neighbour_coord_east(self.position)
            ).visited
        )

    def is_visited_south(self) -> bool:

        """
        Checks if neighbour to the south was visited
        if (neighbour) cell.visited is True return True else return False
        """

        if (not self.is_neighbour_south(coord=self.position, maze=self.dom)):
            return (False)

        return (
            self.dom._get_cell(
                self.get_neighbour_coord_south(self.position)
            ).visited
        )

    def is_visited_west(self) -> bool:

        """
        Checks if neighbour to the west was visited
        if (neighbour) cell.visited is True return True else return False
        """

        if (not self.is_neighbour_west(coord=self.position, maze=self.dom)):
            return (False)

        return (
            self.dom._get_cell(
                self.get_neighbour_coord_west(self.position)
            ).visited
        )

    def is_visited_north(self) -> bool:

        """
        Checks if neighbour to the north was visited
        if (neighbour) cell.visited is True return True else return False
        """

        if (not self.is_neighbour_north(coord=self.position, maze=self.dom)):
            return (False)

        return (
            self.dom._get_cell(
                self.get_neighbour_coord_north(self.position)
            ).visited
        )
