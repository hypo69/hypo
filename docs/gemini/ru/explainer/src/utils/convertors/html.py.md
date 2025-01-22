## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:

1. **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.
2. **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,
    которые импортируются при создании диаграммы.
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!

    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]

        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
    ```

3. **<объяснение>**: Предоставьте подробные объяснения:
   - **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.
   - **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.
   - **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.
   - **Переменные**: Их типы и использование.
   - Выделите потенциальные ошибки или области для улучшения.

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**
```markdown
## <алгоритм>

1.  **`html2escape(input_str)`**:
    *   **Вход**: Строка `input_str`, представляющая HTML-код.
    *   **Обработка**: Вызывает метод `StringFormatter.escape_html_tags(input_str)`, который преобразует HTML-специальные символы (например, `<`, `>`, `&`) в их HTML-сущности (`&lt;`, `&gt;`, `&amp;`).
    *   **Выход**: Строка с HTML-сущностями.
    *   **Пример**: `<p>Hello</p>` -> `&lt;p&gt;Hello&lt;/p&gt;`

2.  **`escape2html(input_str)`**:
    *   **Вход**: Строка `input_str`, содержащая HTML-сущности.
    *   **Обработка**: Вызывает метод `StringFormatter.unescape_html_tags(input_str)`, который преобразует HTML-сущности обратно в соответствующие символы.
    *   **Выход**: Строка с HTML-кодом.
    *   **Пример**: `&lt;p&gt;Hello&lt;/p&gt;` -> `<p>Hello</p>`

3.  **`html2dict(html_str)`**:
    *   **Вход**: Строка `html_str`, представляющая HTML-код.
    *   **Инициализация**: Создается класс `HTMLToDictParser`, который наследует `HTMLParser`.
    *   **Обработка HTML**:
        *   `handle_starttag(tag, attrs)`: Записывает имя текущего тега (`tag`) в `self.current_tag`.
        *   `handle_endtag(tag)`: Очищает текущий тег (`self.current_tag` = `None`).
        *   `handle_data(data)`: Если есть текущий тег, записывает содержимое `data.strip()` в словарь `self.result` с ключом `self.current_tag`.
    *   **Разбор**: Создается экземпляр `HTMLToDictParser` и вызывается метод `parser.feed(html_str)` для разбора HTML.
    *   **Выход**: Словарь, где ключи - имена тегов, а значения - содержимое этих тегов.
    *   **Пример**: `<p>Hello</p><a href="link">World</a>` -> `{'p': 'Hello', 'a': 'World'}`

4.  **`html2ns(html_str)`**:
    *   **Вход**: Строка `html_str`, представляющая HTML-код.
    *   **Обработка**: Вызывает функцию `html2dict(html_str)` для преобразования HTML в словарь.
    *   **Выход**: `SimpleNamespace` объект, где ключи словаря становятся атрибутами, а значения - их значениями.
    *   **Пример**: `<p>Hello</p><a href="link">World</a>` -> `SimpleNamespace(p='Hello', a='World')`. Для доступа используется `result.p` вернет 'Hello', `result.a` вернет 'World'

5.  **`html2pdf(html_str, pdf_file)`**:
    *   **Вход**: Строка `html_str` с HTML-кодом, строка или `Path` `pdf_file` с именем файла PDF.
    *   **Обработка**:
        *   Создается объект `HTML(string=html_str)` из библиотеки `weasyprint`.
        *   Вызывается метод `write_pdf(pdf_file)` для создания PDF-файла по указанному пути.
    *   **Выход**: Возвращает `True` при успешном создании PDF-файла, `None` в случае ошибки.
    *   **Пример**:
        *   HTML: `<h1>Hello</h1><p>World</p>`
        *   PDF: Создаётся файл 'output.pdf' с содержимым "Hello" как заголовок и "World" как параграф.

## <mermaid>

