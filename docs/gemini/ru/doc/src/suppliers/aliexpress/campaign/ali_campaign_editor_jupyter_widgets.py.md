# Модуль: ali_campaign_editor_jupyter_widgets

## Обзор

Модуль `ali_campaign_editor_jupyter_widgets` предоставляет Jupyter-виджеты для редактирования кампаний AliExpress. Он включает виджеты для выбора кампаний, категорий и языков, а также для выполнения действий, таких как инициализация редактора, сохранение кампаний и отображение продуктов.

## Подробнее

Этот модуль предназначен для использования в Jupyter Notebook и предоставляет интерактивный интерфейс для управления кампаниями AliExpress. Он позволяет пользователям выбирать кампании, категории и языки из раскрывающихся списков, а также выполнять различные действия с помощью кнопок.

## Классы

### `JupyterCampaignEditorWidgets`

**Описание**:
Класс `JupyterCampaignEditorWidgets` предоставляет виджеты для взаимодействия с редактором кампаний AliExpress.

**Методы**:
- `__init__`: Инициализирует виджеты и настраивает редактор кампаний.
- `initialize_campaign_editor`: Инициализирует редактор кампаний на основе выбранной кампании и категории.
- `update_category_dropdown`: Обновляет выпадающий список категорий на основе выбранной кампании.
- `on_campaign_name_change`: Обрабатывает изменения в выпадающем списке названий кампаний.
- `on_category_change`: Обрабатывает изменения в выпадающем списке категорий.
- `on_language_change`: Обрабатывает изменения в выпадающем списке языков.
- `save_campaign`: Сохраняет кампанию и ее категории.
- `show_products`: Отображает продукты в выбранной категории.
- `open_spreadsheet`: Открывает Google Spreadsheet в браузере.
- `setup_callbacks`: Настраивает обратные вызовы для виджетов.
- `display_widgets`: Отображает виджеты для взаимодействия в Jupyter Notebook.

**Параметры**:
- `language` (str): Язык кампании.
- `currency` (str): Валюта кампании.
- `campaign_name` (str): Название кампании.
- `category_name` (str): Название категории.
- `category` (SimpleNamespace): Объект категории.
- `campaign_editor` (AliCampaignEditor): Редактор кампаний AliExpress.
- `products` (list[SimpleNamespace]): Список продуктов.

**Примеры**:
```python
>>> editor_widgets: JupyterCampaignEditorWidgets = JupyterCampaignEditorWidgets()
>>> editor_widgets.display_widgets()
```

## Функции

### `__init__`

```python
def __init__(self):
    """Initialize the widgets and set up the campaign editor.

    Sets up the widgets for selecting campaigns, categories, and languages. Also sets up
    default values and callbacks for the widgets.
    """
    ...
```

**Описание**:
Инициализирует виджеты и настраивает редактор кампаний. Устанавливает виджеты для выбора кампаний, категорий и языков. Также устанавливает значения по умолчанию и обратные вызовы для виджетов.

**Примеры**:
```python
editor_widgets = JupyterCampaignEditorWidgets()
```

### `initialize_campaign_editor`

```python
def initialize_campaign_editor(self, _):
    """Initialize the campaign editor.

    Args:
        _: Unused argument, required for button callback.

    Sets up the campaign editor based on the selected campaign and category.
    """
    ...
```

**Описание**:
Инициализирует редактор кампаний.

**Параметры**:
- `_`: Неиспользуемый аргумент, требуется для обратного вызова кнопки.

**Примеры**:
```python
editor_widgets.initialize_campaign_editor(None)
```

### `update_category_dropdown`

```python
def update_category_dropdown(self, campaign_name: str):
    """Update the category dropdown based on the selected campaign.

    Args:
        campaign_name (str): The name of the campaign.

    Example:
        >>> self.update_category_dropdown("SummerSale")
    """
    ...
```

**Описание**:
Обновляет выпадающий список категорий на основе выбранной кампании.

