## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:  

1. **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.  
2. **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости, 
    которые импортируются при создании диаграммы. 
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`, 
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!  
    
    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:\
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
```
## <алгоритм>

**1. `normalize_boolean(input_data)`:**

   - **Начало:** Принимает `input_data` любого типа.
     ```python
     input_data = "yes"  # Пример входных данных
     ```
   - **Проверка типа:** Проверяет, является ли `input_data` булевым значением.
     ```python
     if isinstance(input_data, bool):
         # Если булево значение, то возвращает его
         return input_data
     ```
   - **Преобразование в строку:** Если не булево, преобразует `input_data` в строку, приводит к нижнему регистру и удаляет лишние пробелы.
      ```python
      input_str = str(input_data).strip().lower()  # input_str = "yes"
      ```
   - **Проверка на `True`:** Проверяет, входит ли строка в набор значений, представляющих `True`.
      ```python
      if input_str in {'true', '1', 'yes', 'y', 'on', True, 1}:
         return True
      ```
   - **Проверка на `False`:** Проверяет, входит ли строка в набор значений, представляющих `False`.
     ```python
     if input_str in {'false', '0', 'no', 'n', 'off', False, 0}:
         return False
     ```
   - **Обработка ошибок:** Если преобразование не удалось, логгируется ошибка.
    ```python
    except Exception as ex:
      logger.error('Ошибка в normalize_boolean: ', ex)
    ```
    - **Возврат исходного значения:** Возвращает исходное значение `input_data`, если преобразование не удалось.
      ```python
      logger.debug(f'Неожиданное значение для преобразования в bool: {input_data}')
      return original_input # return "yes"
      ```

**2. `normalize_string(input_data)`:**

   - **Начало:** Принимает `input_data` либо строку, либо список строк.
     ```python
     input_data = ["Hello", "  World!  "]  # Пример входных данных
     ```
   - **Проверка на пустоту:** Если `input_data` пустое, возвращается пустая строка.
     ```python
     if not input_data:
        return ''
     ```
   - **Проверка типа:** Проверяет, является ли `input_data` строкой или списком.
      ```python
      if not isinstance(input_data, (str, list)):
        raise TypeError('Данные должны быть строкой или списком строк.')
      ```
   - **Объединение списка в строку:** Если `input_data` это список, то объединяет строки в одну, разделяя пробелами.
      ```python
      if isinstance(input_data, list):
        input_data = ' '.join(map(str, input_data)) # input_data = "Hello   World!  "
      ```
   - **Удаление HTML-тегов:** Удаляет HTML-теги из строки.
     ```python
     cleaned_str = remove_html_tags(input_data)
     ```
   - **Удаление переносов строк:** Удаляет переносы строк из строки.
     ```python
     cleaned_str = remove_line_breaks(cleaned_str)
     ```
   - **Удаление спецсимволов:** Удаляет специальные символы из строки.
     ```python
     cleaned_str = remove_special_characters(cleaned_str)
     ```
   - **Нормализация пробелов:** Нормализует пробелы, оставляя только одиночные.
      ```python
      normalized_str = ' '.join(cleaned_str.split())
      ```
   - **Кодирование и декодирование UTF-8:** Кодирует и декодирует строку в UTF-8 для гарантии корректного отображения.
      ```python
      return normalized_str.strip().encode('utf-8').decode('utf-8') # return "Hello World!"
      ```
   - **Обработка ошибок:** В случае ошибки, логгируется ошибка и возвращается исходное значение (после преобразования в строку и кодирования в utf-8).
     ```python
     except Exception as ex:
        logger.error('Ошибка в normalize_string: ', ex)
        return str(original_input).encode('utf-8').decode('utf-8')
     ```

