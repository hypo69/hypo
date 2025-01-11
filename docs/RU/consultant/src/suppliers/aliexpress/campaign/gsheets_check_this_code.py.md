# Анализ кода модуля `gsheets_check_this_code.py`

**Качество кода**
7
- Плюсы
    - Код структурирован в класс `AliCampaignGoogleSheet`, что способствует организации и переиспользованию.
    - Используется `logger` для логирования, что облегчает отладку и мониторинг.
    - Присутствует базовая обработка исключений.
    - Применение `SimpleNamespace` для хранения данных.
    - Есть форматирование для Google Sheets.
- Минусы
    - Присутствуют лишние импорты.
    - Комментарии не соответствуют стандарту RST.
    - Некоторые блоки `try-except` можно упростить.
    - Отсутствует подробная документация для модуля, классов и методов.
    - Не везде используется `logger.error` с `exc_info=True` для подробного логирования ошибок.
    - В методе `set_products_worksheet` заголовки определены в комментарии, но используются.
    - Код использует `__dict__`, что может привести к проблемам, если у объектов будут методы. Лучше обращаться к атрибутам явно.
    - Дублирование кода в `set_category_products`, часть кода дублируется из `set_products_worksheet`, также не используется `self.update_cell_range()`.
    - Отсутствует использование `self.update_cell_range()`.
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - В `_format_category_products_worksheet` и `_format_categories_worksheet` код по форматированию слишком длинный.
    - В `set_categories_worksheet` используется проверка на наличие атрибутов, что является избыточным, так как структура объекта `SimpleNamespace` уже известна.

**Рекомендации по улучшению**

1.  **Документация:**
    -   Добавить docstring для модуля.
    -   Добавить docstring для класса `AliCampaignGoogleSheet` и всех его методов, используя формат RST.
2.  **Импорты:**
    -   Удалить лишние импорты, такие как дублирующиеся импорты `SimpleNamespace`, `Worksheet`, `SpreadSheet`, `Driver`, `Chrome`, `pprint`, `logger`, а так же `translate`.
    -   Импортировать `logger` из `src.logger.logger`.
3.  **Обработка ошибок:**
    -   Заменить стандартные блоки `try-except` на более компактное использование `logger.error` с параметром `exc_info=True` для логирования ошибок.
    -   Убрать `raise` после логирования ошибки, если не требуется дальнейшее распространение исключения.
4.  **Улучшения кода:**
    -   Упростить форматирование, выделив в отдельные функции установку ширины столбцов и высоты строк.
    -   Использовать `update_cell_range()` для массовой записи данных в Google Sheets.
    -   Рефакторинг методов `set_products_worksheet` и `set_category_products` с целью избежания дублирования кода, например, выделив общий метод для записи продуктов в Google Sheets.
    -   Использовать явное обращение к атрибутам объекта вместо `__dict__` при формировании строк данных.
5. **Форматирование кода:**
   -   Использовать одинарные кавычки (`'`) для строк в коде Python, двойные только для операций вывода.
6. **Использование `j_loads`:**
    - Убедиться, что никакие данные не загружаются из файлов JSON.
7.  **Комментарии:**
    -   Комментарии должны быть информативными, объяснять логику кода и соответствовать стандарту RST.

**Оптимизированный код**

