from canoepaddle import *
from ithkuil.writing.consonant import consonants
from ithkuil.writing.bottom_ending import bottom_endings
from ithkuil.writing.side_ending import side_endings
from ithkuil.writing.typeset import typeset, draw_letter

#DEBUG redefinition of parts lists for testing.
import ithkuil.writing.consonant as cons
#consonants = [cons.CHacek, cons.LCedilla, cons.Q, cons.G, cons.D, cons.T, cons.K, cons.RHacek, cons.L, cons.J]
#consonants = [cons.LCedilla, cons.D, cons.T, cons.L]
#consonants = consonants + [cons.VerticalBar, cons.SideEndingStub]
#consonants = consonants[-6:]
consonants = [cons.BottomEndingStraightStub]
#consonants = [c for c in consonants if not c.mirrored_x]
import ithkuil.writing.side_ending as se
#side_endings = [se.Normal, se.SideAll]
side_endings = [se.Normal]
#side_endings = side_endings[3:5]
import ithkuil.writing.bottom_ending as be
#bottom_endings = [be.Normal]
#bottom_endings = [be.Normal, be.BottomAll]
#bottom_endings = [be.Acute, be.DoubleBend]
#bottom_endings = bottom_endings[29:]

mode = StrokeMode(1.0)
#mode = OutlineMode(1.0, 0.1)
#mode = StrokeMode(0.6)
#mode = OutlineMode(0.6, 0.1)
#mode = StrokeMode(1.2)

letters = []
seen = set()


def add_letter(c, s, b):
    if (c, s, b) in seen:
        return
    else:
        seen.add((c, s, b))
    letters.append(c(s, b))

for bottom_ending_class in bottom_endings:
    for consonant_class in consonants:
        add_letter(consonant_class, side_endings[0], bottom_ending_class)
for side_ending_class in side_endings:
    for consonant_class in consonants:
        add_letter(consonant_class, side_ending_class, bottom_endings[0])

papers = [
    draw_letter(
        letter,
        mode,
        fixed_width=10.0,
        show_template=True,
        #show_bounds=True,
        #fuse=False,
    )
    for letter in letters
]
page = typeset(
    papers,
    letter_spacing=2.0,
    letters_per_line=10,
    #line_width=100,
    line_spacing=3.0,
    page_margin=5.0,
)
print(page.format_svg(4, resolution=30))
#page.format_svg()
