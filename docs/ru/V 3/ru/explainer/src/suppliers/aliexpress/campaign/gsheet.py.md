## <алгоритм>

Этот код предназначен для работы с Google Sheets, автоматизации заполнения данными о рекламных кампаниях AliExpress, категориях и продуктах.

1.  **Инициализация `AliCampaignGoogleSheet`**:

    *   При создании экземпляра класса `AliCampaignGoogleSheet` происходит инициализация подключения к Google Sheets с использованием ID таблицы, указанного в `spreadsheet_id`.
    *   В конструктор передаются параметры `campaign_name`, `language` и `currency`, которые используются для настройки кампании.
2.  **Очистка данных**:

    *   Метод `clear` удаляет все листы продуктов из таблицы, оставляя только листы `categories`, `product`, `category` и `campaign`.
    *   `delete_products_worksheets` получает список всех листов, исключает основные и удаляет остальные.
3.  **Запись данных о кампании**:

    *   Метод `set_campaign_worksheet` записывает данные о кампании (название, заголовок, язык, валюта, описание) на лист `campaign`.
    *   Данные записываются вертикально, начиная с ячейки A1.
4.  **Запись данных о продуктах**:

    *   Метод `set_products_worksheet` копирует лист `product` и переименовывает его в соответствии с названием категории.
    *   Затем он записывает данные о продуктах на этот лист, извлекая информацию из объектов `SimpleNamespace`.
    *   После записи данных производится форматирование листа.
5.  **Запись данных о категориях**:

    *   Метод `set_categories_worksheet` записывает данные о категориях на лист `categories`.
    *   Перед записью данных лист очищается.
    *   Данные о категориях извлекаются из объекта `SimpleNamespace`.
    *   После записи данных производится форматирование листа.
6.  **Получение данных о категориях**:

    *   Метод `get_categories` получает данные о категориях с листа `categories` и возвращает их в виде списка словарей.
7.  **Запись данных о продуктах для категории**:

    *   Метод `set_category_products` записывает данные о продуктах для указанной категории на лист, скопированный из шаблона `product`.
    *   Данные о продуктах извлекаются из словаря `products`.
    *   После записи данных производится форматирование листа.
8.  **Форматирование листов**:

    *   Методы `_format_categories_worksheet` и `_format_category_products_worksheet` отвечают за форматирование листов `categories` и продуктов соответственно.
    *   Включает установку ширины столбцов, высоты строк и форматирование заголовков.

```mermaid
graph LR
    A[Начало] --> B{Инициализация AliCampaignGoogleSheet};
    B --> C{clear()};
    C --> D{delete_products_worksheets()};
    D --> E{set_campaign_worksheet(campaign)};
    E --> F{set_products_worksheet(category_name)};
    F --> G{set_categories_worksheet(categories)};
    G --> H{get_categories()};
    H --> I{set_category_products(category_name, products)};
    I --> J{_format_categories_worksheet(ws)};
    J --> K{_format_category_products_worksheet(ws)};
    K --> L[Конец];
```

## <mermaid>

```mermaid
flowchart TD
    A[Начало] --> B{__init__(campaign_name, language, currency)};
    B --> C{clear()};
    C --> D{delete_products_worksheets()};
    D --> E{set_campaign_worksheet(campaign)};
    E --> F{set_products_worksheet(category_name)};
    F --> G{set_categories_worksheet(categories)};
    G --> H{get_categories()};
    H --> I{set_category_products(category_name, products)};
    I --> J{_format_categories_worksheet(ws)};
    J --> K{_format_category_products_worksheet(ws)};
    K --> L[Конец];

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style L fill:#f9f,stroke:#333,stroke-width:2px
```

**Объяснение зависимостей:**

*   `time`: Используется для добавления задержек между операциями, например, перед копированием листа.
*   `typing`: Используется для аннотации типов, что улучшает читаемость и облегчает отладку кода.
*   `gspread.worksheet.Worksheet`: Класс, представляющий рабочий лист Google Sheets.
*   `src.goog.spreadsheet.spreadsheet.SpreadSheet`: Базовый класс для работы с Google Sheets, предоставляющий общие методы для подключения, чтения и записи данных.
*   `src.utils.jjson.j_dumps`: Функция для преобразования данных в формат JSON.
*   `src.utils.printer.pprint`: Функция для красивого вывода данных в консоль.
*   `src.logger.logger.logger`: Модуль для логирования событий и ошибок.
*   `src.ai.openai.translate`: Модуль для перевода текста с использованием OpenAI API.
*   `gspread_formatting`: (Закомментированные импорты) Библиотека для форматирования листов Google Sheets.

## <объяснение>

**Импорты:**

*   `time`: Используется для добавления задержек между операциями, например, `time.sleep(10)`.
*   `types.SimpleNamespace`: Используется для создания объектов, к которым можно обращаться по атрибутам, например, `campaign.campaign_name`.
*   `typing.Optional`: Используется для указания, что переменная может быть `None`.
*   `gspread.worksheet.Worksheet`: Класс для работы с отдельными листами Google Sheets.
*   `src.goog.spreadsheet.spreadsheet.SpreadSheet`: Базовый класс для работы с Google Sheets.
*   `src.utils.jjson.j_dumps`: Функция для преобразования данных в JSON-строку.
*   `src.utils.printer.pprint`: Функция для красивой печати данных.
*   `src.logger.logger.logger`: Модуль для логирования.
*   `src.ai.openai.translate`: Модуль для перевода текста с использованием OpenAI.

**Классы:**

