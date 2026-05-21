from abc import ABC, abstractmethod
from pathlib import Path
from typing import Callable, Any
from docx import Document as DocxDocument  # alias


class ABCDocument(ABC):
    """
    Абстрактный класс Документа

    Attributes:
        path (Path | str | None): Путь до документа
        name (str | None): Наименование документа
        document (DocxDocument): Класс документа python-docx
    """
    path: Path | str | None  # путь до документа
    name: str | None  # наименование документа
    _creation_instruction: Callable | None  # инструкция для формирования документа
    _instruction_kwargs: dict[str, Any] | None  # аргументы инструкция для формирования документа
    document: DocxDocument  # alias

    @abstractmethod
    def create_document(self, file_name: str, path: str | Path | None) -> None:
        """
        Создание документа

        Args:
            file_name (str): Наименование документа
            path (str | Path | None): Путь формирования документа
        """
        pass

    @abstractmethod
    def load_document(self) -> None:
        """Загрузка уже имеющегося документа"""
        pass

    @abstractmethod
    def save_document(self) -> None:
        """Сохранение документа"""
        pass

    @abstractmethod
    def run_instruction(self, save_after: bool = True) -> None:
        """
        Запуск инструкции формирования документа

        Args:
            save_after (bool): Сохранить поле выполнения инструкций
       """
        pass
