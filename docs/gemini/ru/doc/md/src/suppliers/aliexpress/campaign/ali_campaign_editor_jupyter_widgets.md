# Модуль hypotez/src/suppliers/aliexpress/campaign/ali_campaign_editor_jupyter_widgets.py

## Обзор

Данный модуль содержит виджеты для управления кампаниями AliExpress в Jupyter Notebook.  Он позволяет выбирать кампании, категории и языки, инициализировать редактор, сохранять кампании и отображать продукты.

## Классы

### `JupyterCampaignEditorWidgets`

**Описание**: Класс предоставляет виджеты для взаимодействия с и управления кампаниями AliExpress, включая выбор кампаний, категорий и языков, а также выполнение действий, таких как инициализация редакторов, сохранение кампаний и отображение продуктов.


**Атрибуты:**

- `language: str = None`: Язык.
- `currency: str = None`: Валюта.
- `campaign_name: str = None`: Название кампании.
- `category_name: str = None`: Название категории.
- `category: SimpleNamespace = None`: Объект категории.
- `campaign_editor: AliCampaignEditor = None`: Объект редактора кампании.
- `products: list[SimpleNamespace] = None`: Список продуктов.


**Методы:**

#### `__init__(self)`

**Описание**: Инициализирует виджеты и настраивает редактор кампании.

**Возвращает**: None

#### `initialize_campaign_editor(self, _)`

**Описание**: Инициализирует редактор кампании.

**Параметры**:
- `_`: Неиспользуемый аргумент, необходимый для обратного вызова кнопки.

**Возвращает**: None

#### `update_category_dropdown(self, campaign_name: str)`

**Описание**: Обновляет выпадающий список категорий на основе выбранной кампании.

**Параметры**:
- `campaign_name (str)`: Название кампании.

**Возвращает**: None

#### `on_campaign_name_change(self, change: dict[str, str])`

**Описание**: Обрабатывает изменения в выпадающем списке названий кампаний.

**Параметры**:
- `change (dict[str, str])`: Словарь изменений, содержащий новое значение.


**Возвращает**: None


#### `on_category_change(self, change: dict[str, str])`

**Описание**: Обрабатывает изменения в выпадающем списке категорий.


**Параметры**:
- `change (dict[str, str])`: Словарь изменений, содержащий новое значение.


**Возвращает**: None


#### `on_language_change(self, change: dict[str, str])`

**Описание**: Обрабатывает изменения в выпадающем списке языков/валют.


**Параметры**:
- `change (dict[str, str])`: Словарь изменений, содержащий новое значение.


**Возвращает**: None

#### `save_campaign(self, _)`

**Описание**: Сохраняет кампанию и её категории.


**Параметры**:
- `_`: Неиспользуемый аргумент, необходимый для обратного вызова кнопки.


**Возвращает**: None

#### `show_products(self, _)`

**Описание**: Отображает продукты в выбранной категории.


**Параметры**:
- `_`: Неиспользуемый аргумент, необходимый для обратного вызова кнопки.


**Возвращает**: None

#### `open_spreadsheet(self, _)`

**Описание**: Открывает Google Таблицу в браузере.


**Параметры**:
- `_`: Неиспользуемый аргумент, необходимый для обратного вызова кнопки.


**Возвращает**: None


#### `setup_callbacks(self)`

**Описание**: Настраивает обратные вызовы для виджетов.


**Возвращает**: None

#### `display_widgets(self)`

**Описание**: Отображает виджеты для взаимодействия в Jupyter Notebook. Автоматически инициализирует редактор кампании с первой выбранной кампанией.


**Возвращает**: None


## Функции

(В модуле отсутствуют функции, кроме встроенных функций python)

## Подключаемые модули

- `header`
- `pathlib`
- `ipywidgets`
- `IPython.display`
- `webbrowser`
- `src.gs`
- `src.suppliers.aliexpress.campaign.AliCampaignEditor`
- `src.suppliers.aliexpress.utils.locales`
- `src.utils.pprint`
- `src.utils.get_directory_names`
- `src.logger`