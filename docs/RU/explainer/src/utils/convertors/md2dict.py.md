## <алгоритм>

1.  **`md2dict(md_string: str)`**:
    *   Принимает строку `md_string` в формате Markdown.
    *   Пытается извлечь JSON содержимое с помощью `extract_json_from_string(md_string)`.
        *   **Пример:** Если `md_string = "Some text {\\"key\\": \\"value\\"}"`, то будет вызван `extract_json_from_string`.
    *   Если JSON найден, возвращает словарь `{"json": json_content}`.
        *   **Пример:**  `return {"json": {"key": "value"}}`.
    *   Если JSON не найден, преобразует `md_string` в HTML с помощью `markdown(md_string)`.
        *   **Пример:** Если `md_string = "# Section\nText"`, то  `html` будет `<h1>Section</h1>\n<p>Text</p>`.
    *   Инициализирует пустой словарь `sections` и переменную `current_section`.
    *   Разбивает HTML на строки и итерируется по ним.
        *   Для каждой строки проверяет, начинается ли она с тега заголовка `<h`.
        *   Если это заголовок, извлекает уровень заголовка и его текст.
            *   **Пример:** Для `<h1 class="some_class">Section Title</h1>`,  `heading_level` будет 1, `section_title` будет "Section Title".
        *   Если уровень заголовка 1, создает новую секцию в `sections`.
            *   **Пример:** `sections = {"Section Title": []}`.
        *   Если уровень заголовка больше 1, добавляет текст заголовка в текущую секцию, если она есть.
            *    **Пример:** Если  `sections = {"Section Title": []}` и  `line = "<h2>Sub Section</h2>"`
                 то `sections = {"Section Title": ["Sub Section"]}`.
        *   Если строка не заголовок, и текущая секция есть, добавляет текст строки в текущую секцию.
            *   **Пример:** Если `sections = {"Section Title": []}` и  `line = "<p>Some text</p>"`, то  `sections = {"Section Title": ["Some text"]}`.
    *   Возвращает словарь `sections`.
        *   **Пример:** `return {"Section Title": ["Some text", "Sub Section"]}`.
    *   При возникновении ошибки логирует её и возвращает пустой словарь.

2.  **`extract_json_from_string(text: str)`**:
    *   Принимает строку `text`.
    *   Пытается найти JSON контент в строке с помощью регулярного выражения `r"\\{.*\\}"`.
        *   **Пример:**  Если `text = "Some text {\\"key\\": \\"value\\"}"`, то JSON будет найден.
    *   Если JSON найден, преобразует его в словарь с помощью `eval()` и возвращает.
        *   **Пример:**  `return {"key": "value"}`.
    *   Если JSON не найден, возвращает `None`.
    *   При возникновении ошибки логирует её и возвращает `None`.

## <mermaid>

```mermaid
flowchart TD
    Start(Start) --> Md2DictFunc[<code>md2dict(md_string)</code><br>Convert Markdown to Dict];
    Md2DictFunc --> ExtractJsonCall{Call <code>extract_json_from_string(md_string)</code>};
    ExtractJsonCall -- JSON Found --> ReturnJson{"Return <code>{'json': json_content}</code>"};
    ExtractJsonCall -- JSON Not Found --> MarkdownConvert[<code>html = markdown(md_string)</code><br>Convert Markdown to HTML];
    MarkdownConvert --> InitSections[<code>sections = {}</code><br>Initialize Sections Dictionary];
     InitSections --> IterateHTML[Iterate through <code>html.splitlines()</code>];
     IterateHTML -- Line is Heading --> HeadingLevelCheck{Check Heading Level};
     HeadingLevelCheck -- Level 1 --> CreateNewSection[Create New Section in <code>sections</code>];
      CreateNewSection --> IterateHTML
    HeadingLevelCheck -- Level > 1 --> AddSubheadingToSection{Add Subheading to current section if exists};
    AddSubheadingToSection --> IterateHTML
    IterateHTML -- Line is not Heading and has text --> AddTextToSection{Add text to current section};
    AddTextToSection --> IterateHTML
      IterateHTML -- No More Lines --> ReturnSections[Return <code>sections</code>];
      IterateHTML -- Exception --> LogErrorMd2Dict[Log Error];
    LogErrorMd2Dict --> ReturnEmptyDict[Return <code>{}</code>];
    ReturnSections --> End(End);
    ReturnJson --> End;
    
   
    
    ExtractJsonCall -- Exception --> LogErrorExtractJson[Log Error];
    LogErrorExtractJson --> ReturnNoneExtractJson[Return <code>None</code>];
    ReturnNoneExtractJson --> MarkdownConvert;
   
```