```mermaid
flowchart TD
    Start[Начало] --> html2escape_call[html2escape(input_str)]
    html2escape_call --> StringFormatterEscape[StringFormatter.escape_html_tags(input_str)]
    StringFormatterEscape --> html2escape_return[Возврат: Строка с HTML-сущностями]
    html2escape_return --> End_html2escape[Конец html2escape]

    Start --> escape2html_call[escape2html(input_str)]
    escape2html_call --> StringFormatterUnescape[StringFormatter.unescape_html_tags(input_str)]
    StringFormatterUnescape --> escape2html_return[Возврат: Строка с HTML]
    escape2html_return --> End_escape2html[Конец escape2html]

    Start --> html2dict_call[html2dict(html_str)]
    html2dict_call --> HTMLToDictParser_init[HTMLToDictParser()]
    HTMLToDictParser_init --> parser_feed[parser.feed(html_str)]
    parser_feed --> handle_starttag[handle_starttag(tag, attrs)]
    parser_feed --> handle_endtag[handle_endtag(tag)]
    parser_feed --> handle_data[handle_data(data)]
    handle_data -->  HTMLToDictParser_return[Возврат: Словарь]
     HTMLToDictParser_return --> End_html2dict[Конец html2dict]


    Start --> html2ns_call[html2ns(html_str)]
    html2ns_call --> html2dict_call_2[html2dict(html_str)]
    html2dict_call_2 -->  SimpleNamespace_create[SimpleNamespace(**html_dict)]
    SimpleNamespace_create --> html2ns_return[Возврат: SimpleNamespace объект]
    html2ns_return --> End_html2ns[Конец html2ns]

   Start --> html2pdf_call[html2pdf(html_str, pdf_file)]
   html2pdf_call --> HTML_create[HTML(string=html_str)]
   HTML_create --> write_pdf[write_pdf(pdf_file)]
   write_pdf --> html2pdf_return[Возврат: True или None]
   html2pdf_return --> End_html2pdf[Конец html2pdf]


    classDef classStyle fill:#f9f,stroke:#333,stroke-width:2px
    class StringFormatterEscape,StringFormatterUnescape,HTMLToDictParser_init,parser_feed,handle_starttag,handle_endtag,handle_data,SimpleNamespace_create classStyle
```

## <объяснение>

### Импорты

*   `re`: Модуль для работы с регулярными выражениями. Используется, хотя в текущей версии кода для функции `html2pdf` удаление неподдерживаемых псевдоклассов вынесено в комментарии.
*   `typing.Dict`: Используется для аннотации типов, указывая, что функция `html2dict` возвращает словарь.
*   `pathlib.Path`: Модуль для работы с путями к файлам. Используется для указания пути к PDF-файлу.
*   `venv.logger`: Модуль логирования, используется для вывода сообщений об ошибках.
*   `src.logger.logger`: Импортирует настраиваемый логгер для проекта из `src.logger.logger`.
*   `types.SimpleNamespace`: Класс для создания простых объектов с атрибутами. Используется для преобразования HTML в объект, у которого теги будут атрибутами.
*   `html.parser.HTMLParser`: Класс для разбора HTML. Используется внутри `html2dict`.
*   `xhtml2pdf.pisa`: Модуль для конвертации HTML в PDF, удален и не используется в коде.
*   `weasyprint.HTML`: Модуль для конвертации HTML в PDF, используется в коде.

### Функции

1.  **`html2escape(input_str: str) -> str`**:
    *   **Аргументы**:
        *   `input_str`: строка, представляющая HTML код.
    *   **Возвращает**: Строку, в которой HTML-символы заменены на их соответствующие HTML-сущности.
    *   **Назначение**: Преобразует HTML-код в безопасную для отображения строку, избегая интерпретации браузером.
    *   **Пример**: `<p>Привет & мир</p>` преобразуется в `&lt;p&gt;Привет &amp; мир&lt;/p&gt;`

2.  **`escape2html(input_str: str) -> str`**:
    *   **Аргументы**:
        *   `input_str`: Строка с HTML-сущностями.
    *   **Возвращает**: Строку, в которой HTML-сущности заменены на соответствующие HTML-символы.
    *   **Назначение**: Преобразует строку с HTML-сущностями обратно в HTML-код.
    *   **Пример**: `&lt;p&gt;Привет &amp; мир&lt;/p&gt;` преобразуется в `<p>Привет & мир</p>`

