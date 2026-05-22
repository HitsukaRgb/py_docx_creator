from dataclasses import fields
from typing import Any

from docx.shared import Pt, Inches
from docx.styles.styles import Styles
from docx.text.paragraph import Paragraph
from docx.text.run import Run

from py_docx_creator.abstract_classes.abc_document.abc_document import ABCDocument
from py_docx_creator.abstract_classes.abc_document.abc_document_style import ABCDocumentStyle
from docx import Document as DocxDocument  # alias


class DocumentStyle(ABCDocumentStyle):
    _document_style: str = None

    @property
    def document_style(self) -> str | None:
        """Стиль документа"""
        return self._document_style

    @document_style.setter
    def document_style(self, value: str) -> None:
        """Стиль документа"""
        self._document_style = value

    def get_document_style(self, document: DocxDocument) -> Styles:
        return document.style[f"{self.document_style}"]

    @staticmethod
    def apply_style(target: ABCDocument | Run | Paragraph, style: Any):
        if isinstance(target, ABCDocument):
            for section in target.document.sections:
                for field in fields(style):
                    value = getattr(style, field.name)
                    if value is not None:
                        # проверка необходимости преобразования типа данных
                        if field.name in ("top_margin", "bottom_margin", "left_margin", "right_margin"):
                            value = Pt(value)
                        setattr(section, field.name, value)
        elif isinstance(target, Run):
            for field in fields(style):
                value = getattr(style, field.name)
                if value is not None:

                    # проверка необходимости преобразования типа данных
                    if field.name in ("size",):
                        value = Pt(value)
                    elif field.name in ("name",):
                        # Получение значения из Enum для названия шрифта
                        value = value.value
                    setattr(target.font, field.name, value)

        elif isinstance(target, Paragraph):
            paragraph_style = target.paragraph_format
            for field in fields(style):
                value = getattr(style, field.name)
                if value is not None:
                    # проверка необходимости преобразования типа данных
                    if field.name in (
                            "space_after", "space_before", "left_indent", "right_indent", "first_line_indent"):
                        if field.name in ("left_indent", "right_indent"):
                            value = Inches(value)
                        else:
                            value = Pt(value)
                    elif field.name in ("alignment",):
                        # Получение значения из Enum для выравнивания
                        value = value.value

                    setattr(paragraph_style, field.name, value)
