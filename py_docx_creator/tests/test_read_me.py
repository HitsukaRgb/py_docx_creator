from pathlib import Path
from unittest import TestCase

from py_docx_creator.core.document.document import Document
from py_docx_creator.core.document.document_creator import DocumentCreator
from py_docx_creator.default_style_preset.default_page_style import DefaultPageStyle
from py_docx_creator.default_style_preset.default_paragraph_style import DefaultHeaderParagraphStyle
from py_docx_creator.default_style_preset.default_text_style import DefaultHeaderTextStyle
from py_docx_creator.enums.enum_align_paragraph import AlignParagraph
from py_docx_creator.enums.enum_base_paragraph_style import BaseParagraphStyle
from py_docx_creator.tests.tools import temp_dir


class TestReadMe(TestCase):
    file_name: str = "Документ.docx"
    text: str = "Тестирование"

    @temp_dir
    def test_classic(self, _directory: Path):
        document = Document(self.file_name, path=_directory)
        paragraph = document.add_paragraph_to_document()
        document.add_run_to_paragraph(paragraph, self.text)
        document.save_document()

    @temp_dir
    def test_fast_write(self, _directory: Path):
        document = Document(self.file_name, path=_directory)
        document.write("Пример быстрой записи", paragraph_style=DefaultHeaderParagraphStyle, text_style=DefaultHeaderTextStyle)
        document.save_document()

    @temp_dir
    def test_fluent_write(self, _directory: Path):
        document = Document(self.file_name, path=_directory)
        document.paragraph("Пример Fluent записи").size(12).bold(True).italic(True).alignment(AlignParagraph.CENTER).base_paragraph_style(BaseParagraphStyle.LIST_NUMBER).add()
        document.paragraph("Пример Fluent записи").size(12).bold(True).italic(True).line_spacing(12).alignment(AlignParagraph.CENTER).base_paragraph_style(
            BaseParagraphStyle.LIST_NUMBER
        ).add()
        document.paragraph("Пример Fluent записи").size(12).bold(True).italic(True).line_spacing(12).alignment(AlignParagraph.CENTER).add()
        document.paragraph("Пример Fluent записи").size(12).bold(True).italic(True).line_spacing(12).alignment(AlignParagraph.CENTER).base_paragraph_style(
            BaseParagraphStyle.LIST_NUMBER
        ).add()
        document.save_document()

        document.save_document()

    @temp_dir
    def test_creation_according_to_instructions(self, _directory: Path):
        def instruction(doc: Document, **kwargs):
            file_name = kwargs.get("name", "document.docx")
            doc.name = file_name
            # Классическая запись
            paragraph = doc.add_paragraph_to_document()
            doc.add_run_to_paragraph(paragraph, f"{file_name} - Пример классической записи")
            # Быстрая запись
            doc.write(f"{file_name} - Пример быстрой записи", paragraph_style=DefaultHeaderParagraphStyle, text_style=DefaultHeaderTextStyle)
            # Fluent запись
            doc.paragraph(f"{file_name} - Пример Fluent записи").italic(True).size(18).first_line_indent(30).space_after(30).add()
            doc.save_document()

        document = Document(self.file_name, path=_directory)
        document.creation_instruction = instruction  # инструкция по формированию документа
        document.instruction_kwargs = {"name": "Конвейерное создание документов.docx"}  # аргументы выполняемой функции
        document.run_instruction()  # запуск формирования документа

    @temp_dir
    def test_pipeline_creation(self, _directory: Path):
        def instruction(doc: Document, **kwargs):
            file_name = kwargs.get("name", "document.docx")
            # Классическая запись
            paragraph = doc.add_paragraph_to_document()
            doc.add_run_to_paragraph(paragraph, f"{file_name} - Пример классической записи")
            # Быстрая запись
            doc.write(f"{file_name} - Пример быстрой записи", paragraph_style=DefaultHeaderParagraphStyle, text_style=DefaultHeaderTextStyle)
            # Fluent запись
            doc.paragraph(f"{file_name} - Пример Fluent записи").italic(True).size(18).first_line_indent(30).space_after(30).add()
            doc.save_document()

        document_creator = DocumentCreator()
        for i in range(10):  # имитация конвейера
            document: Document = Document(f"{i}.docx", path=_directory)
            document.creation_instruction = instruction  # инструкция по формированию документа
            document.instruction_kwargs = {"name": f"{i}.docx"}  # аргументы выполняемой функции
            document_creator.add_document(document)  # список экземпляров `Document` готовых к формированию

        document_creator.start_creating_documents()  # запуск формирования всех документов

    @temp_dir
    def test_custom_styles(self, _directory: Path):
        class MyTextStyle(DefaultHeaderTextStyle):  # Стиль текста
            italic = True
            size = 24

        class MyParagraphStyle(DefaultHeaderParagraphStyle):  # Стиль параграфа
            alignment = AlignParagraph.LEFT

        class MyPageStyle(DefaultPageStyle):  # Стиль страницы
            left_margin = 200.0

        document = Document(self.file_name, path=_directory)
        document.apply_style(document, style=MyPageStyle)  # пример того как задать стиль страницы `PageStyle`
        document.write("Базовый пример использования", paragraph_style=MyParagraphStyle, text_style=MyTextStyle)
        document.save_document()
