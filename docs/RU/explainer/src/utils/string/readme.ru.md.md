# Анализ кода `src.utils.string.normalizer`

## 1. <алгоритм>

Модуль `normalizer` предоставляет набор функций для нормализации различных типов данных, таких как строки, булевы значения, целые числа, числа с плавающей запятой и даты SQL. Ниже приведена пошаговая блок-схема, описывающая основные функции:

**1. `normalize_boolean(input_data)`**

   - **Вход:** `input_data` (различные типы данных).
   - **Логика:**
     - Проверяет `input_data` на эквивалентность `True`, `"true"`, `"yes"` (независимо от регистра), `1`, `True` или любое другое значение `!= False`
     - Если `input_data` эквивалентно `True`, возвращает `True`.
     - В противном случае возвращает `False`.
   - **Выход:** `bool` (логическое значение).

   **Примеры:**
     - `normalize_boolean("yes")` → `True`
     - `normalize_boolean(0)` → `False`
     - `normalize_boolean(1)` → `True`

**2. `normalize_string(input_data)`**
   - **Вход:** `input_data` (строка или список строк).
   - **Логика:**
     - Если `input_data` - список:
       - Вызывает `remove_line_breaks` для каждой строки.
       - Вызывает `remove_html_tags` для каждой строки.
       - Вызывает `remove_special_characters` для каждой строки.
       - Объединяет все строки списка в одну строку, разделенную пробелами.
     - Если `input_data` - строка:
       - Вызывает `remove_line_breaks`.
       - Вызывает `remove_html_tags`.
       - Вызывает `remove_special_characters`.
     - Возвращает очищенную строку.
   - **Выход:** `str` (очищенная строка).

   **Примеры:**
     - `normalize_string(["  test  ", "<div>text</div>"])` → `"test text"`
     - `normalize_string("  test <div>text</div>  ")` → `"test text"`

**3. `normalize_int(input_data)`**

   - **Вход:** `input_data` (число, строка числа или Decimal).
   - **Логика:**
     - Пытается преобразовать `input_data` в `int`.
     - Если преобразование успешно, возвращает `int`.
     - Если возникает исключение `ValueError` или `TypeError`, возвращает `None`.
   - **Выход:** `int` (целое число) или `None`.

   **Примеры:**
     - `normalize_int("42")` → `42`
     - `normalize_int(3.14)` → `3`
     - `normalize_int("abc")` → `None`

**4. `normalize_float(input_data)`**

   - **Вход:** `input_data` (число, строка числа, список чисел).
   - **Логика:**
     - Если `input_data` - список:
       - Проходит по списку, пытаясь преобразовать каждый элемент в `float`.
       - Возвращает список преобразованных `float` чисел, если все преобразования успешны, или `None` в противном случае.
     - Если `input_data` - не список, то пытается преобразовать в `float`.
     - Если преобразование успешно, возвращает `float`.
     - Если возникает ошибка, возвращает `None`.
   - **Выход:** `float` (число с плавающей запятой), `List[float]` или `None`.

   **Примеры:**
     - `normalize_float("3.14")` → `3.14`
     - `normalize_float([1, "2.5", 3])` → `[1.0, 2.5, 3.0]`
     - `normalize_float("abc")` → `None`

**5. `remove_line_breaks(input_str)`**

   - **Вход:** `input_str` (строка).
   - **Логика:**
     - Заменяет все вхождения символов `\n` и `\r` на пустую строку.
   - **Выход:** `str` (строка без символов переноса).

   **Примеры:**
     - `remove_line_breaks("text\nwith\nbreaks")` → `"textwithbreaks"`
     - `remove_line_breaks("text\rwith\rbreaks")` → `"textwithbreaks"`

**6. `remove_html_tags(input_html)`**
    - **Вход:** `input_html` (строка).
    - **Логика:**
      - Использует регулярное выражение для удаления всех HTML-подобных тегов.
    - **Выход:** `str` (строка без HTML-тегов).

    **Примеры:**
      - `remove_html_tags("<p>text</p>")` → `"text"`
      - `remove_html_tags("<div>text</div>")` → `"text"`

**7. `remove_special_characters(input_str)`**
    - **Вход:** `input_str` (строка или список строк).
    - **Логика:**
      - Если `input_str` - список:
          - Проходит по списку, вызывает функцию `_remove_special_characters_single` для каждого элемента
          - Возвращает список строк без спец символов.
      - Если `input_str` - строка:
          - Вызывает функцию `_remove_special_characters_single`.
          - Возвращает строку без спец символов.
    - **Выход:** `str` (строка без специальных символов) или `List[str]`.

    **Примеры:**
      - `remove_special_characters("text@123")` → `"text123"`
      - `remove_special_characters(["text@123","some#test"])` → `["text123", "sometest"]`

