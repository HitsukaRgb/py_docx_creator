# DocxP

**DocxP** — это мой небольшой Python-проект для создания и форматирования Word-документов с использованием библиотеки `python-docx`.
Вы можете дополнять и расширять ее при необходимости. Я постарался построить гибкую основу для последующего расширения.


## Возможности

- Абстрактные классы для описания стилей документа, абзацев и текста.
- Реализация базовых стилей и логики генерации Word-документов.
- Гибкая настройка шрифтов, отступов, выравнивания и др.

## Структура проекта

- `core/` — модуль с основными и абстрактными классами:
  - `AbstractClasses.py` — абстрактные интерфейсы
  - `CoreClasses.py` — реализация базовых стилей
  - `CustomClasses.py` — расширение с пользовательскими стилями

## Установка

```bash
pip install python-docx py_docx_creator
```

## Пример использования

```python
from py_docx_creator.CoreClasses import CoreDocumentCreator, CoreStyleManager
from py_docx_creator.CustomClasses import MainPageStyle, MainDocumentWriter, MainTextStyle, HeaderParagraphStyle, \
    MainParagraphStyle, HeaderTextStyle, FastWriter


class DocumentAPI(CoreDocumentCreator):

    def __init__(self, file_name: str):
        super().__init__()
        self.file_name = file_name
        self.style_manager = CoreStyleManager
        self.write_to_document = FastWriter

    def run(self):
        self.create_document(self.file_name)

        self.style_manager.PAGE_STYLE_MANAGER.apply_style(self.document, MainPageStyle)

        self.write_to_document.write(document=self.document,
                                     text="Заголовок документа",
                                     text_style=HeaderTextStyle,
                                     paragraph_style=HeaderParagraphStyle)

        self.write_to_document.write(document=self.document,
                                     text="Основной текст 1",
                                     text_style=MainTextStyle,
                                     paragraph_style=MainParagraphStyle)

        self.save_document()


if __name__ == '__main__':
    DocumentAPI("Документ.docx").run()

```



