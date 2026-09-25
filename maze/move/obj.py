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
    The Blueprint for orientation and movement in the maze
    """

    __ignore_walls: bool = False

    def move_east(self) -> bool:
        if (self.is_open_east()):
            # TODO: Implement Guard
            neighbour_coord = self.get_neighbour_by_direction(
                    maze=self.dom, coord=self.position, direction="east"
                )[0]
            self._set_position(neighbour_coord)
            self.cell.visit()
        return (False)

    def move_south(self) -> bool:
        if (self.is_open_east()):
            # TODO: Implement Guard
            neighbour_coord = self.get_neighbour_by_direction(
                    maze=self.dom, coord=self.position, direction="south"
                )[0]
            self._set_position(neighbour_coord)
            self.cell.visit()
        return (False)

    def move_west(self) -> bool:
        if (self.is_open_east()):
            # TODO: Implement Guard
            neighbour_coord = self.get_neighbour_by_direction(
                    maze=self.dom, coord=self.position, direction="west"
                )[0]
            self._set_position(neighbour_coord)
            self.cell.visit()
        return (False)

    def move_north(self) -> bool:
        if (self.is_open_east()):
            # TODO: Implement Guard
            neighbour_coord = self.get_neighbour_by_direction(
                    maze=self.dom, coord=self.position, direction="north"
                )[0]
            self._set_position(neighbour_coord)
            self.cell.visit()
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
