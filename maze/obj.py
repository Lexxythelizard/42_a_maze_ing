#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

# import typing
import maze.cells as cell
import maze.base as blueprint

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------


# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class Maze(blueprint.BlueprintMaze):

    """
    maze
    """

    __start: tuple[int, int]
    __goal: tuple[int, int]

    def __init__(
        self,
        size: tuple[int, int] = (2, 2),
        empty: bool = False,
    ) -> None:

        super().__init__(size)

        if (empty):
            return

    def set_visit(self, coord: tuple[int, int]) -> None:
        self._get_cell(coord).visit()

    def set_unvisit(self, coord: tuple[int, int]) -> None:
        self._get_cell(coord).unvisit()

    def set_start(self, coord: tuple[int, int]) -> None:
        self._guard_coord_type(coord)
        self._guard_coord_val(coord, self.get_width(), self.get_height())
        self.__start = coord

    def set_goal(self, coord: tuple[int, int]) -> None:
        self._guard_coord_type(coord)
        self._guard_coord_val(coord, self.get_width(), self.get_height())
        self.__goal = coord

    def get_start(self) -> tuple[int, int]:
        return (self.__start)

    def get_goal(self) -> tuple[int, int]:
        return (self.__goal)

    def _init_empty(self, size: tuple[int, int] = (2, 2)) -> None:

        width: int
        height: int

        width, height = size
        for x in range(width):
            self._get_grid().append(
                [cell.RegularCell() for y in range(height)]
            )

    def close_frame(self, lock: bool = True) -> None:

        width: int
        height: int

        width, height = self.get_size()
        self._get_cell((0, 0)).close_mult_walls(['west', 'north'])
        self._get_cell((width - 1, 0)).close_mult_walls(['north', 'east'])
        self._get_cell((width - 1, height - 1)).close_mult_walls(
            ['east', 'south']
        )
        self._get_cell((0, height - 1)).close_mult_walls(['south', 'west'])
        for i in range(width):
            self._get_cell((i, 0)).close_wall('north')
            self._get_cell((i, height - 1)).close_wall('south')
        for i in range(height):
            self._get_cell((0, i)).close_wall('west')
            self._get_cell((width - 1, i)).close_wall('east')

        if (lock):
            for i in range(width):
                self._get_cell((i, 0)).lock()
                self._get_cell((i, height - 1)).lock()
            for i in range(height):
                self._get_cell((0, i)).lock()
                self._get_cell((width - 1, i)).lock()

    def set_fourty_two(self) -> bool:

        return (False)
