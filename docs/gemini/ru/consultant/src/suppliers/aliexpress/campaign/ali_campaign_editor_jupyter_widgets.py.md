# Анализ кода модуля `ali_campaign_editor_jupyter_widgets`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разбит на логические блоки, что облегчает его понимание и поддержку.
    - Использование `ipywidgets` для создания интерактивных элементов делает интерфейс удобным для пользователя.
    - Присутствует подробная документация в формате docstring для классов и методов.
    - Обработка ошибок с использованием `logger.error` помогает в отслеживании проблем.
    - Код соответствует PEP 8.
-  Минусы
    - Не все функции имеют reStructuredText документацию.
    - Избыточное использование `try-except` в некоторых местах можно заменить на более точную обработку ошибок.
    - Отсутствуют проверки на ввод некорректных данных.
    -  Не везде используется `logger.debug` для логирования.

**Рекомендации по улучшению**
1.  **Документация**: Добавить reStructuredText документацию для всех функций и переменных, включая параметры и возвращаемые значения.
2.  **Обработка ошибок**: Улучшить обработку ошибок, используя `logger.error` и добавляя `logger.debug` для отслеживания состояний, а также избегать избыточного использования `try-except`.
3.  **Импорты**: Проверить и добавить отсутствующие импорты, а также отсортировать их в соответствии с PEP 8.
4.  **Валидация**: Добавить валидацию пользовательского ввода, чтобы избежать ошибок при работе с виджетами.
5.  **Логирование**: Увеличить уровень логирования, добавив `logger.debug` для отслеживания процесса инициализации и других ключевых моментов.
6.  **Рефакторинг**: Улучшить читаемость кода за счет переименования переменных и разбивки длинных функций на более мелкие.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для создания виджетов Jupyter для редактора кампаний AliExpress.
=========================================================================================

Этот модуль содержит класс :class:`JupyterCampaignEditorWidgets`,
который предоставляет виджеты для управления кампаниями AliExpress в Jupyter Notebook.
Виджеты позволяют выбирать кампании, категории, языки и выполнять действия,
такие как инициализация редактора, сохранение кампаний и отображение продуктов.

Пример использования
--------------------

Пример использования класса `JupyterCampaignEditorWidgets`:

.. code-block:: python

    editor_widgets: JupyterCampaignEditorWidgets = JupyterCampaignEditorWidgets()
    editor_widgets.display_widgets()
