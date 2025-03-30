# Проект `hypotez`
# Роль `code explainer`

## АНАЛИЗ КОДА: `prepare_campaigns.py`

### 1. <алгоритм>

Этот скрипт предназначен для подготовки рекламных кампаний AliExpress, обрабатывая категории, данные кампаний и генерируя рекламные материалы.

**Блок-схема процесса подготовки кампании:**

1.  **Запуск скрипта**:
    *   Скрипт запускается с аргументами командной строки, такими как имя кампании, категории, язык и валюта.
    *   Пример: `python prepare_campaigns.py summer_sale -c electronics -l EN -cu USD`

2.  **Обработка аргументов**:
    *   Аргументы командной строки обрабатываются с использованием `argparse`.
    *   Если указан флаг `--all`, обрабатываются все кампании.

3.  **Определение локалей**:
    *   Локали определяются на основе указанных языка и валюты.
    *   Если язык и валюта не указаны, используются все доступные локали из `src.suppliers.aliexpress.utils.locales`.

4.  **Обработка кампании (одиночной или всех)**:
    *   Если указана конкретная кампания, вызывается функция `main_process`.
    *   Если указан флаг `--all`, вызывается функция `process_all_campaigns`.

5.  **Функция `main_process`**:
    *   Определяет, нужно ли обрабатывать конкретные категории или всю кампанию.
    *   Если указаны категории, вызывается функция `process_campaign_category` для каждой категории.
    *   Если категории не указаны, вызывается функция `process_campaign` для всей кампании.

6.  **Функция `process_campaign_category`**:
    *   Создает экземпляр класса `AliCampaignEditor`.
    *   Вызывает метод `process_campaign_category` экземпляра `AliCampaignEditor` для обработки указанной категории.
    *   Возвращает список названий продуктов в категории.

7.  **Функция `process_campaign`**:
    *   Создает экземпляр класса `AliCampaignEditor`.
    *   Вызывает метод `process_campaign` экземпляра `AliCampaignEditor` для обработки всей кампании.
    *   Обрабатывает кампанию для каждой локали (язык и валюта).

8.  **Функция `process_all_campaigns`**:
    *   Получает список всех директорий кампаний из `campaigns_directory`.
    *   Для каждой кампании создает экземпляр класса `AliCampaignEditor`.
    *   Вызывает метод `process_campaign` экземпляра `AliCampaignEditor` для обработки всей кампании.
    *   Обрабатывает кампанию для каждой локали (язык и валюта).

9.  **Класс `AliCampaignEditor`**:
    *   Используется для обработки кампании, включая настройку, обработку категорий и генерацию рекламных материалов.
    *   Методы класса включают `process_campaign_category` и `process_campaign`.

10. **Логирование**:
    *   В процессе работы скрипта используются логи для отслеживания хода выполнения и записи ошибок.

### 2. <mermaid>

```mermaid
flowchart TD
    Start --> Input[Input: campaign_name, categories, language, currency, all]
    Input --> ProcessArgs{Process Arguments}
    ProcessArgs -- all is True --> ProcessAllCampaigns[process_all_campaigns]
    ProcessArgs -- all is False --> MainProcess[main_process]

    ProcessAllCampaigns --> GetCampaignDirs[Get campaign directories]
    GetCampaignDirs --> LoopCampaigns{Loop through campaign directories}
    LoopCampaigns --> AliCampaignEditorAll[AliCampaignEditor.process_campaign()]

    MainProcess --> DetermineLocales{Determine Locales}
    DetermineLocales -- Categories Provided --> LoopCategories{Loop through Categories}
    LoopCategories --> ProcessCategory[process_campaign_category]
    DetermineLocales -- No Categories --> ProcessCampaign[process_campaign]

    ProcessCategory --> AliCampaignEditorCat[AliCampaignEditor.process_campaign_category()]
    ProcessCampaign --> AliCampaignEditor[AliCampaignEditor.process_campaign()]

    AliCampaignEditorCat --> ReturnTitles[Return List of Titles]
    AliCampaignEditor --> ReturnBool[Return True]
    AliCampaignEditorAll --> End

    ReturnTitles --> End
    ReturnBool --> End
    Start --> Header[<code>header.py</code><br> Determine Project Root]

    Header --> import[Import Global Settings: <br><code>from src import gs</code>]
```

