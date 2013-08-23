# TODO: bottom ending DiagonalDownRightOnRight is messing up the
# outline joins on top when flipped, it has a little flat spot.
# TODO: Test suite to try drawing all possible characters.
# TODO: Kerning by taking the convex hull of the written letter then finding a
# spot where they're the right distance apart. This function should be strictly
# increasing because of the convex hull thing.
# TODO: Make really nice pronunciation charts for the writing system and give
# them to John Quijada.
# TODO: Make a program to write your name in phonetic ithkuil.

import math

# Constants.
slant45 = 1 / math.sin(math.radians(45))
slant60 = 1 / math.sin(math.radians(60))
slant75 = 1 / math.sin(math.radians(75))

HALF_HEIGHT = 3.5
BOTTOM = 0
MIDDLE = BOTTOM + HALF_HEIGHT
TOP = MIDDLE + HALF_HEIGHT
UNDER = BOTTOM - 2.0
OVER = TOP + 2.0


def flip_consonant_horizontal(cls):

    class Flipped(cls):

        def draw_character(self, **kwargs):
            paper = cls.draw_character(self, **kwargs)
            paper.mirror_x(0)
            return paper

        def __str__(self):
            return 'Flipped(consonant.{})({}, {})'.format(
                cls.__name__,
                self.side_ending,
                self.bottom_ending,
            )

    return Flipped


class Character:
    def __init__(self, mode):
        self.mode = mode
        self.width = mode.width

    def draw_character(self, **kwargs):
        raise NotImplementedError()


class Ending:
    def __init__(self, character, mode):
        self.character = character
        self.mode = mode
        self.width = mode.width

    def angle(self):
        return None

    def draw(self, pen):
        return