**3. `normalize_int(input_data)`:**

   - **Начало:** Принимает `input_data`, который может быть строкой, целым числом, числом с плавающей точкой или Decimal.
     ```python
     input_data = "42.5"  # Пример входных данных
     ```
   - **Преобразование в int:** Пробует преобразовать `input_data` в целое число. Сначала преобразует в float, потом в int. Если `input_data` - Decimal, то сразу преобразует в int.
     ```python
     try:
        if isinstance(input_data, Decimal):
           return int(input_data)
        return int(float(input_data))
     ```
   - **Обработка ошибок:** Если преобразование не удалось, логгируется ошибка.
    ```python
     except (ValueError, TypeError, InvalidOperation) as ex:
        logger.error('Ошибка в normalize_int: ', ex)
    ```
   - **Возврат исходного значения:** Возвращает исходное значение `input_data`, если преобразование не удалось.
      ```python
      return original_input # return "42.5"
      ```

**4. `normalize_float(value)`:**

   - **Начало:** Принимает `value` любого типа.
     ```python
     value = "3.14"  # Пример входных данных
     ```
   - **Проверка на пустоту:** Если `value` пустое, возвращается 0.
     ```python
     if not value:
        return 0
     ```
   - **Обработка списков/кортежей:** Если `value` является списком или кортежем, рекурсивно вызывает `normalize_float` для каждого элемента, отфильтровывая `None` значения.
     ```python
     if isinstance(value, (list, tuple)):
        return [v for v in (normalize_float(v) for v in value) if v is not None]
     ```
   - **Преобразование во float:** Пробует преобразовать `value` в float.
     ```python
     try:
        return float(value)
     ```
   - **Обработка ошибок:** Если преобразование не удалось, логгируется предупреждение.
      ```python
     except (ValueError, TypeError):
        logger.warning(f"Невозможно преобразовать '{value}' в float.")
     ```
   - **Возврат исходного значения:** Возвращает исходное значение `value`, если преобразование не удалось.
      ```python
      return original_value # return "3.14"
      ```

**5. `normalize_sql_date(input_data)`:**

   - **Начало:** Принимает `input_data` (строка или datetime).
      ```python
       input_data = "2024-12-06" # пример входных данных
      ```
   - **Проверка типа:** Проверяет, является ли `input_data` строкой.
      ```python
      if isinstance(input_data, str):
        # Попытка распарсить дату из строки
            for date_format in ['%Y-%m-%d', '%m/%d/%Y', '%d/%m/%Y']:
                try:
                    normalized_date = datetime.strptime(input_data, date_format).date()
                    return normalized_date.isoformat()  # Возвращаем дату в формате 'YYYY-MM-DD'
                except ValueError:
                    continue
      ```
   - **Проверка типа:** Проверяет, является ли `input_data` datetime объектом.
      ```python
        if isinstance(input_data, datetime):
            return input_data.date().isoformat()
      ```
   - **Обработка ошибок:** Если преобразование не удалось, логгируется ошибка.
    ```python
    except Exception as ex:
      logger.error('Ошибка в normalize_sql_date: ', ex)
    ```
   - **Возврат исходного значения:** Возвращает исходное значение `input_data`, если преобразование не удалось.
     ```python
     logger.debug(f'Не удалось преобразовать в SQL дату: {input_data}')
     return original_input # return "2024-12-06"
     ```

**6. `simplify_string(input_str)`:**

   - **Начало:** Принимает строку `input_str`.
     ```python
     input_str = "It's a test string with 'single quotes', numbers 123 and symbols!"  # Пример входных данных
     ```
   - **Удаление спецсимволов:** Удаляет все символы, кроме букв, цифр и пробелов.
     ```python
     cleaned_str = re.sub(r'[^a-zA-Z0-9\s]', '', input_str) # cleaned_str = "Its a test string with single quotes numbers 123 and symbols"
     ```
   - **Замена пробелов на подчеркивания:** Заменяет пробелы на подчеркивания.
      ```python
      cleaned_str = cleaned_str.replace(' ', '_') # cleaned_str = "Its_a_test_string_with_single_quotes_numbers_123_and_symbols"
      ```
   - **Удаление лишних подчеркиваний:** Удаляет повторяющиеся подчеркивания.
     ```python
     cleaned_str = re.sub(r'_+', '_', cleaned_str) # cleaned_str = "Its_a_test_string_with_single_quotes_numbers_123_and_symbols"
     ```
   - **Возврат:** Возвращает упрощенную строку.
     ```python
     return cleaned_str # return "Its_a_test_string_with_single_quotes_numbers_123_and_symbols"
     ```
    - **Обработка ошибок:**  В случае ошибки логируется ошибка и возвращается исходная строка.
     ```python
     except Exception as ex:
        logger.error("Error simplifying the string", ex)
        return input_str
     ```

