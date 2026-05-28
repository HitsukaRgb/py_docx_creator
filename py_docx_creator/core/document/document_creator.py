from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool

from py_docx_creator.abstract_classes.abc_document.abc_document_creator import (
    ABCDocumentCreator,
)
from py_docx_creator.core.document.document import Document
from itertools import batched


class DocumentCreator(ABCDocumentCreator):
    """
    Класс для конвейерного формирования документов

    Attributes:
        _documents (dict[str | Document] | None): Очередь документов для формирования
        _chunk_size (int): Размер чанка очереди (количество одновременно выполняемых потоков и (или) процессов)
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

    def start_creating_documents(self, use_threads: bool = True, use_multiprocess: bool = False):
        if all([use_threads, use_multiprocess]):
            self._start_creating_documents_with_multiprocess_and_threads()
        elif use_threads:
            self._start_creating_documents_with_threads()
        elif use_multiprocess:
            self._start_creating_documents_with_multiprocess()

    def _start_creating_documents_with_threads(self):
        """
        Формирование документов с разбивкой на потоки.
        Одновременно работает chunk_size потоков.
        """
        with ThreadPoolExecutor(max_workers=self.chunk_size) as executor:
            for document in self.documents.values():
                executor.submit(document.run_instruction)

    def _start_creating_documents_with_multiprocess(self):
        """
        Формирование документов с разбивкой на процессы.
        Одновременно работает chunk_size процессов.
        """
        with Pool(processes=self.chunk_size) as pool:
            for doc in self.documents.values():
                pool.apply_async(doc.run_instruction)
            pool.close()
            pool.join()

    def _start_creating_documents_with_multiprocess_and_threads(self):
        """
        Формирование документов с разбивкой на процессы и потоки.
        Одновременно работает chunk_size процессов и потоков.

        Например:
            При значении chunk_size = 5
            Количество потоков = 5
            Количество процессов = 5
            В одном процессе работает - 5 протоков

        """
        chunks = list(batched(self.documents.values(), self.chunk_size))

        with Pool(processes=self.chunk_size) as pool:
            for chunk in chunks:
                pool.apply_async(self._worker_process_task, args=(self.chunk_size, chunk))
            pool.close()
            pool.join()

    @staticmethod
    def _worker_process_task(chunk_size, documents_chunk):
        with ThreadPoolExecutor(max_workers=chunk_size) as executor:
            for doc in documents_chunk:
                executor.submit(doc.run_instruction)

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
