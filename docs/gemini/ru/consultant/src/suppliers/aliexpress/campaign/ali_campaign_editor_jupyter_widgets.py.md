## Анализ кода модуля `ali_campaign_editor_jupyter_widgets`

**Качество кода**
8
 -  Плюсы
    - Код хорошо структурирован и разбит на логические блоки.
    - Используются виджеты `ipywidgets` для создания интерактивного интерфейса.
    - Присутствует базовая обработка ошибок через `try-except` и логирование.
    - Имеется документация в виде docstring для классов, методов и функций.
    - Код достаточно читаемый благодаря использованию осмысленных имен переменных и функций.
 -  Минусы
    - Не все комментарии соответствуют формату reStructuredText (RST).
    - Используются стандартные блоки `try-except` вместо `logger.error`.
    - Есть неиспользуемый закомментированный код.
    -  Не все функции имеют подробные docstring с примерами использования.
    -  Отсутствует обработка ошибок при получении значения из виджетов (например, `self.language_dropdown.value`).
    - Некоторые методы используют явную передачу None в качестве аргумента для вызова, что может быть сделано неявно.

**Рекомендации по улучшению**

1.  **Документация:**
    -   Переписать все комментарии в формате RST, включая описания модулей, классов, методов и переменных.
    -   Добавить подробные docstring с примерами использования для каждой функции.
2.  **Импорты:**
    -   Удалить неиспользуемый `import header`
    -   Проверить и добавить отсутствующие импорты, если есть необходимость.
3.  **Обработка ошибок:**
    -   Заменить блоки `try-except` на обработку ошибок с помощью `logger.error`, где это возможно.
4.  **Рефакторинг:**
    -   Удалить закомментированный код `get_directory_names`.
    -   Использовать `self.campaign_name_dropdown.value` напрямую в методе `initialize_campaign_editor` вместо присвоения значения в `self.campaign_name`
    -   Упростить вызовы `self.initialize_campaign_editor(None)` используя частичное применение.
5.  **Улучшение кода:**
    -  Добавить проверку на `None` для значений, полученных из виджетов, и использовать `logger.warning` при отсутствии значений.

