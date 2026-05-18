from dataclasses import dataclass

from py_docx_creator.core.style.page_style import PageStyle


@dataclass
class DefaultPageStyle(PageStyle):
    """Формат страницы по умолчанию"""
    top_margin: float | None = 15.0
    bottom_margin: float | None = 10.0
    left_margin: float | None = 75.0
    right_margin: float | None = 75.0