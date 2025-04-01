# Модуль: ali_campaign_editor_jupyter_widgets

## Обзор

Модуль `ali_campaign_editor_jupyter_widgets.py` предоставляет Jupyter widgets для редактора кампаний AliExpress. 
Он содержит класс `JupyterCampaignEditorWidgets`, который позволяет пользователям взаимодействовать с кампаниями AliExpress, 
выбирать кампании, категории и языки, а также выполнять различные действия, такие как инициализация редактора, сохранение кампаний и отображение продуктов.

## Подробней

Этот модуль предназначен для использования в Jupyter notebooks для упрощения управления кампаниями AliExpress. 
Он предоставляет графический интерфейс для выбора параметров кампании и выполнения действий, связанных с редактированием и сохранением данных. 
Модуль использует библиотеку `ipywidgets` для создания интерактивных элементов управления.

## Классы

### `JupyterCampaignEditorWidgets`

**Описание**:
Класс `JupyterCampaignEditorWidgets` предоставляет набор виджетов для взаимодействия с редактором кампаний AliExpress. 
Он включает в себя выпадающие списки для выбора кампаний, категорий и языков, а также кнопки для инициализации редактора, сохранения кампании, отображения продуктов и открытия Google Spreadsheet.

**Как работает класс**:
1.  **Инициализация**: В конструкторе класса инициализируются все необходимые виджеты и устанавливаются значения по умолчанию. 
    Также настраиваются обратные вызовы для обработки изменений в виджетах.
2.  **Взаимодействие с пользователем**: Пользователь может выбирать кампанию, категорию и язык из соответствующих выпадающих списков.
3.  **Инициализация редактора кампаний**: При нажатии на кнопку "Initialize Campaign Editor" происходит инициализация редактора кампаний `AliCampaignEditor` с выбранными параметрами.
4.  **Сохранение кампании**: При нажатии на кнопку "Save Campaign" происходит сохранение кампании и ее категорий с использованием редактора кампаний.
5.  **Отображение продуктов**: При нажатии на кнопку "Show Products" происходит отображение продуктов в выбранной категории.
6.  **Открытие Google Spreadsheet**: При нажатии на кнопку "Open Google Spreadsheet" происходит открытие Google Spreadsheet, связанного с кампанией, в браузере.

**Методы**:

*   `__init__`: Инициализирует виджеты и настраивает редактор кампаний.
*   `initialize_campaign_editor`: Инициализирует редактор кампаний на основе выбранных кампании и категории.
*   `update_category_dropdown`: Обновляет выпадающий список категорий на основе выбранной кампании.
*   `on_campaign_name_change`: Обрабатывает изменения в выпадающем списке кампаний.
*   `on_category_change`: Обрабатывает изменения в выпадающем списке категорий.
*   `on_language_change`: Обрабатывает изменения в выпадающем списке языков.
*   `save_campaign`: Сохраняет кампанию и ее категории.
*   `show_products`: Отображает продукты в выбранной категории.
*   `open_spreadsheet`: Открывает Google Spreadsheet в браузере.
*   `setup_callbacks`: Устанавливает обратные вызовы для виджетов.
*   `display_widgets`: Отображает виджеты в Jupyter notebook.

**Параметры**:

*   `language` (str): Язык кампании.
*   `currency` (str): Валюта кампании.
*   `campaign_name` (str): Название кампании.
*   `category_name` (str): Название категории.
*   `category` (SimpleNamespace): Объект, представляющий категорию.
*   `campaign_editor` (AliCampaignEditor): Редактор кампаний AliExpress.
*   `products` (list[SimpleNamespace]): Список продуктов.
*   `campaigns_directory` (str): Путь к директории с кампаниями.
*   `campaign_name_dropdown` (widgets.Dropdown): Выпадающий список для выбора кампании.
*   `category_name_dropdown` (widgets.Dropdown): Выпадающий список для выбора категории.
*   `language_dropdown` (widgets.Dropdown): Выпадающий список для выбора языка.
*   `initialize_button` (widgets.Button): Кнопка для инициализации редактора кампаний.
*   `save_button` (widgets.Button): Кнопка для сохранения кампании.
*   `show_products_button` (widgets.Button): Кнопка для отображения продуктов.
*   `open_spreadsheet_button` (widgets.Button): Кнопка для открытия Google Spreadsheet.

