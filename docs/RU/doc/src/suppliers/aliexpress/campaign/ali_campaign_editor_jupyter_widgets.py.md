# Модуль `ali_campaign_editor_jupyter_widgets`

## Обзор

Модуль `ali_campaign_editor_jupyter_widgets.py` предоставляет Jupyter виджеты для управления кампаниями AliExpress. Он включает в себя инструменты для выбора кампаний, категорий и языков, а также выполнения таких действий, как инициализация редактора, сохранение кампаний и отображение товаров.

## Содержание

1. [Классы](#классы)
    - [`JupyterCampaignEditorWidgets`](#jupytercampaigneditorwidgets)
2. [Функции](#функции)
   - [`initialize_campaign_editor`](#initialize_campaign_editor)
   - [`update_category_dropdown`](#update_category_dropdown)
   - [`on_campaign_name_change`](#on_campaign_name_change)
   - [`on_category_change`](#on_category_change)
   - [`on_language_change`](#on_language_change)
   - [`save_campaign`](#save_campaign)
   - [`show_products`](#show_products)
   - [`open_spreadsheet`](#open_spreadsheet)
   - [`setup_callbacks`](#setup_callbacks)
   - [`display_widgets`](#display_widgets)

## Классы

### `JupyterCampaignEditorWidgets`

**Описание**:
Класс `JupyterCampaignEditorWidgets` предоставляет виджеты для взаимодействия и управления кампаниями AliExpress. Он позволяет выбирать кампании, категории и языки, а также выполнять действия, такие как инициализация редактора, сохранение кампаний и отображение товаров.

**Методы**:
  - `__init__`: Инициализирует виджеты и настраивает редактор кампаний.
  - `initialize_campaign_editor`: Инициализирует редактор кампаний на основе выбранной кампании и категории.
  - `update_category_dropdown`: Обновляет выпадающий список категорий на основе выбранной кампании.
  - `on_campaign_name_change`: Обрабатывает изменения в выпадающем списке названий кампаний.
  - `on_category_change`: Обрабатывает изменения в выпадающем списке категорий.
  - `on_language_change`: Обрабатывает изменения в выпадающем списке языков.
  - `save_campaign`: Сохраняет кампанию и ее категории.
  - `show_products`: Отображает товары в выбранной категории.
  - `open_spreadsheet`: Открывает Google Spreadsheet в браузере.
  - `setup_callbacks`: Настраивает обратные вызовы для виджетов.
  - `display_widgets`: Отображает виджеты для взаимодействия в Jupyter Notebook.

**Параметры**:
  - `language` (str): Выбранный язык.
  - `currency` (str): Выбранная валюта.
  - `campaign_name` (str): Выбранное название кампании.
  - `category_name` (str): Выбранное название категории.
  - `category` (SimpleNamespace): Выбранная категория.
  - `campaign_editor` (AliCampaignEditor): Экземпляр редактора кампаний AliExpress.
  - `products` (list[SimpleNamespace]): Список товаров.
  - `campaigns_directory` (str): Путь к директории с кампаниями.
  - `campaign_name_dropdown` (ipywidgets.Dropdown): Выпадающий список для выбора названия кампании.
  - `category_name_dropdown` (ipywidgets.Dropdown): Выпадающий список для выбора категории.
  - `language_dropdown` (ipywidgets.Dropdown): Выпадающий список для выбора языка и валюты.
  - `initialize_button` (ipywidgets.Button): Кнопка для инициализации редактора кампаний.
  - `save_button` (ipywidgets.Button): Кнопка для сохранения кампании.
  - `show_products_button` (ipywidgets.Button): Кнопка для отображения товаров.
  - `open_spreadsheet_button` (ipywidgets.Button): Кнопка для открытия Google Spreadsheet.

## Функции

### `initialize_campaign_editor`

**Описание**:
Инициализирует редактор кампаний на основе выбранной кампании и категории.

**Параметры**:
- `_` (Any): Неиспользуемый параметр, необходимый для обратного вызова кнопки.

**Возвращает**:
- `None`

### `update_category_dropdown`

**Описание**:
Обновляет выпадающий список категорий на основе выбранной кампании.

**Параметры**:
- `campaign_name` (str): Название кампании.

**Возвращает**:
- `None`

### `on_campaign_name_change`

**Описание**:
Обрабатывает изменения в выпадающем списке названий кампаний.

**Параметры**:
- `change` (dict[str, str]): Словарь изменений, содержащий новое значение.

**Возвращает**:
- `None`

### `on_category_change`

**Описание**:
Обрабатывает изменения в выпадающем списке категорий.

**Параметры**:
- `change` (dict[str, str]): Словарь изменений, содержащий новое значение.

**Возвращает**:
- `None`

### `on_language_change`

**Описание**:
Обрабатывает изменения в выпадающем списке языков.

**Параметры**:
- `change` (dict[str, str]): Словарь изменений, содержащий новое значение.

**Возвращает**:
- `None`

### `save_campaign`

**Описание**:
Сохраняет кампанию и ее категории.

**Параметры**:
- `_` (Any): Неиспользуемый параметр, необходимый для обратного вызова кнопки.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при сохранении кампании.

### `show_products`

**Описание**:
Отображает товары в выбранной категории.

**Параметры**:
- `_` (Any): Неиспользуемый параметр, необходимый для обратного вызова кнопки.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при отображении товаров.

### `open_spreadsheet`

**Описание**:
Открывает Google Spreadsheet в браузере.

**Параметры**:
- `_` (Any): Неиспользуемый параметр, необходимый для обратного вызова кнопки.

**Возвращает**:
- `None`

### `setup_callbacks`

**Описание**:
Настраивает обратные вызовы для виджетов.

**Параметры**:
- `None`

**Возвращает**:
- `None`

### `display_widgets`

**Описание**:
Отображает виджеты для взаимодействия в Jupyter Notebook.

**Параметры**:
- `None`

**Возвращает**:
- `None`