*   `AliCampaignGoogleSheet(SpreadSheet)`: Класс для работы с Google Sheets в рамках кампаний AliExpress.
    *   `spreadsheet_id`: ID таблицы Google Sheets.
    *   `spreadsheet`: Объект `SpreadSheet` для работы с таблицей.
    *   `worksheet`: Объект `Worksheet` для работы с листом.
    *   `__init__(self, campaign_name: str, language: str | dict = None, currency: str = None)`: Конструктор класса.
    *   `clear(self)`: Очищает данные в таблице.
    *   `delete_products_worksheets(self)`: Удаляет листы продуктов.
    *   `set_campaign_worksheet(self, campaign: SimpleNamespace)`: Записывает данные о кампании на лист.
    *   `set_products_worksheet(self, category_name: str)`: Записывает данные о продуктах на лист.
    *   `set_categories_worksheet(self, categories: SimpleNamespace)`: Записывает данные о категориях на лист.
    *   `get_categories(self)`: Получает данные о категориях с листа.
    *   `set_category_products(self, category_name: str, products: dict)`: Записывает данные о продуктах для категории на лист.
    *   `_format_categories_worksheet(self, ws: Worksheet)`: Форматирует лист `categories`.
    *   `_format_category_products_worksheet(self, ws: Worksheet)`: Форматирует лист продуктов.

**Функции:**

*   `__init__(self, campaign_name: str, language: str | dict = None, currency: str = None)`:
    *   Аргументы:
        *   `campaign_name` (`str`): Название кампании.
        *   `language` (`str` | `dict`, optional): Язык кампании. По умолчанию `None`.
        *   `currency` (`str`, optional): Валюта кампании. По умолчанию `None`.
    *   Назначение: Инициализация объекта `AliCampaignGoogleSheet`.
*   `clear(self)`:
    *   Аргументы: Нет.
    *   Назначение: Очистка данных в таблице.
*   `delete_products_worksheets(self)`:
    *   Аргументы: Нет.
    *   Назначение: Удаление листов продуктов из таблицы.
*   `set_campaign_worksheet(self, campaign: SimpleNamespace)`:
    *   Аргументы:
        *   `campaign` (`SimpleNamespace`): Объект с данными о кампании.
    *   Назначение: Запись данных о кампании на лист `campaign`.
*   `set_products_worksheet(self, category_name: str)`:
    *   Аргументы:
        *   `category_name` (`str`): Название категории.
    *   Назначение: Запись данных о продуктах на лист.
*   `set_categories_worksheet(self, categories: SimpleNamespace)`:
    *   Аргументы:
        *   `categories` (`SimpleNamespace`): Объект с данными о категориях.
    *   Назначение: Запись данных о категориях на лист `categories`.
*   `get_categories(self)`:
    *   Аргументы: Нет.
    *   Возвращаемое значение: Данные о категориях в виде списка словарей.
    *   Назначение: Получение данных о категориях с листа `categories`.
*   `set_category_products(self, category_name: str, products: dict)`:
    *   Аргументы:
        *   `category_name` (`str`): Название категории.
        *   `products` (`dict`): Словарь с данными о продуктах.
    *   Назначение: Запись данных о продуктах для категории на лист.
*   `_format_categories_worksheet(self, ws: Worksheet)`:
    *   Аргументы:
        *   `ws` (`Worksheet`): Объект листа Google Sheets.
    *   Назначение: Форматирование листа `categories`.
*   `_format_category_products_worksheet(self, ws: Worksheet)`:
    *   Аргументы:
        *   `ws` (`Worksheet`): Объект листа Google Sheets.
    *   Назначение: Форматирование листа продуктов.

**Переменные:**

*   `spreadsheet_id`: (`str`): ID таблицы Google Sheets.
*   `spreadsheet`: (`SpreadSheet`): Объект для работы с таблицей Google Sheets.
*   `worksheet`: (`Worksheet`): Объект для работы с листом Google Sheets.

**Потенциальные ошибки и области для улучшения:**

*   Обработка исключений: В большинстве методов используется `try...except`, но в некоторых случаях просто логируется ошибка и выполняется `raise`. Это может привести к прерыванию выполнения программы.
*   Использование `SimpleNamespace`: Использование `SimpleNamespace` может быть неудобным для работы с данными, так как не предоставляет возможности валидации и автозаполнения.
*   Закомментированный код: В коде присутствует закомментированный код, который следует удалить или пересмотреть.
*   Отсутствие документации для некоторых методов: Некоторые методы не имеют документации, что затрудняет понимание их назначения.
*   Форматирование: Жестко заданное форматирование листов может быть негибким.
*   Дублирование кода: Методы `set_products_worksheet` и `set_category_products` содержат много повторяющегося кода.

**Взаимосвязи с другими частями проекта:**

*   `src.goog.spreadsheet.spreadsheet.SpreadSheet`: Используется для работы с Google Sheets.
*   `src.utils.jjson`: Используется для работы с JSON.
*   `src.utils.printer`: Используется для печати данных.
*   `src.logger.logger`: Используется для логирования.
*   `src.ai.openai`: Используется для перевода текста (если это необходимо).

```mermaid
flowchart TD
    Start --> A[<code>src.suppliers.aliexpress.campaign.gsheet.py</code>]
    A --> B[<code>src.goog.spreadsheet.spreadsheet.py</code>]
    A --> C[<code>src.utils.jjson.py</code>]
    A --> D[<code>src.utils.printer.py</code>]
    A --> E[<code>src.logger.logger.py</code>]
    A --> F[<code>src.ai.openai.py</code>]
    style A fill:#f9f,stroke:#333,stroke-width:2px