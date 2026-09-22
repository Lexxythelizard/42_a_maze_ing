#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import typing
import maze.cells as cell
import maze.base as blueprint

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------


class StringContainer:

    maze_type_err = "TypeError: expected Maze, got %s instead"


# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class MazeMap(BlueprintMazeMap):

    """
    MazeMap
    """

    def map_init_unknown(self) -> None:
        for x in range(self.__dom.width):
            for y in range(self.__dom.height):
                self.__map.update(
                    {(x, y): RelativeMazeMap(self.__dom, (x, y))}
                )