**8. `normalize_sql_date(input_data)`**

    - **Вход:** `input_data` (строка или `datetime.datetime`).
    - **Логика:**
      - Если `input_data` - строка, то пытается преобразовать в `datetime`
      - Если преобразование успешно, форматирует в строку `YYYY-MM-DD`.
      - Если преобразование не удалось, или `input_data` - не строка, то проверяет, является ли `datetime`
      - Если `input_data` является `datetime`, то форматирует его в строку `YYYY-MM-DD`.
      - Если это не `datetime`, то возвращает `None`.
    - **Выход:** `str` (дата в формате `YYYY-MM-DD`) или `None`.

    **Примеры:**
      - `normalize_sql_date("2024-01-01")` → `"2024-01-01"`
      - `normalize_sql_date(datetime.datetime(2024, 1, 1))` → `"2024-01-01"`
      - `normalize_sql_date("abc")` → `None`

## 2. <mermaid>

```mermaid
flowchart TD
    subgraph normalize_boolean
        Start_Boolean[Start] --> Check_Boolean_Input{Is input True, "true", "yes", 1 or True?}
        Check_Boolean_Input -- Yes --> Return_True[Return True]
        Check_Boolean_Input -- No --> Return_False[Return False]
    end
    subgraph normalize_string
        Start_String[Start] --> Check_String_Type{Is input a list?}
        Check_String_Type -- Yes --> Loop_Strings[Loop through each string]
        Loop_Strings --> Remove_Line_Breaks_String[Remove Line Breaks]
        Remove_Line_Breaks_String --> Remove_HTML_Tags_String[Remove HTML Tags]
        Remove_HTML_Tags_String --> Remove_Special_Chars_String[Remove Special Characters]
        Remove_Special_Chars_String --> Combine_Strings[Combine strings]
        Combine_Strings --> Return_Cleaned_String[Return Cleaned String]
        Check_String_Type -- No --> Remove_Line_Breaks_Single[Remove Line Breaks]
        Remove_Line_Breaks_Single --> Remove_HTML_Tags_Single[Remove HTML Tags]
        Remove_HTML_Tags_Single --> Remove_Special_Chars_Single[Remove Special Characters]
        Remove_Special_Chars_Single --> Return_Cleaned_String
    end
    subgraph normalize_int
        Start_Int[Start] --> Attempt_Int_Conversion[Attempt to Convert to Integer]
        Attempt_Int_Conversion -- Success --> Return_Integer[Return Integer]
        Attempt_Int_Conversion -- Fail --> Return_None_Int[Return None]
    end
    subgraph normalize_float
        Start_Float[Start] --> Check_Float_Type{Is input a list?}
        Check_Float_Type -- Yes --> Loop_Floats[Loop through each element]
        Loop_Floats --> Attempt_Float_Conversion_List[Attempt to Convert to Float]
        Attempt_Float_Conversion_List -- Success --> Continue_Loop_Float[Continue Loop]
        Continue_Loop_Float -- All Success --> Return_Float_List[Return Float List]
        Attempt_Float_Conversion_List -- Fail --> Return_None_Float_List[Return None]
        Check_Float_Type -- No --> Attempt_Float_Conversion_Single[Attempt to Convert to Float]
         Attempt_Float_Conversion_Single -- Success --> Return_Float[Return Float]
         Attempt_Float_Conversion_Single -- Fail --> Return_None_Float[Return None]
    end
    subgraph remove_line_breaks
        Start_Remove_Line_Breaks[Start] --> Replace_Line_Breaks[Replace Line Breaks]
        Replace_Line_Breaks --> Return_String_No_Breaks[Return String without Line Breaks]
    end
    subgraph remove_html_tags
        Start_Remove_HTML[Start] --> Remove_HTML_Regex[Remove HTML Tags with Regex]
        Remove_HTML_Regex --> Return_String_No_HTML[Return String without HTML Tags]
    end
     subgraph remove_special_characters
        Start_Remove_Special[Start] --> Check_Special_Type{Is input a list?}
        Check_Special_Type -- Yes --> Loop_Special[Loop through each string]
        Loop_Special --> Remove_Special_Chars_Single_List[Remove Special Characters]
        Remove_Special_Chars_Single_List -->  Continue_Loop_Special[Continue Loop]
        Continue_Loop_Special -- All Success --> Return_List_No_Special[Return List without Special Characters]
        Check_Special_Type -- No --> Remove_Special_Chars_Single_String[Remove Special Characters]
        Remove_Special_Chars_Single_String --> Return_String_No_Special[Return String without Special Characters]
     end
     subgraph normalize_sql_date
        Start_SQL_Date[Start] --> Check_SQL_Type{Is input a string?}
         Check_SQL_Type -- Yes --> Attempt_Date_Conversion[Attempt to Convert String to Datetime]
         Attempt_Date_Conversion -- Success --> Format_Date[Format to YYYY-MM-DD]
         Attempt_Date_Conversion -- Fail --> Check_SQL_Is_Datetime{Is input Datetime?}
         Check_SQL_Type -- No --> Check_SQL_Is_Datetime
         Check_SQL_Is_Datetime -- Yes --> Format_Date
         Format_Date --> Return_Formatted_Date[Return Formatted Date]
         Check_SQL_Is_Datetime -- No --> Return_None_Date[Return None]
     end
```

