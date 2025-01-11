## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:  

1.  **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.  
2.  **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости, 
    которые импортируются при создании диаграммы. 
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`, 
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!  
    
    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:\
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]
    
        Header --> import[Import Global Settings: <br><code>from src import gs</code>] 
    ```

3.  **<объяснение>**: Предоставьте подробные объяснения:  
   - **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.  
   - **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.  
   - **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.  
   - **Переменные**: Их типы и использование.  
   - Выделите потенциальные ошибки или области для улучшения.  

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).  

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**

## <алгоритм>

**1. `normalize_boolean(input_data)`**
   - Принимает `input_data` любого типа.
   - Если `input_data` - булево значение, возвращает его.
   - Приводит `input_data` к строке, удаляет пробелы и переводит в нижний регистр.
   - Если строка входит в набор `{"true", "1", "yes", "y", "on", True, 1}`, возвращает `True`.
    - Пример: `"  yes  "` -> `"yes"` -> `True`
   - Если строка входит в набор `{"false", "0", "no", "n", "off", False, 0}`, возвращает `False`.
    - Пример: `"  false "` -> `"false"` -> `False`
   - Логирует ошибку и возвращает исходное значение в случае ошибки или если строка не соответствует ни одному из шаблонов.
   - Пример: `"invalid"` -> возвращает `"invalid"`

**2. `normalize_string(input_data)`**
   - Принимает строку или список строк `input_data`.
   - Если `input_data` пустая, возвращает пустую строку.
   - Если `input_data` не строка и не список, выбрасывает `TypeError`.
   - Если `input_data` список, объединяет его в строку через пробел.
    - Пример: `["Hello", "World"]` -> `"Hello World"`
   - Последовательно применяет `remove_html_tags`, `remove_line_breaks`, и `remove_special_characters`.
   - Удаляет лишние пробелы и кодирует/декодирует в UTF-8.
    - Пример:  `"  <p>Hello</p> \n World! #  "` -> `"Hello World!"`
   - Логирует ошибку и возвращает исходное значение, закодированное в UTF-8, если возникает исключение.

**3. `normalize_int(input_data)`**
   - Принимает `input_data` как строку, целое число, число с плавающей точкой или `Decimal`.
   - Если `input_data` типа `Decimal`, преобразует в `int`.
    - Пример: `Decimal('42')` -> `42`
   - Преобразует `input_data` в `float`, затем в `int`.
    - Пример: `"42.5"` -> `42.5` -> `42`
   - Логирует ошибку и возвращает исходное значение в случае ошибки конвертации.

**4.  `normalize_float(value)`**
    - Принимает `value` любого типа.
    - Если `value` равно `None`, `0` или пустой список/кортеж, возвращает 0.
    - Если `value` список/кортеж, рекурсивно вызывает `normalize_float` для каждого элемента и возвращает список `float` значений, пропуская `None`.
     - Пример: `[1, "2.5", None, 3]` -> `[1.0, 2.5, 3.0]`
    - Пытается преобразовать `value` в `float`.
     - Пример: `"3.14"` -> `3.14`
    - Логирует предупреждение и возвращает исходное значение если не удаётся преобразовать.

**5.  `normalize_sql_date(input_data)`**
    - Принимает `input_data` как строку или объект `datetime`.
    - Если `input_data` строка, пытается распарсить дату, используя форматы `%Y-%m-%d`, `%m/%d/%Y`, `%d/%m/%Y`
        - Пример: `"2024-01-01"` -> `"2024-01-01"`, `"01/01/2024"` -> `"2024-01-01"`
    - Если `input_data` это `datetime`, форматирует его в `YYYY-MM-DD`.
        - Пример: `datetime(2024, 1, 1)` -> `"2024-01-01"`
    - Логирует ошибку и возвращает исходное значение в случае ошибки.
    - Пример: `"invalid date"` -> `"invalid date"`

