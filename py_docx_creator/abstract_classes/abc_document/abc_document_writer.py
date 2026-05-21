from abc import ABC, abstractmethod

from docx import Document as DocxDocument # alias
from docx.text.paragraph import Paragraph
from docx.text.run import Run

from py_docx_creator.abstract_classes.abc_document.abc_document import ABCDocument


class ABCDocumentWriter(ABC):
    """
    Абстрактный класс для наполнения документа

    Attributes:
        document (DocxDocument): Класс документа python-docx

    """

    document: DocxDocument

    @staticmethod
    @abstractmethod
    def add_paragraph_to_document(document: ABCDocument) -> Paragraph | None:
        """
        Добавление параграфа в документ

        Args:
            document (ABCDocument): Документ в который записывается параграф
        Returns:
            Paragraph | None: Возвращает добавленный параграф или None
        """
        pass

    @staticmethod
    @abstractmethod
    def add_run_to_paragraph(paragraph: Paragraph, text: str) -> Run | None:
        """
        Добавить текст в параграф

        Args:
            paragraph (Paragraph): Параграф для записи Run
            text (str): Текст записываемый в Run
        Return:
            Run | None: Возвращает записанный Run или None
        """
        pass

    @staticmethod
    @abstractmethod
    def add_page_break(document: ABCDocument) -> None:
        """
        Добавление разрыва страницы в документ

        Args:
            document (ABCDocument): Документ для добавления разрыва страницы

        """
        pass