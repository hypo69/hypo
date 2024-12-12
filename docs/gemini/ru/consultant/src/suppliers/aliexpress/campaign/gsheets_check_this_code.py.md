# Анализ кода модуля `gsheets_check_this_code.py`

**Качество кода**
7
-  Плюсы
    - Код структурирован в класс `AliCampaignGoogleSheet`, что обеспечивает хорошую организацию.
    - Используется logging для отслеживания ошибок и хода выполнения.
    - Присутствуют docstring для большинства методов и класса.
    - Применение `SimpleNamespace` для представления данных.
 -  Минусы
    -  Импорты не полностью соответствуют ранее обработанным файлам.
    -  Не все комментарии приведены к формату RST.
    -  Есть дублирование кода, например, запись заголовков в таблицу продуктов.
    -  Много избыточных блоков `try-except` с `raise` в конце.
    -  Не везде используется `logger.error` c `exc_info=True`
    -  Используются магические строки в `set_column_width`.

**Рекомендации по улучшению**

1. **Импорты:**
   - Добавить недостающие импорты, такие как `Any` из `typing`.
   - Проверить и унифицировать импорты с другими файлами.

2. **Формат документации:**
   - Привести все комментарии и docstring к формату reStructuredText (RST).
   - Добавить подробные описания к каждой функции, методу, классу и переменной.

3. **Обработка ошибок:**
   - Заменить избыточные `try-except` блоки на обработку ошибок с помощью `logger.error(..., exc_info=True)`.
   - Избегать `raise` после логирования ошибки, если это не требуется для прерывания выполнения.

4. **Рефакторинг:**
   - Вынести повторяющийся код, например, формирование заголовков, в отдельные методы.
   - Использовать константы для магических строк (например, ширина столбцов).
   - Устранить дублирование кода записи продуктов в Google Sheets.

5. **Форматирование:**
   - Привести код к единому стилю, например, PEP 8.
   - Добавить больше пояснений в комментариях для лучшего понимания кода.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с Google Sheets в рамках кампаний AliExpress.
=========================================================================================

Этот модуль содержит класс :class:`AliCampaignGoogleSheet`, который используется для управления
листами Google Sheets, записи данных о категориях и продуктах, а также форматирования листов.

Пример использования
--------------------

Пример создания и использования экземпляра класса `AliCampaignGoogleSheet`:

.. code-block:: python

    campaign_sheet = AliCampaignGoogleSheet(campaign_name='Test Campaign', language='en', currency='USD')
    # ... другие операции с Google Sheets ...
