from .common import Ending, TOP, slant45
from .util import hook


class SideEnding(Ending):

    pattern = NotImplemented
    stem = NotImplemented
    relation = NotImplemented
    transliteration = NotImplemented

    def __init__(self, character, flipped):
        super().__init__(character)
        self.flipped = flipped


class Normal(SideEnding):

    pattern = 'P1'
    stem = 'S1'
    relation = 'UNFRAMED'
    transliteration = ''

    def draw(self, pen):
        if self.flipped:
            pen.line_forward(pen.mode.width, end_slant=-45)
        else:
            pen.line_forward(pen.mode.width, end_slant=45)


class RightOnBottom(SideEnding):

    pattern = 'P1'
    stem = 'S2'
    relation = 'UNFRAMED'
    transliteration = 'a'

    def draw(self, pen):
        pen.line_forward(pen.mode.width, end_slant=45)
        pen.turn_to(-135)
        pen.move_forward(pen.mode.width * slant45)
        pen.turn_to(0)
        pen.line_forward(2, start_slant=45, end_slant=45)


class DownOnBottom(SideEnding):

    pattern = 'P1'
    stem = 'S3'
    relation = 'UNFRAMED'
    transliteration = 'ae'

    def draw(self, pen):
        pen.line_forward(2 * pen.mode.width, end_slant=45)
        pen.turn_to(-135)
        pen.move_forward(pen.mode.width * slant45)
        pen.turn_to(-90)
        pen.line_forward(2, start_slant=45, end_slant=45)


class HookRightOnBottom(SideEnding):

    pattern = 'P2'
    stem = 'S1'
    relation = 'UNFRAMED'
    transliteration = 'a^'

    def draw(self, pen):
        pen.line_forward(pen.mode.width, end_slant=45)
        pen.turn_to(-135)
        pen.move_forward(pen.mode.width * slant45 / 2)
        hook(pen, 120, -30, 2.5, adjust_inside=15)


class HookLeftOnBottom(SideEnding):

    pattern = 'P2'
    stem = 'S2'
    relation = 'UNFRAMED'
    transliteration = 'o'

    def draw(self, pen):
        pen.line_forward(pen.mode.width, end_slant=45)
        pen.turn_to(-135)
        pen.move_forward(pen.mode.width * slant45 / 2)
        hook(pen, 90, 30, 2.5, adjust_inside=15)


class DiagonalDownRightOnBottom(SideEnding):

    pattern = 'P2'
    stem = 'S3'
    relation = 'UNFRAMED'
    transliteration = 'o^'

    def draw(self, pen):
        pen.line_forward(pen.mode.width, end_slant=45)
        pen.turn_to(-135)
        pen.move_forward(pen.mode.width * slant45 / 2 + pen.mode.width / 2)
        pen.turn_to(-45)
        pen.line_forward(2, start_slant=45, end_slant=90)


class FoldDownHookRight(SideEnding):

    pattern = 'P3'
    stem = 'S1'
    relation = 'UNFRAMED'
    transliteration = 'e'

    def draw(self, pen):
        pen.line_forward(2 * pen.mode.width, end_slant=-45)
        pen.turn_to(-45)
        pen.move_forward(pen.mode.width * slant45 / 2)
        hook(pen, -90, -30, 2.5, adjust_inside=15)


class FoldDownHookLeft(SideEnding):

    pattern = 'P3'
    stem = 'S2'
    relation = 'UNFRAMED'
    transliteration = 'e^'

    def draw(self, pen):
        pen.line_forward(2 * pen.mode.width, end_slant=-45)
        pen.turn_to(-45)
        pen.move_forward(pen.mode.width * slant45 / 2)
        hook(pen, -105, 30, 2.5, adjust_inside=15)


class DiagonalDownLeft(SideEnding):

    pattern = 'P3'
    stem = 'S3'
    relation = 'UNFRAMED'
    transliteration = 'i'

    def draw(self, pen):
        pen.line_forward(pen.mode.width, end_slant=-45)
        pen.turn_to(-45)
        pen.move_forward(pen.mode.width * slant45 / 2 + pen.mode.width / 2)
        pen.turn_to(-135)
        pen.line_forward(2, start_slant=-45, end_slant=90)


class DownOnRight(SideEnding):

    pattern = 'P1'
    stem = 'S1'
    relation = 'FRAMED'
    transliteration = 'i^'

    def draw(self, pen):
        pen.line_forward(pen.mode.width / 2, end_slant=45)
        pen.turn_to(45)
        pen.move_forward(pen.mode.width * slant45)
        pen.turn_to(-90)
        pen.line_forward(2.5, start_slant=45, end_slant=45)


