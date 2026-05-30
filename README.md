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
***

## Базовый пример использования

### Классическая запись в стиле `python-docx`

```python

from py_docx_creator.core.document.document import Document

text = "Пример классической записи"

document = Document("Документ.docx")
paragraph = document.add_paragraph_to_document()
run = document.add_run_to_paragraph(paragraph, text)
document.save_document()

```

***

### Быстрая запись

Реализована быстрая запись с помощью метода `write`. При такой записи момент создания параграфа и наполнение run-а пропускается.
Стили в свою очередь для параграфа и текста в нем определяются классами стилей. В данном примере используются стандартные классы стилей
`DefaultHeaderParagraphStyle` для параграфа и `DefaultHeaderTextStyle` для текста в нем.

```python

from py_docx_creator.core.document.document import Document
from py_docx_creator.default_style_preset.default_paragraph_style import DefaultHeaderParagraphStyle
from py_docx_creator.default_style_preset.default_text_style import DefaultHeaderTextStyle

document = Document("Документ.docx")
document.write("Пример быстрой записи", paragraph_style=DefaultHeaderParagraphStyle, text_style=DefaultHeaderTextStyle)
document.save_document()

```

***

### Fluent запись

Реализована возможность записи в стиле `Fluent` где последовательно описываются стили записываемого параграфа и текста. 
При таком подходе каждая запись оканчивается методом `.add()` который записывает параграф в документ с заданным текстом и возвращает картеж из записанного параграфа и run-a (`tuple[Paragraph, Run]`).

```python

from py_docx_creator.core.document.document import Document
from py_docx_creator.enums.enum_align_paragraph import AlignParagraph


document = Document("Документ.docx")
document.paragraph("Пример Fluent записи").size(32).bold(True).italic(True).line_spacing(12).alignment(AlignParagraph.CENTER).add()
document.save_document()

```

***

### Создание документа по инструкции

Предусмотрена возможность прописать шаги формирования документа в отдельной функции типа `Callable`. Аргументы такой функции задаются в отдельном поле класса `Document`.

*** _Важный момент при написании функции-инструкции. 
Для корректной работы первый позиционный аргумент данной функции (в данном примере `doc: Document`) 
обязательно должен быть экземпляр класса `Document`. 
Данный аргумент является системным и прокидывается автоматически при выполнении кода._

```python

from py_docx_creator.core.document.document import Document
from py_docx_creator.default_style_preset.default_paragraph_style import DefaultHeaderParagraphStyle
from py_docx_creator.default_style_preset.default_text_style import DefaultHeaderTextStyle

def instruction(doc: Document, **kwargs):
    file_name = kwargs.get("name", "document.docx")
    doc.name = file_name
    # Классическая запись
    paragraph = doc.add_paragraph_to_document()
    run = doc.add_run_to_paragraph(paragraph, f"{file_name} - Пример классической записи")
    # Быстрая запись
    doc.write(f"{file_name} - Пример быстрой записи", paragraph_style=DefaultHeaderParagraphStyle, text_style=DefaultHeaderTextStyle)
    # Fluent запись
    doc.paragraph(f"{file_name} - Пример Fluent записи").italic(True).size(18).first_line_indent(30).space_after(30).add()
    doc.save_document()

document = Document("document.docx")
document.creation_instruction = instruction # инструкция по формированию документа
document.instruction_kwargs = {"name": "Конвейерное создание документов.docx"} # аргументы выполняемой функции
document.run_instruction() # запуск формирования документа 

```

***

### Конвейерное формирование документов

Реализован простой агрегатор для конвейерного формирования документов `DocumentCreator`. 

