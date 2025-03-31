# Модуль: ali_campaign_editor_jupyter_widgets

## Обзор

Модуль `ali_campaign_editor_jupyter_widgets.py` предоставляет набор виджетов Jupyter для управления кампаниями AliExpress непосредственно в Jupyter Notebook. Он включает в себя инструменты для выбора кампаний, категорий и языков, а также для выполнения таких действий, как инициализация редактора кампаний, сохранение кампаний и отображение продуктов.

## Подробней

Этот модуль предназначен для упрощения процесса редактирования и управления кампаниями AliExpress. Он использует виджеты Jupyter для предоставления интерактивного интерфейса, который позволяет пользователям настраивать параметры кампании, просматривать продукты и сохранять изменения. Модуль интегрируется с Google Sheets для хранения и управления данными кампании.

## Классы

### `JupyterCampaignEditorWidgets`

**Описание**: Класс `JupyterCampaignEditorWidgets` предоставляет виджеты для взаимодействия с редактором кампаний AliExpress.

**Методы**:
- `__init__`: Инициализирует виджеты и настраивает редактор кампаний.
- `initialize_campaign_editor`: Инициализирует редактор кампаний на основе выбранной кампании и категории.
- `update_category_dropdown`: Обновляет выпадающий список категорий на основе выбранной кампании.
- `on_campaign_name_change`: Обрабатывает изменения в выпадающем списке названий кампаний.
- `on_category_change`: Обрабатывает изменения в выпадающем списке категорий.
- `on_language_change`: Обрабатывает изменения в выпадающем списке языков.
- `save_campaign`: Сохраняет кампанию и её категории.
- `show_products`: Отображает продукты в выбранной категории.
- `open_spreadsheet`: Открывает Google Spreadsheet в браузере.
- `setup_callbacks`: Настраивает обратные вызовы для виджетов.
- `display_widgets`: Отображает виджеты для взаимодействия в Jupyter Notebook.

**Параметры**:
- `language` (str): Выбранный язык.
- `currency` (str): Выбранная валюта.
- `campaign_name` (str): Название кампании.
- `category_name` (str): Название категории.
- `category` (SimpleNamespace): Объект SimpleNamespace, представляющий категорию.
- `campaign_editor` (AliCampaignEditor): Экземпляр класса `AliCampaignEditor`.
- `products` (list[SimpleNamespace]): Список объектов SimpleNamespace, представляющих продукты.

**Примеры**:

```python
>>> editor_widgets: JupyterCampaignEditorWidgets = JupyterCampaignEditorWidgets()
>>> editor_widgets.display_widgets()
```

## Функции

### `__init__`

```python
def __init__(self):
    """Инициализирует виджеты и настраивает редактор кампаний.

    Настраивает виджеты для выбора кампаний, категорий и языков. Также настраивает
    значения по умолчанию и обратные вызовы для виджетов.
    """
    ...
```

**Описание**: Инициализирует виджеты Jupyter, устанавливает пути к директориям кампаний, создает выпадающие списки для выбора кампаний, категорий и языков, а также настраивает кнопки для выполнения различных действий.

**Методы**: # если есть методы
- `campaigns_directory`: Возвращает путь к директории кампаний.
- `campaign_name_dropdown`: Возвращает выпадающий список названий кампаний.
- `category_name_dropdown`: Возвращает выпадающий список категорий.
- `language_dropdown`: Возвращает выпадающий список языков.
- `initialize_button`: Возвращает кнопку инициализации редактора кампаний.
- `save_button`: Возвращает кнопку сохранения кампаний.
- `show_products_button`: Возвращает кнопку отображения продуктов.
- `open_spreadsheet_button`: Возвращает кнопку открытия Google Spreadsheet.

**Параметры**: # если есть параметры
- `self.campaigns_directory` (str): Путь к директории кампаний.
- `self.campaign_name_dropdown` (ipywidgets.widgets.Dropdown): Выпадающий список названий кампаний.
- `self.category_name_dropdown` (ipywidgets.widgets.Dropdown): Выпадающий список категорий.
- `self.language_dropdown` (ipywidgets.widgets.Dropdown): Выпадающий список языков.
- `self.initialize_button` (ipywidgets.widgets.Button): Кнопка инициализации редактора кампаний.
- `self.save_button` (ipywidgets.widgets.Button): Кнопка сохранения кампаний.
- `self.show_products_button` (ipywidgets.widgets.Button): Кнопка отображения продуктов.
- `self.open_spreadsheet_button` (ipywidgets.widgets.Button): Кнопка открытия Google Spreadsheet.

**Примеры**:
```python
editor_widgets: JupyterCampaignEditorWidgets = JupyterCampaignEditorWidgets()
```

### `initialize_campaign_editor`

```python
def initialize_campaign_editor(self, _):
    """Инициализирует редактор кампаний.

    Args:
        _: Неиспользуемый аргумент, необходимый для обратного вызова кнопки.

    Устанавливает редактор кампаний на основе выбранной кампании и категории.
    """
    ...
```

**Описание**: Инициализирует редактор кампаний AliExpress на основе выбранных значений кампании, категории и языка/валюты. Получает значения из выпадающих списков и устанавливает соответствующие атрибуты экземпляра класса.

**Параметры**:
- `_`: Неиспользуемый аргумент, требуется для обратного вызова кнопки.

**Примеры**:
```python
self.initialize_campaign_editor(None)
```

