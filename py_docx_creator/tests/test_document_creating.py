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
        document = Document(self.file_name, path=directory)
        document.save_document()
        self.assertIs(Path(directory, self.file_name).exists(), True)

    def _build_pipeline_documents(self, directory: Path) -> DocumentCreator:
        def instruction(doc: Document, **kwargs):
            file_name = kwargs.get("name", None)
            self.assertIsNotNone(file_name)  # Проверка чтения аргументов инструкции
            doc.save_document()

        document_creator = DocumentCreator()
        for i in range(10):
            document: Document = Document(f"{i}.docx", path=directory)
            document.creation_instruction = instruction
            document.instruction_kwargs = {"name": f"{i}.docx"}
            document_creator.add_document(document)
        return document_creator

    @temp_dir
    def test_pipeline_creation_documents_with_thread(self, directory: Path):
        """Тестирование формирования в потоках"""
        document_creator = self._build_pipeline_documents(directory)
        document_creator.start_creating_documents(use_threads=True, use_multiprocess=False)

    @temp_dir
    def test_pipeline_creation_documents_with_multiprocess(self, directory: Path):
        """Тестирование формирования в процессах"""
        document_creator = self._build_pipeline_documents(directory)
        document_creator.start_creating_documents(use_threads=False, use_multiprocess=True)

    @temp_dir
    def test_pipeline_creation_documents_with_multiprocess_and_threads(self, directory: Path):
        """Тестирование формирования в процессах и потоках одновременно"""
        document_creator = self._build_pipeline_documents(directory)
        document_creator.start_creating_documents(use_threads=True, use_multiprocess=True)
