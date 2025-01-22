### Анализ кода модуля `ali_campaign_editor_jupyter_widgets`

**Качество кода**:
- **Соответствие стандартам**: 7
- **Плюсы**:
  - Код хорошо структурирован и разбит на методы, что облегчает его понимание и поддержку.
  - Используются виджеты `ipywidgets` для создания интерактивного интерфейса.
  - Присутствует базовая обработка ошибок через `try-except` блоки и логирование.
  - Используется `logger` для вывода предупреждений и ошибок.
- **Минусы**:
  - Не все функции имеют подробную документацию в формате RST.
  - Используется  `print`  вместо  `logger.warning`  в  `open_spreadsheet`.
  - Есть избыточное использование `try-except` блоков.
  - Не все переменные имеют аннотации типов.
  - Отсутствует использование `j_loads` или `j_loads_ns`.
  - Не все комментарии соответствуют рекомендациям по стилю.

**Рекомендации по улучшению**:
- Добавить RST-документацию для всех методов и классов, включая параметры, возвращаемые значения и примеры использования.
- Заменить использование `print` на `logger.warning` для сообщений пользователю.
- Упростить обработку ошибок, используя `logger.error` с параметром `exc_info=True` для логирования стектрейса, и избегать лишних `try-except` блоков.
- Добавить аннотации типов для переменных, где это возможно, для улучшения читаемости и поддержки кода.
- Удалить закомментированный код  `get_directory_names`.
- Переименовать `campaigns_directory`  на  `campaigns_dir`.
- Добавить  `from src.logger.logger import logger` для явного импорта `logger`.
- Выравнивание импортов.