**Объяснение диаграммы:**

*   **Start**: Начало выполнения скрипта.
*   **Input**: Получение аргументов командной строки (имя кампании, категории, язык, валюта, флаг `--all`).
*   **ProcessArgs**: Обработка аргументов командной строки.
*   **ProcessAllCampaigns**: Функция `process_all_campaigns`, вызывается, если указан флаг `--all`.
*   **MainProcess**: Функция `main_process`, вызывается, если не указан флаг `--all`.
*   **GetCampaignDirs**: Получение списка директорий кампаний из `campaigns_directory`.
*   **LoopCampaigns**: Цикл по директориям кампаний.
*   **AliCampaignEditorAll**: Вызов метода `process_campaign` класса `AliCampaignEditor` для каждой кампании.
*   **DetermineLocales**: Определение локалей на основе указанных языка и валюты.
*   **LoopCategories**: Цикл по категориям, если они указаны.
*   **ProcessCategory**: Функция `process_campaign_category`, вызывается для обработки конкретной категории.
*   **ProcessCampaign**: Функция `process_campaign`, вызывается для обработки всей кампании.
*   **AliCampaignEditorCat**: Вызов метода `process_campaign_category` класса `AliCampaignEditor` для обработки категории.
*   **AliCampaignEditor**: Вызов метода `process_campaign` класса `AliCampaignEditor` для обработки кампании.
*   **ReturnTitles**: Возврат списка названий продуктов.
*   **ReturnBool**: Возврат `True`.
*   **End**: Конец выполнения скрипта.

**Зависимости:**

*   Импортируется класс `AliCampaignEditor` из `src.suppliers.aliexpress.campaign`.
*   Импортируется модуль `locales` из `src.suppliers.aliexpress.utils`.
*   Импортируются функции `get_directory_names` из `src.utils.file`, `j_loads_ns` из `src.utils.jjson` и `pprint` из `src.utils.printer`.
*   Импортируется модуль `logger` из `src.logger.logger`.
*   Импортируется `gs` из `src`.

### 3. <объяснение>

#### Импорты:

*   `header`: Импортирует модуль `header`, который, вероятно, содержит общие функции или настройки для проекта.
*   `argparse`: Используется для обработки аргументов командной строки.
*   `copy`: Используется для создания копий объектов.
*   `pathlib.Path`: Используется для работы с путями к файлам и директориям.
*   `typing.List, typing.Optional`: Используются для аннотации типов.
*   `src.gs`: Импортирует глобальные настройки проекта.
*   `src.suppliers.aliexpress.campaign.AliCampaignEditor`: Импортирует класс `AliCampaignEditor`, который используется для обработки кампаний AliExpress.
*   `src.suppliers.aliexpress.utils.locales`: Импортирует модуль `locales`, который содержит информацию о локалях (языках и валютах).
*   `src.utils.printer.pprint`: Импортирует функцию `pprint` для удобной печати данных.
*   `src.utils.file.get_directory_names`: Импортирует функцию `get_directory_names` для получения списка имен директорий.
*   `src.utils.jjson.j_loads_ns`: Импортирует функцию `j_loads_ns` для загрузки JSON файлов с обработкой пространств имен.
*   `src.logger.logger.logger`: Импортирует объект `logger` для логирования событий.

#### Классы:

*   `AliCampaignEditor`:
    *   Роль: Обработка кампаний AliExpress.
    *   Атрибуты:
        *   `campaign_name`: Имя кампании.
        *   `language`: Язык кампании.
        *   `currency`: Валюта кампании.
    *   Методы:
        *   `process_campaign_category(category_name)`: Обрабатывает категорию в кампании.
        *   `process_campaign()`: Обрабатывает кампанию.
    *   Взаимодействие: Используется в функциях `process_campaign_category`, `process_campaign` и `process_all_campaigns`.

#### Функции:

*   `process_campaign_category(campaign_name: str, category_name: str, language: str, currency: str) -> List[str]`:
    *   Аргументы:
        *   `campaign_name`: Имя кампании.
        *   `category_name`: Имя категории.
        *   `language`: Язык.
        *   `currency`: Валюта.
    *   Возвращаемое значение: `List[str]` - список названий продуктов в категории.
    *   Назначение: Обрабатывает указанную категорию в кампании для заданного языка и валюты.
    *   Пример: `titles = process_campaign_category("summer_sale", "electronics", "EN", "USD")`
