from enum import Enum

from docx.enum.text import WD_ALIGN_PARAGRAPH


class AlignParagraph(Enum):
    """
    Перечень доступных выравниваний для параграфа

    Attributes:
        LEFT (WD_ALIGN_PARAGRAPH): Выравнивание по левому краю.
        CENTER (WD_ALIGN_PARAGRAPH): Выравнивание по центру.
        RIGHT (WD_ALIGN_PARAGRAPH): Выравнивание по правому краю.
        JUSTIFY (WD_ALIGN_PARAGRAPH): Выравнивание по ширине.
        DISTRIBUTE (WD_ALIGN_PARAGRAPH): Распределенное выравнивание.
        JUSTIFY_MED (WD_ALIGN_PARAGRAPH): По ширине со средним интервалом.
        JUSTIFY_HI (WD_ALIGN_PARAGRAPH): По ширине с большим интервалом.
        JUSTIFY_LOW (WD_ALIGN_PARAGRAPH): По ширине с малым интервалом.
        THAI_JUSTIFY (WD_ALIGN_PARAGRAPH): Тайское выравнивание по ширине.
    """
    LEFT: WD_ALIGN_PARAGRAPH = WD_ALIGN_PARAGRAPH.LEFT
    CENTER: WD_ALIGN_PARAGRAPH = WD_ALIGN_PARAGRAPH.CENTER
    RIGHT: WD_ALIGN_PARAGRAPH = WD_ALIGN_PARAGRAPH.RIGHT
    JUSTIFY: WD_ALIGN_PARAGRAPH = WD_ALIGN_PARAGRAPH.JUSTIFY
    DISTRIBUTE: WD_ALIGN_PARAGRAPH = WD_ALIGN_PARAGRAPH.DISTRIBUTE
    JUSTIFY_MED: WD_ALIGN_PARAGRAPH = WD_ALIGN_PARAGRAPH.JUSTIFY_MED
    JUSTIFY_HI: WD_ALIGN_PARAGRAPH = WD_ALIGN_PARAGRAPH.JUSTIFY_HI
    JUSTIFY_LOW: WD_ALIGN_PARAGRAPH = WD_ALIGN_PARAGRAPH.JUSTIFY_LOW
    THAI_JUSTIFY: WD_ALIGN_PARAGRAPH = WD_ALIGN_PARAGRAPH.THAI_JUSTIFY