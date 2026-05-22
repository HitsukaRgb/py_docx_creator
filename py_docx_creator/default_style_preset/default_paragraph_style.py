from dataclasses import dataclass

from py_docx_creator.core.style.paragraph_style import ParagraphStyle
from py_docx_creator.enums.enum_align_paragraph import AlignParagraph


@dataclass
class DefaultHeaderParagraphStyle(ParagraphStyle):
    """
    Стиль параграфа для текста заголовков по умолчанию

    Attributes:
        alignment (AlignParagraph | None): Выравнивание текста = CENTER
        left_indent (float | None): Отступ от левого края страницы = -0.5
        right_indent (float | None): Отступ от правого края страницы = -0.5
    """
    alignment: AlignParagraph = AlignParagraph.CENTER
    left_indent: float = -0.5
    right_indent: float = -0.5


@dataclass
class DefaultMainParagraphStyle(ParagraphStyle):
    """
    Стиль параграфа для основного текста по умолчанию

    Attributes:
        alignment (AlignParagraph | None): Выравнивание текста = JUSTIFY
        space_after (float | None): Отступ после параграфа = 0.0
        left_indent (float | None): Отступ от левого края страницы = -0.5
        right_indent (float | None): Отступ от правого края страницы = -0.5
        line_spacing (float | None): Межстрочный интервал = 1.15
        first_line_indent (float | None): Отступ первой строки (красная строка) = 20
    """
    alignment: AlignParagraph | None = AlignParagraph.JUSTIFY
    space_after: float | None = 0.0
    left_indent: float | None = -0.5
    right_indent: float | None = -0.5
    line_spacing: float | None = 1.15
    first_line_indent: float | None = 20
