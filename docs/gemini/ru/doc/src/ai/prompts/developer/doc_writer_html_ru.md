# Модуль: doc_writer_html_ru

Этот модуль предоставляет класс `DocWriterHTMLRu` для генерации HTML-документации на русском языке из Python-кода.  Он использует Markdown для структуры документации.

## Пример использования

```python
# Пример использования класса DocWriterHTMLRu
from hypotez.src.ai.prompts.developer import doc_writer_html_ru

doc_writer = doc_writer_html_ru.DocWriterHTMLRu()
doc_writer.generate_documentation("your_file.py")
```

## Платформы
Этот модуль работает на платформах поддерживающих Python.

## Синопсис
Этот модуль предназначен для автоматической генерации документации в формате Markdown для Python-кода.  Он обрабатывает комментарии в коде и создает структурированные документы.


## Классы

### `DocWriterHTMLRu`

**Описание:** Класс для генерации HTML-документации на русском языке из Python-кода.

**Атрибуты:**

* `input_file`: Путь к файлу с Python-кодом.
* `output_file`: Путь к выходному файлу с HTML-документацией.
* `doc_templates`: Словарь шаблонов документации для различных типов элементов кода (модули, классы, функции).
* `template_path`: Путь к шаблону для HTML-документации (при необходимости).


**Методы:**

#### `generate_documentation(input_file: str, output_file: str = "documentation.html") -> None`

**Описание:** Генерирует HTML-документацию из Python-файла.

**Параметры:**

* `input_file` (str): Путь к входному файлу с Python-кодом.
* `output_file` (str, optional): Путь к выходному файлу HTML. По умолчанию "documentation.html".

**Возвращает:**

* `None`

**Вызывает исключения:**

* `FileNotFoundError`: Если входной файл не найден.
* `SyntaxError`: Если входной файл содержит синтаксические ошибки.
* `Exception`: При других непредвиденных ошибках.


#### `process_code(code: str) -> str`

**Описание:** Обрабатывает Python-код, извлекая информацию о классах, функциях и комментариях для генерации документации.

**Параметры:**

* `code` (str): Строка с Python-кодом.

**Возвращает:**

* `str`: Обработанный код в формате, подходящем для генерации документации.


#### `generate_html(markdown_content: str) -> str`

**Описание:** Преобразует Markdown-контент в HTML-формат.

**Параметры:**

* `markdown_content` (str): Markdown-документация.

**Возвращает:**

* `str`: HTML-документация.


```