```mermaid
flowchart TD
    Start(Start) --> ExtractJsonFunc[<code>extract_json_from_string(text)</code><br>Extract JSON from String];
    ExtractJsonFunc --> FindJson{Find JSON using Regex};
    FindJson -- JSON Found --> EvalJson[<code>json_match.group()</code><br>Convert JSON with eval];
    EvalJson --> ReturnJsonContent[Return JSON Dict];
    FindJson -- JSON Not Found --> ReturnNone[Return <code>None</code>];
      ExtractJsonFunc -- Exception --> LogErrorExtractJsonString[Log Error];
    LogErrorExtractJsonString --> ReturnNoneString[Return <code>None</code>];
    ReturnJsonContent --> End(End);
    ReturnNone --> End;
    ReturnNoneString --> End
```
### Импорты в mermaid диаграмме:

*   `markdown`:  Импортируется из библиотеки `markdown2`. Используется для преобразования Markdown текста в HTML.
*   `re`:  Импортируется из стандартной библиотеки Python. Используется для работы с регулярными выражениями, в частности, для извлечения JSON и анализа заголовков HTML.
*   `logger`:  Импортируется из `src.logger.logger`. Используется для логирования ошибок в функциях.

## <объяснение>

### Импорты:
*   **`import re`**:
    *   **Назначение:** Модуль `re` (regular expressions) используется для работы с регулярными выражениями.
    *   **Взаимосвязь:** В этом модуле `re` применяется для:
        *   Поиска JSON объектов в тексте с помощью `re.search(json_pattern, text, re.DOTALL)`.
        *   Извлечения уровня заголовка HTML с помощью `re.search(r'h(\\d)', line)`.
        *   Удаления HTML тегов из текста с помощью `re.sub(r'<.*?>', '', line)`.
*   **`from typing import Dict`**:
    *   **Назначение:** Модуль `typing` используется для статической типизации.
    *   **Взаимосвязь:** `Dict` используется для указания типов данных возвращаемых словарей.
*   **`from markdown2 import markdown`**:
    *   **Назначение:** Функция `markdown` из библиотеки `markdown2` преобразует Markdown текст в HTML.
    *  **Взаимосвязь:**  Используется в `md2dict` для конвертации входной строки `md_string` в HTML перед дальнейшей обработкой.
*   **`from src.logger.logger import logger`**:
    *   **Назначение:**  Импортирует объект `logger` для логирования ошибок.
    *   **Взаимосвязь:**  Используется для записи ошибок в лог в функциях `md2dict` и `extract_json_from_string`.

### Функции:

*   **`md2dict(md_string: str) -> Dict[str, dict | list]`**:
    *   **Аргументы**:
        *   `md_string (str)`: Строка Markdown для конвертации.
    *   **Возвращаемое значение**:
        *   `Dict[str, dict | list]`: Словарь, представляющий структуру Markdown. Если найден JSON, то ключ `json` будет содержать JSON. В противном случае структура markdown будет представлена в виде словаря секций.
    *   **Назначение**: Конвертирует строку Markdown в структурированный словарь. Извлекает JSON, если он есть, или делит Markdown на секции, основываясь на заголовках.
    *   **Пример:**
        ```python
        md_string_with_json = "Some text {\\"key\\": \\"value\\"}"
        result_with_json = md2dict(md_string_with_json) # result_with_json = {"json": {"key": "value"}}

        md_string_with_markdown = "# Section 1\nSome Text\n## Sub Section\nMore Text"
        result_with_markdown = md2dict(md_string_with_markdown)
        # result_with_markdown = {"Section 1": ["Some Text", "Sub Section", "More Text"]}

        md_string_with_nested_markdown = "# Section 1\nSome Text\n## Sub Section\nMore Text\n### Sub-sub section\nSub-sub text"
        result_with_nested_markdown = md2dict(md_string_with_nested_markdown)
        # result_with_nested_markdown = {"Section 1": ["Some Text", "Sub Section", "More Text", "Sub-sub section", "Sub-sub text"]}
        ```
