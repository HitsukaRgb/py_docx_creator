from pathlib import Path
from unittest import TestCase

from py_docx_creator.core.document.document import Document
from py_docx_creator.core.document.document_creator import DocumentCreator
from py_docx_creator.tests.tools import temp_dir


class TestDocumentCreating(TestCase):
    """Тестирование формирования документов"""

    file_name: str = "Документ.docx"

    @temp_dir
    def test_single_creation_document(self, directory: Path):
        """Формирование одиночного документа"""
        document = Document()
        document.create_document(self.file_name, path=directory)
        document.save_document()
        self.assertIs(Path(directory, self.file_name).exists(), True)

    @temp_dir
    def test_pipeline_creation_documents(self, directory: Path):
        """Конвейерное формирование"""

        def instruction(doc: Document, **kwargs):
            file_name = kwargs.get("name", None)
            self.assertIsNotNone(file_name)  # Проверка чтения аргументов инструкции
            doc.save_document()

        document_creator = DocumentCreator()
        for i in range(5):
            document: Document = Document()
            document.create_document(f"{i}.docx", path=directory)
            document.creation_instruction = instruction
            document.instruction_kwargs = {"name": f"{i}.docx"}
            document_creator.add_document(document)
        document_creator.start_creating_documents()