3.  **`html2dict(html_str: str) -> Dict[str, str]`**:
    *   **Аргументы**:
        *   `html_str`: HTML-код в виде строки.
    *   **Возвращает**: Словарь, где ключи - это имена тегов, а значения - их содержимое.
    *   **Назначение**: Разбирает HTML-код и преобразует его в словарь.
    *   **Внутренний класс `HTMLToDictParser`**:
        *   `__init__(self)`: Инициализирует словарь `result` для хранения результатов и `current_tag` для отслеживания текущего тега.
        *   `handle_starttag(self, tag, attrs)`: Устанавливает `current_tag` на текущий тег.
        *   `handle_endtag(self, tag)`: Обнуляет `current_tag`.
        *   `handle_data(self, data)`: Если есть текущий тег, то добавляет содержимое этого тега в словарь `result`.
    *   **Пример**: `<p>Hello</p><a href="link">World</a>`  преобразуется в `{'p': 'Hello', 'a': 'World'}`

4.  **`html2ns(html_str: str) -> SimpleNamespace`**:
    *   **Аргументы**:
        *   `html_str`: HTML-код в виде строки.
    *   **Возвращает**: Объект `SimpleNamespace`, где атрибуты - имена HTML-тегов, а значения - их содержимое.
    *   **Назначение**: Преобразует HTML в объект с доступом к содержимому по имени тега.
    *   **Пример**: `<p>Hello</p><a href="link">World</a>`  преобразуется в объект `SimpleNamespace(p='Hello', a='World')`. Доступ: `result.p` вернёт "Hello", `result.a` вернёт "World".

5.  **`html2pdf(html_str: str, pdf_file: str | Path) -> bool | None`**:
    *   **Аргументы**:
        *   `html_str`: HTML-код в виде строки.
        *   `pdf_file`: Путь к PDF-файлу, строка или объект `Path`.
    *   **Возвращает**: `True` при успешном создании PDF, `None` в случае ошибки.
    *   **Назначение**: Конвертирует HTML-код в PDF-файл с использованием библиотеки `weasyprint`.
    *  **Обработка**:
        * Создаётся объект `HTML(string=html_str)` из библиотеки `weasyprint`.
        * Вызывается метод `write_pdf(pdf_file)` для создания PDF-файла по указанному пути.
    *   **Пример**: Преобразует HTML-код `<h1>Заголовок</h1><p>Текст</p>` в PDF-файл, в котором заголовок будет h1, а текст будет p.

### Переменные

*   `input_str`: Используется в функциях `html2escape` и `escape2html`, представляет собой строку, которая должна быть преобразована.
*   `html_str`: Используется в функциях `html2dict` и `html2ns`, представляет собой HTML-код в виде строки.
*   `pdf_file`: Используется в функции `html2pdf`, представляет собой путь к PDF-файлу, строка или объект `Path`.
*  `parser`: экземпляр класса `HTMLToDictParser` для разбора HTML в `html2dict`
*  `result`: словарь в `HTMLToDictParser` для хранения результатов разбора.
*  `current_tag`: строка в `HTMLToDictParser` для отслеживания текущего HTML тега.
*  `html_dict`: словарь, полученный из функции `html2dict`, который затем используется для создания объекта `SimpleNamespace`.

### Потенциальные ошибки и области для улучшения

1.  **Отсутствие обработки ошибок**: В функциях не обрабатываются возможные исключения (например, некорректный HTML-код). Стоит добавить блоки try-except.
2.  **Зависимость от сторонних библиотек**: Код зависит от сторонних библиотек, таких как `weasyprint`, `xhtml2pdf` которые могут отсутствовать. Необходимо предусмотреть проверку и установку этих зависимостей.
3.  **Неполная поддержка CSS**: При конвертации в PDF некоторые CSS-свойства могут не поддерживаться (хотя эта логика удалена из `html2pdf`). Необходимо учитывать это при формировании HTML для PDF.
4.  **Обработка атрибутов тегов**: В `html2dict` и `html2ns` не обрабатываются атрибуты тегов, только их содержимое. В будущем может потребоваться добавить эту функциональность.
5.  **Обработка вложенных тегов**: В `html2dict` при наличии вложенных тегов будет сохранено содержимое только внешнего тега.

### Взаимосвязи с другими частями проекта

*   Модуль является частью `src.utils.convertors`, то есть предназначен для преобразования различных форматов. Он может использоваться другими модулями для работы с HTML, например, для парсинга, форматирования или преобразования в другие форматы, такие как PDF.
*   Использование `src.logger.logger` обеспечивает централизованное логирование, что полезно для отладки и мониторинга приложения.
```