**7. `remove_line_breaks(input_str)`:**

   - **Начало:** Принимает строку `input_str`.
   - **Удаление переносов строк:** Заменяет символы новой строки `\n` и возврата каретки `\r` на пробелы.
     ```python
     return input_str.replace('\n', ' ').replace('\r', ' ').strip()
     ```
    - **Возврат:** Возвращает строку без переносов строк.

**8. `remove_html_tags(input_html)`:**

   - **Начало:** Принимает строку `input_html`.
     ```python
     input_html = "<div>Hello<b>World!</b></div>"  # Пример входных данных
     ```
   - **Удаление HTML тегов:** Удаляет все HTML-теги из строки.
     ```python
      return re.sub(r'<.*?>', '', input_html).strip() # return "HelloWorld!"
     ```
   - **Возврат:** Возвращает строку без HTML тегов.

**9. `remove_special_characters(input_str, chars=None)`:**

   - **Начало:** Принимает `input_str` (строка или список строк) и необязательный список символов `chars`.
   - **Установка символов по умолчанию:** Если `chars` не задан, то используется `#`.
   ```python
     if chars is None:
        chars = ['#']
   ```
   - **Формирование регулярного выражения:** Формирует регулярное выражение для удаления указанных символов.
     ```python
     pattern = '[' + re.escape(''.join(chars)) + ']'
     ```
   - **Обработка списка строк:** Если `input_str` это список, то применяет регулярное выражение к каждой строке.
      ```python
      if isinstance(input_str, list):
        return [re.sub(pattern, '', s) for s in input_str]
      ```
   - **Обработка строки:** Если `input_str` это строка, то применяет регулярное выражение к строке.
      ```python
     return re.sub(pattern, '', input_str)
      ```
   - **Возврат:** Возвращает обработанную строку или список строк.

**10. `normalize_sku(input_str)`:**

    - **Начало:** Принимает строку `input_str`.
      ```python
        input_str = "מקט: 303235"  # Пример входных данных
      ```
    -   **Удаление ивритских ключевых слов:** Удаляет "מקט" или "מק''ט" (ивритские обозначения SKU), игнорируя регистр.
         ```python
         input_str = re.sub(r'מקט|מק\'\'ט', '', input_str, flags=re.IGNORECASE) # input_str = " 303235"
         ```
    -  **Удаление не-буквенно-цифровых символов:**  Удаляет все не-буквенно-цифровые символы.
         ```python
          normalized_sku = re.sub(r'\W+', '', input_str) # normalized_sku = "303235"
         ```
    - **Возврат:** Возвращает нормализованный SKU.
      ```python
         return normalized_sku
      ```
    - **Обработка ошибок:** В случае ошибки возвращает исходную строку.
        ```python
         except Exception as ex:
            logger.error(f"Error normalizing SKU: {ex}")
            return input_str
        ```
## <mermaid>

