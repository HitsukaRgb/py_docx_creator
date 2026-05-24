from dataclasses import dataclass

from py_docx_creator.core.style.text_style import TextStyle
from py_docx_creator.enums.enum_font_names import FontNames


@dataclass
class DefaultMainTextStyle(TextStyle):
    """
    Стиль текста для заголовков по умолчанию

    Attributes:
        size ( float | None): Размер шрифта = 10.0
        name ( str | None): Наименование шрифта = TIMES_NEW_ROMAN
        bold ( bool | None): Жирное начертание шрифта = False
    """

    size: float = 10.0
    name: str = FontNames.TIMES_NEW_ROMAN
    bold: bool = False


@dataclass
class DefaultHeaderTextStyle(TextStyle):
    """
    Стиль основного текста по умолчанию

    Attributes:
        size ( float | None): Размер шрифта = 12.0
        name ( str | None): Наименование шрифта = TIMES_NEW_ROMAN
        bold ( bool | None): Жирное начертание шрифта = True
    """

    size: float = 12.0
    name: str = FontNames.TIMES_NEW_ROMAN
    bold: bool = True