**Анализ диаграммы `mermaid`:**

1.  **`normalize_boolean`**:
    -   Начинается с `Start_Boolean`.
    -   `Check_Boolean_Input` проверяет входные данные на соответствие `True`, `"true"`, `"yes"`, `1` или `True`.
    -   Если условие выполняется, возвращает `Return_True`, иначе — `Return_False`.

2.  **`normalize_string`**:
    -   Начинается с `Start_String`.
    -   `Check_String_Type` проверяет, является ли ввод списком.
        -   Если это список, то выполняется цикл `Loop_Strings`, применяя `remove_line_breaks`, `remove_html_tags` и `remove_special_characters` к каждой строке и далее объединяет строки в `Combine_Strings`
        -   Если это строка, то применяются `remove_line_breaks`, `remove_html_tags` и `remove_special_characters` к строке.
    -   В конце возвращает `Return_Cleaned_String`.

3.  **`normalize_int`**:
    -   Начинается с `Start_Int`.
    -   `Attempt_Int_Conversion` пытается преобразовать входные данные в целое число.
    -   Если преобразование успешно, возвращает `Return_Integer`, иначе — `Return_None_Int`.

4.  **`normalize_float`**:
     - Начинается с `Start_Float`.
    -   `Check_Float_Type` проверяет, является ли ввод списком.
        -   Если это список, то выполняется цикл `Loop_Floats`, применяя `Attempt_Float_Conversion_List` к каждому элементу.
        -   Если все преобразования успешны, возвращает `Return_Float_List`, если хотя бы одно преобразование не удалось, то возвращает `Return_None_Float_List`
        -   Если ввод не список, то применяется `Attempt_Float_Conversion_Single` к нему, если преобразование удалось, то возвращает `Return_Float`, в противном случае `Return_None_Float`

5.  **`remove_line_breaks`**:
    -   Начинается с `Start_Remove_Line_Breaks`.
    -   `Replace_Line_Breaks` заменяет символы переноса строки на пустую строку.
    -   Возвращает `Return_String_No_Breaks`.

6.  **`remove_html_tags`**:
    -   Начинается с `Start_Remove_HTML`.
    -   `Remove_HTML_Regex` удаляет HTML-теги с помощью регулярного выражения.
    -   Возвращает `Return_String_No_HTML`.

7.  **`remove_special_characters`**:
    -   Начинается с `Start_Remove_Special`.
    -   `Check_Special_Type` проверяет, является ли ввод списком
        -   Если это список, то выполняется цикл `Loop_Special`, применяя `Remove_Special_Chars_Single_List` к каждому элементу, и далее возвращает `Return_List_No_Special`
        -   Если это строка, то применяется  `Remove_Special_Chars_Single_String`, и далее возвращается `Return_String_No_Special`

8.  **`normalize_sql_date`**:
    -   Начинается с `Start_SQL_Date`.
    -   `Check_SQL_Type` проверяет, является ли ввод строкой
         -  Если ввод строка, то пытается преобразовать в дату, в случае успеха форматирует `Format_Date` и возвращает `Return_Formatted_Date`.
         -  Если ввод не строка, то проверяет, является ли вводом `datetime`, в случае успеха форматирует `Format_Date` и возвращает `Return_Formatted_Date`, в случае неудачи возвращает `Return_None_Date`.

**Взаимосвязи:**

-   Функции `normalize_string` использует `remove_line_breaks`, `remove_html_tags`, `remove_special_characters`
-  `remove_special_characters` использует вспомогательную функцию `_remove_special_characters_single` для каждого элемента списка.

## 3. <объяснение>

### Импорты:

-   `datetime` -  Используется в `normalize_sql_date` для работы с датами и их преобразования.

### Функции:

1.  **`normalize_boolean(input_data)`**

    -   **Аргументы**:
        -   `input_data` (Any): входные данные любого типа.
    -   **Возвращает**:
        -   `bool`:  `True`, если входные данные эквиваленты `True`, `"true"`, `"yes"` (независимо от регистра), `1`, `True` или любое другое значение `!= False`, `False` в противном случае.
    -   **Назначение**: Преобразует входные данные в булево значение.
    -   **Пример:** `normalize_boolean("yes")` вернет `True`, `normalize_boolean(0)` вернет `False`.

