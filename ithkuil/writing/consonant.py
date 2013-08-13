from .common import (
    Character,
    WIDTH,
    TOP,
    MIDDLE,
    BOTTOM,
    bevel_distance,
    slant45,
    slant60,
    slant75,
    flip_consonant_horizontal as flip,
    flip_ending_horizontal,
)
from canoepaddle import Pen, Paper

import sys


class ConsonantCharacter(Character):

    bottom_type = NotImplemented  # 'straight' or 'slanted'
    bottom_orientation = NotImplemented  # 'left' or 'right'
    side_flipped = NotImplemented  # True for 45 angle, False for -45 angle.
    bottom_heading = None  # None or in the range (-90, 0].

    def __init__(self, side_ending_class, bottom_ending_class):
        self.side_ending = side_ending_class(self)
        if self.bottom_slanted() and self.bottom_orientation == 'left':
            bottom_ending_class = flip_ending_horizontal(bottom_ending_class)
        self.bottom_ending = bottom_ending_class(self)

    def __str__(self):
        return 'consonant.{}({}, {})'.format(
            self.__class__.__name__,
            self.side_ending,
            self.bottom_ending,
        )

    def bottom_straight(self):
        return self.bottom_type == 'straight'

    def bottom_slanted(self):
        return self.bottom_type == 'slanted'

    def draw_character(self, mode):
        paper = Paper()

        # When drawing the body of the consonant, subclasses will start
        # where the side ending is, and end where the bottom ending is.
        pen = Pen()
        pen.set_mode(mode)
        pen.move_to((0, TOP - WIDTH / 2))
        side_ending_position = pen.position
        self.draw(pen)
        bottom_ending_position = pen.position
        bottom_ending_heading = pen.heading
        paper.merge(pen.paper)

        # Draw the side ending.
        pen = Pen()
        pen.set_mode(mode)
        pen.move_to(side_ending_position)
        pen.turn_to(0)
        self.side_ending.draw(pen)
        paper.merge(pen.paper)

        # Draw the bottom ending.
        pen = Pen()
        pen.set_mode(mode)
        pen.move_to(bottom_ending_position)
        if self.bottom_heading is not None:
            pen.turn_to(self.bottom_heading)
        else:
            pen.turn_to(bottom_ending_heading)
        self.bottom_ending.draw(pen)
        if self.bottom_orientation == 'left':
            pen.paper.mirror_x(bottom_ending_position.x)
        paper.merge(pen.paper)

        paper.join_paths()
        paper.fuse_paths()

        return paper


class P(ConsonantCharacter):

    bottom_type = 'straight'
    bottom_orientation = 'right'
    side_flipped = True

    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(3.5)

        pen.turn_to(-45)
        pen.line_to_y(MIDDLE + WIDTH)
        pen.turn_to(-90)
        pen.line_to_y(MIDDLE)


class T(ConsonantCharacter):

    bottom_type = 'straight'
    bottom_orientation = 'right'
    side_flipped = False

    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(4)
        pen.turn_left(90)
        pen.line_to_y(MIDDLE)


class K(ConsonantCharacter):

    bottom_type = 'slanted'
    bottom_orientation = 'right'
    side_flipped = False

    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(4.5)
        pen.turn_to(-60)
        pen.line_to_y(MIDDLE)


class Q(ConsonantCharacter):

    bottom_type = 'slanted'
    bottom_orientation = 'left'
    bottom_heading = -60
    side_flipped = False

    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(4.5)
        pen.turn_to(-45)
        pen.line_to_y(MIDDLE, end_angle=0)
        pen.turn_to(180)
        pen.move_forward(pen.last_slant_width() / 2 + WIDTH * slant60 / 2)
        pen.turn_left(60)
        pen.line_forward(WIDTH, start_angle=0)


class C(ConsonantCharacter):

    bottom_type = 'straight'
    bottom_orientation = 'right'
    side_flipped = False

    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(5)
        pen.turn_to(-90)
        pen.line_to_y(MIDDLE + WIDTH / 2)
        pen.turn_to(0)
        pen.line_forward(3)
        pen.turn_to(-90)
        pen.line_forward(WIDTH)


class CHacek(ConsonantCharacter):

    bottom_type = 'slanted'
    bottom_orientation = 'left'
    bottom_heading = -45
    side_flipped = False

    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(5)
        pen.turn_to(-90)
        pen.line_to_y(MIDDLE + WIDTH / 2)
        pen.turn_to(0)
        pen.line_forward(4)
        pen.turn_to(-135)
        pen.line_forward(1.5 * WIDTH)


