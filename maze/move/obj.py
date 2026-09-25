#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import typing
import maze.move.base as base
# import maze.cells as cell
# import maze.base as blueprint
# import maze.values.constants as const

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------


class StringContainer:

    maze_type_err = "TypeError: expected Maze, got %s instead"
    spaceholder = "[Spaceholder]"


# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class MazeRunner(base.BlueprintMazeRunner, base.Orientation):

    """
    MazeRunner, can move inside the maze and visit cells
    """

    __ignore_walls: bool = False

    def move_east(self) -> bool:
        if (self.is_open_east()):
            if (not self.is_neighbour_east(self.position, self.dom)):
                return (False)
            neighbour_coord = self.get_neighbour_coord_east(self.position)
            self._set_position(neighbour_coord)
            self.cell.visit()
            return (True)
        return (False)

    def move_south(self) -> bool:
        if (self.is_open_south()):
            if (not self.is_neighbour_south(self.position, self.dom)):
                return (False)
            neighbour_coord = self.get_neighbour_coord_south(self.position)
            self._set_position(neighbour_coord)
            self.cell.visit()
            return (True)
        return (False)

    def move_west(self) -> bool:
        if (self.is_open_west()):
            if (not self.is_neighbour_west(self.position, self.dom)):
                return (False)
            neighbour_coord = self.get_neighbour_coord_west(self.position)
            self._set_position(neighbour_coord)
            self.cell.visit()
            return (True)
        return (False)

    def move_north(self) -> bool:
        if (self.is_open_north()):
            if (not self.is_neighbour_north(self.position, self.dom)):
                return (False)
            neighbour_coord = self.get_neighbour_coord_north(self.position)
            self._set_position(neighbour_coord)
            self.cell.visit()
            return (True)
        return (False)

    def move(self, direction: typing.Any) -> bool:
        # TODO: Implement Guard
        if (self.is_open(direction)):
            neighbour_coord = self.get_neighbour_by_direction(
                    maze=self.dom, coord=self.position, direction=direction
                )[0]
            self._set_position(neighbour_coord)
            self.cell.visit()
        return (False)

    def is_visited_east(self) -> bool:
        if (self.is_neighbour_east(coord=self.position, maze=self.dom)):
            return (False)

        return (
            self.dom._get_cell(
                self.get_neighbour_coord_east(self.position)
            ).visited
        )

    def is_visited_south(self) -> bool:
        if (self.is_neighbour_south(coord=self.position, maze=self.dom)):
            return (False)

        return (
            self.dom._get_cell(
                self.get_neighbour_coord_south(self.position)
            ).visited
        )

    def is_visited_west(self) -> bool:
        if (self.is_neighbour_west(coord=self.position, maze=self.dom)):
            return (False)

        return (
            self.dom._get_cell(
                self.get_neighbour_coord_west(self.position)
            ).visited
        )

    def is_visited_north(self) -> bool:
        if (self.is_neighbour_north(coord=self.position, maze=self.dom)):
            return (False)

        return (
            self.dom._get_cell(
                self.get_neighbour_coord_north(self.position)
            ).visited
        )
