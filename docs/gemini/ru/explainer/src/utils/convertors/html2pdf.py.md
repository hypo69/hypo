# Проект `hypotez`
# Роль `code explainer`

## АНАЛИЗ КОДА: `hypotez/src/utils/convertors/html.py`

### 1. <алгоритм>

#### 1. `html2escape`
   - **Вход**: HTML строка.
   - **Обработка**: Преобразует HTML в escape-последовательности с использованием `StringFormatter.escape_html_tags`.
   - **Выход**: Escape-последовательность.
   - **Пример**:
     ```
     html = "<p>Hello, world!</p>"
     result = html2escape(html)  # result == "&lt;p&gt;Hello, world!&lt;/p&gt;"
     ```

#### 2. `escape2html`
   - **Вход**: Строка с escape-последовательностями.
   - **Обработка**: Преобразует escape-последовательности обратно в HTML с использованием `StringFormatter.unescape_html_tags`.
   - **Выход**: HTML строка.
   - **Пример**:
     ```
     escaped = "&lt;p&gt;Hello, world!&lt;/p&gt;"
     result = escape2html(escaped)  # result == "<p>Hello, world!</p>"
     ```

#### 3. `html2dict`
   - **Вход**: HTML строка.
   - **Обработка**: Использует класс `HTMLToDictParser` для разбора HTML и извлечения данных.
   - **Выход**: Словарь, где ключи - теги HTML, значения - их содержимое.
     - Создается экземпляр `HTMLToDictParser`.
     - Вызывается метод `feed` для обработки HTML строки.
     - Результат возвращается в виде словаря.
   - **Пример**:
     ```
     html = "<p>Hello</p><a href='link'>World</a>"
     result = html2dict(html)  # result == {'p': 'Hello', 'a': 'World'}
     ```

#### 4. `html2ns`
   - **Вход**: HTML строка.
   - **Обработка**:
     - Преобразует HTML в словарь с помощью `html2dict`.
     - Преобразует словарь в объект `SimpleNamespace`.
   - **Выход**: Объект `SimpleNamespace`, где атрибуты - теги HTML, значения - их содержимое.
   - **Пример**:
     ```
     html = "<p>Hello</p><a href='link'>World</a>"
     result = html2ns(html)
     print(result.p)  # Вывод: Hello
     print(result.a)  # Вывод: World
     ```

#### 5. `html2pdf`
   - **Вход**: HTML строка и путь к PDF файлу.
   - **Обработка**:
     - Попытка конвертации HTML в PDF с использованием `WeasyPrint`.
     - В случае неудачи, логирование ошибки.
   - **Выход**: `True` в случае успеха, `None` в случае ошибки.
   - **Пример**:
     ```
     html = "<p>Hello, world!</p>"
     pdf_file = "output.pdf"
     result = html2pdf(html, pdf_file)  # Создаст файл output.pdf с содержимым "Hello, world!"
     ```

### 2. <mermaid>

```mermaid
graph TD
    A[html2escape] --> B{StringFormatter.escape_html_tags}
    B --> C[Возврат escape-последовательности]
    D[escape2html] --> E{StringFormatter.unescape_html_tags}
    E --> F[Возврат HTML]
    G[html2dict] --> H{HTMLToDictParser}
    H --> I{parser.feed(html_str)}
    I --> J[Возврат dict]
    K[html2ns] --> L{html2dict}
    L --> M{SimpleNamespace(**html_dict)}
    M --> N[Возврат SimpleNamespace]
    O[html2pdf] --> P{HTML(string=html_str).write_pdf(pdf_file)}
    P --> Q[Возврат True]
    P -- Exception --> R[Логирование ошибки]
    R --> S[Возврат None]
```

**Объяснение `mermaid`:**

- `html2escape`: Функция, преобразующая HTML в escape-последовательности.
- `StringFormatter.escape_html_tags`: Метод, выполняющий преобразование HTML в escape-последовательности.
- `escape2html`: Функция, преобразующая escape-последовательности обратно в HTML.
- `StringFormatter.unescape_html_tags`: Метод, выполняющий преобразование escape-последовательностей в HTML.
- `html2dict`: Функция, преобразующая HTML в словарь.
- `HTMLToDictParser`: Класс, используемый для разбора HTML и извлечения данных.
- `parser.feed(html_str)`: Метод класса `HTMLToDictParser`, который обрабатывает HTML строку.
- `html2ns`: Функция, преобразующая HTML в объект `SimpleNamespace`.
- `html2dict`: Функция, используемая для преобразования HTML в словарь.
- `SimpleNamespace(**html_dict)`: Конструктор `SimpleNamespace`, принимающий словарь в качестве аргументов.
- `html2pdf`: Функция, преобразующая HTML в PDF.
- `HTML(string=html_str).write_pdf(pdf_file)`: Метод, выполняющий конвертацию HTML в PDF с использованием `WeasyPrint`.
- `Логирование ошибки`: Логирование возникающих исключений при генерации PDF.

### 3. <объяснение>

#### Импорты:

