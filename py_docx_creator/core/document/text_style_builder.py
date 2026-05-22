from typing import Self

from py_docx_creator.abstract_classes.abc_document.abc_text_style_builder import ABCTextStyleBuilder
from py_docx_creator.core.style.text_style import TextStyle


class TextStyleBuilder(ABCTextStyleBuilder):
    _size: float | None = None
    _name: str | None = None
    _bold: bool | None = None
    _italic: bool | None = None
    _underline: bool | None = None

    def size(self, size: float | None) -> Self:
        self._size = size
        return self

    def name(self, name: str | None) -> Self:
        self._name = name
        return self

    def bold(self, bold: bool | None) -> Self:
        self._bold = bold
        return self

    def italic(self, italic: bool | None) -> Self:
        self._italic = italic
        return self

    def underline(self, underline: bool | None) -> Self:
        self._underline = underline
        return self

    @property
    def text_style(self):
        return TextStyle(
            size=self._size,
            name=self._name,
            bold=self._bold,
            italic=self._italic,
            underline=self._underline,
        )
