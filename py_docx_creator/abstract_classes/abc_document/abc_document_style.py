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

    @staticmethod
    @abstractmethod
    def apply_style(target: ABCDocument | Run | Paragraph, style: Any) -> None:
        """
        Применение стиля к передаваемому объекту

        Args:
            target (ABCDocument | Run | Paragraph): Цель применения стиля
            style (Any): Применяемый стиль
        """
        pass