- `re`: Используется для работы с регулярными выражениями.
- `typing.Dict`: Используется для аннотации типов, указывая, что переменная должна быть словарем.
- `pathlib.Path`: Используется для работы с путями к файлам и директориям.
- `src.logger.logger.logger`: Используется для логирования событий и ошибок.
- `types.SimpleNamespace`: Используется для создания объектов, к атрибутам которых можно обращаться через точку.
- `html.parser.HTMLParser`: Используется для разбора HTML.
- `xhtml2pdf.pisa`: Используется для конвертации HTML в PDF.
- `weasyprint.HTML`: Используется для конвертации HTML в PDF.

#### Классы:

- `HTMLToDictParser(HTMLParser)`:
  - Роль: Разбор HTML и преобразование его в словарь.
  - Атрибуты:
    - `result`: Словарь, хранящий результаты разбора HTML.
    - `current_tag`: Текущий обрабатываемый тег.
  - Методы:
    - `handle_starttag(self, tag, attrs)`: Обрабатывает начало тега.
    - `handle_endtag(self, tag)`: Обрабатывает конец тега.
    - `handle_data(self, data)`: Обрабатывает данные между тегами.

#### Функции:

- `html2escape(input_str: str) -> str`:
  - Аргументы:
    - `input_str` (str): HTML код для преобразования.
  - Возвращаемое значение:
    - `str`: HTML, преобразованный в escape-последовательности.
  - Назначение: Преобразует HTML в escape-последовательности для безопасного отображения.
  - Пример:
    ```python
    html = "<p>Hello, world!</p>"
    result = html2escape(html)
    print(result)  # Вывод: &lt;p&gt;Hello, world!&lt;/p&gt;
    ```

- `escape2html(input_str: str) -> str`:
  - Аргументы:
    - `input_str` (str): Строка с escape-последовательностями.
  - Возвращаемое значение:
    - `str`: HTML код.
  - Назначение: Преобразует escape-последовательности обратно в HTML.
  - Пример:
    ```python
    escaped = "&lt;p&gt;Hello, world!&lt;/p&gt;"
    result = escape2html(escaped)
    print(result)  # Вывод: <p>Hello, world!</p>
    ```

- `html2dict(html_str: str) -> Dict[str, str]`:
  - Аргументы:
    - `html_str` (str): HTML строка для преобразования.
  - Возвращаемое значение:
    - `dict`: Словарь, где ключи - теги HTML, значения - их содержимое.
  - Назначение: Преобразует HTML в словарь для удобного доступа к данным.
  - Пример:
    ```python
    html = "<p>Hello</p><a href='link'>World</a>"
    result = html2dict(html)
    print(result)  # Вывод: {'p': 'Hello', 'a': 'World'}
    ```

- `html2ns(html_str: str) -> SimpleNamespace`:
  - Аргументы:
    - `html_str` (str): HTML строка для преобразования.
  - Возвращаемое значение:
    - `SimpleNamespace`: Объект `SimpleNamespace` с атрибутами, соответствующими тегам HTML.
  - Назначение: Преобразует HTML в объект `SimpleNamespace` для удобного доступа к данным через атрибуты.
  - Пример:
    ```python
    html = "<p>Hello</p><a href='link'>World</a>"
    result = html2ns(html)
    print(result.p)  # Вывод: Hello
    print(result.a)  # Вывод: World
    ```

- `html2pdf(html_str: str, pdf_file: str | Path) -> bool | None`:
  - Аргументы:
    - `html_str` (str): HTML строка для преобразования.
    - `pdf_file` (str | Path): Путь к PDF файлу.
  - Возвращаемое значение:
    - `bool | None`: `True` в случае успеха, `None` в случае ошибки.
  - Назначение: Преобразует HTML в PDF файл.
  - Пример:
    ```python
    html = "<p>Hello, world!</p>"
    pdf_file = "output.pdf"
    result = html2pdf(html, pdf_file)
    ```

#### Переменные:

- `input_str` (str): Используется как входной параметр для функций `html2escape` и `escape2html`.
- `html_str` (str): Используется как входной параметр для функций `html2dict`, `html2ns` и `html2pdf`.
- `pdf_file` (str | Path): Используется как входной параметр для функции `html2pdf`, определяя путь к выходному PDF файлу.
- `result` (dict): Используется в функции `html2dict` для хранения результата преобразования HTML в словарь.
- `parser` (HTMLToDictParser): Используется в функции `html2dict` как экземпляр класса `HTMLToDictParser` для разбора HTML.
- `logger` (Logger): Используется для логирования ошибок.

#### Потенциальные ошибки и области для улучшения:

- Обработка ошибок в `html2pdf`: В случае неудачи при конвертации HTML в PDF, функция просто возвращает `None`. Желательно добавить более информативное сообщение об ошибке.
- Зависимости: Код использует `WeasyPrint` для конвертации HTML в PDF. Если `WeasyPrint` не установлен, возникнет исключение. Необходимо добавить обработку этого случая.
- Отсутствие обработки CSS: Код не обрабатывает CSS стили при конвертации HTML в PDF. Это может привести к неправильному отображению HTML в PDF.
- Использование `StringFormatter`: В коде используются методы `StringFormatter.escape_html_tags` и `StringFormatter.unescape_html_tags`, но класс `StringFormatter` не определен в данном файле. Необходимо убедиться, что этот класс определен в другом месте проекта и доступен для использования.

#### Взаимосвязи с другими частями проекта:

- `src.logger.logger`: Используется для логирования ошибок.
- `StringFormatter`: (предположительно) Используется для форматирования строк.