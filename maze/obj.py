#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import typing
import maze.cells as cell
import maze.base as blueprint
import maze.move.base as move

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------


# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class Maze(blueprint.BlueprintMaze, move.Orientation):

    """
    Maze holds a two dimensional list of Cells
    can manipulate walls by opening and closing them
    can keep track of start and goal coords
    can set close the frame
    (can set foruty two cells incl pattern) ...under construction

    stats:

    __cells:    contains 2D list of Cells
                list[list[Cell]]
    __width:    length of x-axis
    __height:   length of y-axis
    __start:    coords of start position
    __goal:     coords of goal position

    start and goal are (-1, -1) by default
    open and close methods can are also opening / closing the neighbours
    matching wall if neighbour wall exists and if both are open/closable

    ---------------------------------------------------------------
    next expansion/feature - just if needed:
        .lock_cell(
            coord: tuple[int, int],
            semipermeable: bool = False
        ) -> bool:

        .lock_cell(
            coord: tuple[int, int],
            semipermeable: bool = False
        ) -> bool:

        both will:
            - check if cell on coord is regular or 42 cell
            - check if neighbour is regular or 42 cell
            if cell is 42cell:
                just lock / unlock it
            if cell is regular cell:
                if neighbour is regular cell
                    set its matching opposite side wall as constant
    ----------------------------------------------------------------
    """

    __start: tuple[int, int]
    __goal: tuple[int, int]

    def __init__(
        self,
        size: tuple[int, int] = (2, 2),
        empty: bool = False,
    ) -> None:

        super().__init__(size)
        self.__start = (-1, -1)
        self.__goal = (-1, -1)
        if (empty):
            return

    @property
    def start(self) -> tuple[int, int]:
        return (self.__start)

    @property
    def goal(self) -> tuple[int, int]:
        return (self.__goal)

    def open_wall(
        self,
        coord: tuple[int, int],
        wall: typing.Any,
        semipermeable: bool = False
    ) -> bool:

        """
        opens wall of a cell and its matching (neighbour cell) wall
        (if neighbour wall exists) by default
        if no neighbour or semipermeable=True,
        then just opens the selected cells wall.
        returns:

        success -> True
        else    -> False

        internal logic:
        if wall or matched wall is not openable: reset
        if neighbour: wall is openable:
        |-- if selected: wall is openable:
        |  | --return true
        |  else:
        |  | -- neigbour: reset wall
        |  | -- return False
        else:
        |-- return False
        """

        swap: int
        neighbour: cell.Cell
        neighbour_coord: list[tuple[int, int]]

        self._guard_coord_type(coord)
        self._guard_coord_val(coord, self.get_width(), self.get_height())
        # implement guard valid wall

        neighbour_coord = self.get_neighbour_by_direction(
            coord=coord, maze=self, direction=wall
        )
        if (semipermeable or (not neighbour_coord)):
            return (self._get_cell(coord).open_wall(wall))

        neighbour = self._get_cell(neighbour_coord[0])
        swap = int(neighbour)
        if (neighbour.open_wall(self.get_opposite_direction(wall))):

            if (self._get_cell(coord).open_wall(wall)):
                return (True)

            neighbour._set_walls(swap)
            return (False)

        return (False)

    def open_mult_walls(
        self,
        coord: tuple[int, int],
        walls: typing.Any,
        semipermeable: bool = False
    ) -> bool:

        """
        under construction:
        don't use
        except You set semipermeable=True
        ...but why should You?
        """

        self._guard_coord_type(coord)
        self._guard_coord_val(coord, self.get_width(), self.get_height())

        if semipermeable:
            return (self._get_cell(coord).open_mult_walls(walls))

        # implement alt
        return (False)

    def close_wall(
        self,
        coord: tuple[int, int],
        wall: typing.Any,
        semipermeable: bool = False
    ) -> bool:

        """
        closes wall of a cell and its matching (neighbour cell) wall
        (if neighbour wall exists) by default
        if no neighbour or semipermeable=True,
        then just opens the selected cells wall.
        returns:

        success -> True
        else    -> False

        internal logic:
        if wall or matched wall is not closeable: reset
        if neighbour: wall is closeable:
        |-- if selected: wall is closeable:
        |  | --return true
        |  else:
        |  | -- neigbour: reset wall
        |  | -- return False
        else:
        |-- return False
        """

        swap: int
        neighbour: cell.Cell
        neighbour_coord: list[tuple[int, int]]

        self._guard_coord_type(coord)
        self._guard_coord_val(coord, self.get_width(), self.get_height())
        # implement guard valid wall

        neighbour_coord = self.get_neighbour_by_direction(
            coord=coord, maze=self, direction=wall
        )
        if (semipermeable or (not neighbour_coord)):
            return (self._get_cell(coord).close_wall(wall))

        neighbour = self._get_cell(neighbour_coord[0])
        swap = int(neighbour)
        if (neighbour.close_wall(self.get_opposite_direction(wall))):

            if (self._get_cell(coord).close_wall(wall)):
                return (True)

            neighbour._set_walls(swap)
            return (False)
        return (False)

    def close_mult_walls(
        self,
        coord: tuple[int, int],
        walls: typing.Any,
        semipermeable: bool = False
    ) -> bool:

        """
        under construction:
        don't use
        except You set semipermeable=True
        ...but why should You?
        """

        self._guard_coord_type(coord)
        self._guard_coord_val(coord, self.get_width(), self.get_height())

        if semipermeable:
            return (self._get_cell(coord).close_mult_walls(walls))

        # implement alt
        return (False)

    def set_visit(self, coord: tuple[int, int]) -> None:
        """
        sets selected_cell .cells[coord] to visited
        """
        self._get_cell(coord).visit()

    def set_unvisit(self, coord: tuple[int, int]) -> None:
        """
        sets selected_cell .cells[coord] to visited
        """
        self._get_cell(coord).unvisit()

    def set_start(self, coord: tuple[int, int]) -> None:
        """
        sets coordinates for start position
        raises error if coord is invalid
        NOTE: method is not checking for 42Cells
        """
        self._guard_coord_type(coord)
        self._guard_coord_val(coord, self.get_width(), self.get_height())
        self.__start = coord

    def set_goal(self, coord: tuple[int, int]) -> None:
        """
        sets coordinates for goal position
        raises error if coord is invalid
        NOTE: method is not checking for 42Cells
        """
        self._guard_coord_type(coord)
        self._guard_coord_val(coord, self.get_width(), self.get_height())
        self.__goal = coord

    def get_start(self) -> tuple[int, int]:
        """
        does basicly the same like .start:
        returning coord of start (x, y)
        but was implemented earlier...
        ...maybe remove
        """
        return (self.__start)

    def get_goal(self) -> tuple[int, int]:
        """
        does basicly the same like .goal:
        returning coord of goal (x, y)
        but was implemented earlier...
        ...maybe remove
        """
        return (self.__goal)

    def _init_empty(self, size: tuple[int, int] = (2, 2)) -> None:
        """
        initializes a two dimensional list of Regular cells with open walls
        automaticly called by constructor
        """

        width: int
        height: int

        width, height = size
        for x in range(width):
            self._get_grid().append(
                [cell.RegularCell() for y in range(height)]
            )

    def close_frame(self, lock: bool = True) -> None:

        """
        closes the outer walls of the maze (frame) and makes them constant
        """

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

        """
        Places the FourtyTwoCells
        ...under construction...

        ...always returns False
        """

        return (False)
