## <алгоритм>

**Модуль `normalizer`** предназначен для преобразования и очистки данных различных типов. Он включает в себя функции для нормализации строк, булевых значений, целых чисел, чисел с плавающей точкой и дат.

**1. `normalize_boolean(input_data)`:**
   - **Вход:** `input_data` (любой тип данных).
   - **Проверка:** Проверяется тип данных и значение `input_data`. Если значение входит в предопределенный список ("yes", "true", "1", `True`) или является 1, то возвращает `True`. Если в ("no", "false", "0", `False`) или 0 - возвращает `False`.
   - **Обработка:** Если значение не распознано как `True` или `False` - возвращает `False`.
   - **Пример:**
     - `normalize_boolean('yes')` → `True`
     - `normalize_boolean(0)` → `False`
     - `normalize_boolean('invalid')` → `False`

**2. `normalize_string(input_data)`:**
   - **Вход:** `input_data` (строка или список строк).
   - **Преобразование:** Если `input_data` - список, объединяет элементы в строку.
   - **Удаление:** Удаляет символы новой строки, HTML-теги и специальные символы из полученной строки.
   - **Пример:**
     - `normalize_string(['  Example string  ', '<b>with HTML</b>'])` → `'Example string with HTML'`
     - `normalize_string('  text \\n with breaks  ')` → `'text  with breaks'`
     - `normalize_string('<p>Some Text!</p>')` → `'Some Text!'`

**3. `normalize_int(input_data)`:**
   - **Вход:** `input_data` (строка, целое число, число с плавающей запятой, Decimal).
   - **Преобразование:** Преобразует входные данные в целое число.
   - **Обработка ошибок:** Если преобразование невозможно, возвращает 0.
   - **Пример:**
     - `normalize_int('42')` → `42`
     - `normalize_int(3.14)` → `3`
     - `normalize_int('invalid')` → `0`

**4. `normalize_float(input_data)`:**
   - **Вход:** `input_data` (число, строка, список чисел).
   - **Обработка:** Если `input_data` - список, преобразует каждый элемент в число с плавающей точкой и возвращает список. Если `input_data` - строка или число, преобразует в число с плавающей точкой.
   - **Обработка ошибок:** Если преобразование невозможно, возвращает `None`.
   - **Пример:**
     - `normalize_float('3.14')` → `3.14`
     - `normalize_float([1, '2.5', 3])` → `[1.0, 2.5, 3.0]`
     - `normalize_float('invalid')` → `None`

**5. `remove_line_breaks(input_str)`:**
   - **Вход:** `input_str` (строка).
   - **Удаление:** Удаляет символы новой строки из строки.
   - **Пример:**
     - `remove_line_breaks('String\\nwith line breaks\\r')` → `'Stringwith line breaks'`

**6. `remove_html_tags(input_html)`:**
   - **Вход:** `input_html` (строка).
   - **Удаление:** Удаляет HTML теги из строки.
   - **Пример:**
     - `remove_html_tags('<p>Example text</p>')` → `'Example text'`

**7. `remove_special_characters(input_str)`:**
   - **Вход:** `input_str` (строка или список строк).
   - **Удаление:** Удаляет специальные символы из строки или списка строк.
   - **Пример:**
     - `remove_special_characters('Hello@World!')` → `'HelloWorld'`
     - `remove_special_characters(['Hello@', 'World!'])` → `['Hello', 'World']`

**8. `normalize_sql_date(input_data)`:**
   - **Вход:** `input_data` (строка или объект `datetime`).
   - **Преобразование:** Преобразует входные данные в строку формата `YYYY-MM-DD`.
   - **Пример:**
     - `normalize_sql_date('2024-12-06')` → `'2024-12-06'`
     - `normalize_sql_date(datetime(2024, 12, 6))` → `'2024-12-06'`

## <mermaid>

```mermaid
flowchart TD
    Start[Начало] --> normalizeBooleanCall(<code>normalize_boolean</code>)
    normalizeBooleanCall --> normalizeBooleanEnd{Результат: Bool}

    Start --> normalizeStringCall(<code>normalize_string</code>)
    normalizeStringCall --> removeLineBreaksCall(<code>remove_line_breaks</code>)
    removeLineBreaksCall --> removeHtmlTagsCall(<code>remove_html_tags</code>)
    removeHtmlTagsCall --> removeSpecialCharactersCall(<code>remove_special_characters</code>)
    removeSpecialCharactersCall --> normalizeStringEnd{Результат: String}

    Start --> normalizeIntCall(<code>normalize_int</code>)
    normalizeIntCall --> normalizeIntEnd{Результат: Int}

    Start --> normalizeFloatCall(<code>normalize_float</code>)
    normalizeFloatCall --> normalizeFloatEnd{Результат: Float or List[Float] or None}

    Start --> removeLineBreaksCall2(<code>remove_line_breaks</code>)
    removeLineBreaksCall2 --> removeLineBreaksEnd{Результат: String}

    Start --> removeHtmlTagsCall2(<code>remove_html_tags</code>)
    removeHtmlTagsCall2 --> removeHtmlTagsEnd{Результат: String}

     Start --> removeSpecialCharactersCall2(<code>remove_special_characters</code>)
    removeSpecialCharactersCall2 --> removeSpecialCharactersEnd{Результат: String or List[String]}

    Start --> normalizeSqlDateCall(<code>normalize_sql_date</code>)
    normalizeSqlDateCall --> normalizeSqlDateEnd{Результат: Date String}

    style Start fill:#f9f,stroke:#333,stroke-width:2px
```

