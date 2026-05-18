from dataclasses import dataclass

from py_docx_creator.core.style.paragraph_style import ParagraphStyle
from py_docx_creator.enums.enum_align_paragraph import AlignParagraph


@dataclass
class DefaultHeaderParagraphStyle(ParagraphStyle):
    """Стиль параграфа для текста заголовков по умолчанию"""
    alignment: AlignParagraph = AlignParagraph.CENTER.value
    left_indent: float = -0.5
    right_indent: float = -0.5

@dataclass
class DefaultMainParagraphStyle(ParagraphStyle):
    """Стиль параграфа для основного текста по умолчанию"""
    alignment: AlignParagraph | None = AlignParagraph.JUSTIFY.value
    space_after: float | None = 0.0
    left_indent: float | None = -0.5
    right_indent: float | None = -0.5
    line_spacing: float | None = 1.15
    first_line_indent: float | None = 20