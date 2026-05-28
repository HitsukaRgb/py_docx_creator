from pathlib import Path
from typing import Callable
from unittest import TestCase

from py_docx_creator.abstract_classes.abc_document.abc_document import ABCDocument
from py_docx_creator.core.document.document import Document
from py_docx_creator.enums.enum_align_paragraph import AlignParagraph
from py_docx_creator.enums.enum_document_styles import DocumentStyles
from py_docx_creator.tests.tools import temp_dir


class TestWriting(TestCase):
    """Тестирование записи в документ"""

    file_name: str = "Документ.docx"
    text: str = "Тестирование"

    def classical_writing(self, document: Document):
        """Метод классической записи"""
        paragraph = document.add_paragraph_to_document()
        document.add_run_to_paragraph(paragraph, self.text)

    def fluent_writing(self, document: Document):
        """Метод fluent записи"""
        document.paragraph(self.text).size(32).bold(True).italic(True).line_spacing(12).add()
        document.paragraph(self.text).bold(True).space_after(13).line_spacing(23).add()

    def fast_writing(self, document: Document):
        """Метод быстрой записи"""
        from py_docx_creator.default_style_preset.default_paragraph_style import (
            DefaultHeaderParagraphStyle,
        )
        from py_docx_creator.default_style_preset.default_text_style import (
            DefaultHeaderTextStyle,
        )

        class MyTextStyle(DefaultHeaderTextStyle):  # Стиль текста
            italic = True
            size = 24

        document.write(self.text, paragraph_style=DefaultHeaderParagraphStyle, text_style=MyTextStyle, alignment=AlignParagraph.CENTER)

    @temp_dir
    def _writing_test(self, _directory: Path, writing_func: Callable):
        """
        Тестирование работоспособности методов записи

        Args:
            _directory (Path): Прокидывается автоматически декоратором
            writing_func (Callable): Метод записи

        """
        # Формирование тестируемого документа
        document = Document(self.file_name, path=_directory)
        document.document_style = DocumentStyles.NORMAL
        writing_func(document)
        document.save_document()

        doc_path = Path(_directory, self.file_name)  # Путь до сформированного документа

        # Проверка наличия записанного текста
        result_document = Document(doc_path)
        for paragraphs in result_document.document.paragraphs:
            self.assertEqual(paragraphs.text, self.text)

    def test_fluent_writing(self):
        """Fluent запись"""
        self._writing_test(self.fluent_writing)

    def test_fast_writing(self):
        """Быстрая запись"""
        self._writing_test(self.fast_writing)

    def test_classical_writing(self):
        """Классическая запись"""
        self._writing_test(self.classical_writing)

    @temp_dir
    def test_read_me(self, _directory: Path):
        from py_docx_creator.core.document.document import Document
        from py_docx_creator.default_style_preset.default_paragraph_style import DefaultHeaderParagraphStyle
        from py_docx_creator.default_style_preset.default_text_style import DefaultHeaderTextStyle

        def instruction(doc: Document, **kwargs):
            print(doc)
            file_name = kwargs.get("name", "document.docx")
            doc.name = file_name
            # Классическая запись
            paragraph = doc.add_paragraph_to_document()
            run = doc.add_run_to_paragraph(paragraph, f"{file_name} - Пример классической записи")
            # Быстрая запись
            doc.write(f"{file_name} - Пример быстрой записи", paragraph_style=DefaultHeaderParagraphStyle,
                      text_style=DefaultHeaderTextStyle)
            # Fluent запись
            doc.paragraph(f"{file_name} - Пример Fluent записи").italic(True).size(18).first_line_indent(
                30).space_after(30).add()
            doc.save_document()

        document = Document("document.docx", path=_directory)
        document.creation_instruction = instruction  # инструкция по формированию документа
        document.instruction_kwargs = {"name": "Конвейерное создание документов.docx"}  # аргументы выполняемой функции
        document.run_instruction()  # запуск формирования документа
