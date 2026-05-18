# PDC

**PyDocxCreator** — Небольшой Python-проект для создания и форматирования Word-документов с использованием библиотеки `python-docx`.

Я постарался заложить гибкую основу для последующего расширения.


## Возможности

- Абстрактные классы для описания стилей документа, абзацев и текста.
- Реализация базовых стилей и логики генерации Word-документов.
- Гибкая настройка шрифтов, отступов, выравнивания и др.

## Структура проекта

- `py_docx_creator/`                — модуль с основными и абстрактными классами:
  - `abstract_classes/`             — абстрактные интерфейсы
    - `abc_document/`               — абстрактные классы для описания документа и взаимодействия с ним
    - `abc_style_dataclasses/`      — абстрактные классы для описания стилей
  - `core/` — реализация интерфейсов
    - `document/` — реализация взаимодействия с документом
    - `style/` — реализация пустых базовых шаблонов стилей
  - `default_style_preset/` - несколько заготовленных стилей
  - `enums/` - `enum`ы шрифтов, стилей документа, выравнивания


## Установка

```bash
pip install py_docx_creator
```

## Базовый пример использования

```python

from py_docx_creator.core.document.document import Document
from py_docx_creator.default_style_preset.default_paragraph_style import DefaultHeaderParagraphStyle
from py_docx_creator.default_style_preset.default_text_style import DefaultHeaderTextStyle

document = Document()
document.create_document("Документ.docx")
document.write(document, "Базовый пример использования", paragraph_style=DefaultHeaderParagraphStyle, text_style=DefaultHeaderTextStyle)
document.save_document()

```

Предусмотрена возможность прописать шаги формирования документа в отдельной функции типа `Callable`. Аргументы такой функции задаются в отдельном поле класса `Document`.

*** Важный момент при написании функции-инструкции. Для корректной работы первый позиционный аргумент данной функции (в данном примере `doc: Document`) обязательно должен быть экземпляр класса `Document`. Данный аргумент является системным и прокидывается автоматически при выполнении кода.

```python

from py_docx_creator.core.document.document import Document
from py_docx_creator.default_style_preset.default_paragraph_style import DefaultHeaderParagraphStyle
from py_docx_creator.default_style_preset.default_text_style import DefaultHeaderTextStyle

def instruction(doc: Document, **kwargs):
    file_name = kwargs.get("name", "document.docx")
    doc.create_document(file_name)
    doc.write(doc, "Базовый пример использования", paragraph_style=DefaultHeaderParagraphStyle, text_style=DefaultHeaderTextStyle)

document = Document()
document.create_document("Документ.docx")
document.creation_instruction = instruction # инструкция по формированию документа
document.instruction_kwargs = {"name": "Базовый пример использования.docx"} # аргументы выполняемой функции
document.run_instruction(save_after=True) # запуск формирования документа 

```

Реализован простой агрегатор для конвейерного формирования документов `DocumentCreator`. 

```python

from py_docx_creator.core.document.document import Document
from py_docx_creator.core.document.document_creator import DocumentCreator
from py_docx_creator.default_style_preset.default_paragraph_style import DefaultHeaderParagraphStyle
from py_docx_creator.default_style_preset.default_text_style import DefaultHeaderTextStyle

def instruction(doc: Document, **kwargs):
    file_name = kwargs.get("name", "document.docx")
    doc.create_document(file_name)
    doc.write(doc, "Базовый пример использования", paragraph_style=DefaultHeaderParagraphStyle, text_style=DefaultHeaderTextStyle)

document_creator = DocumentCreator()
for i in range(5): # имитация конвейера
    document: Document = Document()
    document.creation_instruction = instruction # инструкция по формированию документа
    document.instruction_kwargs = {"name": f"{i}.docx"} # аргументы выполняемой функции (в данном случае отличные друг от друга имена файлов)
    document_creator.add_document(document) # список экземпляров `Document` готовых к формированию

document_creator.start_creating_documents(save_after=True) # запуск формирования всех документов

```

## Стили

Реализованы базовые стили:

- Стиль страницы
  - `DefaultPageStyle` - базовый стиль страницы документа (поля/отступы)
- Стиль параграфа
  - `DefaultHeaderParagraphStyle` - базовый стиль параграфа для заголовка
  - `DefaultMainParagraphStyle` - базовый стиль параграфа для основного текста 
- Стиль текста
  - `DefaultHeaderTextStyle` - базовый стиль для текста заголовка
  - `DefaultMainTextStyle` - базовый стиль для основного текста

### Создание собственных стилей
Ниже приведен пример создания стилей на основе базовых стилей

```python

from py_docx_creator.core.document.document import Document
from py_docx_creator.default_style_preset.default_page_style import DefaultPageStyle
from py_docx_creator.default_style_preset.default_paragraph_style import DefaultHeaderParagraphStyle
from py_docx_creator.default_style_preset.default_text_style import DefaultHeaderTextStyle
from py_docx_creator.enums.enum_align_paragraph import AlignParagraph


class MyTextStyle(DefaultHeaderTextStyle): # Стиль текста
    italic = True
    size = 24

class MyParagraphStyle(DefaultHeaderParagraphStyle): # Стиль параграфа
    alignment = AlignParagraph.LEFT.value

class MyPageStyle(DefaultPageStyle): # Стиль страницы
    left_margin = 200.0

document = Document()
document.create_document("Документ.docx")
document.apply_style(document, style=MyPageStyle) # пример того как задать стиль страницы `PageStyle`
document.write(document, "Базовый пример использования", paragraph_style=MyParagraphStyle, text_style=MyTextStyle)
document.save_document()

```

При необходимости есть возможность создать стиль с нуля. Для этого необходимо наследоваться от базовых классов.

- `PageStyle` - для стилей страницы
- `ParagraphStyle` - для стилей параграфа
- `TextStyle` - для стилей текста

### Быстрая смена стиля

Имеется возможность подправить основные параметры стилей прямо на месте записи. Для этого имеются опциональные именованные аргументы.

 - `size: float` - размер шрифта
 - `bold: bool` - жирное начертание
 - `italic: bool` - курсивное начертание
 - `underline: bool` - подчеркнутое начертание
 - `space_after: float` - отступ поле параграфа
 - `alignment: AlignParagraph` - выравнивание параграфа
 - `first_line_indent: float` - отступ первой строки (красная строка)
 - `with_leader: bool` - заполнение строки символом `_`
 - `leader_width: float` - длинна заполнения символом `_` (учитывается только при `with_leader=True`, значение по умолчанию `6.8`)



```python

document.write(document, "Базовый пример использования", 
               paragraph_style=DefaultHeaderParagraphStyle, 
               text_style=DefaultHeaderTextStyle,
               size=12,
               bold=True,
               alignment=AlignParagraph.RIGHT # !!! без .value !!!
               ...
               )

```
или же:
```python

write_config = {
    "paragraph_style": DefaultHeaderParagraphStyle,
    "text_style": DefaultHeaderTextStyle,
    "size": 13,
    "bold": True,
    "space_after": 10
}

document.write(document, "Базовый пример использования", **write_config)

```

### TODO:

- [x] Реализовать многопоточное формирование документов при использовании `DocumentCreator`
- [x] Реализовать взаимодействие с таблицами
- [x] Реализовать запись в виде списка (Word)
- [x] Работа над документацией
- [x] Рефакторинг (при необходимости)

