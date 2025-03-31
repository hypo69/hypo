# Проект `hypotez`
# Роль `code explainer`
## ИНСТРУКЦИЯ  :

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:  

1. **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.  
2. **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости, 
    которые импортируются при создании диаграммы. 
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`, 
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!  
    
    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:\
    ```mermaid\
    flowchart TD\
        Start --> Header[<code>header.py</code><br> Determine Project Root]\
    \
        Header --> import[Import Global Settings: <br><code>from src import gs</code>] \
    ```

3. **<объяснение>**: Предоставь подробные объяснения:  
   - **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.  
   - **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.  
   - **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.  
   - **Переменные**: Их типы и использование.  
   - Выдели потенциальные ошибки или области для улучшения.  

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).  

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)



## Твое поведение при анализе кода:
- всегда смотри системную инструкцию для обработки кода проекта `hypotez`;
- анализируй расположение файла в проекте. Это поможет понять его назначение и взаимосвязь с другими файлами. Расположение файла ты найдешь в самой превой строке кода, начинающейся с `## \\file /...`;
- запоминай предоставленный код и анализируй его связь с другими частями проекта `hypotez`;

**КОНЕЦ ИНСТРУКЦИИ**
```

## \\file /src/utils/string/normalizer.py

### **<алгоритм>**

1.  **`normalize_boolean(input_data: Any) -> bool`**:
    *   Начинается с проверки, является ли входное значение уже булевым. Если да, оно возвращается без изменений.
    *   Преобразует входное значение в строку, приводит к нижнему регистру и удаляет пробелы.
    *   Проверяет, соответствует ли строка одному из строковых представлений `True` (`'true'`, `'1'`, `'yes'`, `'y'`, `'on'`) или `False` (`'false'`, `'0'`, `'no'`, `'n'`, `'off'`).
    *   Возвращает `True` или `False` в соответствии с совпадением. Если преобразование не удалось, логирует ошибку и возвращает исходное значение.

    ```python
    # Пример:
    input_data = 'yes'
    # Преобразование в строку и приведение к нижнему регистру: 'yes' -> 'yes'
    # Проверка на соответствие строковым представлениям True: 'yes' in {'true', '1', 'yes', 'y', 'on'} -> True
    # Возвращается True
    ```

2.  **`normalize_string(input_data: str | list) -> str`**:
    *   Проверяет, является ли входное значение пустой строкой. Если да, возвращает пустую строку.
    *   Проверяет, является ли входное значение строкой или списком. Если нет, вызывает исключение `TypeError`.
    *   Если входное значение является списком, объединяет его элементы в одну строку с пробелами.
    *   Удаляет HTML-теги, переносы строк и специальные символы.
    *   Удаляет лишние пробелы и приводит строку к кодировке UTF-8.
    *   Если преобразование не удалось, логирует ошибку и возвращает исходное значение.

    ```python
    # Пример:
    input_data = ['Hello', '  World!  ']
    # Объединение списка в строку: ['Hello', '  World!  '] -> 'Hello   World!  '
    # Удаление HTML-тегов (не применимо в данном примере)
    # Удаление переносов строк (не применимо в данном примере)
    # Удаление специальных символов (не применимо в данном примере)
    # Удаление лишних пробелов: 'Hello   World!  ' -> 'Hello World!'
    # Приведение к кодировке UTF-8: 'Hello World!' -> 'Hello World!'
    # Возвращается 'Hello World!'
    ```

3.  **`normalize_int(input_data: Union[str, int, float, Decimal]) -> int`**:
    *   Пытается преобразовать входное значение в целое число.
    *   Если входное значение является типом `Decimal`, оно сначала преобразуется в `int`.
    *   Возвращает целое число. Если преобразование не удалось, логирует ошибку и возвращает исходное значение.

    ```python
    # Пример:
    input_data = '42'
    # Преобразование в float: '42' -> 42.0
    # Преобразование в int: 42.0 -> 42
    # Возвращается 42
    ```

4.  **`normalize_float(value: Any) -> float | None`**:
    *   Проверяет, является ли входное значение пустым. Если да, возвращает 0.
    *   Если входное значение является списком или кортежем, рекурсивно нормализует каждый элемент и возвращает список нормализованных значений.
    *   Пытается преобразовать входное значение в число с плавающей точкой.
    *   Возвращает число с плавающей точкой. Если преобразование не удалось, логирует предупреждение и возвращает исходное значение.

    ```python
    # Пример:
    value = "3.14"
    # Преобразование в float: "3.14" -> 3.14
    # Возвращается 3.14
    ```

5.  **`normalize_sql_date(input_data: str) -> str`**:
    *   Пытается преобразовать входное значение в дату в формате SQL (`YYYY-MM-DD`).
    *   Если входное значение является строкой, пытается распарсить его в соответствии с различными форматами даты (`%Y-%m-%d`, `%m/%d/%Y`, `%d/%m/%Y`).
    *   Если входное значение является объектом `datetime`, преобразует его в дату в формате SQL.
    *   Возвращает дату в формате SQL. Если преобразование не удалось, логирует ошибку и возвращает исходное значение.

    ```python
    # Пример:
    input_data = '12/06/2024'
    # Попытка распарсить дату из строки:
    # '%Y-%m-%d': не удается распарсить
    # '%m/%d/%Y': удается распарсить -> datetime(2024, 12, 6)
    # Преобразование в формат SQL: datetime(2024, 12, 6) -> '2024-12-06'
    # Возвращается '2024-12-06'
    ```

6.  **`simplify_string(input_str: str) -> str`**:
    *   Удаляет все символы, кроме букв, цифр и пробелов.
    *   Заменяет пробелы на символы подчеркивания.
    *   Удаляет последовательные символы подчеркивания.
    *   Возвращает упрощенную строку.

    ```python
    # Пример:
    input_str = "It's a test string with 'single quotes', numbers 123 and symbols!"
    # Удаление всех символов, кроме букв, цифр и пробелов: "It's a test string with 'single quotes', numbers 123 and symbols!" -> "Its a test string with single quotes numbers 123 and symbols"
    # Замена пробелов на символы подчеркивания: "Its a test string with single quotes numbers 123 and symbols" -> "Its_a_test_string_with_single_quotes_numbers_123_and_symbols"
    # Удаление последовательных символов подчеркивания (не применимо в данном примере)
    # Возвращается "Its_a_test_string_with_single_quotes_numbers_123_and_symbols"
    ```

7.  **`remove_line_breaks(input_str: str) -> str`**:
    *   Удаляет переносы строк (`\n`) и возвраты каретки (`\r`) из входной строки, заменяя их на пробелы.
    *   Удаляет начальные и конечные пробелы.
    *   Возвращает строку без переносов строк.

    ```python
    # Пример:
    input_str = "Hello\nWorld!\r"
    # Замена переносов строк и возвратов каретки на пробелы: "Hello\nWorld!\r" -> "Hello World! "
    # Удаление начальных и конечных пробелов: "Hello World! " -> "Hello World!"
    # Возвращается "Hello World!"
    ```

8.  **`remove_html_tags(input_html: str) -> str`**:
    *   Удаляет HTML-теги из входной строки.
    *   Удаляет начальные и конечные пробелы.
    *   Возвращает строку без HTML-тегов.

    ```python
    # Пример:
    input_html = "<p>Hello</p> World!"
    # Удаление HTML-тегов: "<p>Hello</p> World!" -> "Hello World!"
    # Удаление начальных и конечных пробелов: "Hello World!" -> "Hello World!"
    # Возвращается "Hello World!"
    ```

9.  **`remove_special_characters(input_str: str | list, chars: list[str] = None) -> str | list`**:
    *   Удаляет указанные специальные символы из строки или списка строк.
    *   Если список символов для удаления не указан, используется список по умолчанию (`['#']`).
    *   Возвращает строку или список строк без указанных символов.

    ```python
    # Пример:
    input_str = "Hello# World!"
    chars = ['#', '!']
    # Удаление специальных символов: "Hello# World!" -> "Hello World"
    # Возвращается "Hello World"
    ```

10. **`normalize_sku(input_str: str) -> str`**:
    *   Удаляет еврейские ключевые слова (`מקט`, `מק''ט`) из входной строки.
    *   Удаляет все не-буквенно-цифровые символы, кроме дефисов.
    *   Возвращает нормализованную строку SKU.

    ```python
    # Пример:
    input_str = "מקט: 303235-A"
    # Удаление еврейских ключевых слов: "מקט: 303235-A" -> ": 303235-A"
    # Удаление всех не-буквенно-цифровых символов, кроме дефисов: ": 303235-A" -> "303235-A"
    # Возвращается "303235-A"
    ```

### **<mermaid>**

```mermaid
flowchart TD
    subgraph normalize_boolean
        A[input_data: Any] --> B{isinstance(input_data, bool)?}
        B -- True --> C[return input_data]
        B -- False --> D[input_str = str(input_data).strip().lower()]
        D --> E{input_str in {'true', '1', 'yes', 'y', 'on', True, 1}?}
        E -- True --> F[return True]
        E -- False --> G{input_str in {'false', '0', 'no', 'n', 'off', False, 0}?}
        G -- True --> H[return False]
        G -- False --> I[logger.debug(f'Неожиданное значение для преобразования в bool: {input_data}')]
        I --> J[return original_input]
    end

    subgraph normalize_string
        AA[input_data: str | list] --> BB{not input_data?}
        BB -- True --> CC[return '']
        BB -- False --> DD{isinstance(input_data, (str, list))?}
        DD -- False --> EE[raise TypeError('Данные должны быть строкой или списком строк.')]
        DD -- True --> FF{isinstance(input_data, list)?}
        FF -- True --> GG[input_data = ' '.join(map(str, input_data))]
        FF -- False --> HH[cleaned_str = remove_html_tags(input_data)]
        HH --> II[cleaned_str = remove_line_breaks(cleaned_str)]
        II --> JJ[cleaned_str = remove_special_characters(cleaned_str)]
        JJ --> KK[normalized_str = ' '.join(cleaned_str.split())]
        KK --> LL[return normalized_str.strip().encode('utf-8').decode('utf-8')]
    end

    subgraph normalize_int
        AAA[input_data: Union[str, int, float, Decimal]] --> BBB{isinstance(input_data, Decimal)?}
        BBB -- True --> CCC[return int(input_data)]
        BBB -- False --> DDD[return int(float(input_data))]
        DDD -- Exception --> EEE[logger.error('Ошибка в normalize_int: ', ex)]
        EEE --> FFF[return original_input]
    end

    subgraph normalize_float
        AAAA[value: Any] --> BBBB{not value?}
        BBBB -- True --> CCCC[return 0]
        BBBB -- False --> DDDD{isinstance(value, (list, tuple))?}
        DDDD -- True --> EEEE[return [v for v in (normalize_float(v) for v in value) if v is not None]]
        DDDD -- False --> FFFF[return float(value)]
        FFFF -- Exception --> GGGG[logger.warning(f"Невозможно преобразовать '{value}' в float.")]
        GGGG --> HHHH[return original_value]
    end

    subgraph normalize_sql_date
        AAAAA[input_data: str] --> BBBBB{isinstance(input_data, str)?}
        BBBBB -- True --> CCCCC[Loop through date_format in ['%Y-%m-%d', '%m/%d/%Y', '%d/%m/%Y']]
        CCCCC --> DDDDD{try parsing date with date_format}
        DDDDD -- Success --> EEEEE[normalized_date = datetime.strptime(input_data, date_format).date()]
        EEEEE --> FFFFF[return normalized_date.isoformat()]
        DDDDD -- ValueError --> CCCCC
        BBBBB -- False --> GGGGG{isinstance(input_data, datetime)?}
        GGGGG -- True --> HHHHH[return input_data.date().isoformat()]
        GGGGG -- False --> IIIII[logger.debug(f'Не удалось преобразовать в SQL дату: {input_data}')]
        IIIII --> JJJJJ[return original_input]
    end

    subgraph simplify_string
        AAAAAA[input_str: str] --> BBBBBB[cleaned_str = re.sub(r'[^a-zA-Z0-9\\s]', '', input_str)]
        BBBBBB --> CCCCCC[cleaned_str = cleaned_str.replace(' ', '_')]
        CCCCCC --> DDDDDD[cleaned_str = re.sub(r'_+', '_', cleaned_str)]
        DDDDDD --> EEEEEE[return cleaned_str]
    end

    subgraph remove_line_breaks
        AAAAAAA[input_str: str] --> BBBBBBB[return input_str.replace('\n', ' ').replace('\r', ' ').strip()]
    end

    subgraph remove_html_tags
        AAAAAAAA[input_html: str] --> BBBBBBBB[return re.sub(r'<.*?>', '', input_html).strip()]
    end

    subgraph remove_special_characters
        AAAAAAAAA[input_str: str | list, chars: list[str] = None] --> BBBBBBBBB{chars is None?}
        BBBBBBBBB -- True --> CCCCCCCCC[chars = ['#']]
        BBBBBBBBB -- False --> CCCCCCCCC[chars = chars]
        CCCCCCCCC --> DDDDDDDDD[pattern = '[' + re.escape(''.join(chars)) + ']']
        DDDDDDDDD --> EEEEEEEEE{isinstance(input_str, list)?}
        EEEEEEEEE -- True --> FFFFFFFFF[return [re.sub(pattern, '', s) for s in input_str]]
        EEEEEEEEE -- False --> GGGGGGGGG[return re.sub(pattern, '', input_str)]
    end

    subgraph normalize_sku
        AAAAAAAAAA[input_str: str] --> BBBBBBBBBB[_str = re.sub(r'מקט|מק\'\'ט', '', input_str, flags=re.IGNORECASE)]
        BBBBBBBBBB --> CCCCCCCCC[normalized_sku = re.sub(r'[^\w-]+', '', _str)]
        CCCCCCCCCC --> DDDDDDDDDD[return normalized_sku]
    end
