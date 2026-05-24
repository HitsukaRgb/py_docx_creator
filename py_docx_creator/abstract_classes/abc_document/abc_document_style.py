from abc import ABC, abstractmethod
from typing import Any

from docx.styles.styles import Styles
from docx.text.paragraph import Paragraph
from docx.text.run import Run

from py_docx_creator.abstract_classes.abc_document.abc_document import ABCDocument


class ABCDocumentStyle(ABC):
    """Абстрактный класс для управления стилями документа"""

    _document_style: str | None

    @abstractmethod
    def get_document_style(self, document: ABCDocument) -> Styles:
        """
        Получение стиля документа

        Args:
            document (ABCDocument): Документ содержащий стиль

        Returns:
            Styles: Стиль документа
        """
        pass

    @classmethod
    @abstractmethod
    def apply_style(cls, target: Any, style: Any) -> None:
        """
        Применение стиля к передаваемому объекту

        Args:
            target (ABCDocument | Run | Paragraph): Цель применения стиля
            style (Any): Применяемый стиль
        """
        pass

    @staticmethod
    @abstractmethod
    def _apply_page_style(target: ABCDocument, style: Any) -> None:
        """
        Применение стиля к страницам документа

        Args:
            target (ABCDocument): Цель применения стиля
            style (Any): Применяемый стиль

        """
        pass

    @staticmethod
    @abstractmethod
    def _apply_paragraph_style(target: Paragraph, style: Any) -> None:
        """
        Применение стиля к параграфу

        Args:
            target (Paragraph): Цель применения стиля
            style (Any): Применяемый стиль

        """
        pass

    @staticmethod
    @abstractmethod
    def _apply_run_style(target: Run, style: Any) -> None:
        """
        Применение стиля к run-у

        Args:
            target (Run): Цель применения стиля
            style (Any): Применяемый стиль

        """
        pass
