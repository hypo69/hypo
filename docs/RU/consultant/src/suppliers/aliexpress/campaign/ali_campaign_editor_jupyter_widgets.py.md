# Анализ кода модуля ali_campaign_editor_jupyter_widgets

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на классы и методы, что облегчает его понимание и поддержку.
    - Используются виджеты ipywidgets для создания интерактивного интерфейса в Jupyter Notebook.
    - Присутствует документация для классов и методов в формате docstring.
    - Используется `logger` для логирования ошибок и предупреждений.
- Минусы
    - Есть закомментированный код, который следует удалить.
    - Не все строки кода соответствуют PEP8.
    - Обработка ошибок не всегда оптимальна (например, `try-except` блоки могут быть заменены на `logger.error`).
    - Не хватает документации для атрибутов класса.
    - В некоторых местах есть избыточность кода, например, повторное присвоение значений.

**Рекомендации по улучшению**

1.  **Удалить закомментированный код**: Убрать неиспользуемый код, такой как `get_directory_names`.
2.  **Улучшить обработку ошибок**: Использовать `logger.error` вместо общих `try-except` блоков, где это возможно.
3.  **Добавить документацию**: Добавить документацию для атрибутов класса.
4.  **Избегать избыточности**:  Убрать лишние присваивания значений переменным.
5.  **Привести в соответствие с PEP8**: Проверить и исправить код в соответствии с рекомендациями PEP8.
6.  **Унифицировать использование кавычек**: Использовать одинарные кавычки для строк в коде, двойные - только для вывода.
7.  **Добавить описание модуля**: Добавить полное описание модуля в начале файла.
8.  **Проверить импорты**: Убедиться, что все необходимые импорты присутствуют.
9.  **Переименовать переменные**: Привести имена переменных в соответствие со стандартом (snake_case)
10. **Использовать f-строки**: Использовать f-строки для форматирования строк, где это необходимо.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для создания и управления виджетами редактора кампаний AliExpress в Jupyter Notebook.
=========================================================================================

Этот модуль предоставляет класс `JupyterCampaignEditorWidgets`, который включает в себя виджеты
для управления кампаниями AliExpress, выбора кампаний, категорий и языков, а также выполнения
таких действий, как инициализация редакторов, сохранение кампаний и отображение товаров.

Класс использует виджеты ipywidgets для создания интерактивного интерфейса в Jupyter Notebook.
Он также включает в себя логирование ошибок и предупреждений с помощью модуля `src.logger.logger`.

Пример использования
--------------------

Пример использования класса `JupyterCampaignEditorWidgets`:

.. code-block:: python

    editor_widgets = JupyterCampaignEditorWidgets()
    editor_widgets.display_widgets()
