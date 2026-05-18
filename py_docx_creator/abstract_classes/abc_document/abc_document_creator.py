from abc import ABC, abstractmethod
from py_docx_creator.abstract_classes.abc_document.abc_document import ABCDocument


class ABCDocumentCreator(ABC):
    _documents: list[ABCDocument] | None

    @abstractmethod
    def add_document(self, document: ABCDocument):
        """Добавление документа в перечень"""
        pass

    @abstractmethod
    def remove_document(self, document_name: str):
        """Удаление документа по его названию"""
        pass

    @abstractmethod
    def start_creating_documents(self):
        """Запуск процесса формирования документов"""
        pass