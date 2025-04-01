# Модуль для работы с виджетами редактора кампаний AliExpress в Jupyter Notebook
=========================================================================================

Модуль содержит класс `JupyterCampaignEditorWidgets`, который предоставляет интерфейс для управления кампаниями AliExpress в Jupyter Notebook.
Он позволяет выбирать кампании, категории и языки, а также выполнять действия, такие как инициализация редактора, сохранение кампаний и отображение продуктов.

## Обзор

Этот модуль предоставляет набор виджетов Jupyter для взаимодействия с редактором кампаний AliExpress. Он позволяет пользователям выбирать кампании, категории и языки, а также выполнять различные действия, такие как инициализация редактора кампаний, сохранение кампаний и отображение продуктов.

## Подробнее

Модуль предназначен для использования в Jupyter Notebook и предоставляет удобный интерфейс для управления кампаниями AliExpress. Он использует виджеты `ipywidgets` для создания интерактивных элементов управления, таких как выпадающие списки и кнопки.

## Классы

### `JupyterCampaignEditorWidgets`

**Описание**: Класс, предоставляющий виджеты для редактора кампаний AliExpress.

**Принцип работы**:
Класс `JupyterCampaignEditorWidgets` создает и управляет набором виджетов Jupyter для взаимодействия с редактором кампаний AliExpress. Он инициализирует виджеты, устанавливает обработчики событий и отображает их в Jupyter Notebook.

**Атрибуты**:
- `language` (str): Выбранный язык кампании.
- `currency` (str): Выбранная валюта кампании.
- `campaign_name` (str): Выбранное имя кампании.
- `category_name` (str): Выбранное имя категории.
- `category` (SimpleNamespace): Объект категории кампании.
- `campaign_editor` (AliCampaignEditor): Экземпляр редактора кампаний AliExpress.
- `products` (list[SimpleNamespace]): Список продуктов кампании.
- `campaigns_directory` (str): Путь к директории с файлами кампаний.
- `campaign_name_dropdown` (widgets.Dropdown): Выпадающий список для выбора имени кампании.
- `category_name_dropdown` (widgets.Dropdown): Выпадающий список для выбора категории.
- `language_dropdown` (widgets.Dropdown): Выпадающий список для выбора языка и валюты.
- `initialize_button` (widgets.Button): Кнопка для инициализации редактора кампаний.
- `save_button` (widgets.Button): Кнопка для сохранения кампании.
- `show_products_button` (widgets.Button): Кнопка для отображения продуктов.
- `open_spreadsheet_button` (widgets.Button): Кнопка для открытия Google Spreadsheet.

**Методы**:
- `__init__`: Инициализирует виджеты и настраивает редактор кампаний.
- `initialize_campaign_editor`: Инициализирует редактор кампаний на основе выбранных кампании и категории.
- `update_category_dropdown`: Обновляет выпадающий список категорий на основе выбранной кампании.
- `on_campaign_name_change`: Обрабатывает изменения в выпадающем списке имен кампаний.
- `on_category_change`: Обрабатывает изменения в выпадающем списке категорий.
- `on_language_change`: Обрабатывает изменения в выпадающем списке языков.
- `save_campaign`: Сохраняет кампанию и ее категории.
- `show_products`: Отображает продукты в выбранной категории.
- `open_spreadsheet`: Открывает Google Spreadsheet в браузере.
- `setup_callbacks`: Устанавливает обработчики событий для виджетов.
- `display_widgets`: Отображает виджеты для взаимодействия в Jupyter Notebook.

### `__init__`
```python
    def __init__(self):
        """Initialize the widgets and set up the campaign editor.

        Sets up the widgets for selecting campaigns, categories, and languages. Also sets up
        default values and callbacks for the widgets.
        """
        self.campaigns_directory:str = Path(
            gs.path.google_drive, "aliexpress", "campaigns"
        )
        
        if not self.campaigns_directory.exists():
            raise FileNotFoundError(
                f"Directory does not exist: {self.campaigns_directory}"
            )

        #self.languages = {"EN": "USD", "HE": "ILS", "RU": "ILS"}
        self.campaign_name_dropdown = widgets.Dropdown(
            options = get_directory_names(self.campaigns_directory),
            description = "Campaign Name:",
        )
        self.category_name_dropdown = widgets.Dropdown(
            options=[], description="Category:"
        )
        self.language_dropdown = widgets.Dropdown(
            options=[f"{key} {value}" for locale in locales for key, value in locale.items()],
            description="Language/Currency:",
        )
        self.initialize_button = widgets.Button(
            description="Initialize Campaign Editor",
            disabled=False,
        )
        self.save_button = widgets.Button(
            description="Save Campaign",
            disabled=False,
        )
        self.show_products_button = widgets.Button(
            description="Show Products",
            disabled=False,
        )
        self.open_spreadsheet_button = widgets.Button(
            description="Open Google Spreadsheet",
            disabled=False,
        )

        # Set up callbacks
        self.setup_callbacks()

        # Initialize with default values
        self.initialize_campaign_editor(None)
```