### `update_category_dropdown`

```python
def update_category_dropdown(self, campaign_name: str):
    """Обновляет выпадающий список категорий на основе выбранной кампании.

    Args:
        campaign_name (str): Название кампании.

    Example:
        >>> self.update_category_dropdown("SummerSale")
    """
    ...
```

**Описание**: Обновляет выпадающий список категорий на основе выбранного имени кампании.

**Параметры**:
- `campaign_name` (str): Название кампании.

**Примеры**:
```python
self.update_category_dropdown("SummerSale")
```

### `on_campaign_name_change`

```python
def on_campaign_name_change(self, change: dict[str, str]):
    """Обрабатывает изменения в выпадающем списке названий кампаний.

    Args:
        change (dict[str, str]): Словарь изменений, содержащий новое значение.

    Example:
        >>> self.on_campaign_name_change({'new': 'SummerSale'})
    """
    ...
```

**Описание**: Обрабатывает событие изменения названия кампании в выпадающем списке. Обновляет атрибут `campaign_name` и вызывает `update_category_dropdown` для обновления списка категорий.

**Параметры**:
- `change` (dict[str, str]): Словарь, содержащий информацию об изменении.

**Примеры**:
```python
self.on_campaign_name_change({'new': 'SummerSale'})
```

### `on_category_change`

```python
def on_category_change(self, change: dict[str, str]):
    """Обрабатывает изменения в выпадающем списке категорий.

    Args:
        change (dict[str, str]): Словарь изменений, содержащий новое значение.

    Example:
        >>> self.on_category_change({'new': 'Electronics'})
    """
    ...
```

**Описание**: Обрабатывает событие изменения категории в выпадающем списке. Обновляет атрибут `category_name` и вызывает `initialize_campaign_editor` для переинициализации редактора кампаний с новой категорией.

**Параметры**:
- `change` (dict[str, str]): Словарь, содержащий информацию об изменении.

**Примеры**:
```python
self.on_category_change({'new': 'Electronics'})
```

### `on_language_change`

```python
def on_language_change(self, change: dict[str, str]):
    """Обрабатывает изменения в выпадающем списке языков.

    Args:
        change (dict[str, str]): Словарь изменений, содержащий новое значение.

    Example:
        >>> self.on_language_change({'new': 'EN USD'})
    """
    ...
```

**Описание**: Обрабатывает событие изменения языка в выпадающем списке. Обновляет атрибуты `language` и `currency` и вызывает `initialize_campaign_editor` для переинициализации редактора кампаний с новым языком и валютой.

**Параметры**:
- `change` (dict[str, str]): Словарь, содержащий информацию об изменении.

**Примеры**:
```python
self.on_language_change({'new': 'EN USD'})
```

### `save_campaign`

```python
def save_campaign(self, _):
    """Сохраняет кампанию и её категории.

    Args:
        _: Неиспользуемый аргумент, необходимый для обратного вызова кнопки.

    Example:
        >>> self.save_campaign(None)
    """
    ...
```

**Описание**: Сохраняет кампанию и ее категории, используя значения, выбранные в выпадающих списках. Инициализирует `AliCampaignEditor` и вызывает метод `save_categories_from_worksheet` для сохранения данных.

**Параметры**:
- `_`: Неиспользуемый аргумент, требуется для обратного вызова кнопки.

**Примеры**:
```python
self.save_campaign(None)
```

### `show_products`

```python
def show_products(self, _):
    """Отображает продукты в выбранной категории.

    Args:
        _: Неиспользуемый аргумент, необходимый для обратного вызова кнопки.

    Example:
        >>> self.show_products(None)
    """
    ...
```

**Описание**: Отображает продукты в выбранной категории, инициализирует `AliCampaignEditor` и вызывает метод `set_products_worksheet` для отображения данных в Google Sheets.

**Параметры**:
- `_`: Неиспользуемый аргумент, требуется для обратного вызова кнопки.

**Примеры**:
```python
self.show_products(None)
```

### `open_spreadsheet`

```python
def open_spreadsheet(self, _):
    """Открывает Google Spreadsheet в браузере.

    Args:
        _: Неиспользуемый аргумент, необходимый для обратного вызова кнопки.

    Example:
        >>> self.open_spreadsheet(None)
    """
    ...
```

**Описание**: Открывает связанный Google Spreadsheet в браузере. Требует предварительной инициализации `campaign_editor`.

**Параметры**:
- `_`: Неиспользуемый аргумент, требуется для обратного вызова кнопки.

**Примеры**:
```python
self.open_spreadsheet(None)
```

### `setup_callbacks`

```python
def setup_callbacks(self):
    """Настраивает обратные вызовы для виджетов."""
    ...
```

**Описание**: Устанавливает обратные вызовы для виджетов, чтобы реагировать на изменения значений и нажатия кнопок.

### `display_widgets`

```python
def display_widgets(self):
    """Отображает виджеты для взаимодействия в Jupyter notebook.

    Инициализирует редактор кампаний автоматически с первой выбранной кампанией.

    Example:
        >>> self.display_widgets()
    """
    ...
```

**Описание**: Отображает все виджеты в Jupyter Notebook для взаимодействия с пользователем. Включает выпадающие списки для выбора кампании, категории и языка, а также кнопки для инициализации редактора, сохранения кампании, отображения продуктов и открытия Google Spreadsheet.

**Примеры**:
```python
self.display_widgets()