#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import typing
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
    def get_neighbours_directions(
        coord: tuple[int, int],
        maze: blueprint.BlueprintMaze
    ) -> list[tuple[int, int]]:

        neighbours = list()
        x1, y1 = coord
        for direction in const.Directions.hierarchy:
            x2, y2 = const.Directions.relative_directions[direction]
            neighbours.append((x1 + x2, y1 + y2))

        return (neighbours)