## <объяснение>

**Импорты:**

-   Модуль `normalizer` не имеет явных импортов, что говорит о его автономности и независимости от других частей проекта, кроме стандартных библиотек Python. Однако, из описания кода следует, что модуль использует `src.logger` для логирования, но данный факт не отражен в предоставленном коде.

**Классы:**
   - В данном модуле нет классов. Весь функционал реализован с помощью функций.

**Функции:**

1.  **`normalize_boolean(input_data)`:**
    -   **Аргументы:** `input_data` - входное значение любого типа.
    -   **Возвращает:** `bool` - `True` если `input_data` представляет истинное значение, в противном случае `False`.
    -   **Назначение:** Приводит входные данные к логическому типу.
    -   **Пример:**
        -   `normalize_boolean("yes")` вернет `True`.
        -   `normalize_boolean(0)` вернет `False`.

2.  **`normalize_string(input_data)`:**
    -   **Аргументы:** `input_data` - строка или список строк.
    -   **Возвращает:** `str` - нормализованная строка в кодировке UTF-8.
    -   **Назначение:** Очищает строку от лишних пробелов, HTML тегов и специальных символов.
    -   **Пример:**
        -   `normalize_string(['  example ', '<b>html</b>'])` вернет `'example html'`.

3.  **`normalize_int(input_data)`:**
    -   **Аргументы:** `input_data` - строка, целое, число с плавающей точкой или Decimal.
    -   **Возвращает:** `int` - преобразованное целое число.
    -   **Назначение:** Преобразует входные данные в целое число.
    -   **Пример:**
        -   `normalize_int('42')` вернет `42`.
        -   `normalize_int(3.14)` вернет `3`.

4.  **`normalize_float(input_data)`:**
    -   **Аргументы:** `input_data` - число, строка или список чисел.
    -   **Возвращает:** `float` или `List[float]` или `None` - число с плавающей точкой, список таких чисел или None, если преобразование невозможно.
    -   **Назначение:** Преобразует входные данные в число с плавающей точкой.
    -   **Пример:**
        -   `normalize_float('3.14')` вернет `3.14`.
        -   `normalize_float([1, '2.5'])` вернет `[1.0, 2.5]`.

5.  **`remove_line_breaks(input_str)`:**
    -   **Аргументы:** `input_str` - входная строка.
    -   **Возвращает:** `str` - строка без символов новой строки.
    -   **Назначение:** Удаляет символы новой строки из строки.
    -   **Пример:**
        -   `remove_line_breaks('text\\nwith\\rbreaks')` вернет `'textwithbreaks'`.

6.  **`remove_html_tags(input_html)`:**
    -   **Аргументы:** `input_html` - входная строка с HTML-тегами.
    -   **Возвращает:** `str` - строка без HTML тегов.
    -   **Назначение:** Удаляет HTML теги из строки.
    -   **Пример:**
        -   `remove_html_tags('<p>text</p>')` вернет `'text'`.

7.  **`remove_special_characters(input_str)`:**
    -   **Аргументы:** `input_str` - строка или список строк.
    -   **Возвращает:** `str` или `List[str]` - строка или список строк без специальных символов.
    -   **Назначение:** Удаляет специальные символы из строки или списка строк.
    -   **Пример:**
        -   `remove_special_characters('text@!')` вернет `'text'`.
        -   `remove_special_characters(['text@', '!'])` вернет `['text', '']`.

8. **`normalize_sql_date(input_data)`:**
   -   **Аргументы:** `input_data` - строка или объект `datetime`.
   -   **Возвращает:** `str` - нормализованная дата в формате `YYYY-MM-DD`.
   -   **Назначение:** Преобразует входную дату в формат SQL.
   -   **Пример:**
        -   `normalize_sql_date('2024-12-06')` вернет `'2024-12-06'`

**Переменные:**

- В данном коде нет глобальных переменных. Все данные передаются через аргументы функций.

**Потенциальные ошибки и области для улучшения:**

-   **Отсутствует обработка ошибок в функциях `remove_html_tags` и `remove_special_characters`**: Если входные данные не соответствуют ожидаемым, функции могут возвращать неожиданные результаты или вызывать исключения.
-   **Жесткая зависимость от строковых представлений `True`/`False`:** функция `normalize_boolean` может работать некорректно в случае, если значения true и false представлены на других языках.
-   **Нет механизма для определения root проекта:** В требованиях упоминается использование `src.logger`. В таком случае, желательно добавить импорт `header` для определения root проекта.

**Цепочка взаимосвязей:**

-   Модуль `normalizer` может использоваться в различных частях проекта, где требуется преобразование или очистка данных. В примере использования видно, что функции импортируются и используются для обработки данных.
-   Упоминается использование `src.logger` для логирования, что указывает на связь с модулем логирования.
-   Модуль предназначен для работы с данными из разных источников, включая пользовательский ввод, данные из баз данных и внешних API, что указывает на его важную роль в конвейере обработки данных проекта.