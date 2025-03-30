# Модуль `ali_campaign_editor_jupyter_widgets`

## Обзор

Модуль `ali_campaign_editor_jupyter_widgets.py` предоставляет Jupyter виджеты для управления кампаниями AliExpress.
Он включает виджеты для выбора кампаний, категорий и языков, а также для выполнения таких действий, как инициализация редакторов, сохранение кампаний и отображение продуктов.

## Оглавление

- [Классы](#классы)
    - [`JupyterCampaignEditorWidgets`](#jupytercampaigneditorwidgets)
- [Функции](#функции)

## Классы

### `JupyterCampaignEditorWidgets`

**Описание**: Класс `JupyterCampaignEditorWidgets` предоставляет виджеты для взаимодействия и управления кампаниями AliExpress, включая выбор кампаний, категорий и языков, а также выполнение действий, таких как инициализация редакторов, сохранение кампаний и отображение продуктов.

**Атрибуты класса**:
- `language` (str): Выбранный язык.
- `currency` (str): Выбранная валюта.
- `campaign_name` (str): Название выбранной кампании.
- `category_name` (str): Название выбранной категории.
- `category` (SimpleNamespace): Объект категории.
- `campaign_editor` (AliCampaignEditor): Редактор кампании AliExpress.
- `products` (list[SimpleNamespace]): Список продуктов.

**Методы**:

- `__init__`
- `initialize_campaign_editor`
- `update_category_dropdown`
- `on_campaign_name_change`
- `on_category_change`
- `on_language_change`
- `save_campaign`
- `show_products`
- `open_spreadsheet`
- `setup_callbacks`
- `display_widgets`

#### `__init__`

**Описание**: Инициализирует виджеты и настраивает редактор кампании. Устанавливает виджеты для выбора кампаний, категорий и языков. Также устанавливает значения по умолчанию и обратные вызовы для виджетов.

```python
    def __init__(self):
        """Initialize the widgets and set up the campaign editor.

        Sets up the widgets for selecting campaigns, categories, and languages. Also sets up
        default values and callbacks for the widgets.
        """
```
#### `initialize_campaign_editor`

**Описание**: Инициализирует редактор кампании. Настраивает редактор кампании на основе выбранной кампании и категории.

**Параметры**:
- `_` (Any): Неиспользуемый аргумент, необходим для обратного вызова кнопки.

```python
    def initialize_campaign_editor(self, _):
        """Initialize the campaign editor.

        Args:
            _: Unused argument, required for button callback.

        Sets up the campaign editor based on the selected campaign and category.
        """
```

#### `update_category_dropdown`

**Описание**: Обновляет выпадающий список категорий на основе выбранной кампании.

**Параметры**:
- `campaign_name` (str): Название кампании.

```python
    def update_category_dropdown(self, campaign_name: str):
        """Update the category dropdown based on the selected campaign.

        Args:
            campaign_name (str): The name of the campaign.

        Example:
            >>> self.update_category_dropdown("SummerSale")
        """
```

#### `on_campaign_name_change`

**Описание**: Обрабатывает изменения в выпадающем списке названий кампаний.

**Параметры**:
- `change` (dict[str, str]): Словарь изменений, содержащий новое значение.

```python
    def on_campaign_name_change(self, change: dict[str, str]):
        """Handle changes in the campaign name dropdown.

        Args:
            change (dict[str, str]): The change dictionary containing the new value.

        Example:
            >>> self.on_campaign_name_change({'new': 'SummerSale'})
        """
```

#### `on_category_change`

**Описание**: Обрабатывает изменения в выпадающем списке категорий.

**Параметры**:
- `change` (dict[str, str]): Словарь изменений, содержащий новое значение.

```python
    def on_category_change(self, change: dict[str, str]):
        """Handle changes in the category dropdown.

        Args:
            change (dict[str, str]): The change dictionary containing the new value.

        Example:
            >>> self.on_category_change({'new': 'Electronics'})
        """
```

#### `on_language_change`

**Описание**: Обрабатывает изменения в выпадающем списке языков.

**Параметры**:
- `change` (dict[str, str]): Словарь изменений, содержащий новое значение.

```python
    def on_language_change(self, change: dict[str, str]):
        """Handle changes in the language dropdown.

        Args:
            change (dict[str, str]): The change dictionary containing the new value.

        Example:
            >>> self.on_language_change({'new': 'EN USD'})
        """
```

#### `save_campaign`

**Описание**: Сохраняет кампанию и ее категории.

**Параметры**:
- `_`: Неиспользуемый аргумент, необходим для обратного вызова кнопки.

```python
    def save_campaign(self, _):
        """Save the campaign and its categories.

        Args:
            _: Unused argument, required for button callback.

        Example:
            >>> self.save_campaign(None)
        """
```

#### `show_products`

**Описание**: Отображает продукты в выбранной категории.

**Параметры**:
- `_`: Неиспользуемый аргумент, необходим для обратного вызова кнопки.

```python
    def show_products(self, _):
        """Display the products in the selected category.

        Args:
            _: Unused argument, required for button callback.

        Example:
            >>> self.show_products(None)
        """
```

#### `open_spreadsheet`

**Описание**: Открывает Google Spreadsheet в браузере.

**Параметры**:
- `_`: Неиспользуемый аргумент, необходим для обратного вызова кнопки.

```python
    def open_spreadsheet(self, _):
        """Open the Google Spreadsheet in a browser.

        Args:
            _: Unused argument, required for button callback.

        Example:
            >>> self.open_spreadsheet(None)
        """
```

#### `setup_callbacks`

**Описание**: Устанавливает обратные вызовы для виджетов.

```python
    def setup_callbacks(self):
        """Set up callbacks for the widgets."""
```

#### `display_widgets`

**Описание**: Отображает виджеты для взаимодействия в Jupyter Notebook.

```python
    def display_widgets(self):
        """Display the widgets for interaction in the Jupyter notebook.

        Initializes the campaign editor automatically with the first campaign selected.

        Example:
            >>> self.display_widgets()
        """
```

## Функции

В данном модуле нет отдельных функций, все основные действия выполняются методами класса `JupyterCampaignEditorWidgets`.