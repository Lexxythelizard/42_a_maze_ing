#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

# import maze
# import maze.ui as ui
# from maze.cells import Cell
# import typing
import random
from maze.construct.base import MazeDrill
from maze.move import MazeRunner
# from maze.values.constants import Directions

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class ConstructionWorker(MazeRunner, MazeDrill):

    """
    ConstructionWorker is an evolved (MazeRunner) MazeCrawler
    with a Tool: MazeDrill.
        see help(MazeDrill)
    It can do everything MazeCrawler can do plus what MazeDrill provides
    additionally it can carve a maze alogorythmicly.

    stats:
        __dom:          the related Maze instance
        __position:     the cluster of RealtiveMazeMap instances
                        {(x, y): RelativeMazeMap}
        __work_stack:   the stack full of tasks {coord: directions}
                        {(x, y): [<valid and unvisited directions>]}
        __shuffle:      if shuffle is true, is uses random and .seed
                        bool: False by default
        __seed:         fixed seed to use if shuffle
                        int: 0 by default

    assign it to a position by initializing, call .init_work_stack()
    and then call .process() over and over until it returns False

    traverses a fixed pattern, except You set .shuffle = True
    TIPP:   use a fix seed to pick a start posititon randomly, before
            You initializing the instance, then set .seed and .shuffle
            and loop from outside with time.sleep()
            and display every step with ascii rendering :)
    """

    __work_stack: dict[tuple[int, int], list[str]] = {}
    __shuffle: bool = False
    __seed: int = 0

    @property
    def work_stack(self) -> dict[tuple[int, int], list[str]]:
        return (self.__work_stack)

    @property
    def shuffle(self) -> bool:
        return (self.__shuffle)

    @property
    def seed(self) -> int:
        return (self.__seed)

    def _add_current_position_to_work_stack(self) -> int:

        """
        Adds current position to workload.
        gets directions, filteres non existing, filters visited
        updates workload
        if .shuffle is True, shuffles filtered list

        return number elements in filtered list
        """

        directions: list[str]

        directions = self.get_ordererd_directions()
        directions = [
            element for element in directions if self.is_neighbour(
                maze=self.dom, coord=self.position, direction=element
            )
        ]
        directions = [
            element for element in directions if not self.is_visited(element)
        ]
        if (self.__shuffle):
            random.Random(self.__seed).shuffle(directions)
        self.work_stack.update({self.position: directions})
        return (len(directions))

    def _remove_current_position_from_workstack(self) -> int:

        """
        Removes current position from work_stack.
        returns length of removed value
        pops workload
        return numer of not processed directions (0 is good)

        raises error if item doesn't exist
        """

        if (not self.__work_stack):
            return (0)

        val = self.__work_stack.pop(self.position)
        return (len(val))

    def process(self) -> bool:

        """
        work_stack {<coord>: list[<existing and unvisited directions>]}
        processes datas in work_stack traverses and backtracks
        by orchestering:
            ._add_current_position_to_work_stack
            ._remove_current_position_from_workstack
        picks the last item in work_stack compares the current position
        with key of the last item in stack

        traverse to the fist direction in list if possible
        if no traverse was possible at this position it does back tracking

        returns True after it finished the process
        returns False if work_stack was empty
        """

        ctrl_pos: tuple[int, int]
        directions: list[str]
        direction: str

        if (not self.__work_stack):
            return (False)

        ctrl_pos, directions = \
            list(self.__work_stack.items())[-1]
        if (self.position != ctrl_pos):
            raise IndexError(
                '[Spaceholder]: position and key are not alligned'
            )

        # directions will be filtered again
        directions = [
            element for element in directions if not self.is_visited(element)
        ]
        # if that would be too much maybe just filtering in loop below

        while (directions):
            direction = directions.pop(0)

            if (ctrl := self.traverse(direction)):
                print("ctrl", ctrl)
                print("pos", self.position)
                self._add_current_position_to_work_stack()
                return (True)

        # if (not directions):
        self._remove_current_position_from_workstack()
        if (self.__work_stack):
            self._set_position(list(self.__work_stack.keys())[-1])
        return (True)