class L(ConsonantCharacter):
    bottom_type = 'slanted'
    bottom_orientation = 'right'
    side_flipped = False
    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(5.5 + self.side_ending.offset_x(), start_angle=self.side_ending.angle())
        pen.turn_to(-90)
        pen.line_to_y(MIDDLE)
        pen.turn_to(-45)
        pen.line_to_y(
            BOTTOM + self.bottom_ending.offset_y(pen),
            end_angle=self.bottom_ending.angle(),
        )


class L(ConsonantCharacter):
    bottom_type = 'slanted'
    bottom_orientation = 'right'
    side_flipped = False
    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(5.5 + self.side_ending.offset_x(), start_angle=self.side_ending.angle())
        pen.turn_to(-90)
        pen.line_to_y(MIDDLE)
        pen.turn_to(-45)
        pen.line_to_y(
            BOTTOM + self.bottom_ending.offset_y(pen),
            end_angle=self.bottom_ending.angle(),
        )


class H(ConsonantCharacter):
    bottom_type = 'straight'
    bottom_orientation = 'left'
    side_flipped = False
    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(
            4 + self.side_ending.offset_x(),
            start_angle=self.side_ending.angle(),
            end_angle=45,
        )
        pen.turn_left(45)
        pen.move_forward(pen.last_slant_width() / 2 + WIDTH / 2)
        pen.turn_to(-45)
        pen.line_to_y(MIDDLE)
        pen.turn_to(-90)
        pen.line_to_y(
            BOTTOM + self.bottom_ending.offset_y(pen),
            end_angle=self.bottom_ending.angle(),
        )


class PStop(ConsonantCharacter):
    bottom_type = 'straight'
    bottom_orientation = 'left'
    side_flipped = False
    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(
            4.5 + self.side_ending.offset_x(),
            start_angle=self.side_ending.angle(),
        )
        pen.turn_to(-60)
        pen.line_to_y(MIDDLE - pen.last_slant_width() / slant45 / 2, end_angle=45)
        pen.turn_to(45)
        pen.move_forward(pen.last_slant_width() / 2 + WIDTH * slant45 / 2)
        pen.turn_to(-90)
        pen.line_to_y(
            BOTTOM + self.bottom_ending.offset_y(pen),
            start_angle=45,
            end_angle=self.bottom_ending.angle(),
        )


class TStop(ConsonantCharacter):
    bottom_type = 'straight'
    bottom_orientation = 'left'
    side_flipped = True
    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(
            5 + self.side_ending.offset_x(),
            start_angle=self.side_ending.angle(),
            end_angle=-45,
        )
        pen.turn_to(-45)
        pen.move_forward(WIDTH * slant45)
        pen.turn_to(-90)
        pen.line_to_y(
            BOTTOM + self.bottom_ending.offset_y(pen),
            start_angle=-45,
            end_angle=self.bottom_ending.angle(),
        )


class KStop(ConsonantCharacter):
    bottom_type = 'straight'
    bottom_orientation = 'left'
    side_flipped = True
    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(
            5 + self.side_ending.offset_x(),
            start_angle=self.side_ending.angle(),
            end_angle=-45,
        )
        pen.turn_to(-45)
        pen.move_forward(WIDTH * slant45)
        pen.turn_to(180)
        pen.line_forward(WIDTH / 2 + bevel_distance / 2, start_angle=-45)
        pen.turn_left(45)
        pen.line_forward(bevel_distance)
        pen.turn_to(-90)
        pen.line_to_y(
            BOTTOM + self.bottom_ending.offset_y(pen),
            end_angle=self.bottom_ending.angle(),
        )


class QStop(ConsonantCharacter):
    bottom_type = 'slanted'
    bottom_orientation = 'right'
    side_flipped = False
    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(
            5 + self.side_ending.offset_x(),
            start_angle=self.side_ending.angle(),
        )
        pen.turn_to(-60)
        pen.line_to_y(MIDDLE, end_angle=0)
        pen.turn_to(180)
        pen.move_forward(WIDTH * slant60)
        pen.turn_to(-60)
        pen.line_to_y(
            BOTTOM + self.bottom_ending.offset_y(pen),
            start_angle=0,
            end_angle=self.bottom_ending.angle(),
        )


