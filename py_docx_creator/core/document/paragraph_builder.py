from typing import Self

from py_docx_creator.abstract_classes.abc_document.abc_paragraph_builder import ABCParagraphBuilder
from py_docx_creator.core.style.paragraph_style import ParagraphStyle
from py_docx_creator.enums.enum_align_paragraph import AlignParagraph


class ParagraphBuilder(ABCParagraphBuilder):
    _alignment: AlignParagraph | None = None
    _space_after: float | None = None
    _space_before: float | None = None
    _left_indent: float | None = None
    _right_indent: float | None = None
    _line_spacing: float | None = None
    _first_line_indent: float | None = None
    _page_break_before: bool | None = None

    @property
    def paragraph_style(self) -> ParagraphStyle:
        return ParagraphStyle(
            alignment=self._alignment,
            space_after=self._space_after,
            space_before=self._space_before,
            left_indent=self._left_indent,
            right_indent=self._right_indent,
            line_spacing=self._line_spacing,
            first_line_indent=self._first_line_indent,
            page_break_before=self._page_break_before,
        )

    def alignment(self, alignment: AlignParagraph | None) -> Self:
        self._alignment = alignment
        return self

    def space_after(self, space_after: float | None) -> Self:
        self._space_after = space_after
        return self

    def space_before(self, space_before: float | None) -> Self:
        self._space_before = space_before
        return self

    def left_indent(self, left_indent: float | None) -> Self:
        self._left_indent = left_indent
        return self

    def right_indent(self, right_indent: float | None) -> Self:
        self._right_indent = right_indent
        return self

    def line_spacing(self, line_spacing: float | None) -> Self:
        self._line_spacing = line_spacing
        return self

    def first_line_indent(self, first_line_indent: float | None) -> Self:
        self._first_line_indent = first_line_indent
        return self

    def page_break_before(self, page_break_before: bool | None) -> Self:
        self._page_break_before = page_break_before
        return self
