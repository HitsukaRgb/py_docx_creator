from pathlib import Path
from typing import Callable, Any

from py_docx_creator.abstract_classes.abc_document.abc_document import ABCDocument
from docx import Document as DocxDocument # alias

from py_docx_creator.core.document.document_style import DocumentStyle
from py_docx_creator.core.document.document_writer import Writer


class BaseDocument(ABCDocument):
    path: Path | str | None = None # путь до документа
    name: str | None = None # наименование документа
    _creation_instruction: Callable | None = None # инструкция для формирования документа
    _instruction_kwargs: dict[str, Any] | None # аргументы инструкция для формирования документа
    document: DocxDocument # alias

    def __init__(self, file_name: str | Path | None = None):
        if file_name:
            path = Path(file_name)
            if path.exists():
                if path.name.endswith(".docx") and not path.name.startswith("~"):
                    self.path = path
                    self.name = path.name

    def create_document(self, file_name, path: str | Path | None = None):
        self.document = DocxDocument()
        self.name = file_name
        if not path and self.path is None:
            self.path = Path.cwd()

    def load_document(self):
        self.document = DocxDocument(self.path or self.name)

    def save_document(self):
        self.document.save(self.name)

    def run_instruction(self, save_after: bool=True):
        """Запуск формирования документа"""
        if self.creation_instruction:
            self.creation_instruction(self, **self._instruction_kwargs)
            if save_after:
                self.save_document()
        else:
            raise Exception("Инструкция не задана!")

    @property
    def creation_instruction(self) -> Callable:
        """Функция для формирования документа"""
        return self._creation_instruction

    @creation_instruction.setter
    def creation_instruction(self, value: Callable) -> None:
        """Функция для формирования документа"""
        self._creation_instruction = value

    @property
    def instruction_kwargs(self) -> dict[str | Any] | None:
        return self._instruction_kwargs

    @instruction_kwargs.setter
    def instruction_kwargs(self, value: dict[str | Any] | None) -> None:
        self._instruction_kwargs = value

class DocumentBaseDocumentMixin(BaseDocument):

    def __init__(self):
        super().__init__()

class DocumentWriterMixin(Writer):
    pass

class Document(BaseDocument, Writer, DocumentStyle):
    pass