**Назначение**: Инициализирует виджеты и настраивает редактор кампаний.

**Как работает функция**:
1. **Определение пути к директории кампаний**:
   - Определяет путь к директории, в которой хранятся файлы кампаний AliExpress. Используется модуль `gs` для получения пути к Google Drive и конкатенирует его с путем к кампаниям AliExpress.
2. **Проверка существования директории**:
   - Проверяет, существует ли директория кампаний. Если директория не существует, вызывается исключение `FileNotFoundError`.
3. **Инициализация выпадающих списков и кнопок**:
   - Инициализирует выпадающий список `campaign_name_dropdown` для выбора имени кампании. Опции для этого списка загружаются из имен поддиректорий в директории кампаний.
   - Инициализирует выпадающий список `category_name_dropdown` для выбора категории. На момент инициализации опции для этого списка пусты.
   - Инициализирует выпадающий список `language_dropdown` для выбора языка и валюты. Опции для этого списка генерируются на основе данных из модуля `locales`.
   - Инициализирует кнопки `initialize_button`, `save_button`, `show_products_button` и `open_spreadsheet_button` для выполнения соответствующих действий.
4. **Настройка обработчиков событий**:
   - Вызывает метод `setup_callbacks` для установки обработчиков событий для виджетов.
5. **Инициализация редактора кампаний**:
   - Вызывает метод `initialize_campaign_editor` для инициализации редактора кампаний с значениями по умолчанию.

**ASCII схема работы функции**:

```
A [Определение пути к директории кампаний]
    |
B [Проверка существования директории]
    |
    -- C [Инициализация выпадающих списков и кнопок]
    |
D [Настройка обработчиков событий]
    |
E [Инициализация редактора кампаний]
```

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
        
        self.campaign_name = self.campaign_name_dropdown.value or None
        self.category_name = self.category_name_dropdown.value or None
        
        self.language, self.currency = self.language_dropdown.value.split()
        if self.campaign_name:
            self.update_category_dropdown(self.campaign_name)
            self.campaign_editor = AliCampaignEditor(campaign_name = self.campaign_name, language = self.language, currency = self.currency)
            
            if self.category_name:
                self.category = self.campaign_editor.get_category(self.category_name)
                self.products = self.campaign_editor.get_category_products(self.category_name)
        else:
            logger.warning(
                "Please select a campaign name before initializing the editor."
            )
```

**Назначение**: Инициализирует редактор кампаний.

**Параметры**:
- `_`: Неиспользуемый аргумент, необходимый для обратного вызова кнопки.

**Как работает функция**:

1. **Получение значений из виджетов**:
   - Извлекает имя кампании из выпадающего списка `campaign_name_dropdown` и сохраняет его в атрибуте `campaign_name`. Если значение не выбрано, устанавливает `campaign_name` в `None`.
   - Извлекает имя категории из выпадающего списка `category_name_dropdown` и сохраняет его в атрибуте `category_name`. Если значение не выбрано, устанавливает `category_name` в `None`.
   - Извлекает язык и валюту из выпадающего списка `language_dropdown`, разделяя строку на две части, и сохраняет их в атрибутах `language` и `currency` соответственно.
2. **Проверка наличия имени кампании**:
   - Проверяет, было ли выбрано имя кампании. Если имя кампании выбрано, выполняет следующие действия:
     - Обновляет выпадающий список категорий, вызывая метод `update_category_dropdown` с именем кампании.
     - Создает экземпляр класса `AliCampaignEditor` с выбранным именем кампании, языком и валютой.
     - Если имя категории также выбрано, выполняет следующие действия:
       - Получает объект категории из редактора кампаний, вызывая метод `get_category` с именем категории.
       - Получает список продуктов категории из редактора кампаний, вызывая метод `get_category_products` с именем категории.
3. **Вывод предупреждения**:
   - Если имя кампании не выбрано, выводит предупреждение в лог с помощью `logger.warning`, предлагая выбрать имя кампании перед инициализацией редактора.

**ASCII схема работы функции**:

```
A [Получение значений из виджетов]
    |
