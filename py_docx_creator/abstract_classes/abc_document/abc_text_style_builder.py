from abc import ABC, abstractmethod
from typing import Self

from py_docx_creator.abstract_classes.abc_style_dataclasses.abc_text_style import ABCTextStyle


class ABCTextStyleBuilder(ABC):
    """
        Класс стилизации текста.

    Attributes:
        _size ( float | None): Размер шрифта
        _name ( str | None): Наименование шрифта
        _bold ( bool | None): Жирное начертание шрифта
        _italic ( bool | None): Курсивное начертание шрифта
        _underline ( bool | None): Подчеркнутое начертание шрифта
    """
    _size: float | None
    _name: str | None
    _bold: bool | None
    _italic: bool | None
    _underline: bool | None

    @abstractmethod
    def size(self, size: float | None) -> Self:
        """
        Размер шрифта

        Args:
            size (float | None): -> Размер шрифта
        """
        pass

    @abstractmethod
    def name(self, name: str | None) -> Self:
        """
        Наименование шрифта

        Args:
            name (str | None): -> Наименование шрифта
        """
        pass

    @abstractmethod
    def bold(self, bold: bool | None) -> Self:
        """
        Жирное начертание шрифта

        Args:
            bold (bool | None): -> Жирное начертание шрифта
        """
        pass

    @abstractmethod
    def italic(self, italic: bool | None) -> Self:
        """
        Курсивное начертание шрифта

        Args:
            italic (bool | None): -> Курсивное начертание шрифта
        """
        pass

    @abstractmethod
    def underline(self, underline: bool | None) -> Self:
        """
        Подчеркнутое начертание шрифта

        Args:
            underline (bool | None): -> Подчеркнутое начертание шрифта
        """
        pass

    @property
    @abstractmethod
    def text_style(self) -> ABCTextStyle:
        """
        Стиль текста

        Returns:
            ABCTextStyle: Dataclass стиля текста
        """
        pass
