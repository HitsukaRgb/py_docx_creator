from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from docx.text.paragraph import Paragraph
from docx.text.run import Run

if TYPE_CHECKING:
    from py_docx_creator.abstract_classes.abc_document.abc_document import ABCDocument


class ABCBuilder(ABC):
    """
    Абстрактный класс Builder для "Fluent" стилизации параграфов и текста

    Attributes:
        _document (Document): Документ для записи
        _text (str): Записываемый текст

    """

    _document: "ABCDocument"
    _text: str

    @property
    @abstractmethod
    def document(self) -> "ABCDocument":
        """Документ для записи"""
        pass

    @document.setter
    def document(self, document) -> None:
        """
        Установка документа для записи

        Args:
            document (Document): Документ для записи

        """
        pass

    @property
    @abstractmethod
    def text(self) -> str:
        """Записываемый текст"""
        pass

    @text.setter
    def text(self, text) -> None:
        """
        Установка записываемого текста

        Args:
            text (str): Записываемый текст

        """
        pass

    @abstractmethod
    def add(self) -> tuple[Paragraph, Run]:
        """
        Commit для завершения записи в стиле "Fluent"

        Returns:
            tuple[Paragraph, Run]: Записанные параграф и run
        """
        pass