*   `process_campaign(campaign_name: str, language: Optional[str] = None, currency: Optional[str] = None, campaign_file: Optional[str] = None) -> bool`:
    *   Аргументы:
        *   `campaign_name`: Имя кампании.
        *   `language`: Язык (необязательный).
        *   `currency`: Валюта (необязательная).
        *   `campaign_file`: Путь к файлу кампании (необязательный).
    *   Возвращаемое значение: `bool` - `True`, если кампания обработана успешно, иначе `False`.
    *   Назначение: Обрабатывает кампанию для заданного языка и валюты. Если язык и валюта не указаны, обрабатывает для всех доступных локалей.
    *   Пример: `res = process_campaign("summer_sale", "EN", "USD", "campaign_file.json")`
*   `process_all_campaigns(language: Optional[str] = None, currency: Optional[str] = None) -> None`:
    *   Аргументы:
        *   `language`: Язык (необязательный).
        *   `currency`: Валюта (необязательная).
    *   Возвращаемое значение: `None`.
    *   Назначение: Обрабатывает все кампании в директории `campaigns` для заданного языка и валюты. Если язык и валюта не указаны, обрабатывает для всех доступных локалей.
    *   Пример: `process_all_campaigns("EN", "USD")`
*   `main_process(campaign_name: str, categories: List[str] | str, language: Optional[str] = None, currency: Optional[str] = None) -> None`:
    *   Аргументы:
        *   `campaign_name`: Имя кампании.
        *   `categories`: Список категорий (может быть пустым).
        *   `language`: Язык (необязательный).
        *   `currency`: Валюта (необязательная).
    *   Возвращаемое значение: `None`.
    *   Назначение: Главная функция для обработки кампании. Определяет, нужно ли обрабатывать конкретные категории или всю кампанию.
    *   Пример: `main_process("summer_sale", ["electronics"], "EN", "USD")`
*   `main() -> None`:
    *   Аргументы: Нет.
    *   Возвращаемое значение: `None`.
    *   Назначение: Главная функция для парсинга аргументов командной строки и инициации обработки.
    *   Пример: `main()`

#### Переменные:

*   `campaigns_directory`:
    *   Тип: `pathlib.Path`
    *   Использование: Путь к директории с кампаниями AliExpress.
    *   Значение: `gs.path.google_drive / 'aliexpress' / 'campaigns'`
*   `_l`:
    *   Тип: `List[Tuple[str, str]]`
    *   Использование: Список кортежей, содержащих язык и валюту для обработки кампании.
    *   Значение: Формируется на основе `locales` или аргументов командной строки.

#### Потенциальные ошибки и области для улучшения:

*   В функции `process_campaign` всегда возвращается `True`, даже если в процессе обработки кампании произошла ошибка. Это может привести к неверной интерпретации результатов обработки.
*   Не хватает обработки исключений в функциях `process_campaign_category`, `process_campaign` и `process_all_campaigns`. В случае возникновения ошибки, скрипт просто завершится.
*   Использование `pprint` для отладочной печати. Лучше использовать `logger.debug` для отладочной информации.
*   Отсутствует валидация аргументов командной строки.

#### Взаимосвязи с другими частями проекта:

*   Использует `gs` из `src` для получения пути к директории с кампаниями.
*   Использует `AliCampaignEditor` из `src.suppliers.aliexpress.campaign` для обработки кампаний.
*   Использует `locales` из `src.suppliers.aliexpress.utils` для получения информации о локалях.
*   Использует `get_directory_names` из `src.utils.file` для получения списка имен директорий.
*   Использует `j_loads_ns` из `src.utils.jjson` для загрузки JSON файлов с обработкой пространств имен.
*   Использует `logger` из `src.logger.logger` для логирования событий.

---
**Header.py**
```mermaid
flowchart TD
    Start --> Header[<code>header.py</code><br> Determine Project Root]

    Header --> import[Import Global Settings: <br><code>from src import gs</code>]