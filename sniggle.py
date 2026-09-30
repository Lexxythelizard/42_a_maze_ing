#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import os
import maze
import maze.ui as ui
from maze.cells import Cell
from maze.construct import ConstructionWorker
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

    cli_obj = ui.CLIOutput(main_obj)
    move_obj = maze.MazeRunner(dom=main_obj, position=main_obj.start)
    map_obj = maze.MazeMap(dom=main_obj)
    construct_obj = ConstructionWorker(dom=main_obj, position=(0, 0))

    # close frame (and set constant walls)
    main_obj.close_frame()

    # close all
    for x in range(main_obj.width):
        for y in range(main_obj.height):
            main_obj.cells[x][y].close_mult_walls(15)

    # update cli_obj and print frame
    cli_obj.set_frame_blank()
    print(cli_obj.frame % (tuple(' ') * (3 * 3)))
    
    # start at arbitary point
    # get list of direction
    #    move and open walls, if neighbour exists and not visited
    #    else next element in list

    # start random
    # get list of cell: hierarchy
    # while list            --> some would refer list[-1]
    #    for direction in hierarchie
    #        if neighbor exists (coords valid) and is unvisited:
    #             .open_wall(coord, direction)
    #             add new element to stack
    #             repeat
    #                 --> some would break and star with last element
    #    if loop endet pop last item from list

    # test construction worker

    print("test constructionworker dom: %s" % construct_obj.dom)
    print("test constructionworker position: (%d, %d)" % construct_obj.position)
    print("test move east: %s" % construct_obj.move_east())
    print("test position: (%d, %d)" % construct_obj.position)
    print("test carve east: %s" % construct_obj.carve_passage_east())
    print("test move east: %s" % construct_obj.move_east())
    print("test position: (%d, %d)" % construct_obj.position)
    print("test traverse south: %s" % construct_obj.traverse_south())
    print("test position: (%d, %d)" % construct_obj.position)

    # update cli_obj and print frame
    cli_obj.set_frame_blank()
    print(cli_obj.frame % (tuple(' ') * (3 * 3)))

    print("test traverse west: %s" % construct_obj.traverse_west())
    print("test position: (%d, %d)" % construct_obj.position)
    print("test traverse south: %s" % construct_obj.traverse_south())
    print("test position: (%d, %d)" % construct_obj.position)
    print("test traverse east: %s" % construct_obj.traverse_east())
    print("test position: (%d, %d)" % construct_obj.position)
    print("test traverse east: %s" % construct_obj.traverse_east())
    print("test position: (%d, %d)" % construct_obj.position)
    print("test traverse east: %s" % construct_obj.traverse_east())
    print("test position: (%d, %d)" % construct_obj.position)
    print("test traverse north: %s" % construct_obj.traverse_north())
    print("test position: (%d, %d)" % construct_obj.position)
    print("test traverse north: %s" % construct_obj.traverse_north())
    print("test position: (%d, %d)" % construct_obj.position)
    print("test traverse north: %s" % construct_obj.traverse_north())
    print("test position: (%d, %d)" % construct_obj.position)

    # update cli_obj and print frame
    cli_obj.set_frame_blank()
    print(cli_obj.frame % (tuple(' ') * (3 * 3)))

    print("\n------------------------------------")

# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++


if __name__ == '__main__':

    main()