**6. `simplify_string(input_str)`**
    - Принимает строку `input_str`.
    - Удаляет все символы, кроме букв, цифр и пробелов.
        - Пример: `"It's a test! 123"` -> `"Its a test 123"`
    - Заменяет пробелы на подчеркивания.
         - Пример: `"Its a test 123"` -> `"Its_a_test_123"`
    - Удаляет повторяющиеся подчеркивания.
         - Пример: `"Its__a__test_123"` -> `"Its_a_test_123"`
    - Логирует ошибку и возвращает исходную строку в случае ошибки.

**7. `remove_line_breaks(input_str)`**
   - Принимает строку `input_str`.
   - Заменяет `\n` и `\r` на пробелы, удаляет пробелы в начале и конце строки.
     - Пример: `"Hello\nWorld\r"` -> `"Hello World"`

**8. `remove_html_tags(input_html)`**
   - Принимает строку `input_html`.
   - Удаляет HTML теги.
     - Пример:  `"<p>Hello</p>"` -> `"Hello"`

**9. `remove_special_characters(input_str, chars=None)`**
   - Принимает строку или список строк `input_str` и список символов `chars` для удаления.
   - Если `chars` не задан, то по умолчанию используется список `['#']`.
   -  Создает регулярное выражение на основе списка `chars`.
   - Если `input_str` - список, применяет регулярное выражение к каждому элементу.
    - Пример: `["Hello#", "World#"], chars=["#"]` -> `["Hello", "World"]`
   - Если `input_str` - строка, применяет регулярное выражение к строке.
     - Пример:  `"Hello#"` -> `"Hello"`

**10. `normalize_sku(input_str)`**
    - Принимает строку `input_str`, представляющую SKU.
    - Удаляет `"מקט"` или `"מק'ט"` (игнорируя регистр).
        - Пример: `"מקט: 303235"` -> `": 303235"`
    - Удаляет все не-буквенно-цифровые символы.
       - Пример: `": 303235"` -> `"303235"`
    - Логирует ошибку и возвращает исходное значение в случае ошибки.
    
## <mermaid>