```mermaid
flowchart TD
    Start[Начало] --> normalizeBoolean[<code>normalize_boolean(input_data)</code><br>Нормализация в Boolean];
    Start --> normalizeString[<code>normalize_string(input_data)</code><br>Нормализация строки];
    Start --> normalizeInt[<code>normalize_int(input_data)</code><br>Нормализация в Integer];
    Start --> normalizeFloat[<code>normalize_float(value)</code><br>Нормализация в Float];
    Start --> normalizeSQLDate[<code>normalize_sql_date(input_data)</code><br>Нормализация в SQL Date];
    Start --> simplifyString[<code>simplify_string(input_str)</code><br>Упрощение строки];    
    
    
    normalizeBoolean --> CheckBooleanType{Проверка типа:<br><code>isinstance(input_data, bool)</code>};
    CheckBooleanType -- Yes --> ReturnBooleanValue[Вернуть:<br><code>input_data</code>];
    CheckBooleanType -- No --> ConvertToString[Преобразовать в строку:<br><code>str(input_data).strip().lower()</code>];
    ConvertToString --> CheckTrueValues{Проверка на значения True};
    CheckTrueValues -- Yes --> ReturnTrue[Вернуть: <code>True</code>];
    CheckTrueValues -- No --> CheckFalseValues{Проверка на значения False};
    CheckFalseValues -- Yes --> ReturnFalse[Вернуть: <code>False</code>];
    CheckFalseValues -- No --> LogErrorBoolean[Логгировать ошибку];
    LogErrorBoolean --> ReturnOriginalBoolean[Вернуть:<br><code>original_input</code>];    
    
    normalizeString --> CheckInputStringEmpty{Проверка на пустоту:<br><code>if not input_data</code>};
    CheckInputStringEmpty -- Yes --> ReturnEmptyString[Вернуть:<br><code>''</code>];
    CheckInputStringEmpty -- No --> CheckInputStringType{Проверка типа:<br><code>isinstance(input_data, (str, list))</code>};
    CheckInputStringType -- No --> RaiseTypeError[Вызвать:<br><code>TypeError</code>];
    CheckInputStringType -- Yes --> CheckInputIsList{Проверка списка:<br><code>isinstance(input_data, list)</code>};
    CheckInputIsList -- Yes --> JoinListToString[Объединить список в строку:<br><code>' '.join(map(str, input_data))</code>];
    JoinListToString --> RemoveHTMLTags[Удалить HTML теги:<br><code>remove_html_tags(input_data)</code>];
    CheckInputIsList -- No --> RemoveHTMLTags;
    RemoveHTMLTags --> RemoveLineBreaks[Удалить переносы строк:<br><code>remove_line_breaks(cleaned_str)</code>];
    RemoveLineBreaks --> RemoveSpecialCharacters[Удалить спец. символы:<br><code>remove_special_characters(cleaned_str)</code>];
    RemoveSpecialCharacters --> NormalizeSpaces[Нормализовать пробелы:<br><code>' '.join(cleaned_str.split())</code>];
    NormalizeSpaces --> EncodeUTF8[Кодировать в UTF-8];
    EncodeUTF8 --> ReturnNormalizedString[Вернуть:<br><code>normalized_str.strip().encode('utf-8').decode('utf-8')</code>];
    
    
    normalizeInt --> TryConvertToInteger[Попытка преобразования в int];
    TryConvertToInteger --> ReturnIntegerValue[Вернуть: <code>int(float(input_data))</code>];
    TryConvertToInteger -- Exception --> LogErrorInteger[Логгировать ошибку];
    LogErrorInteger --> ReturnOriginalInteger[Вернуть:<br><code>original_input</code>];
    
    normalizeFloat --> CheckValueEmpty{Проверка на пустоту:<br><code>if not value</code>};
    CheckValueEmpty -- Yes --> ReturnZero[Вернуть: <code>0</code>];
    CheckValueEmpty -- No --> CheckValueIsListOrTuple{Проверка на список/кортеж:<br><code>isinstance(value, (list, tuple))</code>};
    CheckValueIsListOrTuple -- Yes --> NormalizeListElements[Нормализовать элементы списка:<br><code>[normalize_float(v) for v in value]</code>];
    NormalizeListElements --> ReturnFloatList[Вернуть:<br><code>float_list</code>];
    CheckValueIsListOrTuple -- No --> TryConvertToFloat[Попытка преобразования в float];
    TryConvertToFloat --> ReturnFloatValue[Вернуть: <code>float(value)</code>];
    TryConvertToFloat -- Exception --> LogWarningFloat[Логгировать предупреждение];
    LogWarningFloat --> ReturnOriginalFloat[Вернуть:<br><code>original_value</code>];
  
    normalizeSQLDate --> CheckSQLDateIsString{Проверка типа:<br><code>isinstance(input_data, str)</code>};
    CheckSQLDateIsString -- Yes --> ParseStringDate[Парсить дату из строки];
    ParseStringDate -- Success --> ReturnSQLDateString[Вернуть:<br><code>date.isoformat()</code>];
    ParseStringDate -- Fail --> CheckSQLDateIsDateTime{Проверка типа:<br><code>isinstance(input_data, datetime)</code>};
    CheckSQLDateIsDateTime -- Yes --> ReturnSQLDateFromDateTime[Вернуть:<br><code>input_data.date().isoformat()</code>];
    CheckSQLDateIsDateTime -- No --> LogErrorSQLDate[Логгировать ошибку];
    LogErrorSQLDate --> ReturnOriginalSQLDate[Вернуть:<br><code>original_input</code>];
  
    simplifyString --> RemoveSpecialCharsFromString[Удалить спец. символы:<br><code>re.sub(r'[^a-zA-Z0-9\\s]', '', input_str)</code>];
    RemoveSpecialCharsFromString --> ReplaceSpacesWithUnderscores[Заменить пробелы на подчеркивания:<br><code>cleaned_str.replace(' ', '_')</code>];
    ReplaceSpacesWithUnderscores --> RemoveConsecutiveUnderscores[Удалить повторяющиеся подчеркивания:<br><code>re.sub(r'_+', '_', cleaned_str)</code>];
    RemoveConsecutiveUnderscores --> ReturnSimplifiedString[Вернуть:<br><code>cleaned_str</code>];
    RemoveConsecutiveUnderscores -- Exception --> LogErrorSimplifyString[Логгировать ошибку];
    LogErrorSimplifyString --> ReturnOriginalSimplifyString[Вернуть:<br><code>input_str</code>];
    
    normalizeBoolean --> End
    ReturnBooleanValue --> End
    ReturnTrue --> End
    ReturnFalse --> End
    ReturnOriginalBoolean --> End
    
    normalizeString --> End
    ReturnEmptyString --> End
    RaiseTypeError --> End
    ReturnNormalizedString --> End
    
    normalizeInt --> End
    ReturnIntegerValue --> End
    ReturnOriginalInteger --> End

    normalizeFloat --> End
    ReturnZero --> End
    ReturnFloatList --> End
    ReturnFloatValue --> End
    ReturnOriginalFloat --> End
    
    normalizeSQLDate --> End
    ReturnSQLDateString --> End
    ReturnSQLDateFromDateTime --> End
    ReturnOriginalSQLDate --> End

    simplifyString --> End
    ReturnSimplifiedString --> End
    ReturnOriginalSimplifyString --> End

    
    
    End[Конец]

    style Start fill:#f9f,stroke:#333,stroke-width:2px
    style End fill:#ccf,stroke:#333,stroke-width:2px
```
### <объяснение>