"""
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

    Этот класс предоставляет виджеты для взаимодействия и управления кампаниями AliExpress,
    включая выбор кампаний, категорий и языков, а также выполнение таких действий,
    как инициализация редакторов, сохранение кампаний и отображение товаров.

    :ivar str language: Выбранный язык кампании.
    :ivar str currency: Выбранная валюта кампании.
    :ivar str campaign_name: Выбранное имя кампании.
    :ivar str category_name: Выбранное имя категории.
    :ivar SimpleNamespace category: Выбранная категория.
    :ivar AliCampaignEditor campaign_editor: Редактор кампаний AliExpress.
    :ivar list[SimpleNamespace] products: Список продуктов в выбранной категории.
    :ivar Path campaigns_directory: Путь к директории с кампаниями.

    Пример:
        >>> editor_widgets = JupyterCampaignEditorWidgets()
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

        Настраивает виджеты для выбора кампаний, категорий и языков. Также настраивает
        значения по умолчанию и обратные вызовы для виджетов.
        """
        # определение пути к каталогу с кампаниями
        self.campaigns_directory:Path = Path(
            gs.path.google_drive, 'aliexpress', 'campaigns'
        )
        
        if not self.campaigns_directory.exists():
             # проверка существования директории
            raise FileNotFoundError(
                f'Directory does not exist: {self.campaigns_directory}'
            )
        # Создание выпадающего списка для выбора имени кампании
        self.campaign_name_dropdown = widgets.Dropdown(
            options=get_directory_names(self.campaigns_directory),
            description='Campaign Name:',
        )
        # Создание выпадающего списка для выбора категории
        self.category_name_dropdown = widgets.Dropdown(
            options=[], description='Category:'
        )
        # Создание выпадающего списка для выбора языка и валюты
        self.language_dropdown = widgets.Dropdown(
             options=[f'{key} {value}' for locale in locales for key, value in locale.items()],
            description='Language/Currency:',
        )
        # Создание кнопки для инициализации редактора кампаний
        self.initialize_button = widgets.Button(
            description='Initialize Campaign Editor',
            disabled=False,
        )
        # Создание кнопки для сохранения кампании
        self.save_button = widgets.Button(
            description='Save Campaign',
            disabled=False,
        )
        # Создание кнопки для отображения товаров
        self.show_products_button = widgets.Button(
            description='Show Products',
            disabled=False,
        )
        # Создание кнопки для открытия гугл таблицы
        self.open_spreadsheet_button = widgets.Button(
            description='Open Google Spreadsheet',
            disabled=False,
        )
        # Настройка обратных вызовов
        self.setup_callbacks()
        # Инициализация редактора кампаний со значениями по умолчанию
        self.initialize_campaign_editor(None)

    def initialize_campaign_editor(self, _):
        """
        Инициализирует редактор кампаний.

        Args:
            _ (Any): Неиспользуемый аргумент, необходимый для обратного вызова кнопки.

        Настраивает редактор кампаний на основе выбранной кампании и категории.
        """
        # получение значений из выпадающих списков
        self.campaign_name = self.campaign_name_dropdown.value or None
        self.category_name = self.category_name_dropdown.value or None
        # разделение значения языка и валюты
        self.language, self.currency = self.language_dropdown.value.split()
        
        if self.campaign_name:
            # обновление списка категорий
            self.update_category_dropdown(self.campaign_name)
            # создание экземпляра редактора кампаний
            self.campaign_editor = AliCampaignEditor(
                campaign_name=self.campaign_name,
                language=self.language,
                currency=self.currency
            )
            if self.category_name:
                # получение категории и списка товаров
                self.category = self.campaign_editor.get_category(self.category_name)
                self.products = self.campaign_editor.get_category_products(self.category_name)
        else:
             # логирование предупреждения, если имя кампании не выбрано
            logger.warning(
                'Please select a campaign name before initializing the editor.'
            )

    def update_category_dropdown(self, campaign_name: str):
        """
        Обновляет выпадающий список категорий на основе выбранной кампании.

        Args:
            campaign_name (str): Имя кампании.
        """
        # определение пути к директории категорий
        campaign_path = self.campaigns_directory / campaign_name / 'category'
         # получение имен категорий
        campaign_categories = get_directory_names(campaign_path)
        # обновление списка опций выпадающего списка
        self.category_name_dropdown.options = campaign_categories

    def on_campaign_name_change(self, change: dict[str, str]):
        """
        Обрабатывает изменения в выпадающем списке имени кампании.

        Args:
            change (dict[str, str]): Словарь изменений, содержащий новое значение.
        """
        # обновление имени кампании
        self.campaign_name = change['new']
        # обновление списка категорий
        self.update_category_dropdown(self.campaign_name)
         # повторная инициализация редактора
        self.initialize_campaign_editor(None)

    def on_category_change(self, change: dict[str, str]):
        """
        Обрабатывает изменения в выпадающем списке категорий.

        Args:
            change (dict[str, str]): Словарь изменений, содержащий новое значение.
        """
        # обновление имени категории
        self.category_name = change['new']
        # повторная инициализация редактора
        self.initialize_campaign_editor(None)

    def on_language_change(self, change: dict[str, str]):
        """
        Обрабатывает изменения в выпадающем списке языка.

        Args:
            change (dict[str, str]): Словарь изменений, содержащий новое значение.
        """
         # разделение значения языка и валюты
        self.language, self.currency = change['new'].split()
        # повторная инициализация редактора
        self.initialize_campaign_editor(None)

    def save_campaign(self, _):
        """
        Сохраняет кампанию и ее категории.

        Args:
            _ (Any): Неиспользуемый аргумент, необходимый для обратного вызова кнопки.
        """
        # получение значений из выпадающих списков
        self.campaign_name = self.campaign_name_dropdown.value
        self.category_name = self.category_name_dropdown.value
        # разделение значения языка и валюты
        self.language, self.currency = self.language_dropdown.value.split()
        if self.campaign_name and self.language:
            # создание экземпляра редактора кампаний
            self.campaign_editor = AliCampaignEditor(
                campaign_name=self.campaign_name,
                category_name=self.category_name if self.category_name else None,
                language=self.language,
            )
            try:
                 # сохранение категорий из гугл таблицы
                self.campaign_editor.save_categories_from_worksheet()
            except Exception as ex:
                # логирование ошибки
                logger.error('Error saving campaign.', ex, exc_info=True)
        else:
             # логирование предупреждения, если имя кампании или язык не выбраны
            logger.warning(
                'Please select campaign name and language/currency before saving the campaign.'
            )

    def show_products(self, _):
        """
        Отображает товары в выбранной категории.

        Args:
            _ (Any): Неиспользуемый аргумент, необходимый для обратного вызова кнопки.
        """
        # получение значений из выпадающих списков
        campaign_name = self.campaign_name_dropdown.value
        category_name = self.category_name_dropdown.value
        try:
            # создание экземпляра редактора кампаний
            self.campaign_editor = AliCampaignEditor(
                campaign_name=campaign_name,
                language=self.language,
                currency=self.currency,
            )
            # установка товаров в гугл таблицу
            self.campaign_editor.set_products_worksheet(category_name)
        except Exception as ex:
            # логирование ошибки
            logger.error('Error displaying products.', ex, exc_info=True)

    def open_spreadsheet(self, _):
        """
        Открывает Google Spreadsheet в браузере.

        Args:
            _ (Any): Неиспользуемый аргумент, необходимый для обратного вызова кнопки.
        """
        if self.campaign_editor:
            # открытие гугл таблицы в браузере
            spreadsheet_url = f'https://docs.google.com/spreadsheets/d/{self.campaign_editor.spreadsheet_id}/edit'
            webbrowser.open(spreadsheet_url)
        else:
             # вывод сообщения, если редактор не инициализирован
            print('Please initialize the campaign editor first.')

    def setup_callbacks(self):
        """Настраивает обратные вызовы для виджетов."""
        # установка обратных вызовов для виджетов
        self.campaign_name_dropdown.observe(self.on_campaign_name_change, names='value')
        self.category_name_dropdown.observe(self.on_category_change, names='value')
        self.language_dropdown.observe(self.on_language_change, names='value')
        self.initialize_button.on_click(self.initialize_campaign_editor)
        self.save_button.on_click(self.save_campaign)
        self.show_products_button.on_click(self.show_products)
        self.open_spreadsheet_button.on_click(self.open_spreadsheet)

    def display_widgets(self):
        """
        Отображает виджеты для взаимодействия в Jupyter Notebook.

        Инициализирует редактор кампаний автоматически при выборе первой кампании.
        """
        # отображение виджетов в jupyter notebook
        display(
            self.campaign_name_dropdown,
            self.category_name_dropdown,
            self.language_dropdown,
            self.initialize_button,
            self.save_button,
            self.show_products_button,
            self.open_spreadsheet_button,
        )
        # инициализация редактора кампаний с первой выбранной кампанией
        self.initialize_campaign_editor(None)