```mermaid
flowchart TD
    subgraph Normalization Functions
        normalizeBoolean(input_data) -->|bool| returnBool(bool)
        normalizeBoolean(input_data) -->|string| processString(input_data)
        processString(input_data) -- yes --> returnTrue(True)
        processString(input_data) -- no --> returnFalse(False)
        processString(input_data) -- unexpected --> returnOriginalInput(original_input)
        
        normalizeString(input_data) -->|input is empty| returnEmptyString("")
        normalizeString(input_data) -->|not str or list| throwTypeError(TypeError)
        normalizeString(input_data) -->|is list| joinListToString(input_data)
        joinListToString(input_data) --> cleanedString(cleaned_str)
        cleanedString(cleaned_str) --> removeHTML(cleaned_str)
        removeHTML(cleaned_str) --> removeLineBreaks(cleaned_str)
        removeLineBreaks(cleaned_str) --> removeSpecialChars(cleaned_str)
        removeSpecialChars(cleaned_str) --> normalizeWhiteSpace(cleaned_str)
        normalizeWhiteSpace(cleaned_str) -->|success| returnUTF8String(normalized_str)
        normalizeWhiteSpace(cleaned_str) -->|error| returnOriginalUTF8(original_input)

        normalizeInt(input_data) -->|Decimal| convertDecimalToInt(input_data)
        normalizeInt(input_data) -->|not Decimal| convertFloatToInt(input_data)
        convertFloatToInt(input_data) -->|success| returnInt(int)
        convertFloatToInt(input_data) -->|error| returnOriginalInt(original_input)
        
        normalizeFloat(value) -->|None, 0, or empty list/tuple| returnZero(0)
        normalizeFloat(value) -->|list/tuple| processList(value)
        processList(value) -->|success| returnFloatList(list)
        processList(value) -->|recursion| normalizeFloat(v)
        normalizeFloat(value) -->|single value| convertToFloat(value)
        convertToFloat(value) -->|success| returnFloat(float)
        convertToFloat(value) -->|error| returnOriginalFloat(original_value)

        normalizeSQLDate(input_data) -->|string| parseDateString(input_data)
        parseDateString(input_data) -->|success| returnSQLDate(normalized_date)
        parseDateString(input_data) -->|datetime| formatDatetime(input_data)
        formatDatetime(input_data) --> returnSQLDateFromDatetime(normalized_date)
        parseDateString(input_data) -->|error| returnOriginalSQLDate(original_input)
        
        simplifyString(input_str) --> removeNonAlphanumeric(input_str)
        removeNonAlphanumeric(input_str) --> replaceSpaceWithUnderscore(cleaned_str)
        replaceSpaceWithUnderscore(cleaned_str) --> removeConsecutiveUnderscore(cleaned_str)
        removeConsecutiveUnderscore(cleaned_str) -->|success| returnSimplifiedString(cleaned_str)
        removeConsecutiveUnderscore(cleaned_str) -->|error| returnOriginalString(input_str)
        
        removeLineBreaks(input_str) --> returnStringWithoutLineBreaks(input_str)

        removeHTMLTags(input_html) --> returnStringWithoutHTML(input_html)

        removeSpecialCharacters(input_str, chars) -->|list| processListChars(input_str)
        processListChars(input_str) --> returnListWithoutSpecialChars(list)
         removeSpecialCharacters(input_str, chars) -->|string| processStringChars(input_str)
        processStringChars(input_str) --> returnStringWithoutSpecialChars(input_str)

        normalizeSKU(input_str) --> removeHebrewKeywords(input_str)
         removeHebrewKeywords(input_str) --> removeNonAlphanumericSKU(input_str)
        removeNonAlphanumericSKU(input_str) -->|success| returnNormalizedSKU(normalized_sku)
        removeNonAlphanumericSKU(input_str) -->|error| returnOriginalSKU(input_str)

    end
    
    Start --> normalizeBoolean(input_data)
    Start --> normalizeString(input_data)
    Start --> normalizeInt(input_data)
    Start --> normalizeFloat(value)
    Start --> normalizeSQLDate(input_data)
     Start --> simplifyString(input_str)
    Start --> removeLineBreaks(input_str)
    Start --> removeHTMLTags(input_html)
     Start --> removeSpecialCharacters(input_str, chars)
     Start --> normalizeSKU(input_str)
```

**Анализ зависимостей:**

*   **re**: Используется для работы с регулярными выражениями, для удаления HTML-тегов, специальных символов, упрощения строк и нормализации SKU.
*   **html**: Не используется в коде. Вероятно, планировалось использование для работы с HTML, но в итоге используется `re`.
*   **datetime**: Используется для обработки и форматирования дат в `normalize_sql_date`.
*   **decimal**: Используется для обработки чисел с плавающей точкой в `normalize_int`.
*   **typing**: Используется для аннотации типов, что повышает читаемость и облегчает отладку.
*   **src.logger.logger**: Используется для логирования ошибок и предупреждений, что позволяет отслеживать проблемы в процессе нормализации.

## <объяснение>

**Импорты:**

*   `import re`: Модуль `re` используется для работы с регулярными выражениями. Он необходим для функций `remove_html_tags`, `remove_special_characters`, `simplify_string`, и `normalize_sku`, где используются регулярные выражения для поиска и замены определенных шаблонов в строках.
*   `import html`: Модуль `html` импортируется, но не используется в представленном коде. Возможно, планировалось использовать его для обработки HTML, но в итоге для удаления HTML-тегов используется модуль `re`.
*   `from datetime import datetime`:  Импортируется класс `datetime` для работы с датами и временем, используется в `normalize_sql_date` для преобразования строк в объекты дат и их форматирования в SQL формат.
*   `from decimal import Decimal, InvalidOperation`: Импортируются класс `Decimal` для точных вычислений с плавающей точкой и исключение `InvalidOperation` для обработки ошибок при работе с `Decimal`. Используется в `normalize_int` для конвертации значений в целое число, если входное значение является объектом `Decimal`.
*   `from typing import Any, List, Union`: Модуль `typing` используется для аннотации типов, что улучшает читаемость кода и позволяет статическим анализаторам кода проверять типы переменных. `Any` означает, что тип переменной может быть любым, `List` – список, `Union` –  тип, который может быть одним из нескольких указанных типов.
*   `from src.logger.logger import logger`: Импортируется объект `logger` из модуля `src.logger.logger`. Этот объект используется для логирования ошибок и отладочной информации в функциях, обеспечивая отслеживание проблем и процесса выполнения.