**Импорты:**

*   `re`: Модуль `re` используется для работы с регулярными выражениями. В данном коде он применяется для удаления HTML-тегов, специальных символов, упрощения строк и нормализации SKU.
*   `html`: Модуль `html` используется для обработки HTML-сущностей. В этом коде он не используется, но импортирован. Возможно, он был нужен ранее или планировался к использованию.
*   `datetime`: Модуль `datetime` используется для работы с датами и временем. В данном коде он используется в функции `normalize_sql_date` для преобразования различных форматов даты в SQL-формат.
*   `decimal`: Модуль `decimal` используется для работы с десятичными числами с фиксированной точностью. В данном коде он используется в функциях `normalize_int` для корректной обработки чисел Decimal, а также для обработки исключений `InvalidOperation`.
*   `typing`: Модуль `typing` используется для аннотации типов, что помогает делать код более читаемым и позволяет инструментам статического анализа проверять типы. Здесь используются `Any`, `List`, `Union`.
    *   `Any`: Указывает, что переменная или параметр может быть любого типа.
    *   `List`: Указывает на список.
    *    `Union`: Указывает, что переменная может принимать значения из нескольких типов.
*   `src.logger.logger`: Импортирует пользовательский модуль `logger` из пакета `src`, использующийся для логирования ошибок и предупреждений в приложении. Это позволяет отслеживать проблемы и отлаживать код.

**Функции:**