**Примеры**:

```python
# Создание экземпляра виджетов редактора кампаний
editor_widgets: JupyterCampaignEditorWidgets = JupyterCampaignEditorWidgets()

# Отображение виджетов в Jupyter notebook
editor_widgets.display_widgets()
```

## Функции

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

**Назначение**:
Инициализация виджетов и настройка редактора кампаний.

**Как работает функция**:

1.  **Определение пути к директории кампаний**: Определяется путь к директории, где хранятся кампании AliExpress, используя `gs.path.google_drive`.
2.  **Проверка существования директории**: Проверяется, существует ли директория кампаний. Если директория не существует, вызывается исключение `FileNotFoundError`.
3.  **Создание выпадающего списка для выбора кампании**: Создается выпадающий список (`widgets.Dropdown`) для выбора названия кампании. Опции списка заполняются названиями директорий, находящихся в директории кампаний.
4.  **Создание выпадающего списка для выбора категории**: Создается выпадающий список для выбора категории.
5.  **Создание выпадающего списка для выбора языка и валюты**: Создается выпадающий список для выбора языка и валюты. Опции списка формируются на основе данных из модуля `locales`.
6.  **Создание кнопок для выполнения действий**: Создаются кнопки для инициализации редактора кампаний, сохранения кампании, отображения продуктов и открытия Google Spreadsheet.
7.  **Настройка обратных вызовов для обработки событий**: Настраиваются обратные вызовы (`self.setup_callbacks()`) для обработки событий, таких как изменение выбранного значения в выпадающих списках и нажатие на кнопки.
8.  **Инициализация редактора кампаний со значениями по умолчанию**: Вызывается метод `self.initialize_campaign_editor(None)` для инициализации редактора кампаний со значениями по умолчанию.

**Параметры**:
-   Отсутствуют

**Возвращает**:
-   Отсутствует

**Вызывает исключения**:
-   `FileNotFoundError`: Если директория кампаний не существует.

**Примеры**:

```python
# Пример создания экземпляра класса JupyterCampaignEditorWidgets
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

**Назначение**:
Инициализация редактора кампаний.

**Как работает функция**:

1.  **Получение значений из выпадающих списков**: Получаются выбранные значения из выпадающих списков кампании, категории и языка.
2.  **Разделение языка и валюты**: Значение выпадающего списка языка разделяется на язык и валюту.
3.  **Проверка наличия названия кампании**: Проверяется, выбрано ли название кампании. Если название кампании не выбрано, выводится предупреждение в лог.
4.  **Обновление выпадающего списка категорий**: Если название кампании выбрано, вызывается метод `self.update_category_dropdown(self.campaign_name)` для обновления выпадающего списка категорий на основе выбранной кампании.
5.  **Создание экземпляра редактора кампаний**: Создается экземпляр класса `AliCampaignEditor` с выбранными параметрами кампании, языка и валюты.
6.  **Получение категории и продуктов**: Если название категории выбрано, вызываются методы `self.campaign_editor.get_category(self.category_name)` и `self.campaign_editor.get_category_products(self.category_name)` для получения информации о категории и продуктах.

**Параметры**:
-   `_`: Неиспользуемый аргумент, необходимый для обратного вызова кнопки.

**Возвращает**:
-   Отсутствует

**Примеры**:

```python
# Пример инициализации редактора кампаний
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

**Назначение**:
Обновление выпадающего списка категорий на основе выбранной кампании.

**Как работает функция**:

1.  **Формирование пути к директории категорий**: Формируется путь к директории категорий для выбранной кампании.
2.  **Получение списка категорий**: Вызывается функция `get_directory_names(campaign_path)` для получения списка названий директорий категорий.
3.  **Обновление опций выпадающего списка категорий**: Опции выпадающего списка категорий обновляются полученным списком названий категорий.

**Параметры**:
-   `campaign_name` (str): Название кампании.

**Возвращает**:
-   Отсутствует

**Примеры**:

