#!/usr/bin/python3

# ++++++++++++++++++++++++++++ imports ++++++++++++++++++++++++++++

# import

# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ globals ++++++++++++++++++++++++++++

# ---------------------------- strings ----------------------------

class StringContainer:

    map_key_error = "ValueError: Invalid map key! expected one of %s got %s"

# ---------------------------- sniggle ----------------------------


# ++++++++++++++++++++++++++++ classes ++++++++++++++++++++++++++++

# ---------------------------- abstr/par ----------------------------

class Directions:

    north = 1
    east = 2
    south = 4
    west = 8

    none = 0
    unknown = 16
    blocked = -1
    ft_cell = 42

    directions = {
        "n": 1, "north": 1,
        "e": 2, "east": 2,
        "s": 4, "south": 4,
        "w": 8, "west": 8
    }

    relative_directions = {
        "n": (0, -1), "north": (0, -1), 1: (0, -1),
        "e": (1, 0), "east": (1, 0), 2: (1, 0),
        "s": (0, 1), "south": (0, 1), 4: (0, 1),
        "w": (-1, 0), "west": (-1, 0), 8: (-1, 0)
    }

    relative_directions_reversed = {
        (0, -1): "north",
        (1, 0): "east",
        (0, 1): "south",
        (-1, 0): "west"
    }

    hierarchy = [
        "east", "south", "west", "north"
    ]

    valid_map_keys = [
        north, east, south, west,
        none, unknown, blocked, ft_cell
    ]

    @classmethod
    def guard_map_key(cls, key: int) -> None:
        if (key not in cls.valid_map_keys):
            raise ValueError(
                StringContainer.map_key_error %
                (cls.valid_map_keys, key)
            )

    @classmethod
    def get_direction_by_coord(
        cls,
        position_coord: tuple[int, int],
        neighbour_coord: tuple[int, int]
    ) -> int:

        x1: int
        y1: int
        x2: int
        y2: int

        x1, y1 = position_coord
        x2, y2 = neighbour_coord
        return (
            cls.directions.get(
                cls.relative_directions_reversed.get(
                    (x2 - x1, y2 - y1),
                    'NULL'
                ),
                0b0000
            )
        )

# ++++++++++++++++++++++++++++ funcs ++++++++++++++++++++++++++++


# ---------------------------- sniggle ----------------------------

# def ...

# ---------------------------- utils ----------------------------

# def ...

# ---------------------------- run ----------------------------


def main() -> None:
    pass


# ++++++++++++++++++++++++++++ run ++++++++++++++++++++++++++++

if __name__ == '__main__':

    main()
