from abc import ABC, abstractmethod

from docx import Document
from docx.text.paragraph import Paragraph
from docx.text.run import Run

from py_docx_creator.abstract_classes.abc_document.abc_document import ABCDocument


class ABCDocumentWriter(ABC):
    """Класс для наполнения документа"""
    document: Document

    @staticmethod
    @abstractmethod
    def add_paragraph_to_document(document: ABCDocument) -> Paragraph | None:
        """Добавление параграфа в документ"""
        pass

    @staticmethod
    @abstractmethod
    def add_run_to_paragraph(paragraph: Paragraph, text: str) -> Run | None:
        """Добавить текст в параграф"""
        pass

    @staticmethod
    @abstractmethod
    def add_page_break(document: ABCDocument) -> None:
        """Добавление разрыва страницы в документ"""
        pass