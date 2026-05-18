from abc import ABC, abstractmethod
from typing import Any

from docx.styles.styles import Styles
from docx.text.paragraph import Paragraph
from docx.text.run import Run

from py_docx_creator.abstract_classes.abc_document.abc_document import ABCDocument


class ABCDocumentStyle(ABC):
    """Стиль документа"""
    _document_style: str | None

    @abstractmethod
    def get_document_style(self, document: ABCDocument) -> Styles | None:
        """Получение стиля документа"""
        pass

    @staticmethod
    @abstractmethod
    def apply_style(target: ABCDocument | Run | Paragraph, style: Any):
        """Применение стиля к передаваемому объекту"""
        pass