**Функции:**

*   `normalize_boolean(input_data: Any) -> bool`:
    -   **Аргументы**: `input_data` (любой тип).
    -   **Возвращает**: `bool` (булево значение).
    -   **Назначение**: Нормализует входные данные к булевому значению. Принимает различные типы данных, такие как строки, целые числа и логические значения, и пытается преобразовать их в `True` или `False`. Если преобразование невозможно, возвращает исходное значение и логгирует debug сообщение.
    -   **Пример**: `normalize_boolean("yes")` вернет `True`, `normalize_boolean(0)` вернет `False`, `normalize_boolean("invalid")` вернет `"invalid"`.

*   `normalize_string(input_data: str | list) -> str`:
    -   **Аргументы**: `input_data` (строка или список строк).
    -   **Возвращает**: `str` (нормализованная строка).
    -   **Назначение**: Нормализует входные данные к строке. Удаляет HTML-теги, разрывы строк, специальные символы и лишние пробелы. Возвращает строку в UTF-8.
    -   **Пример**: `normalize_string("<p>Hello</p> \n World! #")` вернет `"Hello World!"`.

*   `normalize_int(input_data: Union[str, int, float, Decimal]) -> int`:
    -   **Аргументы**: `input_data` (строка, целое число, число с плавающей точкой или `Decimal`).
    -   **Возвращает**: `int` (целое число).
    -   **Назначение**: Нормализует входные данные к целому числу. Пытается преобразовать входные данные в целое число. Если преобразование невозможно, возвращает исходное значение и логгирует ошибку.
    -   **Пример**: `normalize_int("42.5")` вернет `42`, `normalize_int(Decimal("42"))` вернет `42`.

*   `normalize_float(value: Any) -> float | None`:
    -   **Аргументы**: `value` (любой тип).
    -   **Возвращает**: `float` (число с плавающей точкой) или `None`, если преобразование невозможно.
    -   **Назначение**: Нормализует входные данные к числу с плавающей точкой. Пытается преобразовать входные данные в число с плавающей точкой. Поддерживает списки и кортежи, рекурсивно обрабатывая их элементы. Если преобразование невозможно, возвращает исходное значение и логгирует предупреждение.
     -   **Пример**: `normalize_float("3.14")` вернет `3.14`, `normalize_float([1, "2.5", 3])` вернет `[1.0, 2.5, 3.0]`, `normalize_float("invalid")` вернет `"invalid"`.

*   `normalize_sql_date(input_data: str) -> str`:
    -   **Аргументы**: `input_data` (строка или объект datetime).
    -   **Возвращает**: `str` (дата в формате `YYYY-MM-DD`).
    -   **Назначение**: Нормализует входные данные к дате в формате SQL. Пытается распознать различные форматы даты и преобразовать их в формат `YYYY-MM-DD`. Если преобразование невозможно, возвращает исходное значение и логгирует debug сообщение.
    -  **Пример**: `normalize_sql_date("12/06/2024")` вернет `"2024-12-06"`. `normalize_sql_date("invalid date")` вернет `"invalid date"`.

*   `simplify_string(input_str: str) -> str`:
    -   **Аргументы**: `input_str` (строка).
    -   **Возвращает**: `str` (упрощенная строка).
    -   **Назначение**: Упрощает строку, оставляя только буквы, цифры и заменяя пробелы на подчеркивания, удаляет дублирующие подчеркивания.
      -   **Пример**: `simplify_string("It's a test! 123")` вернет `"Its_a_test_123"`.

