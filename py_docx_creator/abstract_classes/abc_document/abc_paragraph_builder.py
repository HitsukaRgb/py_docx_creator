from abc import ABC, abstractmethod
from typing import Self

from py_docx_creator.abstract_classes.abc_style_dataclasses.abc_paragraph_style import (
    ABCParagraphStyle,
)
from py_docx_creator.enums.enum_align_paragraph import AlignParagraph
from py_docx_creator.enums.enum_base_paragraph_style import BaseParagraphStyle


class ABCParagraphBuilder(ABC):
    """
    Стиль форматирования параграфа.

    Attributes:
        _alignment (AlignParagraph | None): Выравнивание текста (влево, по центру, по ширине и т.п.).
        _space_after (float | None): Отступ после параграфа.
        _space_before (float | None): Отступ перед параграфом.
        _left_indent (float | None): Отступ от левого края страницы.
        _right_indent (float | None): Отступ от правого края страницы.
        _line_spacing (float | None): Межстрочный интервал.
        _first_line_indent (float | None): Отступ первой строки (красная строка).
        _page_break_before (bool | None): Разрыв страницы перед параграфом.
    """

    _text: str | None
    _alignment: AlignParagraph | None
    _space_after: float | None
    _space_before: float | None
    _left_indent: float | None
    _right_indent: float | None
    _line_spacing: float | None
    _first_line_indent: float | None
    _page_break_before: bool | None
    _base_paragraph_style: BaseParagraphStyle | None

    @abstractmethod
    def alignment(self, alignment: AlignParagraph | None) -> Self:
        """
        Выравнивание текста (влево, по центру, по ширине и т.п.).

        Args:
            alignment (AlignParagraph | None): Выравнивание текста (влево, по центру, по ширине и т.п.).

        Returns:
            Self: Класс Builder

        """
        pass

    @abstractmethod
    def space_after(self, space_after: float | None) -> Self:
        """
        Отступ после параграфа.

        Args:
            space_after (float | None): Отступ после параграфа.

        Returns:
            Self: Класс Builder

        """
        pass

    @abstractmethod
    def space_before(self, space_before: float | None) -> Self:
        """
        Отступ перед параграфом.

        Args:
            space_before (float | None): Отступ перед параграфом.

        Returns:
            Self: Класс Builder

        """
        pass

    @abstractmethod
    def left_indent(self, left_indent: float | None) -> Self:
        """
        Отступ от левого края страницы.

        Args:
            left_indent (float | None): Отступ от левого края страницы.

        Returns:
            Self: Класс Builder

        """
        pass

    @abstractmethod
    def right_indent(self, right_indent: float | None) -> Self:
        """
        Отступ от правого края страницы.

        Args:
            right_indent (float | None): Отступ от правого края страницы.

        Returns:
            Self: Класс Builder

        """
        pass

    @abstractmethod
    def line_spacing(self, line_spacing: float | None) -> Self:
        """
        Межстрочный интервал.

        Args:
            line_spacing (float | None): Межстрочный интервал.

        Returns:
            Self: Класс Builder

        """
        pass

    @abstractmethod
    def first_line_indent(self, first_line_indent: float | None) -> Self:
        """
        Отступ первой строки (красная строка).

        Args:
            first_line_indent (float | None): Отступ первой строки (красная строка).

        Returns:
            Self: Класс Builder

        """
        pass

    @abstractmethod
    def page_break_before(self, page_break_before: bool | None) -> Self:
        """
        Разрыв страницы перед параграфом.

        Args:
            page_break_before (bool | None): Разрыв страницы перед параграфом.

        Returns:
            Self: Класс Builder

        """
        pass

    @abstractmethod
    def base_paragraph_style(self, style: BaseParagraphStyle) -> ABCParagraphStyle:
        """
        Базовый стиль параграфа

        Args:
            style (BaseParagraphStyle): Базовый стиль
        Returns:
            Self: Класс Builder
        """
        pass

    @property
    @abstractmethod
    def paragraph_style(self) -> ABCParagraphStyle:
        """
        Стиль параграфа

        Returns:
            ABCParagraphStyle: Dataclass стиля параграфа
        """
        pass
