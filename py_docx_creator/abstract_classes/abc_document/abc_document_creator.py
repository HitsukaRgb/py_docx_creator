from abc import ABC, abstractmethod
from queue import Queue

from py_docx_creator.abstract_classes.abc_document.abc_document import ABCDocument


class ABCDocumentCreator(ABC):
    """
    Абстрактный класс для конвейерного формирования документов

    Attributes:
        _documents (Queue): Очередь документов для формирования
        _chunk_size (int): Размер чанка очереди (количество одновременно выполняемых потоков)
    """

    _documents: dict[str | ABCDocument] | None
    _chunk_size: int | None

    @abstractmethod
    def add_document(self, document: ABCDocument) -> None:
        """
        Добавление документа в перечень

        Args:
            document (ABCDocument): Добавляемый в перечень для выполнения документ
        """
        pass

    @abstractmethod
    def remove_document(self, document_name: str) -> None:
        """
        Удаление документа по его названию

        Args:
            document_name: (str): Наименование документа для удаления
        """
        pass

    @abstractmethod
    def start_creating_documents(self) -> None:
        """Запуск процесса формирования документов"""
        pass

    @property
    @abstractmethod
    def chunk_size(self) -> int:
        """Размер чанка очереди (количество одновременно выполняемых потоков)"""
        pass

    @chunk_size.setter
    @abstractmethod
    def chunk_size(self, value: int) -> None:
        pass