```

Диаграмма `mermaid` описывает потоки данных и логику внутри каждой функции нормализации. Каждая функция представлена как подграф, показывающий шаги преобразования входных данных и возвращаемое значение.

Импортированные зависимости:
*   `re`: Используется в функциях `simplify_string`, `remove_html_tags`, `remove_special_characters` и `normalize_sku` для операций с регулярными выражениями, таких как удаление HTML-тегов, специальных символов и упрощение строк.
*   `html`: Не используется в предоставленном коде.
*   `datetime`: Используется в функции `normalize_sql_date` для работы с датами и их преобразования в формат SQL.
*   `decimal`: Используется в функции `normalize_int` для обработки чисел с плавающей точкой с фиксированной точностью.
*   `typing`: Используется для аннотации типов, таких как `Any`, `List`, `Union`, чтобы указать типы входных и выходных данных функций.
*   `src.logger.logger`: Используется для логирования ошибок и отладочной информации в каждой функции нормализации.

### **<объяснение>**

**Импорты**:

*   `re`: Модуль регулярных выражений, используемый для поиска и замены текста на основе шаблонов.
*   `html`: Модуль для работы с HTML-сущностями (не используется напрямую в данном коде).
*   `datetime`: Модуль для работы с датой и временем.
*   `decimal.Decimal`: Класс для представления десятичных чисел с фиксированной точностью.
*   `decimal.InvalidOperation`: Исключение, которое может быть вызвано при недопустимой операции с `Decimal`.
*   `typing.Any`: Тип, указывающий, что переменная может быть любого типа.
*   `typing.List`: Тип, представляющий список элементов определенного типа.
*   `typing.Union`: Тип, указывающий, что переменная может быть одного из нескольких типов.
*   `src.logger.logger`: Пользовательский модуль для логирования.

**Функции**:

*   `normalize_boolean(input_data: Any) -> bool`:
    *   Принимает любое значение и пытается преобразовать его в булево.
    *   Возвращает `True` или `False` в зависимости от входного значения.
    *   Пример: `normalize_boolean('yes')` вернет `True`.
*   `normalize_string(input_data: str | list) -> str`:
    *   Принимает строку или список строк и нормализует ее.
    *   Удаляет HTML-теги, переносы строк и специальные символы.
    *   Возвращает нормализованную строку в кодировке UTF-8.
    *   Пример: `normalize_string(['Hello', '  World!  '])` вернет `'Hello World!'`.
*   `normalize_int(input_data: Union[str, int, float, Decimal]) -> int`:
    *   Принимает строку, целое число, число с плавающей точкой или `Decimal` и пытается преобразовать его в целое число.
    *   Возвращает целое число.
    *   Пример: `normalize_int('42')` вернет `42`.
*   `normalize_float(value: Any) -> float | None`:
    *   Принимает любое значение и пытается преобразовать его в число с плавающей точкой.
    *   Если входное значение является списком или кортежем, рекурсивно нормализует каждый элемент и возвращает список нормализованных значений.
    *   Возвращает число с плавающей точкой или `None`, если преобразование не удалось.
    *   Пример: `normalize_float("3.14")` вернет `3.14`.
*   `normalize_sql_date(input_data: str) -> str`:
    *   Принимает строку и пытается преобразовать ее в дату в формате SQL (`YYYY-MM-DD`).
    *   Поддерживает различные форматы даты.
    *   Возвращает дату в формате SQL или исходное значение, если преобразование не удалось.
    *   Пример: `normalize_sql_date('12/06/2024')` вернет `'2024-12-06'`.
*   `simplify_string(input_str: str) -> str`:
    *   Принимает строку и упрощает ее, оставляя только буквы, цифры и заменяя пробелы на символы подчеркивания.
    *   Возвращает упрощенную строку.
*   `remove_line_breaks(input_str: str) -> str`:
    *   Удаляет переносы строк (`\n`) и возвраты каретки (`\r`) из входной строки.
    *   Возвращает строку без переносов строк.
*   `remove_html_tags(input_html: str) -> str`:
    *   Удаляет HTML-теги из входной строки.
    *   Возвращает строку без HTML-тегов.
*   `remove_special_characters(input_str: str | list, chars: list[str] = None) -> str | list`:
    *   Удаляет указанные специальные символы из строки или списка строк.
    *   Возвращает строку или список строк без указанных символов.
*   `normalize_sku(input_str: str) -> str`:
    *   Нормализует SKU, удаляя еврейские ключевые слова и не-буквенно-цифровые символы (кроме дефисов).
    *   Возвращает нормализованную строку SKU.

**Переменные**:

*   `original_input`: Используется для сохранения исходного значения входных данных в функциях нормализации. Если преобразование не удалось, возвращается исходное значение.
*   `logger`: Экземпляр логгера, используемый для записи ошибок и отладочной информации.
*   `chars`: Список символов, которые нужно удалить в функции `remove_special_characters`.
*   `pattern`: Шаблон регулярного выражения для удаления специальных символов в функции `remove_special_characters`.

**Потенциальные ошибки и области для улучшения**:

*   В некоторых функциях нормализации, таких как `normalize_boolean`, в случае ошибки возвращается исходное значение. Это может привести к непредсказуемому поведению, если вызывающая сторона ожидает булево значение. Возможно, лучше выбрасывать исключение или возвращать `None`.
*   В функции `normalize_string` можно добавить возможность указания кодировки входной строки.
*   В функции `normalize_sql_date` можно добавить возможность указания формата даты.

**Взаимосвязи с другими частями проекта**:

*   Этот модуль используется для нормализации данных перед их сохранением в базе данных или использованием в других частях проекта.
*   Модуль `src.logger.logger` используется для логирования ошибок и отладочной информации.