#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

import os

from maze.cells import RegularCell, FourtyTwoCell
from maze.map.obj import RelativeMazeMap, MazeMap
from maze.move.obj import MazeRunner
from maze.construct import ConstructionWorker
from maze import Maze

# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++


class Settings:

    programmers_name = "[programmers name]"


class StringContainer:

    motivation = "  Hi %s,\n\tGirl, You can do I.T. :)"

    menu = "  Menu: display Documentation for:\n\n"
    menu += "\t[1] / \"42cell\"\t\t: FourtyTwoCell\n"
    menu += "\t[2] / \"cell\"\t\t: RegularCell\n"
    menu += "\t[3] / \"maze\"\t\t: Maze\n"
    menu += "\t[4] / \"relative map\"\t: RelativeMazeMap\n"
    menu += "\t[5] / \"map\"\t\t: MazeMap\n"
    menu += "\t[6] / \"mazerunner\"\t: MazeRunner\n"
    menu += "\t[7] / \"construct\"\t: ConstructionWorker\n"
    menu += "\t[x]\t\t\t: Exit\n\n"
    menu += "  select: "


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++


class DocContainer:

    docs = {
        "42cell": FourtyTwoCell,
        '1': FourtyTwoCell,
        "cell": RegularCell,
        '2': RegularCell,
        "maze": Maze,
        '3': Maze,
        "relative map": RelativeMazeMap,
        '4': RelativeMazeMap,
        "map": MazeMap,
        '5': MazeMap,
        "mazerunner": MazeRunner,
        '6': MazeRunner,
        "construct": ConstructionWorker,
        '7': ConstructionWorker
    }

    invalid_inp = "invalid input, valid inputs are:\n\t%s" % docs.keys()


# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- sniggle ----------------------------


def motivation() -> None:
    print(StringContainer.motivation % Settings.programmers_name)


# ---------------------------- utils ----------------------------

# def ...

# ---------------------------- run ----------------------------


def main() -> None:

    print("\n------------------------------------\n")

    motivation()
    print('\n')

    while ((inp := input(StringContainer.menu).lower()) != 'x'):
        os.system('clear')

        if (inp in DocContainer.docs.keys()):
            help(DocContainer.docs[inp])

        motivation()
        print('\n')

    print("\n------------------------------------")


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