*   `remove_line_breaks(input_str: str) -> str`:
    -   **Аргументы**: `input_str` (строка).
    -   **Возвращает**: `str` (строка без разрывов строк).
    -   **Назначение**: Удаляет разрывы строк (`\n` и `\r`) из входной строки.
     -   **Пример**: `remove_line_breaks("Hello\nWorld\r")` вернет `"Hello World"`.

*   `remove_html_tags(input_html: str) -> str`:
    -   **Аргументы**: `input_html` (строка с HTML).
    -   **Возвращает**: `str` (строка без HTML-тегов).
    -   **Назначение**: Удаляет HTML-теги из входной строки.
     -   **Пример**: `remove_html_tags("<p>Hello</p>")` вернет `"Hello"`.

*   `remove_special_characters(input_str: str | list, chars: list[str] = None) -> str | list`:
    -   **Аргументы**: `input_str` (строка или список строк), `chars` (список символов для удаления, по умолчанию `['#']`).
    -   **Возвращает**: `str | list` (строка или список строк без указанных символов).
    -   **Назначение**: Удаляет указанные специальные символы из входной строки или списка строк.
    -   **Пример**: `remove_special_characters("Hello#", ["#"])` вернет `"Hello"`, `remove_special_characters(["Hello#", "World#"], ["#"])` вернет `["Hello", "World"]`.

*   `normalize_sku(input_str: str) -> str`:
    -   **Аргументы**: `input_str` (строка, представляющая SKU).
    -   **Возвращает**: `str` (нормализованная строка SKU).
    -   **Назначение**: Нормализует строку SKU, удаляя специфические ивритские слова и все не-буквенно-цифровые символы.
     -   **Пример**: `normalize_sku("מקט: 303235")` вернет `"303235"`, `normalize_sku("invalid SKU")` вернет `"invalid SKU"`

**Переменные:**

*   `original_input`: Используется во многих функциях для сохранения исходного значения входных данных перед их преобразованием. Это позволяет вернуть исходное значение в случае ошибки.
*   `logger`: Объект для логирования, импортированный из `src.logger.logger`. Используется для записи ошибок, предупреждений и отладочной информации.
*   `cleaned_str`: Используется в функциях `normalize_string` и `simplify_string` для хранения промежуточных результатов преобразования строк.
*    `normalized_str`: Используется в функциях `normalize_string` и `normalize_sku` для хранения нормализованных строк.
*    `value`: Используется в функции `normalize_float` для хранения входного значения.

**Потенциальные ошибки и области для улучшения:**

*   **Обработка ошибок**: Везде используется `try-except` блоки для обработки исключений, которые возникают при преобразовании данных. Тем не менее, можно добавить более точную обработку конкретных типов исключений (например, `ValueError` или `TypeError`) для более детального логирования и более точной обработки ошибок.
*   **Производительность**: В функциях `remove_special_characters` и `simplify_string` используется `re.sub`, что может быть не самым быстрым решением для очень больших строк. Можно исследовать альтернативные подходы, такие как `str.translate` (если применимо).
*    **HTML**: Модуль `html` импортирован, но не используется. Стоит его убрать или применить по назначению.
*   **Логирование**: В некоторых функциях (например, `normalize_boolean`, `normalize_sql_date`) используется `logger.debug` вместо `logger.warning` для нештатных ситуаций.  Стоит унифицировать использование `logger.debug` и `logger.warning`.

**Цепочка взаимосвязей:**

*   **Ввод данных**: Все функции получают входные данные разных типов, которые могут поступать из внешних источников, например, из CSV файлов, JSON, API и так далее.
*   **Нормализация**: Функции выполняют нормализацию данных, приводя их к общему виду.
*   **Логирование**:  Используется для отслеживания процесса нормализации.
*   **Использование**:  Результат нормализации используется другими модулями проекта, например, для сохранения в базу данных, обработки или анализа.