from concurrent.futures import ThreadPoolExecutor

from py_docx_creator.abstract_classes.abc_document.abc_document_creator import (
    ABCDocumentCreator,
)
from py_docx_creator.core.document.document import Document


class DocumentCreator(ABCDocumentCreator):
    """
    Класс для конвейерного формирования документов

    Attributes:
        _documents (dict[str | Document] | None): Очередь документов для формирования
        _chunk_size (int): Размер чанка очереди (количество одновременно выполняемых потоков)
    """

    _documents: dict[str | Document] | None
    _chunk_size: int | None

    def __init__(self, chunk_size: int = 5):
        self.documents = {}
        self.chunk_size = chunk_size

    def add_document(self, document: Document):
        self.documents[document.name] = document

    def remove_document(self, document_name: str):
        if document_name in self.documents:
            del self.documents[document_name]

    def start_creating_documents(self):
        with ThreadPoolExecutor(max_workers=self.chunk_size) as executor:
            for doc_name, document in self.documents.items():
                executor.submit(document.run_instruction)

    @property
    def documents(self) -> dict[str | None] | None:
        return self._documents

    @documents.setter
    def documents(self, value: dict[str | Document]):
        self._documents = value

    @property
    def chunk_size(self):
        return self._chunk_size

    @chunk_size.setter
    def chunk_size(self, value: int):
        self._chunk_size = value
