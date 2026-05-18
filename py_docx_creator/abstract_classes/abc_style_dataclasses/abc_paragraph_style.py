from abc import ABC
from dataclasses import dataclass

from py_docx_creator.enums.enum_align_paragraph import AlignParagraph


@dataclass
class ABCParagraphStyle(ABC):
    """
    Стиль форматирования параграфа.

    Атрибуты:
        alignment (AlignParagraph | None): Выравнивание текста (влево, по центру, по ширине и т.п.).
        space_after (float | None): Отступ после параграфа.
        space_before (float | None): Отступ перед параграфом.
        left_indent (float | None): Отступ от левого края страницы.
        right_indent (float | None): Отступ от правого края страницы.
        line_spacing (float | None): Межстрочный интервал.
        first_line_indent (float | None): Отступ первой строки (красная строка).
        page_break_before (bool | None): Разрыв страницы перед параграфом.
    """
    alignment: AlignParagraph | None  # выравнивание
    space_after: float | None  # отступ до параграфа
    space_before: float | None  # отступ после параграфа
    left_indent: float | None  # отступ от левого края
    right_indent: float | None  # отступ от правого края
    line_spacing: float | None  # межстрочный интервал
    first_line_indent: float | None  # отступ красной строки
    page_break_before: bool | None  # разрыв страницы перед параграфом