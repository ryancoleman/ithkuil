# TODO: please refactor canoepaddle .text
# TODO: template color doesn't match between this and bottom ending chart
from canoepaddle import Pen, StrokeOutlineMode

from ithkuil.writing.primary import primary_characters
from ithkuil.writing.typeset import draw_letter, typeset
import ithkuil.writing.bottom_ending as be

font = 'Caudex'
font_size = 8
red = '#d6041a'
black = '#260003'
gray = '#233042'
mode = StrokeOutlineMode(1.0, 0.2, red, black)

papers = []
for primary_class in primary_characters:
    letter = primary_class(be.Normal, be.Normal, mode)
    letter_paper = draw_letter(
        letter,
        fixed_width=30.0,
        show_template=True,
        fuse=False,
    )
    letter_paper.translate((5, 0), bounds=False)

    p = Pen()
    p.move_to((-8, 3))
    p.text(
        letter.case,
        6.0,
        'Caudex',
        '#233042',
        centered=True,
    )
    p.move_to((-8, -3))
    p.text(
        letter.pronunciation,
        6.0,
        'Caudex',
        '#233042',
        centered=True,
    )
    letter_paper.merge(p.paper)
    papers.append(letter_paper)

page = typeset(
    papers,
    letter_spacing=1.0,
    letters_per_line=6,
    line_spacing=3.5,
    page_margin=5.0,
)

print(page.format_svg(4, resolution=1000 / page.bounds().width))