```python
# Пример обновления выпадающего списка категорий для кампании "SummerSale"
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

**Назначение**:
Обработчик изменений в выпадающем списке кампаний.

**Как работает функция**:

1.  **Получение нового значения**: Получается новое значение из словаря `change`, содержащего информацию об изменении.
2.  **Обновление названия кампании**: Обновляется атрибут `self.campaign_name` новым значением.
3.  **Обновление выпадающего списка категорий**: Вызывается метод `self.update_category_dropdown(self.campaign_name)` для обновления выпадающего списка категорий на основе выбранной кампании.
4.  **Повторная инициализация редактора кампаний**: Вызывается метод `self.initialize_campaign_editor(None)` для повторной инициализации редактора кампаний с новой кампанией.

**Параметры**:
-   `change` (dict[str, str]): Словарь, содержащий информацию об изменении.

**Возвращает**:
-   Отсутствует

**Примеры**:

```python
# Пример вызова обработчика изменений с новым значением "SummerSale"
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

**Назначение**:
Обработчик изменений в выпадающем списке категорий.

**Как работает функция**:

1.  **Получение нового значения**: Получается новое значение из словаря `change`, содержащего информацию об изменении.
2.  **Обновление названия категории**: Обновляется атрибут `self.category_name` новым значением.
3.  **Повторная инициализация редактора кампаний**: Вызывается метод `self.initialize_campaign_editor(None)` для повторной инициализации редактора кампаний с новой категорией.

**Параметры**:
-   `change` (dict[str, str]): Словарь, содержащий информацию об изменении.

**Возвращает**:
-   Отсутствует

**Примеры**:

```python
# Пример вызова обработчика изменений с новым значением "Electronics"
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

**Назначение**:
Обработчик изменений в выпадающем списке языков.

**Как работает функция**:

1.  **Получение нового значения**: Получается новое значение из словаря `change`, содержащего информацию об изменении.
2.  **Разделение языка и валюты**: Новое значение разделяется на язык и валюту с использованием метода `split()`.
3.  **Обновление атрибутов языка и валюты**: Обновляются атрибуты `self.language` и `self.currency` полученными значениями.
4.  **Повторная инициализация редактора кампаний**: Вызывается метод `self.initialize_campaign_editor(None)` для повторной инициализации редактора кампаний с новым языком и валютой.

**Параметры**:
-   `change` (dict[str, str]): Словарь, содержащий информацию об изменении.

**Возвращает**:
-   Отсутствует

**Примеры**:

```python
# Пример вызова обработчика изменений с новым значением "EN USD"
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

**Назначение**:
Сохранение кампании и ее категорий.

**Как работает функция**:

1.  **Получение значений из выпадающих списков**: Получаются значения названия кампании, названия категории, языка и валюты из соответствующих выпадающих списков.
2.  **Проверка наличия названия кампании и языка**: Проверяется, выбраны ли название кампании и язык. Если название кампании или язык не выбраны, выводится предупреждение в лог.
3.  **Создание экземпляра редактора кампаний**: Создается экземпляр класса `AliCampaignEditor` с выбранными параметрами кампании, категории и языка.
4.  **Сохранение категорий из worksheet**: Вызывается метод `self.campaign_editor.save_categories_from_worksheet()` для сохранения категорий из worksheet.
5.  **Обработка исключений**: Если при сохранении категорий возникает исключение, оно логируется с использованием `logger.error`.

**Параметры**:
-   `_`: Неиспользуемый аргумент, необходимый для обратного вызова кнопки.

**Возвращает**:
-   Отсутствует

**Примеры**:

```python
# Пример сохранения кампании
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

**Назначение**:
Отображение продуктов в выбранной категории.

**Как работает функция**:

1.  **Получение значений названия кампании и названия категории**: Получаются значения названия кампании и названия категории из соответствующих выпадающих списков.
2.  **Создание экземпляра редактора кампаний**: Создается экземпляр класса `AliCampaignEditor` с выбранными параметрами кампании, языка и валюты.
3.  **Установка worksheet продуктов**: Вызывается метод `self.campaign_editor.set_products_worksheet(category_name)` для установки worksheet продуктов для выбранной категории.
4.  **Обработка исключений**: Если при отображении продуктов возникает исключение, оно логируется с использованием `logger.error`.

**Параметры**:
-   `_`: Неиспользуемый аргумент, необходимый для обратного вызова кнопки.

**Возвращает**:
-   Отсутствует

**Примеры**:

```python
# Пример отображения продуктов
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

