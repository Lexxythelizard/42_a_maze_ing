#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import os
import maze
import maze.ui as ui
from maze.cells import Cell
from maze.values.constants import Directions

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++


class Settings:

    programmers_name = "[programmers name]"


class StringContainer:

    motivation = "  Hi %s,\n\tGirl, You can do I.T. :)"


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- sniggle ----------------------------


def motivation() -> None:
    print(StringContainer.motivation % Settings.programmers_name)


# ---------------------------- utils ----------------------------

# def ...

# ---------------------------- run ----------------------------


def main() -> None:

    main_obj: maze.Maze
    cli_obj: ui.CLIOutput
    move_obj: maze.MazeRunner
    map_obj: maze.MazeMap

    switch: bool
    rel_neighbours: dict[tuple[int, int], Cell]
    rel_neighbours_unfiltered: dict[tuple[int, int], Cell]

    print("\n------------------------------------\n")

    os.system('clear')
    motivation()
    print('')

    # initialize a 3 x 3 maze

    main_obj = maze.Maze((3, 3))
    main_obj.set_start((0, 0))
    main_obj.set_goal((2, 1))

    # Cool, now lets use the prototype of CLIOutput to visualize it
    cli_obj = ui.CLIOutput(main_obj)

    # initializing the maze runner to move inside the maze at start position
    move_obj = maze.MazeRunner(dom=main_obj, position=main_obj.start)

    # initializing the maze runner to move inside the maze at start position
    map_obj = maze.MazeMap(dom=main_obj)

    # the new initialized maze is empty no walls and no frames have been set

    # use main_obj.close_wall(<coord>, <wall>)
    #    coord: tuple[int, int]:    (x, y)
    #    wall:  str | int :
    #         1, 2, 4, 8, 'n', 'e', 's', 'w', "north", "east", "south", "west"
    # main_obj.close_wall((1, 1), "east") will close east wall of cell (1, 1)
    # and west wall of of cell (2, 1)

    main_obj.close_wall((1, 1), "east")

    # now let's check
    print("ctrl: cell (2, 1) expected 2; is %d" % int(main_obj.cells[1][1]))
    print("ctrl: cell (2, 1) expected 8; is %d" % int(main_obj.cells[1][1]))

    # main_obj.cells[x][y] retuns the same as main_obj._get_cell((x, y))
    # ---> main_obj._get_cell(()) ;    use double paranthesis bc 1 arg tuple

    # please use main_obj.close_wall() / main_obj.open_wall()
    #     this will also manage the neighbour cells
    #     accessing a cell directly would make the maze wall 'semipermeable'
    # both will return either True or False

    # for more details check out help(maze.Maze)

    # update frame
    cli_obj.set_frame_blank()
    print('\n  just one wall closed:')
    print(cli_obj.frame % (tuple(' ') * (3 * 3)))

    # now let's set the outer walls by using one simple command
    # outer walls wil get set constant automaticly
    # the attempt to open the will return False
    main_obj.close_frame()

    # update and print frame
    cli_obj.set_frame_blank()
    print('\n  outer walls got closed:')
    print(cli_obj.frame % (tuple(' ') * (3 * 3)))

    # now lets close some other walls
    main_obj.close_wall((0, 0), "east")
    main_obj.close_wall((1, 1), "south")

    # update and print frame
    cli_obj.set_frame_blank()
    print('\n  closed some other walls:')
    print(cli_obj.frame % (tuple(' ') * (3 * 3)))

    # now let's check how to use the maze runner

    print("\nnow let's do is_open_*() checks")
    print("is open east: %s" % move_obj.is_open_east())
    print("is open south: %s" % move_obj.is_open_south())
    print('')

    print("\nnow let's check move*()")
    print("move east: --> %s" % move_obj.move_east())
    print("check position x: %d, y: %d" % move_obj.position)
    print("move south: --> %s" % move_obj.move_south())
    print("check position: x: %d, y: %d" % move_obj.position)
    print('')

    print("\nnow let's do is_visited_*() checks")
    print("is visited east: %s" % move_obj.is_visited_east())
    print("is visted north: %s" % move_obj.is_visited_north())
    print('')

    # cool, now we can build an rudimental algorythm with it:

    print(
        "positon maze runner for searching: x: %d, y: %d" % move_obj.position
    )
    while (move_obj.position != main_obj.goal):

        switch = False
        for direction in Directions.hierarchy:
            if (not move_obj.is_visited(direction)):
                if (move_obj.is_open(direction)):
                    move_obj.move(direction)
                    switch = True
                    break

        if (not switch):
            for direction in Directions.hierarchy:
                if (move_obj.is_open(direction)):
                    move_obj.move(direction)
                    break

        print("positon maze runner: x: %d, y: %d" % move_obj.position)

    print('')

    # super, now lets check

    # use the orchestering maze map to interact with relativ maze maps
    # (recommended)

    # for example lets print two relative maze maps

    map_obj.dev_print_relative_map((0, 0))
    print('')
    map_obj.dev_print_relative_map((1, 1))
    print('')

    # now let's set one or two arbitary map cells of the relative map (1, 1)
    # map_obj.set_relative_map_cell(<coord_map>, <coord_cell>, <key>)
    map_obj.set_relative_map_cell(coord_map=(1, 1), coord_cell=(0, 1), key=8)
    map_obj.set_relative_map_cell(coord_map=(1, 1), coord_cell=(0, 0), key=8)
    map_obj.set_relative_map_cell(coord_map=(1, 1), coord_cell=(1, 0), key=1)
    map_obj.set_relative_map_cell(coord_map=(1, 1), coord_cell=(1, 2), key=8)

    # lets print relative map 0, 0 and relative map 1, 1 again
    # we wil see, that map 0, 0 is still untouched :)

    print("after setting some values to map (not to maze)")
    map_obj.dev_print_relative_map((0, 0))
    print('')
    map_obj.dev_print_relative_map((1, 1))
    print('')

    # now lets get the relative neighbours
    # return dict {<coord>: <cell>} : cell means real maze cell not map cell!
    rel_neighbours = map_obj.get_relative_neighbours(coord=(1, 1))
    rel_neighbours_unfiltered = map_obj.get_relative_neighbours(
        coord=(1, 1), restricted=False
    )
    # by default we wil just get the neighbours which are not seperated
    # by a direct wall.
    print("Ordered in hierarchy: %s" % Directions.hierarchy)
    print(
        "relative neighbours of cell 1, 1 - filteres:\n",
        rel_neighbours
    )
    print(
        "relative neighbours of cell 1, 1 - unfiltered:\n",
        rel_neighbours_unfiltered
    )

    # dict {<neighbour_coord>: <cell>}
    # <cell> could be checked with int(<cell>) or <cell>.east_wall, .west_wall
    # etc...
    # DO NOT use <cell>.open_wall / <cell>.close_wall()
    # insteade use <maze>.close_wall(<neighbour_coord>) /
    # <maze>.open_wall(<neighbour_coord>)

    # for example

    # for coord, cell in rel_neighbours.items():
    #     do something with main_obj and coord
    #     just read or compare cell (like a just-read-pointer)

    print("\n------------------------------------")

    # Have fun to try out stuff :)

# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++


if __name__ == '__main__':

    main()