B [Проверка наличия имени кампании]
    |
    -- C [Обновление выпадающего списка категорий]
    |
    -- D [Создание экземпляра AliCampaignEditor]
    |
    -- E [Получение объекта категории и списка продуктов (если категория выбрана)]
    |
F [Вывод предупреждения (если имя кампании не выбрано)]
```

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

        campaign_path = self.campaigns_directory / campaign_name / "category"
        campaign_categories = get_directory_names(campaign_path)
        self.category_name_dropdown.options = campaign_categories
```

**Назначение**: Обновляет выпадающий список категорий на основе выбранной кампании.

**Параметры**:
- `campaign_name` (str): Имя кампании.

**Как работает функция**:

1. **Определение пути к директории категорий кампании**:
   - Формирует путь к директории, содержащей категории для указанной кампании. Путь строится на основе `self.campaigns_directory`, `campaign_name` и поддиректории `"category"`.
2. **Получение списка категорий**:
   - Использует функцию `get_directory_names` для получения списка имен поддиректорий в директории категорий кампании.
3. **Обновление опций выпадающего списка категорий**:
   - Устанавливает опции выпадающего списка `self.category_name_dropdown` равными полученному списку категорий.

**ASCII схема работы функции**:

```
A [Определение пути к директории категорий кампании]
    |
B [Получение списка категорий]
    |
C [Обновление опций выпадающего списка категорий]
```

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
        self.campaign_name = change["new"]
        self.update_category_dropdown(self.campaign_name)
        self.initialize_campaign_editor(None)  # Reinitialize with newcampaign
```

**Назначение**: Обрабатывает изменения в выпадающем списке имен кампаний.

**Параметры**:
- `change` (dict[str, str]): Словарь изменений, содержащий новое значение.

**Как работает функция**:

1. **Извлечение нового имени кампании**:
   - Извлекает новое имя кампании из словаря `change` по ключу `"new"` и сохраняет его в атрибуте `self.campaign_name`.
2. **Обновление выпадающего списка категорий**:
   - Вызывает метод `update_category_dropdown` с новым именем кампании для обновления выпадающего списка категорий.
3. **Повторная инициализация редактора кампаний**:
   - Вызывает метод `initialize_campaign_editor` для повторной инициализации редактора кампаний с новым именем кампании.

**ASCII схема работы функции**:

```
A [Извлечение нового имени кампании]
    |
B [Обновление выпадающего списка категорий]
    |
C [Повторная инициализация редактора кампаний]
```

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
        self.category_name = change["new"]
        self.initialize_campaign_editor(None)  # Reinitialize with new category
```

**Назначение**: Обрабатывает изменения в выпадающем списке категорий.

**Параметры**:
- `change` (dict[str, str]): Словарь изменений, содержащий новое значение.

**Как работает функция**:

1. **Извлечение нового имени категории**:
   - Извлекает новое имя категории из словаря `change` по ключу `"new"` и сохраняет его в атрибуте `self.category_name`.
2. **Повторная инициализация редактора кампаний**:
   - Вызывает метод `initialize_campaign_editor` для повторной инициализации редактора кампаний с новым именем категории.

**ASCII схема работы функции**:

```
A [Извлечение нового имени категории]
    |
B [Повторная инициализация редактора кампаний]
```

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
        self.language, self.currency = change["new"].split()
        self.initialize_campaign_editor(None)  # Reinitialize with new language/currency
```

**Назначение**: Обрабатывает изменения в выпадающем списке языков.

**Параметры**:
- `change` (dict[str, str]): Словарь изменений, содержащий новое значение.

**Как работает функция**:

1. **Извлечение нового языка и валюты**:
   - Извлекает новую строку языка и валюты из словаря `change` по ключу `"new"`.
   - Разделяет строку на две части (язык и валюту) с помощью метода `split()` и сохраняет их в атрибутах `self.language` и `self.currency` соответственно.
2. **Повторная инициализация редактора кампаний**:
   - Вызывает метод `initialize_campaign_editor` для повторной инициализации редактора кампаний с новым языком и валютой.

**ASCII схема работы функции**:

```
A [Извлечение нового языка и валюты]
    |
