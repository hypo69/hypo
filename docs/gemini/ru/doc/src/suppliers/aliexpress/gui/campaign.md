# Модуль hypotez/src/suppliers/aliexpress/gui/campaign.py

## Обзор

Этот модуль предоставляет класс `CampaignEditor` для редактирования кампаний AliExpress.  Класс позволяет открывать JSON-файлы с данными о кампании, загружать их, отображать и редактировать информацию, а также готовить кампанию к использованию.

## Классы

### `CampaignEditor`

**Описание**:  Класс `CampaignEditor` представляет собой виджет PyQt6 для редактирования данных кампании AliExpress. Он предоставляет интерфейс для открытия файла, загрузки данных, редактирования полей (Название, Описание, Название акции) и запуска подготовки кампании.

**Атрибуты**:

- `data: SimpleNamespace`: Содержит загруженные данные кампании в формате `SimpleNamespace`.
- `current_campaign_file: str`: Путь к текущему загруженному файлу кампании.
- `editor: AliCampaignEditor`: Экземпляр класса `AliCampaignEditor` для подготовки кампании.


**Методы**:

#### `__init__(self, parent=None, main_app=None)`

**Описание**: Инициализирует виджет `CampaignEditor`.

**Параметры**:
- `parent` (Optional): Родительский виджет.
- `main_app` (Optional): Экземпляр главного приложения.

#### `setup_ui(self)`

**Описание**: Настраивает пользовательский интерфейс (UI).

#### `setup_connections(self)`

**Описание**: Настраивает соединения между элементами UI и обработчиками событий.

#### `open_file(self)`

**Описание**: Открывает диалоговое окно выбора файла для открытия JSON-файла кампании.

**Возвращает** :
-  Не имеет возвращаемого значения.

#### `load_file(self, campaign_file)`

**Описание**: Загружает JSON-файл кампании.

**Параметры**:
- `campaign_file (str)`: Путь к файлу кампании.

**Возвращает**:
-  Не имеет возвращаемого значения.

**Обрабатывает исключения**:
- `Exception`: При ошибке загрузки JSON файла выводится сообщение об ошибке.


#### `create_widgets(self, data)`

**Описание**: Создает виджеты для отображения и редактирования загруженных данных кампании.

**Параметры**:
- `data (SimpleNamespace)`: Данные кампании.


#### `prepare_campaign(self)`

**Описание**: Асинхронно подготавливает кампанию к использованию.

**Возвращает**:
- Не имеет возвращаемого значения.

**Обрабатывает исключения**:
- `Exception`: Если подготовка кампании завершается ошибкой, выводится сообщение об ошибке.


## Функции

(Здесь нет функций в этом модуле)


##  Обрабатываемые исключения

(Все исключения обрабатываются в методах)


## Замечания

- Для корректной работы требуется наличие модулей `header`, `asyncio`, `sys`, `pathlib`, `types`, `PyQt6`, `qasync`, `src.utils.jjson`, `src.suppliers.aliexpress.campaign`, `styles`.
- В коде используются виджеты PyQt6 для построения пользовательского интерфейса.
-  Используется асинхронная обработка (`@asyncSlot`) для подготовки кампаний, что улучшает отзывчивость приложения.