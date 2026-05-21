from abc import ABC
from dataclasses import dataclass


@dataclass
class ABCPageStyle(ABC):
    """
    Стиль страницы.

    Attributes:
        top_margin ( float | None): Отступ сверху
        bottom_margin ( float | None): Отступ снизу
        left_margin ( float | None): Отступ слева
        right_margin ( float | None): Отступ справа
    """

    top_margin: float | None  # отступ сверху
    bottom_margin: float | None  # отступ снизу
    left_margin: float | None  # отступ слева
    right_margin: float | None  # отступ справа