B [Повторная инициализация редактора кампаний]
```

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
        self.campaign_name = self.campaign_name_dropdown.value
        self.category_name = self.category_name_dropdown.value
        self.language, self.currency = self.language_dropdown.value.split()

        if self.campaign_name and self.language:
            self.campaign_editor = AliCampaignEditor(
                campaign_name=self.campaign_name,
                category_name=self.category_name if self.category_name else None,
                language=self.language,
            )
            try:
                self.campaign_editor.save_categories_from_worksheet()
            except Exception as ex:
                logger.error("Error saving campaign.", ex, True)
        else:
            logger.warning (
                "Please select campaign name and language/currency before saving the campaign."
            )
```

**Назначение**: Сохраняет кампанию и ее категории.

**Параметры**:
- `_`: Неиспользуемый аргумент, необходимый для обратного вызова кнопки.

**Как работает функция**:

1. **Получение значений из виджетов**:
   - Получает имя кампании из выпадающего списка `campaign_name_dropdown` и сохраняет его в атрибуте `self.campaign_name`.
   - Получает имя категории из выпадающего списка `category_name_dropdown` и сохраняет его в атрибуте `self.category_name`.
   - Получает язык и валюту из выпадающего списка `language_dropdown` и сохраняет их в атрибутах `self.language` и `self.currency`.
2. **Проверка наличия имени кампании и языка**:
   - Проверяет, выбраны ли имя кампании и язык. Если оба значения выбраны, выполняет следующие действия:
     - Создает экземпляр класса `AliCampaignEditor` с выбранным именем кампании, именем категории (если выбрано) и языком.
     - Пытается сохранить категории из рабочего листа, вызывая метод `save_categories_from_worksheet` редактора кампаний.
     - Если при сохранении возникает исключение, выводит сообщение об ошибке в лог с помощью `logger.error`.
3. **Вывод предупреждения**:
   - Если имя кампании или язык не выбраны, выводит предупреждение в лог с помощью `logger.warning`, предлагая выбрать имя кампании и язык/валюту перед сохранением кампании.

**ASCII схема работы функции**:

```
A [Получение значений из виджетов]
    |
B [Проверка наличия имени кампании и языка]
    |
    -- C [Создание экземпляра AliCampaignEditor]
    |
    -- D [Сохранение категорий из рабочего листа]
    |
    -- E [Вывод сообщения об ошибке (если возникло исключение)]
    |
F [Вывод предупреждения (если имя кампании или язык не выбраны)]
```

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
        campaign_name = self.campaign_name_dropdown.value
        category_name = self.category_name_dropdown.value

        try:
            self.campaign_editor = AliCampaignEditor(
                campaign_name=campaign_name,
                language=self.language,
                currency=self.currency,
            )
            self.campaign_editor.set_products_worksheet(category_name)
        except Exception as ex:
            logger.error("Error displaying products.", ex, True)
```

**Назначение**: Отображает продукты в выбранной категории.

**Параметры**:
- `_`: Неиспользуемый аргумент, необходимый для обратного вызова кнопки.

**Как работает функция**:

1. **Получение имени кампании и категории**:
   - Получает имя кампании из выпадающего списка `campaign_name_dropdown` и сохраняет его в переменной `campaign_name`.
   - Получает имя категории из выпадающего списка `category_name_dropdown` и сохраняет его в переменной `category_name`.
2. **Создание экземпляра `AliCampaignEditor` и установка рабочего листа продуктов**:
   - Пытается создать экземпляр класса `AliCampaignEditor` с выбранным именем кампании, языком и валютой.
   - Вызывает метод `set_products_worksheet` редактора кампаний с именем категории для установки рабочего листа продуктов.
3. **Обработка исключений**:
   - Если при создании экземпляра `AliCampaignEditor` или установке рабочего листа продуктов возникает исключение, выводит сообщение об ошибке в лог с помощью `logger.error`.

**ASCII схема работы функции**:

```
A [Получение имени кампании и категории]
    |
B [Создание экземпляра AliCampaignEditor и установка рабочего листа продуктов]
    |
C [Обработка исключений]
```

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
        if self.campaign_editor:
            spreadsheet_url = f"https://docs.google.com/spreadsheets/d/{self.campaign_editor.spreadsheet_id}/edit"
            webbrowser.open(spreadsheet_url)
        else:
            print("Please initialize the campaign editor first.")
```

**Назначение**: Открывает Google Spreadsheet в браузере.

**Параметры**:
- `_`: Неиспользуемый аргумент, необходимый для обратного вызова кнопки.

**Как работает функция**:

1. **Проверка инициализации редактора кампаний**:
   - Проверяет, был ли инициализирован редактор кампаний (т.е. существует ли атрибут `self.campaign_editor`).
2. **Открытие Google Spreadsheet**:
   - Если редактор кампаний инициализирован, формирует URL для Google Spreadsheet на основе `spreadsheet_id` редактора кампаний.
   - Открывает URL в браузере с помощью модуля `webbrowser`.