**Назначение**:
Открытие Google Spreadsheet в браузере.

**Как работает функция**:

1.  **Проверка инициализации редактора кампаний**: Проверяется, инициализирован ли редактор кампаний.
2.  **Формирование URL Google Spreadsheet**: Если редактор кампаний инициализирован, формируется URL Google Spreadsheet на основе `self.campaign_editor.spreadsheet_id`.
3.  **Открытие URL в браузере**: URL открывается в браузере с помощью `webbrowser.open(spreadsheet_url)`.
4.  **Вывод сообщения об ошибке**: Если редактор кампаний не инициализирован, выводится сообщение об ошибке.

**Параметры**:
-   `_`: Неиспользуемый аргумент, необходимый для обратного вызова кнопки.

**Возвращает**:
-   Отсутствует

**Примеры**:

```python
# Пример открытия Google Spreadsheet
editor_widgets.open_spreadsheet(None)
```

### `setup_callbacks`

```python
    def setup_callbacks(self):
        """Set up callbacks for the widgets."""
        self.campaign_name_dropdown.observe(self.on_campaign_name_change, names="value")
        self.category_name_dropdown.observe(self.on_category_change, names="value")
        self.language_dropdown.observe(self.on_language_change, names="value")
        self.initialize_button.on_click(self.initialize_campaign_editor)
        self.save_button.on_click(self.save_campaign)
        self.show_products_button.on_click(self.show_products)
        self.open_spreadsheet_button.on_click(self.open_spreadsheet)
```

**Назначение**:
Установка обратных вызовов для виджетов.

**Как работает функция**:

1.  **Установка обработчика изменений для выпадающего списка кампаний**: Устанавливается обработчик `self.on_campaign_name_change` для события изменения значения в выпадающем списке кампаний.
2.  **Установка обработчика изменений для выпадающего списка категорий**: Устанавливается обработчик `self.on_category_change` для события изменения значения в выпадающем списке категорий.
3.  **Установка обработчика изменений для выпадающего списка языков**: Устанавливается обработчик `self.on_language_change` для события изменения значения в выпадающем списке языков.
4.  **Установка обработчика клика для кнопки инициализации**: Устанавливается обработчик `self.initialize_campaign_editor` для события клика по кнопке инициализации.
5.  **Установка обработчика клика для кнопки сохранения**: Устанавливается обработчик `self.save_campaign` для события клика по кнопке сохранения.
6.  **Установка обработчика клика для кнопки отображения продуктов**: Устанавливается обработчик `self.show_products` для события клика по кнопке отображения продуктов.
7.  **Установка обработчика клика для кнопки открытия Google Spreadsheet**: Устанавливается обработчик `self.open_spreadsheet` для события клика по кнопке открытия Google Spreadsheet.

**Параметры**:
-   Отсутствуют

**Возвращает**:
-   Отсутствует

**Примеры**:

```python
# Пример установки обратных вызовов
editor_widgets.setup_callbacks()
```

### `display_widgets`

```python
    def display_widgets(self):
        """Display the widgets for interaction in the Jupyter notebook.

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

**Назначение**:
Отображение виджетов для взаимодействия в Jupyter notebook.

**Как работает функция**:

1.  **Отображение виджетов**: Вызывается функция `display` для отображения выпадающих списков кампаний, категорий, языков, а также кнопок инициализации, сохранения, отображения продуктов и открытия Google Spreadsheet.
2.  **Инициализация редактора кампаний**: Вызывается метод `self.initialize_campaign_editor(None)` для инициализации редактора кампаний с первой выбранной кампанией.

**Параметры**:
-   Отсутствуют

**Возвращает**:
-   Отсутствует

**Примеры**:

```python
# Пример отображения виджетов
editor_widgets.display_widgets()