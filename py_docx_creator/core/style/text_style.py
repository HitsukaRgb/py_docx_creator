from copy import deepcopy
from dataclasses import dataclass

from py_docx_creator.abstract_classes.abc_style_dataclasses.abc_text_style import ABCTextStyle

@dataclass
class TextStyle(ABCTextStyle):
    """
    Стиль текста.

    Attributes:
        size ( float | None): Размер шрифта
        name ( str | None): Наименование шрифта
        bold ( bool | None): Жирное начертание шрифта
        italic ( bool | None): Курсивное начертание шрифта
        underline ( bool | None): Подчеркнутое начертание шрифта
    """

    size: float | None = None  # размер шрифта
    name: str | None = None  # наименование шрифта
    bold: bool | None = None  # жирное начертание шрифта
    italic: bool | None = None  # курсивное начертание шрифта
    underline: bool | None = None  # подчеркнутое начертание шрифта

