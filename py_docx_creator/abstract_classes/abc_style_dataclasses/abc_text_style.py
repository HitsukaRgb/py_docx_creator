from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class ABCTextStyle(ABC):
    """
    Стиль текста.

    Атрибуты:
        size ( float | None): # размер шрифта
        name ( str | None): # наименование шрифта
        bold ( bool | None): # жирное начертание шрифта
        italic ( bool | None): # курсивное начертание шрифта
        underline ( bool | None): # подчеркнутое начертание шрифта
    """

    size: float | None  # размер шрифта
    name: str | None  # наименование шрифта
    bold: bool | None  # жирное начертание шрифта
    italic: bool | None  # курсивное начертание шрифта
    underline: bool | None  # подчеркнутое начертание шрифта