1.  **`normalize_boolean(input_data: Any) -> bool`**:
    *   **Аргументы**:
        *   `input_data`: Данные любого типа, которые могут быть интерпретированы как булево значение.
    *   **Возвращаемое значение**:
        *   `bool`: Булево представление входных данных.
    *   **Назначение**: Приводит входные данные к булеву типу. Поддерживает различные представления булевых значений, такие как `true`, `false`, `1`, `0`, `yes`, `no` и т.д.
    *   **Пример**:
        ```python
        normalize_boolean("yes")  # Возвращает True
        normalize_boolean(0)     # Возвращает False
        normalize_boolean("invalid") # Возвращает "invalid"
        ```
2.  **`normalize_string(input_data: str | list) -> str`**:
    *   **Аргументы**:
        *   `input_data`: Строка или список строк.
    *   **Возвращаемое значение**:
        *   `str`: Очищенная и нормализованная строка в UTF-8 формате.
    *   **Назначение**: Приводит строку или список строк к нормализованному виду: удаляет HTML-теги, переносы строк, специальные символы, нормализует пробелы и кодирует в UTF-8.
    *   **Пример**:
        ```python
        normalize_string("  <h1>Hello</h1> \n World!  ")  # Возвращает "Hello World!"
        normalize_string(["Hello", "World!"])  # Возвращает "Hello World!"
        ```
    *   **Ошибки**: Вызывает `TypeError`, если `input_data` не является строкой или списком.
3.  **`normalize_int(input_data: Union[str, int, float, Decimal]) -> int`**:
    *   **Аргументы**:
        *   `input_data`: Число, строка, число с плавающей точкой или `Decimal`, которые можно интерпретировать как целое число.
    *   **Возвращаемое значение**:
        *   `int`: Целое представление входных данных.
    *   **Назначение**: Преобразует входные данные в целое число.
    *   **Пример**:
        ```python
        normalize_int("42")   # Возвращает 42
        normalize_int(42.5)  # Возвращает 42
        normalize_int(Decimal('42.5')) # Возвращает 42
        normalize_int("invalid")   # Возвращает "invalid"
        ```
4.  **`normalize_float(value: Any) -> float | None`**:
    *   **Аргументы**:
        *   `value`: Значение любого типа, которое нужно преобразовать в float.
    *   **Возвращаемое значение**:
        *   `float | None`: Число с плавающей точкой или список таких чисел или None, если преобразование не удалось.
    *   **Назначение**: Преобразует входное значение или список значений в float.
    *   **Пример**:
        ```python
        normalize_float("3.14")  # Возвращает 3.14
        normalize_float([1, "2.5", 3])  # Возвращает [1.0, 2.5, 3.0]
        normalize_float("invalid")  # Возвращает "invalid"
        ```
5.  **`normalize_sql_date(input_data: str) -> str`**:
    *   **Аргументы**:
        *   `input_data`: Строка, представляющая дату.
    *   **Возвращаемое значение**:
        *   `str`: Нормализованная дата в SQL формате YYYY-MM-DD или исходное значение, если преобразование не удалось.
    *   **Назначение**: Приводит различные форматы даты к SQL формату YYYY-MM-DD.
    *   **Пример**:
        ```python
        normalize_sql_date("2024-12-06")   # Возвращает "2024-12-06"
        normalize_sql_date("12/06/2024")  # Возвращает "2024-12-06"
         normalize_sql_date("06/12/2024")  # Возвращает "2024-12-06"
        normalize_sql_date("invalid") # Возвращает "invalid"
        ```
6.  **`simplify_string(input_str: str) -> str`**:
    *   **Аргументы**:
        *   `input_str`: Строка для упрощения.
    *   **Возвращаемое значение**:
        *   `str`: Упрощенная строка, содержащая только буквы, цифры и подчеркивания.
    *   **Назначение**: Упрощает строку, удаляя все символы, кроме букв, цифр и пробелов, заменяет пробелы на подчеркивания и удаляет повторяющиеся подчеркивания.
    *   **Пример**:
         ```python
         simplify_string("It's a test string with 'single quotes', numbers 123 and symbols!") # Возвращает "Its_a_test_string_with_single_quotes_numbers_123_and_symbols"
         ```