*   **`extract_json_from_string(text: str) -> dict | None`**:
    *   **Аргументы**:
        *   `text (str)`: Строка для извлечения JSON.
    *   **Возвращаемое значение**:
        *   `dict | None`: Извлеченный JSON (словарь) или `None`, если JSON не найден.
    *   **Назначение**: Извлекает JSON из строки.
    *   **Пример**:
        ```python
        text_with_json = "Some text {\\"key\\": \\"value\\"}"
        extracted_json = extract_json_from_string(text_with_json) # extracted_json = {"key": "value"}

        text_without_json = "Some text"
        extracted_none = extract_json_from_string(text_without_json) # extracted_none = None
        ```

### Переменные:

*   `md_string` (в `md2dict`): Строка с Markdown текстом.
*   `html` (в `md2dict`): HTML строка, полученная после конвертации Markdown.
*   `sections` (в `md2dict`): Словарь, где ключами являются названия секций, а значениями - список строк секции (либо подзаголовки, либо текст).
*   `current_section` (в `md2dict`): Текущая секция, в которую добавляется текст или подзаголовок.
*    `line` (в `md2dict`):  Строка HTML кода.
*   `heading_level_match` (в `md2dict`): Результат поиска уровня заголовка в HTML теге.
*   `heading_level` (в `md2dict`): Уровень заголовка.
*   `section_title` (в `md2dict`):  Текст заголовка.
*   `clean_text` (в `md2dict`):  Строка текста без HTML тегов.
*   `json_pattern` (в `extract_json_from_string`): Регулярное выражение для поиска JSON.
*   `json_match` (в `extract_json_from_string`): Результат поиска JSON с помощью регулярного выражения.
*   `text` (в `extract_json_from_string`): Строка, из которой извлекается JSON.
*  `json_content`: Результат извлечения JSON из строки

### Потенциальные ошибки и области для улучшения:

*   **Безопасность `eval`:** Функция `extract_json_from_string` использует `eval` для преобразования JSON, что является потенциально небезопасным. В рабочей среде следует использовать `json.loads` для безопасного преобразования JSON.
*   **Обработка ошибок:** В `extract_json_from_string` обрабатывается только общее исключение. Возможно, следует обрабатывать `json.JSONDecodeError` для более точного логирования ошибок при парсинге JSON.
*   **Сложная структура Markdown:** Код обрабатывает только заголовки и текст. Он не обрабатывает сложные структуры Markdown, такие как таблицы, списки и т.д.
*   **Оптимизация:**  Регулярное выражение для поиска JSON может быть оптимизировано.
* **Обработка вложенности:** Алгоритм не предусматривает вложенности секций. Подзаголовки добавляются как элементы в текущую секцию.

### Взаимосвязь с другими частями проекта:

*   **`src.logger.logger`**: Используется для логирования ошибок в модуле `src.utils.convertors.md2dict`. Это позволяет отслеживать проблемы, возникающие при конвертации Markdown в словарь.
*   **`markdown2`**: Внешняя библиотека, необходимая для конвертации Markdown в HTML.

Этот модуль `md2dict.py` служит важным звеном в конвейере обработки текстовых данных, позволяя извлекать структурированную информацию из Markdown файлов. Он может быть частью более крупной системы, где Markdown используется для хранения данных, конфигураций или пользовательского контента, который нужно автоматически обработать.