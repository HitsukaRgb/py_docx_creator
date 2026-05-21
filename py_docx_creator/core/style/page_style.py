from dataclasses import dataclass

from py_docx_creator.abstract_classes.abc_style_dataclasses.abc_page_style import ABCPageStyle


@dataclass
class PageStyle(ABCPageStyle):
    """
    Стиль страницы.

    Attributes:
        top_margin ( float | None): Отступ сверху
        bottom_margin ( float | None): Отступ снизу
        left_margin ( float | None): Отступ слева
        right_margin ( float | None): Отступ справа
    """

    top_margin: float | None = None
    bottom_margin: float | None = None
    left_margin: float | None = None
    right_margin: float | None = None