class CStop(ConsonantCharacter):
    bottom_type = 'slanted'
    bottom_orientation = 'right'
    side_flipped = False
    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(
            5 + self.side_ending.offset_x(),
            start_angle=self.side_ending.angle(),
        )
        pen.turn_to(-90)
        pen.line_to_y(MIDDLE + WIDTH / 2, end_angle=45)
        pen.turn_to(45)
        pen.move_forward(WIDTH * slant45 / 2 + WIDTH * slant75 / 2)
        pen.turn_to(-60)
        pen.line_to_y(
            BOTTOM + self.bottom_ending.offset_y(pen),
            start_angle=45,
            end_angle=self.bottom_ending.angle(),
        )


class CHacekStop(ConsonantCharacter):
    bottom_type = 'slanted'
    bottom_orientation = 'left'
    side_flipped = True
    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(
            5 + self.side_ending.offset_x(),
            start_angle=self.side_ending.angle(),
            end_angle=-45,
        )
        pen.turn_to(-45)
        pen.move_forward(WIDTH * slant45)
        pen.turn_to(-90)
        pen.line_to_y(MIDDLE - WIDTH / 2, start_angle=-45)
        pen.turn_to(0)
        pen.line_forward(2)
        pen.turn_to(-135)
        pen.line_to_y(
            BOTTOM + self.bottom_ending.offset_y(pen),
            start_angle=-45,
            end_angle=self.bottom_ending.angle(),
        )


class F(ConsonantCharacter):
    bottom_type = 'straight'
    bottom_orientation = 'left'
    side_flipped = True
    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(
            4.5 + self.side_ending.offset_x(),
            start_angle=self.side_ending.angle(),
        )
        pen.turn_to(-45)
        pen.line_to_y(TOP - 2 * WIDTH, end_angle=0)
        pen.turn_to(180)
        pen.move_forward(WIDTH * slant45 / 2 + WIDTH / 2)
        pen.turn_to(-90)
        pen.line_to_y(
            BOTTOM + self.bottom_ending.offset_y(pen),
            start_angle=0,
            end_angle=self.bottom_ending.angle(),
        )


class TCedilla(ConsonantCharacter):
    bottom_type = 'straight'
    bottom_orientation = 'left'
    side_flipped = False
    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(
            5 + self.side_ending.offset_x(),
            start_angle=self.side_ending.angle(),
        )
        pen.turn_to(-90)
        pen.line_to_y(MIDDLE - WIDTH / 2, end_angle=45)
        pen.turn_to(45)
        pen.move_forward(WIDTH * slant45)
        pen.turn_to(-90)
        pen.line_to_y(
            BOTTOM + self.bottom_ending.offset_y(pen),
            start_angle=45,
            end_angle=self.bottom_ending.angle(),
        )


class X(ConsonantCharacter):
    bottom_type = 'slanted'
    bottom_orientation = 'left'
    side_flipped = False
    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(
            5.5 + self.side_ending.offset_x(),
            start_angle=self.side_ending.angle(),
        )
        pen.turn_to(-60)
        pen.line_to_y(MIDDLE, end_angle=0)
        pen.turn_to(0)
        pen.move_forward(WIDTH * slant60)
        pen.turn_to(-120)
        pen.line_to_y(
            BOTTOM + self.bottom_ending.offset_y(pen),
            start_angle=0,
            end_angle=self.bottom_ending.angle(),
        )


class S(ConsonantCharacter):
    bottom_type = 'straight'
    bottom_orientation = 'left'
    side_flipped = False
    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(
            5 + self.side_ending.offset_x(),
            start_angle=self.side_ending.angle(),
        )
        pen.turn_to(-90)
        pen.line_to_y(MIDDLE - WIDTH / 2, end_angle=45)
        pen.turn_to(45)
        pen.move_forward(WIDTH * slant45)
        pen.turn_to(0)
        pen.line_forward(WIDTH / 2 + 1 + bevel_distance / 2, start_angle=45)
        pen.turn_right(45)
        pen.line_forward(bevel_distance)
        pen.turn_to(-90)
        pen.line_to_y(
            BOTTOM + self.bottom_ending.offset_y(pen),
            end_angle=self.bottom_ending.angle(),
        )


class SHacek(ConsonantCharacter):
    bottom_type = 'straight'
    bottom_orientation = 'left'
    side_flipped = True
    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(
            5 + self.side_ending.offset_x(),
            start_angle=self.side_ending.angle(),
            end_angle=-45,
        )
        pen.turn_to(-45)
        pen.move_forward(WIDTH * slant45)
        pen.turn_to(-90)
        pen.line_to_y(MIDDLE - WIDTH / 2, start_angle=-45)
        pen.turn_to(0)
        pen.line_forward(2)
        pen.turn_to(-90)
        pen.line_to_y(
            BOTTOM + self.bottom_ending.offset_y(pen),
            start_angle=-45,
            end_angle=self.bottom_ending.angle(),
        )