```python

from py_docx_creator.core.document.document import Document
from py_docx_creator.core.document.document_creator import DocumentCreator
from py_docx_creator.default_style_preset.default_paragraph_style import DefaultHeaderParagraphStyle
from py_docx_creator.default_style_preset.default_text_style import DefaultHeaderTextStyle


def instruction(doc: Document, **kwargs):
    file_name = kwargs.get("name", "document.docx")
    # Классическая запись
    paragraph = doc.add_paragraph_to_document()
    run = doc.add_run_to_paragraph(paragraph, f"{file_name} - Пример классической записи")
    # Быстрая запись
    doc.write(f"{file_name} - Пример быстрой записи", paragraph_style=DefaultHeaderParagraphStyle, text_style=DefaultHeaderTextStyle)
    # Fluent запись
    doc.paragraph(f"{file_name} - Пример Fluent записи").italic(True).size(18).first_line_indent(30).space_after(30).add()
    doc.save_document()

document_creator = DocumentCreator()
for i in range(10):  # имитация конвейера
    document: Document = Document(f"{i}.docx")
    document.creation_instruction = instruction  # инструкция по формированию документа
    document.instruction_kwargs = {"name": f"{i}.docx"}  # аргументы выполняемой функции
    document_creator.add_document(document)  # список экземпляров `Document` готовых к формированию

document_creator.start_creating_documents()  # запуск формирования всех документов

```

Формирование документов по умолчанию происходит в многопоточном режиме (`use_threads=True`, `use_multiprocess=False`). 
Количество одновременно работающих потоков задается атрибутом
`chunk_size` у класса `DocumentCreator` (по умолчанию `chunk_size = 5`).

Предусмотрена возможность формирования документов в `multiprocess` режиме. 

```python
document_creator.start_creating_documents(use_threads=False, use_multiprocess=True)
```

Также предусмотрена возможность формирования документов в `multiprocess + thread` режиме. 


```python
document_creator.start_creating_documents(use_threads=True, use_multiprocess=True)
```

При таком подходе документы для формирования разбиваются на чанки равные `chunk_size` и запускаются процессы 
количество которых равно`chunk_size`. В каждом процессе запускаются потоки. Количество одновременно работающих потоков
в каждом из процессов равно `chunk_size`.

*** _Рекомендуется использовать при большом объеме создаваемых документов со сложной структурой (инструкцией)._

***

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

***

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
    alignment = AlignParagraph.LEFT

class MyPageStyle(DefaultPageStyle): # Стиль страницы
    left_margin = 200.0

document = Document("Документ.docx")
document.apply_style(document, style=MyPageStyle) # пример того как задать стиль страницы `PageStyle`
document.write("Базовый пример использования", paragraph_style=MyParagraphStyle, text_style=MyTextStyle)
document.save_document()

```

При необходимости есть возможность создать стиль с нуля. Для этого необходимо наследоваться от базовых классов.

- `PageStyle` - для стилей страницы
- `ParagraphStyle` - для стилей параграфа
- `TextStyle` - для стилей текста

***

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
 - `base_paragraph_style` - базовый стиль параграфа (список, нумерованный список, ...)



```python

document.write("Базовый пример использования", 
               paragraph_style=DefaultHeaderParagraphStyle, 
               text_style=DefaultHeaderTextStyle,
               size=12,
               bold=True,
               alignment=AlignParagraph.RIGHT
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

document.write("Базовый пример использования", **write_config)

```

***

### Автоматический сброс нумерации списков

По умолчанию в `python-docx` встроенные нумерованные списки связываются в один глобальный список по всему документу. 
Если вы создаете список, затем прерываете его обычным текстом, а ниже создаете новый список, его нумерация не начнется заново, 
а продолжится с предыдущего места.

Реализовано решение данной проблемы. Если между двумя нумерованными абзацами появляется текст без стиля списка, 
библиотека принудительно разрывает связь и начинает нумерацию следующего списка с 1.

### TODO:

- [x] Реализовать многопоточное формирование документов при использовании `DocumentCreator`
- [ ] Реализовать взаимодействие с таблицами
- [x] Реализовать запись в виде списка (Word)
- [ ] Работа над документацией
- [ ] Рефакторинг (при необходимости)

