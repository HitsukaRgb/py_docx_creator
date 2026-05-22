from abc import ABC
from dataclasses import dataclass


@dataclass
class ABCTextStyle(ABC):
    """
    Стиль текста.

    Attributes:
        size ( float | None): Размер шрифта
        name ( str | None): Наименование шрифта
        bold ( bool | None): Жирное начертание шрифта
        italic ( bool | None): Курсивное начертание шрифта
        underline ( bool | None): Подчеркнутое начертание шрифта
    """

    size: float | None
    name: str | None
    bold: bool | None
    italic: bool | None
    underline: bool | None