"""
MODE = 'dev'

import time
from types import SimpleNamespace
from typing import Optional, List, Dict, Any
from gspread.worksheet import Worksheet
from gspread_formatting import (
    cellFormat,
    textFormat,
    numberFormat,
    format_cell_range,
    set_column_width,
    set_row_height,
    Color
)
from src.goog.spreadsheet.spreadsheet import SpreadSheet
from src.webdriver.driver import Driver, Chrome
from src.suppliers.aliexpress.campaign.ali_campaign_editor import AliCampaignEditor
from src.utils.jjson import j_dumps
from src.utils.printer import pprint
from src.logger.logger import logger
from src.ai.openai import translate


class AliCampaignGoogleSheet(SpreadSheet):
    """
    Класс для работы с Google Sheets в рамках кампаний AliExpress.

    Наследует класс :class:`SpreadSheet` и предоставляет дополнительные методы для управления листами
    Google Sheets, записи данных о категориях и продуктах, и форматирования листов.
    """

    spreadsheet_id = '1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0'
    spreadsheet: SpreadSheet
    worksheet: Worksheet
    driver: Driver = Driver(Chrome)
    COLUMN_WIDTHS = {
        'A': 250, 'B': 220, 'C': 220, 'D': 220, 'E': 200, 'F': 200, 'G': 200, 'H': 200,
        'I': 200, 'J': 200, 'K': 200, 'L': 200, 'M': 200, 'N': 200, 'O': 200, 'P': 200,
        'Q': 200, 'R': 200, 'S': 200, 'T': 200, 'U': 200, 'V': 200, 'W': 200, 'X': 200, 'Y': 200
    }

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
        # Инициализация SpreadSheet с ID таблицы
        super().__init__(spreadsheet_id=self.spreadsheet_id)
        # Инициализация редактора кампаний
        self.editor = AliCampaignEditor(campaign_name=campaign_name, language=language, currency=currency)
        # Вызов метода для очистки данных
        self.clear()
        # Вызов метода для установки данных кампании в Google Sheets
        self.set_campaign_worksheet(self.editor.campaign)
        # Вызов метода для установки данных категорий
        self.set_categories_worksheet(self.editor.campaign.category)
        # Открытие Google Sheets в браузере
        self.driver.get_url(f'https://docs.google.com/spreadsheets/d/{self.spreadsheet_id}')

    def clear(self):
        """
        Очищает содержимое рабочих листов.

        Удаляет листы продуктов и очищает данные на листах категорий и других указанных листах.
        """
        try:
            # Вызов метода для удаления рабочих листов
            self.delete_products_worksheets()
        except Exception as ex:
            # Логирование ошибки
            logger.error("Ошибка очистки", ex, exc_info=True)

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
                    logger.success(f"Worksheet '{sheet.title}' deleted.")
        except Exception as ex:
            logger.error("Error deleting all worksheets.", ex, exc_info=True)
            raise

    def set_campaign_worksheet(self, campaign: SimpleNamespace):
        """
        Записывает данные кампании в лист Google Sheets.

        :param campaign: Объект SimpleNamespace с данными кампании.
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
            logger.info("Campaign data written to 'campaign' worksheet vertically.")

        except Exception as ex:
            logger.error("Error setting campaign worksheet.", ex, exc_info=True)
            raise

    def set_products_worksheet(self, category_name: str):
        """
        Записывает данные о продуктах из SimpleNamespace в Google Sheets.

        :param category_name: Имя категории для получения продуктов.
        :type category_name: str
        """
        if category_name:
            category: SimpleNamespace = getattr(self.editor.campaign.category, category_name)
            products: list[SimpleNamespace] = category.products
        else:
            logger.warning("No products found for category.")
            return

        ws = self.copy_worksheet('product', category_name)
        try:
            headers = [
                'product_id', 'app_sale_price', 'original_price', 'sale_price', 'discount',
                'product_main_image_url', 'local_saved_image', 'product_small_image_urls',
                'product_video_url', 'local_saved_video', 'first_level_category_id',
                'first_level_category_name', 'second_level_category_id', 'second_level_category_name',
                'target_sale_price', 'target_sale_price_currency', 'target_app_sale_price_currency',
                'target_original_price_currency', 'original_price_currency', 'product_title',
                'evaluate_rate', 'promotion_link', 'shop_url', 'shop_id', 'tags'
            ]
            self._write_headers(ws, headers)
            row_data = []

            for product in products:
                _ = product.__dict__
                row_data.append([
                    str(_.get('product_id')),
                    _.get('product_title'),
                    _.get('promotion_link'),
                    str(_.get('app_sale_price')),
                    _.get('original_price'),
                    _.get('sale_price'),
                    _.get('discount'),
                    _.get('product_main_image_url'),
                    _.get('local_saved_image'),
                    ', '.join(_.get('product_small_image_urls', [])),
                    _.get('product_video_url'),
                    _.get('local_saved_video'),
                    _.get('first_level_category_id'),
                    _.get('first_level_category_name'),
                    _.get('second_level_category_id'),
                    _.get('second_level_category_name'),
                    _.get('target_sale_price'),
                    _.get('target_sale_price_currency'),
                    _.get('target_app_sale_price_currency'),
                    _.get('target_original_price_currency'),
                    _.get('original_price_currency'),
                    _.get('evaluate_rate'),
                    _.get('shop_url'),
                    _.get('shop_id'),
                    ', '.join(_.get('tags', []))
                ])

            for index, row in enumerate(row_data, start=2):
                ws.update(f'A{index}:Y{index}', [row])
                logger.info(f"Products {str(_.get('product_id'))} updated.")

            self._format_category_products_worksheet(ws)
            logger.info("Products updated in worksheet.")

        except Exception as ex:
            logger.error("Error setting products worksheet.", ex, exc_info=True)
            raise

    def set_categories_worksheet(self, categories: SimpleNamespace):
        """
        Записывает данные из объекта SimpleNamespace с категориями в Google Sheets.

        :param categories: Объект, где ключи - категории с данными для записи.
        :type categories: SimpleNamespace
        """
        ws: Worksheet = self.get_worksheet('categories')
        ws.clear()

        try:
            category_data = categories.__dict__
            required_attrs = ['name', 'title', 'description', 'tags', 'products_count']

            if all(all(hasattr(category, attr) for attr in required_attrs) for category in category_data.values()):
                headers = ['Name', 'Title', 'Description', 'Tags', 'Products Count']
                ws.update('A1:E1', [headers])

                rows = []
                for category in category_data.values():
                    row_data = [
                        category.name,
                        category.title,
                        category.description,
                        ', '.join(category.tags),
                        category.products_count,
                    ]
                    rows.append(row_data)
                ws.update(f'A2:E{1 + len(rows)}', rows)
                self._format_categories_worksheet(ws)
                logger.info("Category fields updated from SimpleNamespace object.")
            else:
                logger.warning("One or more category objects do not contain all required attributes.")
        except Exception as ex:
            logger.error("Error updating fields from SimpleNamespace object.", ex, exc_info=True)
            raise

    def get_categories(self) -> List[Dict]:
        """
        Получает данные из таблицы Google Sheets.

        :return: Данные из таблицы в виде списка словарей.
        :rtype: List[Dict]
        """
        ws = self.get_worksheet('categories')
        data = ws.get_all_records()
        logger.info("Categories data retrieved from worksheet.")
        return data

    def set_category_products(self, category_name: str, products: list[dict]):
        """
        Записывает данные о продуктах в новую таблицу Google Sheets.

        :param category_name: Название категории.
        :type category_name: str
        :param products: Список словарей с данными о продуктах.
        :type products: list[dict]
        """
        if category_name:
            category_ns: SimpleNamespace = getattr(self.editor.campaign.category, category_name)
        else:
            logger.warning("No products found for category.")
            return

        ws = self.copy_worksheet('product', category_name)
        try:
            headers = [
                'product_id', 'app_sale_price', 'original_price', 'sale_price', 'discount',
                'product_main_image_url', 'local_saved_image', 'product_small_image_urls',
                'product_video_url', 'local_saved_video', 'first_level_category_id',
                'first_level_category_name', 'second_level_category_id', 'second_level_category_name',
                'target_sale_price', 'target_sale_price_currency', 'target_app_sale_price_currency',
                'target_original_price_currency', 'original_price_currency', 'product_title',
                'evaluate_rate', 'promotion_link', 'shop_url', 'shop_id', 'tags'
            ]
            self._write_headers(ws, headers)
            row_data = []
            for product in products:
                _ = product
                row_data.append([
                    str(_.get('product_id')),
                    str(_.get('app_sale_price')),
                    _.get('original_price'),
                    _.get('sale_price'),
                    _.get('discount'),
                    _.get('product_main_image_url'),
                    _.get('local_saved_image'),
                    ', '.join(_.get('product_small_image_urls', [])),
                    _.get('product_video_url'),
                    _.get('local_saved_video'),
                    _.get('first_level_category_id'),
                    _.get('first_level_category_name'),
                    _.get('second_level_category_id'),
                    _.get('second_level_category_name'),
                    _.get('target_sale_price'),
                    _.get('target_sale_price_currency'),
                    _.get('target_app_sale_price_currency'),
                    _.get('target_original_price_currency'),
                    _.get('original_price_currency'),
                    _.get('product_title'),
                    _.get('evaluate_rate'),
                    _.get('promotion_link'),
                    _.get('shop_url'),
                    _.get('shop_id'),
                    ', '.join(_.get('tags', []))
                ])
            for index, row in enumerate(row_data, start=2):
                ws.update(f'A{index}:Y{index}', [row])
                logger.info(f"Products {str(_.get('product_id'))} updated.")
            self._format_category_products_worksheet(ws)
            logger.info("Products updated in worksheet.")

        except Exception as ex:
            logger.error("Error updating products in worksheet.", ex, exc_info=True)
            raise

    def _write_headers(self, ws: Worksheet, headers: list[str]):
        """
        Записывает заголовки в первую строку листа Google Sheets.

        :param ws: Рабочий лист Google Sheets.
        :type ws: Worksheet
        :param headers: Список заголовков.
        :type headers: list[str]
        """
        updates = [{'range': 'A1:Y1', 'values': [headers]}]
        ws.batch_update(updates)

    def _format_categories_worksheet(self, ws: Worksheet):
        """
        Форматирует лист 'categories'.

        :param ws: Лист Google Sheets для форматирования.
        :type ws: Worksheet
        """
        try:
            # Установка ширины столбцов
            set_column_width(ws, 'A:A', 150)
            set_column_width(ws, 'B:B', 200)
            set_column_width(ws, 'C:C', 300)
            set_column_width(ws, 'D:D', 200)
            set_column_width(ws, 'E:E', 150)

            # Установка высоты строк
            set_row_height(ws, '1:1', 40)

            # Форматирование заголовков
            header_format = cellFormat(
                textFormat=textFormat(bold=True, fontSize=12),
                horizontalAlignment='CENTER',
                verticalAlignment='MIDDLE',
                backgroundColor=Color(0.8, 0.8, 0.8)
            )
            format_cell_range(ws, 'A1:E1', header_format)

            logger.info("Categories worksheet formatted.")
        except Exception as ex:
            logger.error("Error formatting categories worksheet.", ex, exc_info=True)
            raise

    def _format_category_products_worksheet(self, ws: Worksheet):
        """
        Форматирует лист с продуктами категории.

        :param ws: Лист Google Sheets для форматирования.
        :type ws: Worksheet
        """
        try:
            for column, width in self.COLUMN_WIDTHS.items():
                set_column_width(ws, f'{column}:{column}', width)
            set_row_height(ws, '1:1', 40)
            header_format = cellFormat(
                textFormat=textFormat(bold=True, fontSize=12),
                horizontalAlignment='CENTER',
                verticalAlignment='TOP',
                backgroundColor=Color(0.8, 0.8, 0.8)
            )
            format_cell_range(ws, 'A1:Y1', header_format)
            logger.info("Category products worksheet formatted.")
        except Exception as ex:
            logger.error("Error formatting category products worksheet.", ex, exc_info=True)
            raise
```