class DiagonalDownRightOnTop(SideEnding):

    pattern = 'P1'
    stem = 'S2'
    relation = 'FRAMED'
    transliteration = 'e:'

    def draw(self, pen):
        pen.line_forward(pen.mode.width / 2, end_slant=45)
        pen.turn_to(45)
        pen.move_forward(pen.mode.width * slant45 / 2 + pen.mode.width / 2)
        pen.turn_to(-45)
        pen.line_to_y(TOP - pen.mode.width, start_slant=45, end_slant=0)


class FoldUp(SideEnding):

    pattern = 'P1'
    stem = 'S3'
    relation = 'FRAMED'
    transliteration = 'u'

    def draw(self, pen):
        pen.line_forward(pen.mode.width / 2, end_slant=45)
        pen.turn_to(45)
        pen.move_forward(pen.mode.width * slant45)
        pen.turn_to(90)
        pen.line_forward(2, start_slant=45, end_slant=45)


class UpOnRight(SideEnding):

    pattern = 'P2'
    stem = 'S1'
    relation = 'FRAMED'
    transliteration = 'u^'

    def draw(self, pen):
        pen.line_forward(pen.mode.width / 2, end_slant=-45)
        pen.turn_to(-45)
        pen.move_forward(pen.mode.width * slant45)
        pen.turn_to(90)
        pen.line_forward(2.5, start_slant=-45, end_slant=-45)


class DiagonalUpRightOnTop(SideEnding):

    pattern = 'P2'
    stem = 'S2'
    relation = 'FRAMED'
    transliteration = 'y'

    def draw(self, pen):
        pen.line_forward(pen.mode.width / 2, end_slant=-45)
        pen.turn_to(-45)
        pen.move_forward(pen.mode.width * slant45 / 2 + pen.mode.width / 2)
        pen.turn_to(45)
        pen.line_to_y(TOP, start_slant=-45, end_slant=0)


class FoldDown(SideEnding):

    pattern = 'P2'
    stem = 'S3'
    relation = 'FRAMED'
    transliteration = 'u:'

    def draw(self, pen):
        pen.line_forward(pen.mode.width / 2, end_slant=-45)
        pen.turn_to(-45)
        pen.move_forward(pen.mode.width * slant45)
        pen.turn_to(-90)
        pen.line_forward(2, start_slant=-45, end_slant=-45)


class FoldUpHookLeft(SideEnding):

    pattern = 'P3'
    stem = 'S1'
    relation = 'FRAMED'
    transliteration = 'o:'

    def draw(self, pen):
        pen.line_forward(pen.mode.width, end_slant=45)
        pen.turn_to(45)
        pen.move_forward(pen.mode.width * slant45 / 2)
        hook(pen, 90, 30, 2.5, adjust_inside=15)


class FoldUpHookRight(SideEnding):

    pattern = 'P3'
    stem = 'S2'
    relation = 'FRAMED'
    transliteration = 'o%'

    def draw(self, pen):
        pen.line_forward(pen.mode.width, end_slant=45)
        pen.turn_to(45)
        pen.move_forward(pen.mode.width * slant45 / 2)
        hook(pen, 105, -30, 2.5, adjust_inside=15)


class DiagonalUpLeft(SideEnding):

    pattern = 'P3'
    stem = 'S3'
    relation = 'FRAMED'
    transliteration = 'i+'

    def draw(self, pen):
        pen.line_forward(pen.mode.width, end_slant=45)
        pen.turn_to(45)
        pen.move_forward(pen.mode.width * slant45 / 2 + pen.mode.width / 2)
        pen.turn_to(135)
        pen.line_forward(2, start_slant=45, end_slant=0)


# Character list.

side_endings = [
    Normal,
    RightOnBottom,
    DownOnBottom,
    HookRightOnBottom,
    HookLeftOnBottom,
    DiagonalDownRightOnBottom,
    FoldDownHookRight,
    FoldDownHookLeft,
    DiagonalDownLeft,
    DownOnRight,
    DiagonalDownRightOnTop,
    FoldUp,
    UpOnRight,
    DiagonalUpRightOnTop,
    FoldDown,
    FoldUpHookLeft,
    FoldUpHookRight,
    DiagonalUpLeft,
]


def make_side_endings_by_psr():
    table = {}
    for se in side_endings:
        key = (se.pattern, se.stem, se.relation)
        table[key] = se
    return table
side_endings_by_psr = make_side_endings_by_psr()


def make_side_endings_by_transliteration():
    table = {}
    for se in side_endings:
        if se.transliteration != '':
            table[se.transliteration] = se
    return table
side_endings_by_transliteration = make_side_endings_by_transliteration()


class SideAll(SideEnding):
    """
    A debug ending showing every one of the endings superimposed.
    """
    def draw(self, pen):
        start_position = pen.position
        for side_ending_class in side_endings:
            if side_ending_class == SideAll:
                continue
            side_ending = side_ending_class(
                self.character,
                self.flipped,
            )
            pen.move_to(start_position)
            pen.turn_to(0)
            side_ending.draw(pen)
        pen.move_to(start_position)