```python
"""
Модуль для работы с Google Sheets для управления рекламными кампаниями AliExpress.
=================================================================================

Этот модуль содержит класс :class:`AliCampaignGoogleSheet`, который используется для управления
рекламными кампаниями AliExpress через Google Sheets. Он предоставляет методы для создания,
очистки и форматирования листов, а также для записи и чтения данных о кампаниях, категориях
и продуктах.

Пример использования
--------------------

Пример создания экземпляра класса `AliCampaignGoogleSheet`:

.. code-block:: python

    campaign_sheet = AliCampaignGoogleSheet(campaign_name='Test Campaign', language='ru', currency='RUB')
    campaign_sheet.set_campaign_worksheet(campaign_sheet.editor.campaign)
"""
import time
from types import SimpleNamespace
from typing import Optional, List, Dict
from pathlib import Path
from gspread.worksheet import Worksheet
from gspread_formatting import (
    cellFormat,
    textFormat,
    format_cell_range,
    set_column_width,
    set_row_height,
    Color
)

from src.goog.spreadsheet.spreadsheet import SpreadSheet
from src.webdriver.driver import Driver, Chrome
from src.suppliers.aliexpress.campaign.ali_campaign_editor import AliCampaignEditor
from src.utils.printer import pprint
from src.logger.logger import logger

class AliCampaignGoogleSheet(SpreadSheet):
    """
    Класс для работы с Google Sheets в рамках кампаний AliExpress.

    Наследует класс SpreadSheet и предоставляет дополнительные методы для управления листами Google Sheets,
    записи данных о категориях и продуктах, и форматирования листов.
    """
    spreadsheet_id = '1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0'
    spreadsheet: SpreadSheet
    worksheet: Worksheet
    driver: Driver = Driver(Chrome)

    def __init__(self, campaign_name: str, language: str | dict = None, currency: str = None):
        """
        Инициализирует AliCampaignGoogleSheet с указанным ID Google Sheets и дополнительными параметрами.

        :param campaign_name: Название кампании.
        :type campaign_name: str
        :param language: Язык для кампании.
        :type language: str | dict, optional
        :param currency: Валюта для кампании.
        :type currency: str, optional
        """
        super().__init__(spreadsheet_id=self.spreadsheet_id)
        self.editor = AliCampaignEditor(campaign_name=campaign_name, language=language, currency=currency)
        self.clear()
        self.set_campaign_worksheet(self.editor.campaign)
        self.set_categories_worksheet(self.editor.campaign.category)
        self.driver.get_url(f'https://docs.google.com/spreadsheets/d/{self.spreadsheet_id}')

    def clear(self):
        """
        Очищает содержимое.

        Удаляет листы продуктов и очищает данные на листах категорий и других указанных листах.
        """
        try:
            self.delete_products_worksheets()
        except Exception as ex:
            logger.error('Ошибка очистки', ex, exc_info=True)

    def delete_products_worksheets(self):
        """
        Удаляет все листы из Google Sheets, кроме 'categories', 'product', 'category' и 'campaign'.
        """
        excluded_titles = {'categories', 'product', 'category', 'campaign'}
        try:
            worksheets = self.spreadsheet.worksheets()
            for sheet in worksheets:
                if sheet.title not in excluded_titles:
                    self.spreadsheet.del_worksheet_by_id(sheet.id)
                    logger.info(f'Worksheet \'{sheet.title}\' deleted.')
        except Exception as ex:
            logger.error('Error deleting all worksheets.', ex, exc_info=True)

    def set_campaign_worksheet(self, campaign: SimpleNamespace):
        """
        Записывает данные кампании на лист Google Sheets.

        :param campaign: SimpleNamespace объект с данными кампании.
        :type campaign: SimpleNamespace
        """
        try:
            ws: Worksheet = self.get_worksheet('campaign')

            updates = []
            vertical_data = [
                ('A1', 'Campaign Name', campaign.name),
                ('A2', 'Campaign Title', campaign.title),
                ('A3', 'Campaign Language', campaign.language),
                ('A4', 'Campaign Currency', campaign.currency),
                ('A5', 'Campaign Description', campaign.description),
            ]

            for cell, header, value in vertical_data:
                updates.append({'range': cell, 'values': [[header]]})
                updates.append({'range': f'B{cell[1]}', 'values': [[str(value)]]})

            if updates:
                ws.batch_update(updates)

            logger.info('Campaign data written to \'campaign\' worksheet vertically.')

        except Exception as ex:
            logger.error('Error setting campaign worksheet.', ex, exc_info=True)

    def set_products_worksheet(self, category_name: str):
        """
        Записывает данные продуктов на лист Google Sheets.

        :param category_name: Название категории для получения продуктов.
        :type category_name: str
        """
        if not category_name:
            logger.warning('No products found for category.')
            return
        
        try:
            category: SimpleNamespace = getattr(self.editor.campaign.category, category_name)
            products: list[SimpleNamespace] = category.products
        except AttributeError as ex:
           logger.error(f'Не найдена категория {category_name=}', ex, exc_info=True)
           return

        ws = self.copy_worksheet('product', category_name)
        
        try:
            headers = [
                'product_id', 'app_sale_price', 'original_price', 'sale_price', 'discount',
                'product_main_image_url', 'local_image_path', 'product_small_image_urls',
                'product_video_url', 'local_video_path', 'first_level_category_id',
                'first_level_category_name', 'second_level_category_id', 'second_level_category_name',
                'target_sale_price', 'target_sale_price_currency', 'target_app_sale_price_currency',
                'target_original_price_currency', 'original_price_currency', 'product_title',
                'evaluate_rate', 'promotion_link', 'shop_url', 'shop_id', 'tags'
            ]
            self.update_cell_range(ws, 'A1:Y1', [headers])

            row_data = []
            for product in products:
                row_data.append([
                    str(getattr(product, 'product_id', '')),
                    getattr(product, 'product_title', ''),
                    getattr(product, 'promotion_link', ''),
                    str(getattr(product, 'app_sale_price', '')),
                    getattr(product, 'original_price', ''),
                    getattr(product, 'sale_price', ''),
                    getattr(product, 'discount', ''),
                    getattr(product, 'product_main_image_url', ''),
                    getattr(product, 'local_image_path', ''),
                    ', '.join(getattr(product, 'product_small_image_urls', [])),
                    getattr(product, 'product_video_url', ''),
                    getattr(product, 'local_video_path', ''),
                    getattr(product, 'first_level_category_id', ''),
                    getattr(product, 'first_level_category_name', ''),
                    getattr(product, 'second_level_category_id', ''),
                    getattr(product, 'second_level_category_name', ''),
                    getattr(product, 'target_sale_price', ''),
                    getattr(product, 'target_sale_price_currency', ''),
                    getattr(product, 'target_app_sale_price_currency', ''),
                    getattr(product, 'target_original_price_currency', ''),
                    getattr(product, 'original_price_currency', ''),
                    getattr(product, 'evaluate_rate', ''),
                    getattr(product, 'shop_url', ''),
                    getattr(product, 'shop_id', ''),
                    ', '.join(getattr(product, 'tags', [])),
                ])
                
            self.update_cell_range(ws, f'A2:Y{len(row_data) + 1}', row_data)
            self._format_category_products_worksheet(ws)
            logger.info('Products updated in worksheet.')

        except Exception as ex:
            logger.error('Error setting products worksheet.', ex, exc_info=True)

    def set_categories_worksheet(self, categories: SimpleNamespace):
        """
        Записывает данные категорий в Google Sheets.

        :param categories: SimpleNamespace объект, содержащий данные о категориях.
        :type categories: SimpleNamespace
        """
        ws: Worksheet = self.get_worksheet('categories')
        ws.clear()
        
        try:
            category_data = categories.__dict__
            headers = ['Name', 'Title', 'Description', 'Tags', 'Products Count']
            self.update_cell_range(ws, 'A1:E1', [headers])
            
            rows = []
            for category in category_data.values():
                rows.append([
                    getattr(category, 'name', ''),
                    getattr(category, 'title', ''),
                    getattr(category, 'description', ''),
                    ', '.join(getattr(category, 'tags', [])),
                    getattr(category, 'products_count', '')
                ])
            self.update_cell_range(ws, f'A2:E{1 + len(rows)}', rows)
            self._format_categories_worksheet(ws)

            logger.info('Category fields updated from SimpleNamespace object.')

        except Exception as ex:
            logger.error('Error updating fields from SimpleNamespace object.', ex, exc_info=True)

    def get_categories(self) -> list[dict]:
        """
        Получает данные из таблицы Google Sheets.

        :return: Данные из таблицы в виде списка словарей.
        :rtype: list[dict]
        """
        ws = self.get_worksheet('categories')
        data = ws.get_all_records()
        logger.info('Categories data retrieved from worksheet.')
        return data

    def set_category_products(self, category_name: str, products: list[dict]):
        """
        Записывает данные о продуктах в новую таблицу Google Sheets.

        :param category_name: Название категории.
        :type category_name: str
        :param products: Список словарей с данными о продуктах.
        :type products: list[dict]
        """
        if not category_name:
            logger.warning('No products found for category.')
            return
        
        try:
            ws = self.copy_worksheet('product', category_name)
            headers = [
                'product_id', 'app_sale_price', 'original_price', 'sale_price', 'discount',
                'product_main_image_url', 'local_image_path', 'product_small_image_urls',
                'product_video_url', 'local_video_path', 'first_level_category_id',
                'first_level_category_name', 'second_level_category_id', 'second_level_category_name',
                'target_sale_price', 'target_sale_price_currency', 'target_app_sale_price_currency',
                'target_original_price_currency', 'original_price_currency', 'product_title',
                'evaluate_rate', 'promotion_link', 'shop_url', 'shop_id', 'tags'
            ]
            self.update_cell_range(ws, 'A1:Y1', [headers])
            
            row_data = []
            for product in products:
                row_data.append([
                    str(product.get('product_id', '')),
                    str(product.get('app_sale_price', '')),
                    product.get('original_price', ''),
                    product.get('sale_price', ''),
                    product.get('discount', ''),
                    product.get('product_main_image_url', ''),
                    product.get('local_image_path', ''),
                    ', '.join(product.get('product_small_image_urls', [])),
                    product.get('product_video_url', ''),
                    product.get('local_video_path', ''),
                    product.get('first_level_category_id', ''),
                    product.get('first_level_category_name', ''),
                    product.get('second_level_category_id', ''),
                    product.get('second_level_category_name', ''),
                    product.get('target_sale_price', ''),
                    product.get('target_sale_price_currency', ''),
                    product.get('target_app_sale_price_currency', ''),
                    product.get('target_original_price_currency', ''),
                    product.get('original_price_currency', ''),
                    product.get('product_title', ''),
                    product.get('evaluate_rate', ''),
                    product.get('promotion_link', ''),
                    product.get('shop_url', ''),
                    product.get('shop_id', ''),
                    ', '.join(product.get('tags', [])),
                ])
            self.update_cell_range(ws, f'A2:Y{len(row_data) + 1}', row_data)
            self._format_category_products_worksheet(ws)
            logger.info('Products updated in worksheet.')

        except Exception as ex:
            logger.error('Error updating products in worksheet.', ex, exc_info=True)


    def _set_column_widths(self, ws: Worksheet, widths: dict):
        """
        Устанавливает ширину столбцов в Google Sheets.

        :param ws: Лист Google Sheets для форматирования.
        :type ws: Worksheet
        :param widths: Словарь с ширинами столбцов.
        :type widths: dict
        """
        for col_range, width in widths.items():
            set_column_width(ws, col_range, width)

    def _set_row_heights(self, ws: Worksheet, heights: dict):
        """
        Устанавливает высоту строк в Google Sheets.

        :param ws: Лист Google Sheets для форматирования.
        :type ws: Worksheet
        :param heights: Словарь с высотами строк.
        :type heights: dict
        """
        for row_range, height in heights.items():
            set_row_height(ws, row_range, height)


    def _format_categories_worksheet(self, ws: Worksheet):
        """
        Форматирует лист 'categories'.

        :param ws: Лист Google Sheets для форматирования.
        :type ws: Worksheet
        """
        try:
            self._set_column_widths(ws, {
                'A:A': 150,
                'B:B': 200,
                'C:C': 300,
                'D:D': 200,
                'E:E': 150
            })

            self._set_row_heights(ws, {'1:1': 40})

            header_format = cellFormat(
                textFormat=textFormat(bold=True, fontSize=12),
                horizontalAlignment='CENTER',
                verticalAlignment='MIDDLE',
                backgroundColor=Color(0.8, 0.8, 0.8)
            )
            format_cell_range(ws, 'A1:E1', header_format)
            logger.info('Categories worksheet formatted.')
        except Exception as ex:
            logger.error('Error formatting categories worksheet.', ex, exc_info=True)

    def _format_category_products_worksheet(self, ws: Worksheet):
        """
        Форматирует лист с продуктами категории.

        :param ws: Лист Google Sheets для форматирования.
        :type ws: Worksheet
        """
        try:
            self._set_column_widths(ws, {
                'A:A': 250,
                'B:B': 220,
                'C:C': 220,
                'D:D': 220,
                'E:E': 200,
                'F:F': 200,
                'G:G': 200,
                'H:H': 200,
                'I:I': 200,
                'J:J': 200,
                'K:K': 200,
                'L:L': 200,
                'M:M': 200,
                'N:N': 200,
                'O:O': 200,
                'P:P': 200,
                'Q:Q': 200,
                'R:R': 200,
                'S:S': 200,
                'T:T': 200,
                'U:U': 200,
                'V:V': 200,
                'W:W': 200,
                'X:X': 200,
                'Y:Y': 200,
            })
            self._set_row_heights(ws, {'1:1': 40})
            header_format = cellFormat(
                textFormat=textFormat(bold=True, fontSize=12),
                horizontalAlignment='CENTER',
                verticalAlignment='TOP',
                backgroundColor=Color(0.8, 0.8, 0.8)
            )
            format_cell_range(ws, 'A1:Y1', header_format)
            logger.info('Category products worksheet formatted.')
        except Exception as ex:
            logger.error('Error formatting category products worksheet.', ex, exc_info=True)

    def update_cell_range(self, ws: Worksheet, cell_range: str, data: list[list]):
        """
        Обновляет ячейки в Google Sheets.

        :param ws: Лист Google Sheets.
        :type ws: Worksheet
        :param cell_range: Диапазон ячеек.
        :type cell_range: str
        :param data: Данные для записи.
        :type data: list[list]
        """
        try:
            ws.update(cell_range, data)
        except Exception as ex:
             logger.error(f'Error updating cell range {cell_range} in worksheet.', ex, exc_info=True)
```