class R(ConsonantCharacter):
    bottom_type = 'straight'
    bottom_orientation = 'left'
    side_flipped = False
    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(
            5.5 + self.side_ending.offset_x(),
            start_angle=self.side_ending.angle(),
        )
        pen.turn_to(-45)
        pen.line_to_y(MIDDLE + WIDTH / 2)
        pen.turn_to(180)
        pen.line_forward(3.5)
        pen.turn_to(-90)
        pen.line_to_y(
            BOTTOM + self.bottom_ending.offset_y(pen),
            end_angle=self.bottom_ending.angle(),
        )


class W(ConsonantCharacter):
    bottom_type = 'straight'
    bottom_orientation = 'left'
    side_flipped = False
    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(
            4.5 + self.side_ending.offset_x(),
            start_angle=self.side_ending.angle(),
            end_angle=45,
        )
        pen.turn_left(45)
        pen.move_forward(WIDTH * slant45)
        pen.turn_to(-90)
        pen.line_to_y(
            BOTTOM + self.bottom_ending.offset_y(pen),
            end_angle=self.bottom_ending.angle(),
            start_angle=45,
        )


class L(ConsonantCharacter):
    bottom_type = 'slanted'
    bottom_orientation = 'right'
    side_flipped = False
    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(
            5 + self.side_ending.offset_x(),
            start_angle=self.side_ending.angle(),
        )
        pen.turn_to(-90)
        pen.line_to_y(MIDDLE)
        pen.turn_to(-45)
        pen.line_to_y(
            BOTTOM + self.bottom_ending.offset_y(pen),
            end_angle=self.bottom_ending.angle(),
        )


class M(ConsonantCharacter):
    bottom_type = 'slanted'
    bottom_orientation = 'left'
    side_flipped = False
    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(
            5.5 + self.side_ending.offset_x(),
            start_angle=self.side_ending.angle(),
        )
        pen.turn_to(-45)
        pen.line_to_y(MIDDLE)
        pen.turn_to(-120)
        pen.line_to_y(
            BOTTOM + self.bottom_ending.offset_y(pen),
            end_angle=self.bottom_ending.angle(),
        )


class NHacek(ConsonantCharacter):
    bottom_type = 'slanted'
    bottom_orientation = 'right'
    side_flipped = True
    def draw(self, pen):
        pen.turn_to(180)
        pen.line_forward(
            5 + self.side_ending.offset_x(),
            start_angle=self.side_ending.angle(),
            end_angle=-45,
        )
        pen.turn_to(-45)
        pen.move_forward(WIDTH * slant45)
        pen.turn_to(-90)
        pen.line_to_y(MIDDLE - WIDTH / 2, start_angle=-45)
        pen.turn_to(-45)
        pen.line_to_y(
            BOTTOM + self.bottom_ending.offset_y(pen),
            end_angle=self.bottom_ending.angle(),
        )


B = flip(P)
D = flip(T)
G = flip(K)
RHacek = flip(Q)
ZDot = flip(C)
J = flip(CHacek)
Stop = flip(H)
PH = flip(PStop)
TH = flip(TStop)
KH = flip(KStop)
QH = flip(QStop)
CH = flip(CStop)
CHacekH = flip(CHacekStop)
V = flip(F)
Dh = flip(TCedilla)
Xh = flip(X)
Z = flip(S)
ZHacek = flip(SHacek)
Y = flip(W)
LCedilla = flip(L)
CCedilla = flip(R)
N = flip(M)
TLCedilla = flip(NHacek)


consonants = [
    P,
    T,
    K,
    Q,
    C,
    CHacek,
    B,
    D,
    G,
    Stop,
    ZDot,
    J,
    PStop,
    TStop,
    KStop,
    QStop,
    CStop,
    CHacekStop,
    PH,
    TH,
    KH,
    QH,
    CH,
    CHacekH,
    F,
    TCedilla,
    X,
    Xh,
    S,
    SHacek,
    V,
    Dh,
    H,
    RHacek,
    Z,
    ZHacek,
    W,
    L,
    Y,
    LCedilla,
    R,
    CCedilla,
    M,
    N,
    NHacek,
    TLCedilla,
]