7.  **`remove_line_breaks(input_str: str) -> str`**:
    *   **Аргументы**:
        *   `input_str`: Строка для обработки.
    *   **Возвращаемое значение**:
        *   `str`: Строка без переносов строк.
    *   **Назначение**: Удаляет переносы строк (`\n`, `\r`) из строки, заменяя их на пробелы.

8.  **`remove_html_tags(input_html: str) -> str`**:
    *   **Аргументы**:
        *   `input_html`: Строка, содержащая HTML-теги.
    *   **Возвращаемое значение**:
        *   `str`: Строка без HTML-тегов.
    *   **Назначение**: Удаляет HTML-теги из входной строки.
    *    **Пример**:
        ```python
        remove_html_tags("<div>Hello<b>World!</b></div>") # Возвращает "HelloWorld!"
        ```

9.  **`remove_special_characters(input_str: str | list, chars: list[str] = None) -> str | list`**:
    *   **Аргументы**:
        *   `input_str`: Строка или список строк для обработки.
        *   `chars`: Список символов для удаления. По умолчанию `['#']`.
    *   **Возвращаемое значение**:
        *   `str | list`: Строка или список строк, из которых удалены указанные символы.
    *   **Назначение**: Удаляет указанные специальные символы из строки или списка строк.
     *    **Пример**:
         ```python
        remove_special_characters("Hello#World", ["#"]) # Возвращает "HelloWorld"
         remove_special_characters(["Hello#", "World#"], ["#"]) # Возвращает ["Hello", "World"]
         ```

10. **`normalize_sku(input_str: str) -> str`**:
    *   **Аргументы**:
        *   `input_str`: Строка, содержащая SKU.
    *   **Возвращаемое значение**:
        *   `str`: Нормализованная строка SKU.
    *   **Назначение**:  Нормализует SKU, удаляя ивритские ключевые слова "מקט" и "מק''ט" (регистронезависимо), а также все не-буквенно-цифровые символы.
     *   **Пример**:
           ```python
          normalize_sku("מקט: 303235") # Возвращает "303235"
           normalize_sku("מק''ט: 12345") # Возвращает "12345"
           normalize_sku("invalid") # Возвращает "invalid"
           ```

**Переменные:**

*   `original_input`: Сохраняет исходные данные перед их обработкой в функциях `normalize_boolean`, `normalize_string`, `normalize_int`, `normalize_sql_date`, `normalize_float`. Используется для возврата исходного значения при ошибке преобразования.
*   `input_str`: Используется в `normalize_boolean`, `normalize_string`, `simplify_string`, `remove_line_breaks`, `remove_special_characters` для хранения входных данных в виде строки.
*   `cleaned_str`: Используется в `normalize_string`, `simplify_string` для хранения промежуточных результатов после применения преобразований.
*   `normalized_str`: Используется в `normalize_string` для хранения результата нормализации строки.
*   `normalized_sku`: Используется в `normalize_sku` для хранения результата нормализации SKU.
*   `date_format`: Используется в `normalize_sql_date` для хранения форматов даты.
*   `pattern`: Используется в `remove_special_characters` для хранения регулярного выражения.
*   `value`: Используется в `normalize_float` для хранения входного значения.
*    `chars`: Используется в `remove_special_characters` для хранения списка символов для удаления.

**Взаимосвязи с другими частями проекта:**

*   Модуль используется как вспомогательный модуль для нормализации данных в других частях проекта.
*   Модуль `logger` используется для логирования ошибок, что позволяет отслеживать проблемы и отлаживать код.
*   Модуль не зависит напрямую от других модулей проекта, но его функции могут быть вызваны в любом модуле, где требуется нормализация данных.

**Потенциальные ошибки и области для улучшения:**

*   **Обработка ошибок**: В функциях `normalize_boolean`, `normalize_int`, `normalize_float`, `normalize_sql_date` при возникновении исключений возвращается исходное значение.  Это может привести к тому, что ошибки могут быть проигнорированы или не