3. **Вывод сообщения об ошибке**:
   - Если редактор кампаний не инициализирован, выводит сообщение в консоль, предлагая сначала инициализировать редактор кампаний.

**ASCII схема работы функции**:

```
A [Проверка инициализации редактора кампаний]
    |
    -- B [Формирование URL и открытие Google Spreadsheet (если редактор инициализирован)]
    |
C [Вывод сообщения об ошибке (если редактор не инициализирован)]
```

**Примеры**:

```python
editor_widgets.open_spreadsheet(None)
```

### `setup_callbacks`
```python
    def setup_callbacks(self):\n        """Set up callbacks for the widgets."""
        self.campaign_name_dropdown.observe(self.on_campaign_name_change, names="value")
        self.category_name_dropdown.observe(self.on_category_change, names="value")
        self.language_dropdown.observe(self.on_language_change, names="value")
        self.initialize_button.on_click(self.initialize_campaign_editor)
        self.save_button.on_click(self.save_campaign)
        self.show_products_button.on_click(self.show_products)
        self.open_spreadsheet_button.on_click(self.open_spreadsheet)
```

**Назначение**: Устанавливает обратные вызовы для виджетов.

**Как работает функция**:

1. **Установка обработчиков для выпадающих списков**:
   - Устанавливает обработчик `self.on_campaign_name_change` для события изменения значения в выпадающем списке `self.campaign_name_dropdown`.
   - Устанавливает обработчик `self.on_category_change` для события изменения значения в выпадающем списке `self.category_name_dropdown`.
   - Устанавливает обработчик `self.on_language_change` для события изменения значения в выпадающем списке `self.language_dropdown`.
2. **Установка обработчиков для кнопок**:
   - Устанавливает обработчик `self.initialize_campaign_editor` для события клика по кнопке `self.initialize_button`.
   - Устанавливает обработчик `self.save_campaign` для события клика по кнопке `self.save_button`.
   - Устанавливает обработчик `self.show_products` для события клика по кнопке `self.show_products_button`.
   - Устанавливает обработчик `self.open_spreadsheet` для события клика по кнопке `self.open_spreadsheet_button`.

**ASCII схема работы функции**:

```
A [Установка обработчиков для выпадающих списков]
    |
B [Установка обработчиков для кнопок]
```

**Примеры**:

```python
editor_widgets.setup_callbacks()
```

### `display_widgets`
```python
    def display_widgets(self):\n        """Display the widgets for interaction in the Jupyter notebook.

        Initializes the campaign editor automatically with the first campaign selected.

        Example:
            >>> self.display_widgets()
        """
        display(
            self.campaign_name_dropdown,
            self.category_name_dropdown,
            self.language_dropdown,
            self.initialize_button,
            self.save_button,
            self.show_products_button,
            self.open_spreadsheet_button,
        )
        # Initialize the campaign editor with the first campaign selected
        self.initialize_campaign_editor(None)
```

**Назначение**: Отображает виджеты для взаимодействия в Jupyter Notebook.

**Как работает функция**:

1. **Отображение виджетов**:
   - Использует функцию `display` из модуля `IPython.display` для отображения виджетов в Jupyter Notebook. Отображаются следующие виджеты:
     - `self.campaign_name_dropdown`
     - `self.category_name_dropdown`
     - `self.language_dropdown`
     - `self.initialize_button`
     - `self.save_button`
     - `self.show_products_button`
     - `self.open_spreadsheet_button`
2. **Инициализация редактора кампаний**:
   - Вызывает метод `initialize_campaign_editor` для инициализации редактора кампаний с выбранными значениями по умолчанию.

**ASCII схема работы функции**:

```
A [Отображение виджетов]
    |
B [Инициализация редактора кампаний]
```

**Примеры**:

```python
editor_widgets.display_widgets()
```

## Функции

В данном модуле также используются функции из других модулей:

### `get_directory_names(path: Path) -> list[str]`

Эта функция находится в модуле `src.utils.printer`.

**Назначение**: Получает список имен поддиректорий из указанного пути.

**Параметры**:
- `path` (Path): Путь к директории для поиска поддиректорий.

**Возвращает**:
- `list[str]`: Список имен поддиректорий.

**Примеры**:

```python
from pathlib import Path
from src.utils.printer import get_directory_names

directories = get_directory_names(Path("/path/to/directory"))
print(directories)  # Вывод: ['dir1', 'dir2', ...]