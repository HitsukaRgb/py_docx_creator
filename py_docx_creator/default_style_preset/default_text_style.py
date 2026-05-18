from dataclasses import dataclass

from py_docx_creator.core.style.text_style import TextStyle
from py_docx_creator.enums.enum_font_names import FontNames


@dataclass
class DefaultMainTextStyle(TextStyle):
    """Стиль текста для заголовков по умолчанию"""
    size: float = 10.0
    name: str = FontNames.TimesNewRoman.value
    bold: bool = False


@dataclass
class DefaultHeaderTextStyle(TextStyle):
    """Стиль основного текста по умолчанию"""
    size: float = 12.0
    name: str = FontNames.TimesNewRoman.value
    bold: bool = True

