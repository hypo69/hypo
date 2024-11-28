# Модуль hypotez/src/suppliers/aliexpress/gui/campaign.py

## Обзор

Этот модуль предоставляет класс `CampaignEditor` для редактирования кампаний AliExpress.  Он использует `QScrollArea`, `QPushButton`, `QLineEdit` и другие виджеты PyQt для отображения и редактирования данных кампании, загруженных из JSON файла. Класс также включает асинхронную функцию `prepare_campaign` для подготовки кампании.

## Оглавление

- [Модуль hypotez/src/suppliers/aliexpress/gui/campaign.py](#модуль-hypotezsrcsuppliersaliexpressguicampaignpy)
- [Класс `CampaignEditor`](#класс-campaigneditor)
    - [Метод `__init__`](#метод-init)
    - [Метод `setup_ui`](#метод-setup_ui)
    - [Метод `setup_connections`](#метод-setup_connections)
    - [Метод `open_file`](#метод-open_file)
    - [Метод `load_file`](#метод-load_file)
    - [Метод `create_widgets`](#метод-create_widgets)
    - [Метод `prepare_campaign`](#метод-prepare_campaign)


## Классы

### `CampaignEditor`

**Описание**: Класс `CampaignEditor` представляет собой виджет PyQt для редактирования данных кампаний AliExpress.

**Атрибуты**:

- `data`: `SimpleNamespace`, данные кампании, загруженные из JSON файла.
- `current_campaign_file`: `str`, путь к файлу кампании.
- `editor`: `AliCampaignEditor`, объект для подготовки кампании.
- `main_app`: `object`, ссылка на главное приложение.

**Методы**:

#### `__init__`

**Описание**: Инициализирует виджет `CampaignEditor`.

**Параметры**:
- `parent` (Optional): Родительский виджет.
- `main_app` (object): Главное приложение.

**Возвращает**:
-  None

#### `setup_ui`

**Описание**: Настраивает пользовательский интерфейс виджета.

**Возвращает**:
- None

#### `setup_connections`

**Описание**: Устанавливает соединения между сигналами и слотами.

**Возвращает**:
- None

#### `open_file`

**Описание**: Открывает диалог выбора файла JSON кампании.

**Возвращает**:
- None

#### `load_file`

**Описание**: Загружает данные из файла JSON кампании.

**Параметры**:
- `campaign_file` (str): Путь к файлу JSON кампании.

**Возвращает**:
- None

**Возможные исключения**:
- `Exception`: Возникает при ошибке загрузки JSON файла.  Сообщается пользователю с помощью `QtWidgets.QMessageBox.critical`.

#### `create_widgets`

**Описание**: Создает виджеты для отображения данных кампании.

**Параметры**:
- `data` (SimpleNamespace): Данные кампании.

**Возвращает**:
- None


#### `prepare_campaign`

**Описание**: Асинхронно подготавливает кампанию.

**Возвращает**:
- None

**Возможные исключения**:
- `Exception`: Возникает при ошибке подготовки кампании. Сообщается пользователю с помощью `QtWidgets.QMessageBox.critical`.