2.  **`normalize_string(input_data)`**

    -   **Аргументы**:
        -   `input_data` (str | list): строка или список строк для нормализации.
    -   **Возвращает**:
        -   `str`: нормализованная строка в кодировке UTF-8.
    -   **Назначение**: Нормализует строку или список строк, удаляя лишние пробелы, HTML-теги и специальные символы.
    -   **Пример:** `normalize_string(["  text  ", "<b>html</b>"])` вернет `"text html"`.

3.  **`normalize_int(input_data)`**

    -   **Аргументы**:
        -   `input_data` (str | int | float | Decimal): входные данные для преобразования в целое число.
    -   **Возвращает**:
        -   `int` : целое число, если преобразование успешно, иначе `None`.
    -   **Назначение**: Преобразует входные данные в целое число, если это возможно.
    -   **Пример:** `normalize_int("42")` вернет `42`, `normalize_int(3.14)` вернет `3`.

4.  **`normalize_float(input_data)`**

    -   **Аргументы**:
        -  `value (Any)`: Число, строка или список чисел.
    -   **Возвращает**:
        -   `float | List[float] | None`: число с плавающей запятой, список чисел с плавающей запятой или `None` в случае ошибки.
    -   **Назначение**: Преобразует входные данные в число с плавающей запятой.
    -   **Пример:** `normalize_float("3.14")` вернет `3.14`, `normalize_float([1, "2.5", 3])` вернет `[1.0, 2.5, 3.0]`.

5.  **`remove_line_breaks(input_str)`**

    -   **Аргументы**:
        -   `input_str` (str): строка для обработки.
    -   **Возвращает**:
        -   `str`: строка без символов переноса строки.
    -   **Назначение**: Удаляет символы новой строки (`\n`, `\r`) из строки.
    -   **Пример:** `remove_line_breaks("text\nwith\nbreaks")` вернет `"textwithbreaks"`.

6.  **`remove_html_tags(input_html)`**

    -   **Аргументы**:
        -   `input_html` (str): строка с HTML-тегами.
    -   **Возвращает**:
        -   `str`: строка без HTML-тегов.
    -   **Назначение**: Удаляет HTML-теги из строки.
    -   **Пример:** `remove_html_tags("<p>text</p>")` вернет `"text"`.

7.  **`remove_special_characters(input_str)`**

    -   **Аргументы**:
        -   `input_str` (str | list): строка или список строк для обработки.
    -   **Возвращает**:
        -   `str`: строка без специальных символов.
    -   **Назначение**: Удаляет специальные символы из строки или списка строк.
    -   **Пример:** `remove_special_characters("text@123")` вернет `"text123"`.

8.  **`normalize_sql_date(input_data)`**
    -   **Аргументы**:
        -   `input_data` (str | datetime): строка или объект `datetime`.
    -   **Возвращает**:
        -   `str`: строка с датой в формате `YYYY-MM-DD`.
    -   **Назначение**: Преобразует входные данные в строку с датой SQL.
    -  **Пример:** `normalize_sql_date("2024-01-01")` вернет `"2024-01-01"`, `normalize_sql_date(datetime.datetime(2024,1,1))` вернет `"2024-01-01"`

### Переменные:

-   В основном используются локальные переменные внутри функций, такие как `input_data`, `input_str` и т.д., для хранения временных значений.
-   `pattern` используется в `remove_html_tags` для определения регулярного выражения для удаления HTML-тегов.

### Потенциальные ошибки и улучшения:

-   **Обработка ошибок**:
    - В функциях `normalize_int`, `normalize_float` обрабатываются ошибки при преобразовании типов, возвращая `None`. Возможно, стоит регистрировать такие ошибки через `logger` для отслеживания проблем с входными данными.
-   **Унификация обработки ошибок**:
    -  В функциях нормализации чисел, можно использовать один общий механизм обработки ошибок (например, декоратор), для предотвращения дублирования кода.
-   **Регулярные выражения**:
    - В `remove_special_characters` можно использовать более гибкое регулярное выражение, позволяющее настраивать список удаляемых символов.
-   **Поддержка других форматов даты**:
    - Функция `normalize_sql_date` поддерживает только формат `YYYY-MM-DD`. Можно добавить поддержку других форматов, если это необходимо.
-  **Производительность**:
    - В функциях, обрабатывающих списки, можно использовать генераторы или map для повышения производительности при работе с большими списками.

### Взаимосвязи с другими частями проекта:

-   **Логирование**: Модуль использует `src.logger` для логирования ошибок и предупреждений.
-   **Глобальные настройки**: Модуль использует глобальные настройки из `src.gs`, хотя это явно не показано в предоставленной документации.
-   Модуль является частью пакета `src.utils`, который используется для различных утилит в проекте.

Этот анализ предоставляет подробное представление о модуле `normalizer`, его функциональности, внутреннем устройстве и возможных улучшениях.