**Оптимизированный код**:
```python
# -*- coding: utf-8 -*-
"""
Модуль для создания виджетов Jupyter для редактора кампаний AliExpress
====================================================================

Модуль содержит класс :class:`JupyterCampaignEditorWidgets`, который предоставляет
виджеты для управления кампаниями AliExpress в Jupyter Notebook.

Пример использования:
---------------------
.. code-block:: python

    editor_widgets: JupyterCampaignEditorWidgets = JupyterCampaignEditorWidgets()
    editor_widgets.display_widgets()
"""
from types import SimpleNamespace
import webbrowser
from pathlib import Path

from IPython.display import display
from ipywidgets import widgets

from src import gs
from src.logger.logger import logger  # явный импорт logger
from src.suppliers.aliexpress.campaign import AliCampaignEditor
from src.suppliers.aliexpress.utils import locales
from src.utils.printer import get_directory_names


class JupyterCampaignEditorWidgets:
    """
    Виджеты для редактора кампаний AliExpress.

    Этот класс предоставляет виджеты для взаимодействия и управления кампаниями AliExpress,
    включая выбор кампаний, категорий и языков, а также выполнение действий, таких как
    инициализация редакторов, сохранение кампаний и отображение продуктов.

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

    def __init__(self) -> None:
        """
        Инициализация виджетов и настройка редактора кампаний.

        Устанавливает виджеты для выбора кампаний, категорий и языков. Также устанавливает
        значения по умолчанию и обратные вызовы для виджетов.
        """
        self.campaigns_dir: Path = Path(  # переименовано для краткости
            gs.path.google_drive, "aliexpress", "campaigns"
        )

        if not self.campaigns_dir.exists():
            raise FileNotFoundError(
                f"Directory does not exist: {self.campaigns_dir}"
            )

        self.campaign_name_dropdown = widgets.Dropdown(
            options=get_directory_names(self.campaigns_dir),
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
        self.setup_callbacks()
        self.initialize_campaign_editor(None)

    def initialize_campaign_editor(self, _) -> None:
        """
        Инициализация редактора кампаний.

        :param _: Неиспользуемый аргумент, необходим для обратного вызова кнопки.
        :type _: Any

        Устанавливает редактор кампаний на основе выбранной кампании и категории.
        """
        self.campaign_name = self.campaign_name_dropdown.value or None
        self.category_name = self.category_name_dropdown.value or None

        if self.language_dropdown.value:  # check if language_dropdown has a value
            self.language, self.currency = self.language_dropdown.value.split()
        else:
             self.language, self.currency = None, None # Set default values if no language is selected
        
        if self.campaign_name:
            self.update_category_dropdown(self.campaign_name)
            self.campaign_editor = AliCampaignEditor(
                campaign_name=self.campaign_name,
                language=self.language,
                currency=self.currency,
            )

            if self.category_name:
                self.category = self.campaign_editor.get_category(self.category_name)
                self.products = self.campaign_editor.get_category_products(self.category_name)
        else:
            logger.warning(
                "Please select a campaign name before initializing the editor."
            )

    def update_category_dropdown(self, campaign_name: str) -> None:
        """
        Обновление выпадающего списка категорий на основе выбранной кампании.

        :param campaign_name: Название кампании.
        :type campaign_name: str

        :Example:
            >>> self.update_category_dropdown("SummerSale")
        """
        campaign_path = self.campaigns_dir / campaign_name / "category"
        campaign_categories = get_directory_names(campaign_path)
        self.category_name_dropdown.options = campaign_categories

    def on_campaign_name_change(self, change: dict[str, str]) -> None:
        """
        Обработчик изменений в выпадающем списке кампаний.

        :param change: Словарь изменений, содержащий новое значение.
        :type change: dict[str, str]

        :Example:
            >>> self.on_campaign_name_change({'new': 'SummerSale'})
        """
        self.campaign_name = change["new"]
        self.update_category_dropdown(self.campaign_name)
        self.initialize_campaign_editor(None)

    def on_category_change(self, change: dict[str, str]) -> None:
        """
        Обработчик изменений в выпадающем списке категорий.

        :param change: Словарь изменений, содержащий новое значение.
        :type change: dict[str, str]

        :Example:
            >>> self.on_category_change({'new': 'Electronics'})
        """
        self.category_name = change["new"]
        self.initialize_campaign_editor(None)

    def on_language_change(self, change: dict[str, str]) -> None:
        """
        Обработчик изменений в выпадающем списке языков.

        :param change: Словарь изменений, содержащий новое значение.
        :type change: dict[str, str]

        :Example:
            >>> self.on_language_change({'new': 'EN USD'})
        """
        self.language, self.currency = change["new"].split()
        self.initialize_campaign_editor(None)

    def save_campaign(self, _) -> None:
        """
        Сохранение кампании и ее категорий.

        :param _: Неиспользуемый аргумент, необходим для обратного вызова кнопки.
        :type _: Any

        :Example:
            >>> self.save_campaign(None)
        """
        self.campaign_name = self.campaign_name_dropdown.value
        self.category_name = self.category_name_dropdown.value
        if self.language_dropdown.value:
            self.language, self.currency = self.language_dropdown.value.split()
        else:
             self.language, self.currency = None, None  # Set default values if no language is selected


        if self.campaign_name and self.language:
            self.campaign_editor = AliCampaignEditor(
                campaign_name=self.campaign_name,
                category_name=self.category_name if self.category_name else None,
                language=self.language,
                currency=self.currency
            )
            try:
                self.campaign_editor.save_categories_from_worksheet()
            except Exception as ex:
                 logger.error("Error saving campaign.", exc_info=True) # Используем exc_info для логирования стектрейса
        else:
            logger.warning(
                "Please select campaign name and language/currency before saving the campaign."
            )

    def show_products(self, _) -> None:
        """
        Отображение продуктов в выбранной категории.

        :param _: Неиспользуемый аргумент, необходим для обратного вызова кнопки.
        :type _: Any

        :Example:
            >>> self.show_products(None)
        """
        campaign_name = self.campaign_name_dropdown.value
        category_name = self.category_name_dropdown.value
        if self.language_dropdown.value:
             self.language, self.currency = self.language_dropdown.value.split()
        else:
             self.language, self.currency = None, None

        try:
            self.campaign_editor = AliCampaignEditor(
                campaign_name=campaign_name,
                language=self.language,
                currency=self.currency,
            )
            self.campaign_editor.set_products_worksheet(category_name)
        except Exception as ex:
             logger.error("Error displaying products.", exc_info=True) # Используем exc_info для логирования стектрейса

    def open_spreadsheet(self, _) -> None:
        """
        Открытие Google Spreadsheet в браузере.

        :param _: Неиспользуемый аргумент, необходим для обратного вызова кнопки.
        :type _: Any

        :Example:
            >>> self.open_spreadsheet(None)
        """
        if self.campaign_editor:
            spreadsheet_url = f"https://docs.google.com/spreadsheets/d/{self.campaign_editor.spreadsheet_id}/edit"
            webbrowser.open(spreadsheet_url)
        else:
            logger.warning("Please initialize the campaign editor first.")  # заменили print на logger.warning

    def setup_callbacks(self) -> None:
        """Настройка обратных вызовов для виджетов."""
        self.campaign_name_dropdown.observe(self.on_campaign_name_change, names="value")
        self.category_name_dropdown.observe(self.on_category_change, names="value")
        self.language_dropdown.observe(self.on_language_change, names="value")
        self.initialize_button.on_click(self.initialize_campaign_editor)
        self.save_button.on_click(self.save_campaign)
        self.show_products_button.on_click(self.show_products)
        self.open_spreadsheet_button.on_click(self.open_spreadsheet)

    def display_widgets(self) -> None:
        """
        Отображение виджетов для взаимодействия в Jupyter Notebook.

        Инициализирует редактор кампаний автоматически с первой выбранной кампанией.

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
        self.initialize_campaign_editor(None)