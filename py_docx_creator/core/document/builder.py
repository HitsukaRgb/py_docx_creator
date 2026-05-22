from typing import TypeVar, TYPE_CHECKING

from docx.text.paragraph import Paragraph
from docx.text.run import Run

from py_docx_creator.core.document.paragraph_builder import ParagraphBuilder
from py_docx_creator.core.document.text_style_builder import TextStyleBuilder

if TYPE_CHECKING:
    from py_docx_creator.core.document.document import Document


class Builder(ParagraphBuilder, TextStyleBuilder):
    """
    Класс Builder для "Fluent" стилизации параграфов и текста

    Attributes:
        _document (Document): Документ для записи
        _text (str): Записываемый текст

    """
    _document: "Document"
    _text: str

    @property
    def document(self):
        """Документ для записи"""
        return self._document

    @document.setter
    def document(self, document):
        """
        Установка документа для записи

        Args:
            document (Document): Документ для записи

        """
        self._document = document

    @property
    def text(self):
        """Записываемый текст"""
        return self._text

    @text.setter
    def text(self, text):
        """
        Установка записываемого текста

        Args:
            text (str): Записываемый текст

        """
        self._text = text

    def add(self) -> tuple[Paragraph, Run]:
        """
        Commit для завершения записи в стиле "Fluent"

        Returns:
            tuple[Paragraph, Run]: Записанные параграф и run
        """
        paragraph = self.document.add_paragraph_to_document(self.document)
        self.document.apply_style(paragraph, self.paragraph_style)
        run = self.document.add_run_to_paragraph(paragraph, self.text)
        self.document.apply_style(run, self.text_style)
        return paragraph, run
