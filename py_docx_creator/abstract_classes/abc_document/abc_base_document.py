from abc import ABC, abstractmethod
from pathlib import Path
from typing import Callable, Any
from docx import Document as DocxDocument  # alias


class ABCBaseDocument(ABC):
    """
    Абстрактный класс билдера Документа

    Attributes:
        path (Path | str | None): Путь до документа
        name (str | None): Наименование документа
        document (DocxDocument): Класс документа python-docx
    """

    path: Path | str | None  # путь до документа
    name: str | None = None  # наименование документа
    _creation_instruction: Callable | None  # инструкция для формирования документа
    _instruction_kwargs: dict[str, Any] | None  # аргументы инструкция для формирования документа
    document: type[DocxDocument] | None  # alias

    @abstractmethod
    def create_document(self):
        """Инициализация документа"""
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
    def run_instruction(self, document: "ABCDocument") -> None:
        """Запуск инструкции формирования документа"""
        pass

    @property
    @abstractmethod
    def creation_instruction(self) -> Callable:
        """Функция для формирования документа"""
        pass

    @creation_instruction.setter
    def creation_instruction(self, value: Callable) -> None:
        """Функция для формирования документа"""
        pass

    @property
    @abstractmethod
    def instruction_kwargs(self) -> dict[str | Any] | None:
        """Аргументы инструкции"""
        pass

    @instruction_kwargs.setter
    def instruction_kwargs(self, value: dict[str | Any] | None) -> None:
        pass

    @staticmethod
    @abstractmethod
    def _is_valid_existing_file(path: Path) -> bool:
        """Проверка пути"""
        pass
