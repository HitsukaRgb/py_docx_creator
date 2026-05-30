from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from docx.text.paragraph import Paragraph
from docx.text.run import Run

from py_docx_creator.abstract_classes.abc_document.abc_builder import ABCBuilder

from py_docx_creator.abstract_classes.abc_style_dataclasses.abc_paragraph_style import ABCParagraphStyle
from py_docx_creator.abstract_classes.abc_style_dataclasses.abc_text_style import ABCTextStyle
from py_docx_creator.enums.enum_align_paragraph import AlignParagraph
from py_docx_creator.enums.enum_base_paragraph_style import BaseParagraphStyle

if TYPE_CHECKING:
    from py_docx_creator.abstract_classes.abc_document.abc_document import ABCDocument


class ABCDocumentWriter(ABC):
    """
    Абстрактный класс для наполнения документа

    """

    @staticmethod
    @abstractmethod
    def add_paragraph_to_document(document: "ABCDocument") -> Paragraph | None:
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
    def add_page_break(document: "ABCDocument") -> None:
        """
        Добавление разрыва страницы в документ

        Args:
            document (ABCDocument): Документ для добавления разрыва страницы

        """
        pass

    @abstractmethod
    def paragraph(self, text: str | None) -> ABCBuilder | type[ABCBuilder]:
        """
        Инициализация style билдера

        Args:
            text (str | None): Записываемый в документ текст
        Returns:
            Builder: Экземпляр style билдера
        """
        pass

    @abstractmethod
    def write(
        self,
        text: str,
        paragraph_style: ABCParagraphStyle | type[ABCParagraphStyle],
        text_style: ABCTextStyle | type[ABCTextStyle],
        target: Paragraph | None = None,
        size: float | None = None,
        bold: bool | None = None,
        italic: bool | None = None,
        underline: bool | None = None,
        space_after: float | None = None,
        alignment: AlignParagraph | None = None,
        first_line_indent: float | None = None,
        with_leader: bool = False,
        leader_width: float = 6.8,
        base_paragraph_style: BaseParagraphStyle | None = None,
    ) -> Paragraph:
        """
        Метод быстрой записи в документ

        Args:

            text (str): Записываемый текст
            paragraph_style (ABCParagraphStyle): Стиль создаваемого параграфа
            text_style (ABCTextStyle): Стиль записываемого текста
            target (Paragraph | None): Цель записи
            size (float | None): Размер шрифта записываемого текста
            bold (bool | None): Включить ли жирное начертание для записываемого текста
            italic (bool | None): Включить ли курсивное начертание для записываемого текста
            underline (bool | None): Включить ли подчеркнутое начертание для записываемого текста
            space_after (float | None): Размер отступа после созданного параграфа
            alignment (AlignParagraph | None): Выравнивание для созданного параграфа
            first_line_indent (float | None): Размер отступа для первой строки (красная строка)
            with_leader (bool | None): Включить ли заполнение остатка строки табуляцией со знаком '_'
            leader_width (float): Размер заполняемой табуляцией строки. По умолчанию: 6.8
            base_paragraph_style (BaseParagraphStyle | None): Базовый стиль параграфа (Список, Нумерованный список, ...)
        Returns:
            Paragraph: Созданный параграф
        """
        pass