**Параметры**:
- `campaign_name` (str): Название кампании.

**Примеры**:
```python
editor_widgets.update_category_dropdown("SummerSale")
```

### `on_campaign_name_change`

```python
def on_campaign_name_change(self, change: dict[str, str]):
    """Handle changes in the campaign name dropdown.

    Args:
        change (dict[str, str]): The change dictionary containing the new value.

    Example:
        >>> self.on_campaign_name_change({'new': 'SummerSale'})
    """
    ...
```

**Описание**:
Обрабатывает изменения в выпадающем списке названий кампаний.

**Параметры**:
- `change` (dict[str, str]): Словарь изменений, содержащий новое значение.

**Примеры**:
```python
editor_widgets.on_campaign_name_change({'new': 'SummerSale'})
```

### `on_category_change`

```python
def on_category_change(self, change: dict[str, str]):
    """Handle changes in the category dropdown.

    Args:
        change (dict[str, str]): The change dictionary containing the new value.

    Example:
        >>> self.on_category_change({'new': 'Electronics'})
    """
    ...
```

**Описание**:
Обрабатывает изменения в выпадающем списке категорий.

**Параметры**:
- `change` (dict[str, str]): Словарь изменений, содержащий новое значение.

**Примеры**:
```python
editor_widgets.on_category_change({'new': 'Electronics'})
```

### `on_language_change`

```python
def on_language_change(self, change: dict[str, str]):
    """Handle changes in the language dropdown.

    Args:
        change (dict[str, str]): The change dictionary containing the new value.

    Example:
        >>> self.on_language_change({'new': 'EN USD'})
    """
    ...
```

**Описание**:
Обрабатывает изменения в выпадающем списке языков.

**Параметры**:
- `change` (dict[str, str]): Словарь изменений, содержащий новое значение.

**Примеры**:
```python
editor_widgets.on_language_change({'new': 'EN USD'})
```

### `save_campaign`

```python
def save_campaign(self, _):
    """Save the campaign and its categories.

    Args:
        _: Unused argument, required for button callback.

    Example:
        >>> self.save_campaign(None)
    """
    ...
```

**Описание**:
Сохраняет кампанию и ее категории.

**Параметры**:
- `_`: Неиспользуемый аргумент, требуется для обратного вызова кнопки.

**Примеры**:
```python
editor_widgets.save_campaign(None)
```

### `show_products`

```python
def show_products(self, _):
    """Display the products in the selected category.

    Args:
        _: Unused argument, required for button callback.

    Example:
        >>> self.show_products(None)
    """
    ...
```

**Описание**:
Отображает продукты в выбранной категории.

**Параметры**:
- `_`: Неиспользуемый аргумент, требуется для обратного вызова кнопки.

**Примеры**:
```python
editor_widgets.show_products(None)
```

### `open_spreadsheet`

```python
def open_spreadsheet(self, _):
    """Open the Google Spreadsheet in a browser.

    Args:
        _: Unused argument, required for button callback.

    Example:
        >>> self.open_spreadsheet(None)
    """
    ...
```

**Описание**:
Открывает Google Spreadsheet в браузере.

**Параметры**:
- `_`: Неиспользуемый аргумент, требуется для обратного вызова кнопки.

**Примеры**:
```python
editor_widgets.open_spreadsheet(None)
```

### `setup_callbacks`

```python
def setup_callbacks(self):
    """Set up callbacks for the widgets."""
    ...
```

**Описание**:
Настраивает обратные вызовы для виджетов.

### `display_widgets`

```python
def display_widgets(self):
    """Display the widgets for interaction in the Jupyter notebook.

    Initializes the campaign editor automatically with the first campaign selected.

    Example:
        >>> self.display_widgets()
    """
    ...
```

**Описание**:
Отображает виджеты для взаимодействия в Jupyter Notebook.

**Примеры**:
```python
editor_widgets.display_widgets()