**Оптимизиробанный код**
```python
"""
Модуль для создания и управления виджетами редактора кампаний AliExpress.
========================================================================

Этот модуль содержит класс :class:`JupyterCampaignEditorWidgets`, который предоставляет
интерактивные виджеты для управления кампаниями AliExpress в Jupyter Notebook.
Он позволяет пользователю выбирать кампании, категории и языки, а также выполнять
различные действия, такие как инициализация редактора, сохранение кампаний и просмотр продуктов.

Пример использования
--------------------

Пример создания и отображения виджетов:

.. code-block:: python

    editor_widgets = JupyterCampaignEditorWidgets()
    editor_widgets.display_widgets()
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

MODE = 'dev'

from types import SimpleNamespace
from pathlib import Path
from ipywidgets import widgets
from IPython.display import display
import webbrowser
from functools import partial

from src import gs
from src.suppliers.aliexpress.campaign import AliCampaignEditor
from src.suppliers.aliexpress.utils import locales
from src.utils.printer import pprint, get_directory_names
from src.logger.logger import logger

class JupyterCampaignEditorWidgets:
    """
    Виджеты для редактора кампаний AliExpress.

    Этот класс предоставляет виджеты для взаимодействия и управления кампаниями AliExpress,
    включая выбор кампаний, категорий и языков, а также выполнение таких действий,
    как инициализация редакторов, сохранение кампаний и отображение продуктов.

    :ivar language: Выбранный язык.
    :vartype language: str
    :ivar currency: Выбранная валюта.
    :vartype currency: str
    :ivar campaign_name: Выбранное имя кампании.
    :vartype campaign_name: str
    :ivar category_name: Выбранное имя категории.
    :vartype category_name: str
    :ivar category: Выбранная категория.
    :vartype category: SimpleNamespace
    :ivar campaign_editor: Экземпляр редактора кампаний AliExpress.
    :vartype campaign_editor: AliCampaignEditor
    :ivar products: Список продуктов.
    :vartype products: list[SimpleNamespace]


    :Example:

    >>> editor_widgets: JupyterCampaignEditorWidgets = JupyterCampaignEditorWidgets()
    >>> editor_widgets.display_widgets()
    """
    # Class attributes declaration
    language: str = None
    currency: str = None
    campaign_name: str = None
    category_name: str = None
    category:SimpleNamespace = None
    campaign_editor: AliCampaignEditor = None
    products:list[SimpleNamespace] = None
    def __init__(self):
        """
        Инициализация виджетов и настройка редактора кампаний.

        Устанавливает виджеты для выбора кампаний, категорий и языков.
        Также устанавливает значения по умолчанию и обратные вызовы для виджетов.
        """
        self.campaigns_directory:str = Path(
            gs.path.google_drive, "aliexpress", "campaigns"
        )
        
        if not self.campaigns_directory.exists():
            raise FileNotFoundError(
                f"Directory does not exist: {self.campaigns_directory}"
            )

        # self.languages = {"EN": "USD", "HE": "ILS", "RU": "ILS"}
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
        self.initialize_campaign_editor()
    
    def initialize_campaign_editor(self, _ = None):
        """
        Инициализация редактора кампаний.

        Настраивает редактор кампаний на основе выбранной кампании и категории.

        :param _:  Неиспользуемый аргумент, необходим для обратного вызова кнопки.
        """
        # Получает значения из виджетов.
        campaign_name = self.campaign_name_dropdown.value
        category_name = self.category_name_dropdown.value
        language_currency = self.language_dropdown.value

        if not campaign_name:
            logger.warning("Please select a campaign name before initializing the editor.")
            return

        if not language_currency:
             logger.warning("Please select a language/currency before initializing the editor.")
             return
        
        self.language, self.currency = language_currency.split()
        self.update_category_dropdown(campaign_name)
        self.campaign_editor = AliCampaignEditor(campaign_name = campaign_name, language = self.language, currency = self.currency)
        
        if category_name:
            self.category = self.campaign_editor.get_category(category_name)
            self.products = self.campaign_editor.get_category_products(category_name)
        
    def update_category_dropdown(self, campaign_name: str):
        """
        Обновление выпадающего списка категорий на основе выбранной кампании.

        :param campaign_name: Название кампании.
        :type campaign_name: str

        :Example:
        >>> self.update_category_dropdown("SummerSale")
        """
        campaign_path = self.campaigns_directory / campaign_name / "category"
        campaign_categories = get_directory_names(campaign_path)
        self.category_name_dropdown.options = campaign_categories

    def on_campaign_name_change(self, change: dict[str, str]):
        """
        Обработка изменений в выпадающем списке имен кампаний.

        :param change: Словарь изменений, содержащий новое значение.
        :type change: dict[str, str]

        :Example:
            >>> self.on_campaign_name_change({'new': 'SummerSale'})
        """
        # Обновляет выпадающий список категорий и инициализирует редактор
        self.update_category_dropdown(change["new"])
        self.initialize_campaign_editor()

    def on_category_change(self, change: dict[str, str]):
        """
        Обработка изменений в выпадающем списке категорий.

        :param change: Словарь изменений, содержащий новое значение.
        :type change: dict[str, str]

        :Example:
            >>> self.on_category_change({'new': 'Electronics'})
        """
        # Инициализирует редактор с новой категорией
        self.initialize_campaign_editor()
        
    def on_language_change(self, change: dict[str, str]):
        """
        Обработка изменений в выпадающем списке языков.

        :param change: Словарь изменений, содержащий новое значение.
        :type change: dict[str, str]

        :Example:
            >>> self.on_language_change({'new': 'EN USD'})
        """
        # Инициализирует редактор с новым языком
        self.initialize_campaign_editor()

    def save_campaign(self, _ = None):
        """
        Сохранение кампании и ее категорий.

        Сохраняет кампанию и ее категории в Google Sheets.

        :param _: Неиспользуемый аргумент, необходим для обратного вызова кнопки.

         :Example:
            >>> self.save_campaign()
        """
        campaign_name = self.campaign_name_dropdown.value
        category_name = self.category_name_dropdown.value
        language_currency = self.language_dropdown.value
        
        if not campaign_name:
            logger.warning("Please select a campaign name before saving the campaign.")
            return
        if not language_currency:
            logger.warning("Please select a language/currency before saving the campaign.")
            return

        language, currency = language_currency.split()
        try:
            self.campaign_editor = AliCampaignEditor(
                campaign_name=campaign_name,
                category_name=category_name if category_name else None,
                language=language,
            )
            self.campaign_editor.save_categories_from_worksheet()
        except Exception as ex:
            logger.error("Error saving campaign.", ex, True)

    def show_products(self, _ = None):
        """
        Отображение продуктов в выбранной категории.

        Устанавливает продукты в Google Sheets.

        :param _: Неиспользуемый аргумент, необходим для обратного вызова кнопки.

        :Example:
            >>> self.show_products()
        """
        campaign_name = self.campaign_name_dropdown.value
        category_name = self.category_name_dropdown.value
        language_currency = self.language_dropdown.value

        if not campaign_name:
           logger.warning("Please select a campaign name before showing the products.")
           return
        if not language_currency:
           logger.warning("Please select a language/currency before showing the products.")
           return
        
        language, currency = language_currency.split()
        try:
            self.campaign_editor = AliCampaignEditor(
                campaign_name=campaign_name,
                language=language,
                currency=currency,
            )
            self.campaign_editor.set_products_worksheet(category_name)
        except Exception as ex:
             logger.error("Error displaying products.", ex, True)


    def open_spreadsheet(self, _ = None):
        """
        Открытие Google Spreadsheet в браузере.

        Открывает Google Spreadsheet в браузере, если редактор кампаний инициализирован.

        :param _: Неиспользуемый аргумент, необходим для обратного вызова кнопки.

        :Example:
            >>> self.open_spreadsheet()
        """
        if self.campaign_editor:
            spreadsheet_url = f"https://docs.google.com/spreadsheets/d/{self.campaign_editor.spreadsheet_id}/edit"
            webbrowser.open(spreadsheet_url)
        else:
            print("Please initialize the campaign editor first.")

    def setup_callbacks(self):
        """
        Настройка обратных вызовов для виджетов.

        Устанавливает обратные вызовы для отслеживания изменений в виджетах.
        """
        self.campaign_name_dropdown.observe(self.on_campaign_name_change, names="value")
        self.category_name_dropdown.observe(self.on_category_change, names="value")
        self.language_dropdown.observe(self.on_language_change, names="value")
        self.initialize_button.on_click(self.initialize_campaign_editor)
        self.save_button.on_click(self.save_campaign)
        self.show_products_button.on_click(self.show_products)
        self.open_spreadsheet_button.on_click(self.open_spreadsheet)

    def display_widgets(self):
        """
        Отображение виджетов для взаимодействия в Jupyter Notebook.

        Отображает виджеты для выбора кампаний, категорий и языков, а также кнопки
        для выполнения различных действий.

        :Example:
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
        self.initialize_campaign_editor()