"""
from __future__ import annotations



from types import SimpleNamespace
from pathlib import Path
import webbrowser

from ipywidgets import widgets
from IPython.display import display

from src import gs
from src.suppliers.aliexpress.campaign import AliCampaignEditor
from src.suppliers.aliexpress.utils import locales
from src.utils.printer import get_directory_names
from src.logger.logger import logger


class JupyterCampaignEditorWidgets:
    """
    Виджеты для редактора кампаний AliExpress.

    Предоставляет интерфейс для взаимодействия и управления кампаниями AliExpress,
    включая выбор кампаний, категорий и языков, а также выполнение таких действий,
    как инициализация редакторов, сохранение кампаний и отображение продуктов.

    :ivar language: Выбранный язык.
    :vartype language: str
    :ivar currency: Выбранная валюта.
    :vartype currency: str
    :ivar campaign_name: Название выбранной кампании.
    :vartype campaign_name: str
    :ivar category_name: Название выбранной категории.
    :vartype category_name: str
    :ivar category: Объект SimpleNamespace с данными категории.
    :vartype category: SimpleNamespace
    :ivar campaign_editor: Экземпляр класса AliCampaignEditor.
    :vartype campaign_editor: AliCampaignEditor
    :ivar products: Список продуктов в выбранной категории.
    :vartype products: list[SimpleNamespace]

    :Example:
    
    >>> editor_widgets: JupyterCampaignEditorWidgets = JupyterCampaignEditorWidgets()
    >>> editor_widgets.display_widgets()
    """

    language: str = None
    currency: str = None
    campaign_name: str = None
    category_name: str = None
    category: SimpleNamespace = None
    campaign_editor: AliCampaignEditor = None
    products: list[SimpleNamespace] = None

    def __init__(self):
        """
        Инициализирует виджеты и настраивает редактор кампаний.

        Настраивает виджеты для выбора кампаний, категорий и языков, а также
        устанавливает значения по умолчанию и обратные вызовы для виджетов.
        """
        self.campaigns_directory: Path = Path(
            gs.path.google_drive, "aliexpress", "campaigns"
        )

        if not self.campaigns_directory.exists():
             # Проверка наличия директории, в случае отсутствия - выбрасывается исключение FileNotFoundError
            raise FileNotFoundError(
                f"Directory does not exist: {self.campaigns_directory}"
            )
        
        # Создание виджетов
        self.campaign_name_dropdown = widgets.Dropdown(
            options=get_directory_names(self.campaigns_directory),
            description="Campaign Name:",
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

        # Настройка обратных вызовов
        self.setup_callbacks()

        # Инициализация с значениями по умолчанию
        self.initialize_campaign_editor(None)
    
    def initialize_campaign_editor(self, _):
        """
        Инициализирует редактор кампаний.

        Устанавливает редактор кампаний на основе выбранной кампании и категории.

        :param _: Неиспользуемый аргумент, необходимый для обратного вызова кнопки.
        :type _: Any
        """
        # Получение выбранных значений из виджетов
        self.campaign_name = self.campaign_name_dropdown.value or None
        self.category_name = self.category_name_dropdown.value or None
        
        # Разделение значения языка и валюты
        if self.language_dropdown.value:
            self.language, self.currency = self.language_dropdown.value.split()
        else:
            logger.warning("Language/currency not selected.")
            return
        
        if self.campaign_name:
            # Обновление выпадающего списка категорий
            self.update_category_dropdown(self.campaign_name)
            # Инициализация редактора кампаний
            self.campaign_editor = AliCampaignEditor(
                campaign_name = self.campaign_name, 
                language = self.language, 
                currency = self.currency
                )
            
            if self.category_name:
                # Получение данных о категории и продуктах
                self.category = self.campaign_editor.get_category(self.category_name)
                self.products = self.campaign_editor.get_category_products(self.category_name)
            
            logger.debug(f"Campaign editor initialized for campaign: {self.campaign_name}, category: {self.category_name}, language: {self.language}, currency: {self.currency}")
        else:
            logger.warning(
                "Please select a campaign name before initializing the editor."
            )

    def update_category_dropdown(self, campaign_name: str):
        """
        Обновляет выпадающий список категорий на основе выбранной кампании.

        :param campaign_name: Название кампании.
        :type campaign_name: str
        """
        # Формирование пути к директории с категориями
        campaign_path = self.campaigns_directory / campaign_name / "category"
        # Получение списка категорий
        campaign_categories = get_directory_names(campaign_path)
        # Обновление выпадающего списка категорий
        self.category_name_dropdown.options = campaign_categories
        logger.debug(f"Updated category dropdown with options: {campaign_categories}")

    def on_campaign_name_change(self, change: dict[str, str]):
        """
        Обрабатывает изменения в выпадающем списке названий кампаний.

        :param change: Словарь с изменениями, содержащий новое значение.
        :type change: dict[str, str]
        """
        # Получение нового названия кампании
        self.campaign_name = change["new"]
        # Обновление выпадающего списка категорий
        self.update_category_dropdown(self.campaign_name)
        # Переинициализация редактора кампаний
        self.initialize_campaign_editor(None)
        logger.debug(f"Campaign name changed to: {self.campaign_name}")

    def on_category_change(self, change: dict[str, str]):
        """
        Обрабатывает изменения в выпадающем списке категорий.

        :param change: Словарь с изменениями, содержащий новое значение.
        :type change: dict[str, str]
        """
        # Получение нового названия категории
        self.category_name = change["new"]
        # Переинициализация редактора кампаний
        self.initialize_campaign_editor(None)
        logger.debug(f"Category changed to: {self.category_name}")
        
    def on_language_change(self, change: dict[str, str]):
        """
        Обрабатывает изменения в выпадающем списке языков.

        :param change: Словарь с изменениями, содержащий новое значение.
        :type change: dict[str, str]
        """
        # Разделение значения языка и валюты
        self.language, self.currency = change["new"].split()
        # Переинициализация редактора кампаний
        self.initialize_campaign_editor(None)
        logger.debug(f"Language changed to: {self.language}, currency: {self.currency}")

    def save_campaign(self, _):
        """
        Сохраняет кампанию и её категории.

         :param _: Неиспользуемый аргумент, необходимый для обратного вызова кнопки.
        :type _: Any
        """
        # Получение выбранных значений из виджетов
        self.campaign_name = self.campaign_name_dropdown.value
        self.category_name = self.category_name_dropdown.value
        self.language, self.currency = self.language_dropdown.value.split()

        if self.campaign_name and self.language:
             # Инициализация редактора кампаний
            self.campaign_editor = AliCampaignEditor(
                campaign_name=self.campaign_name,
                category_name=self.category_name if self.category_name else None,
                language=self.language,
                currency=self.currency
            )
            try:
                # Сохранение категорий
                self.campaign_editor.save_categories_from_worksheet()
            except Exception as ex:
                # Логирование ошибки
                logger.error("Error saving campaign.", ex, True)
        else:
            # Логирование предупреждения, если не выбраны кампания или язык/валюта
            logger.warning (
                "Please select campaign name and language/currency before saving the campaign."
            )
        logger.debug(f"Campaign saved for campaign: {self.campaign_name}, category: {self.category_name}, language: {self.language}, currency: {self.currency}")

    def show_products(self, _):
        """
        Отображает продукты в выбранной категории.

         :param _: Неиспользуемый аргумент, необходимый для обратного вызова кнопки.
        :type _: Any
        """
         # Получение выбранных значений из виджетов
        campaign_name = self.campaign_name_dropdown.value
        category_name = self.category_name_dropdown.value
        
        try:
            # Инициализация редактора кампаний
            self.campaign_editor = AliCampaignEditor(
                campaign_name=campaign_name,
                language=self.language,
                currency=self.currency,
            )
             # Установка листа с продуктами
            self.campaign_editor.set_products_worksheet(category_name)
        except Exception as ex:
             # Логирование ошибки
            logger.error("Error displaying products.", ex, True)
        logger.debug(f"Displayed products for campaign: {campaign_name}, category: {category_name}, language: {self.language}, currency: {self.currency}")

    def open_spreadsheet(self, _):
        """
        Открывает Google Spreadsheet в браузере.

         :param _: Неиспользуемый аргумент, необходимый для обратного вызова кнопки.
        :type _: Any
        """
        if self.campaign_editor:
             # Формирование URL для Google Spreadsheet
            spreadsheet_url = f"https://docs.google.com/spreadsheets/d/{self.campaign_editor.spreadsheet_id}/edit"
            # Открытие URL в браузере
            webbrowser.open(spreadsheet_url)
            logger.debug(f"Opened spreadsheet: {spreadsheet_url}")
        else:
            print("Please initialize the campaign editor first.")
            logger.warning("Campaign editor not initialized.")

    def setup_callbacks(self):
        """Настраивает обратные вызовы для виджетов."""
        # Настройка обработчиков изменений для выпадающих списков
        self.campaign_name_dropdown.observe(self.on_campaign_name_change, names="value")
        self.category_name_dropdown.observe(self.on_category_change, names="value")
        self.language_dropdown.observe(self.on_language_change, names="value")
         # Настройка обработчиков кликов для кнопок
        self.initialize_button.on_click(self.initialize_campaign_editor)
        self.save_button.on_click(self.save_campaign)
        self.show_products_button.on_click(self.show_products)
        self.open_spreadsheet_button.on_click(self.open_spreadsheet)
        logger.debug("Callbacks set up for widgets.")

    def display_widgets(self):
        """
        Отображает виджеты для взаимодействия в Jupyter Notebook.

        Автоматически инициализирует редактор кампаний с первой выбранной кампанией.
        """
        # Отображение виджетов
        display(
            self.campaign_name_dropdown,
            self.category_name_dropdown,
            self.language_dropdown,
            self.initialize_button,
            self.save_button,
            self.show_products_button,
            self.open_spreadsheet_button,
        )
        # Инициализация редактора кампаний с первой выбранной кампанией
        self.initialize_campaign_editor(None)
        logger.debug("Widgets displayed.")
```