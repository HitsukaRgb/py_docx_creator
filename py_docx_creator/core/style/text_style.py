from copy import deepcopy
from dataclasses import dataclass

from py_docx_creator.abstract_classes.abc_style_dataclasses.abc_text_style import ABCTextStyle

@dataclass
class TextStyle(ABCTextStyle):
    """
    Стиль текста.

    Атрибуты:
        size ( float | None): # размер шрифта
        name ( str | None): # наименование шрифта
        bold ( bool | None): # жирное начертание шрифта
        italic ( bool | None): # курсивное начертание шрифта
        underline ( bool | None): # подчеркнутое начертание шрифта
    """

    size: float | None = None  # размер шрифта
    name: str | None = None  # наименование шрифта
    bold: bool | None = None  # жирное начертание шрифта
    italic: bool | None = None  # курсивное начертание шрифта
    underline: bool | None = None  # подчеркнутое начертание шрифта

