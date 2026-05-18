from py_docx_creator.abstract_classes.abc_document.abc_document_creator import ABCDocumentCreator
from py_docx_creator.core.document.document import Document


class DocumentCreator(ABCDocumentCreator):
    _documents: list[Document] | None

    def __init__(self):
        self.documents = []

    def add_document(self, document: Document):
        """Добавление документа в перечень"""
        self.documents.append(document)

    def remove_document(self, document_name: str):
        """Удаление документа по его названию"""
        if self.documents:
            for index_document, document in enumerate(self.documents):
                if document.name == document_name:
                    del self.documents[index_document]


    def start_creating_documents(self, save_after: bool=True):
        """Запуск процесса формирования документов"""
        # todo: Реализовать многопоточный подход
        for document in self.documents:
            document.run_instruction(save_after)

    @property
    def documents(self) -> list[Document] | None:
        return self._documents

    @documents.setter
    def documents(self, value: list[Document]):
        self._documents = value

