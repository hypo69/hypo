## Анализ кода модуля gsheet

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разбит на логические блоки, каждый из которых выполняет определенную функцию.
    - Используется класс `AliCampaignGoogleSheet`, который наследуется от `SpreadSheet`, что способствует переиспользованию кода и упрощает его поддержку.
    - Присутствует логирование ошибок и информационных сообщений через `logger`.
    - Присутствуют docstring для классов, методов, параметров.
    - Код соответствует pep8.
-  Минусы
    - Не все импорты используются, что необходимо исправить.
    - Есть дублирование кода в методах `set_products_worksheet` и `set_category_products`.
    -  В некоторых местах используется `str(_.get(...))` что избыточно так как все данные из таблицы - `str`
    -  Не используется `j_dumps`

**Рекомендации по улучшению**

1. **Импорты**:
    - Удалить неиспользуемые импорты.
    - Добавить импорты для `Color`, `cellFormat`, `textFormat`, `format_cell_range`, `set_column_width`, `set_row_height` из `gspread_formatting`.
2.  **Удаление дублирования**:
    - Вынести общую логику записи продуктов в отдельный метод, чтобы избежать дублирования кода в `set_products_worksheet` и `set_category_products`.
3.  **Упрощение кода**:
    - Упростить код, используя более итерируемые методы для записи данных, например, через `ws.update_cells()`.
    - Избавиться от лишнего `str()` при получении данных из `dict`.
4.  **Обработка ошибок**:
    - Изменить обработку ошибок, заменив `try...except` на проверку `if not` и логирование ошибки в `logger`.
5.  **Комментарии**:
    - Улучшить комментарии в коде, чтобы они были более информативными и соответствовали формату RST.
    - Добавить описание модуля.
6.  **Именование переменных**:
    -  Использовать более конкретные имена переменных для повышения читаемости кода.

**Оптимизированный код**

```python
"""
Модуль для работы с Google Sheets в рамках рекламных кампаний AliExpress.
======================================================================

Этот модуль предоставляет класс :class:`AliCampaignGoogleSheet`,
который наследуется от :class:`src.goog.spreadsheet.spreadsheet.SpreadSheet`
и используется для управления данными в Google Sheets, связанными с рекламными
кампаниями AliExpress. Он включает методы для чтения, записи и форматирования данных
о кампаниях, категориях и продуктах.

Пример использования
--------------------

Пример создания и использования класса `AliCampaignGoogleSheet`:

.. code-block:: python

    campaign_sheet = AliCampaignGoogleSheet(campaign_name='test_campaign', language='ru', currency='USD')
    campaign_sheet.clear()  # Очистка данных в Google Sheets
    # ... добавление данных в таблицы ...
"""
import time
from types import SimpleNamespace
from typing import Optional, Any, List, Dict
from gspread.worksheet import Worksheet
from src.goog.spreadsheet.spreadsheet import SpreadSheet
from src.utils.jjson import j_dumps
from src.utils.printer import pprint
from src.logger.logger import logger
from gspread_formatting import (
    cellFormat,
    textFormat,
    numberFormat,
    format_cell_range,
    set_column_width,
    set_row_height,
    Color
)


class AliCampaignGoogleSheet(SpreadSheet):
    """
    Класс для работы с Google Sheets в рамках кампаний AliExpress.

    Наследует класс SpreadSheet и предоставляет дополнительные методы для управления листами Google Sheets,
    записи данных о категориях и продуктах, и форматирования листов.
    """
    spreadsheet_id = '1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0'
    spreadsheet: SpreadSheet = None
    worksheet: Worksheet = None

    def __init__(self, campaign_name: str, language: str | dict = None, currency: str = None):
        """
        Инициализирует AliCampaignGoogleSheet с указанным ID Google Sheets и дополнительными параметрами.

        Args:
            campaign_name (str): Название кампании.
            language (str, optional): Язык кампании. Defaults to None.
            currency (str, optional): Валюта кампании. Defaults to None.
        """
        # Инициализация SpreadSheet с указанным ID spreadsheet
        super().__init__(spreadsheet_id=self.spreadsheet_id)

    def clear(self):
        """
        Очищает содержимое.

        Удаляет листы продуктов и очищает данные на листах категорий и других указанных листах.
        """
        try:
            self.delete_products_worksheets()
        except Exception as ex:
            logger.error("Ошибка очистки", ex)

    def delete_products_worksheets(self):
        """
        Удаляет все листы из Google Sheets, кроме 'categories', 'product', 'category', 'campaign'.
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
        Записывает данные о кампании в Google Sheets.

        Args:
            campaign (SimpleNamespace): Объект SimpleNamespace с данными кампании.
        """
        try:
            ws: Worksheet = self.get_worksheet('campaign')

            # Подготовка данных для записи
            updates = []
            vertical_data = [
                ('A1', 'Campaign Name', campaign.campaign_name),
                ('A2', 'Campaign Title', campaign.title),
                ('A3', 'Campaign Language', campaign.language),
                ('A4', 'Campaign Currency', campaign.currency),
                ('A5', 'Campaign Description', campaign.description),
            ]
            # Добавление операций обновления в список batch_update
            for cell, header, value in vertical_data:
                updates.append({'range': cell, 'values': [[header]]})
                updates.append({'range': f'B{cell[1]}', 'values': [[str(value)]]})
            # Выполнение пакетного обновления
            if updates:
                ws.batch_update(updates)

            logger.info("Campaign data written to 'campaign' worksheet vertically.")

        except Exception as ex:
            logger.error("Error setting campaign worksheet.", ex, exc_info=True)
            raise

    def set_products_worksheet(self, category_name: str):
        """
        Записывает данные о продуктах в Google Sheets.

        Args:
            category_name (str): Имя категории, для которой необходимо записать продукты.
        """
        if not category_name:
            logger.warning(f"No products found for {category_name=}")
            return

        try:
            category: SimpleNamespace = getattr(self.editor.campaign.category, category_name)
            products: list[SimpleNamespace] = category.products
        except Exception as ex:
             logger.error(f"Ошибка получения категории или продуктов {category_name=}.", ex, exc_info=True)
             return
             
        if not products:
            logger.warning(f"No products found for {category_name=}")
            return
        
        ws = self.copy_worksheet('product', category_name)

        try:
            self._write_products_data(ws, products)
            self._format_category_products_worksheet(ws)
            logger.info("Products updated in worksheet.")

        except Exception as ex:
            logger.error("Error setting products worksheet.", ex, exc_info=True)
            raise

    def set_categories_worksheet(self, categories: SimpleNamespace):
        """
        Записывает данные из объекта SimpleNamespace с категориями в Google Sheets.

        Args:
            categories (SimpleNamespace): Объект, где ключи — это категории с данными для записи.
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

    def get_categories(self):
        """
        Получает данные из таблицы Google Sheets.

        Returns:
            list[dict]: Данные из таблицы в виде списка словарей.
        """
        ws = self.get_worksheet('categories')
        data = ws.get_all_records()
        logger.info("Categories data retrieved from worksheet.")
        return data

    def set_category_products(self, category_name: str, products: list[dict]):
        """
        Записывает данные о продуктах в новую таблицу Google Sheets.

        Args:
            category_name (str): Название категории.
            products (list[dict]): Список словарей с данными о продуктах.
        """
        if not category_name:
            logger.warning("No products found for category.")
            return
        
        ws = self.copy_worksheet('product', category_name)
        try:
            self._write_products_data(ws, products)
            self._format_category_products_worksheet(ws)
            logger.info("Products updated in worksheet.")
        except Exception as ex:
            logger.error("Error updating products in worksheet.", ex, exc_info=True)
            raise

    def _write_products_data(self, ws: Worksheet, products: list[dict|SimpleNamespace]):
        """
        Записывает данные о продуктах в Google Sheets.

        Args:
            ws (Worksheet): Лист Google Sheets для записи данных.
            products (list[dict|SimpleNamespace]): Список продуктов для записи.
        """
        headers = [
                'product_id', 'app_sale_price', 'original_price', 'sale_price', 'discount',
                'product_main_image_url', 'local_image_path', 'product_small_image_urls',
                'product_video_url', 'local_video_path', 'first_level_category_id',
                'first_level_category_name', 'second_level_category_id', 'second_level_category_name',
                'target_sale_price', 'target_sale_price_currency', 'target_app_sale_price_currency',
                'target_original_price_currency', 'original_price_currency', 'product_title',
                'evaluate_rate', 'promotion_link', 'shop_url', 'shop_id', 'tags'
            ]
        
        ws.update('A1:Y1', [headers])

        row_data = []
        for product in products:
            if isinstance(product, SimpleNamespace):
                product_dict = product.__dict__
            else:
                 product_dict = product
            row_data.append([
                str(product_dict.get('product_id')),
                product_dict.get('product_title'),
                product_dict.get('promotion_link'),
                str(product_dict.get('app_sale_price')),
                product_dict.get('original_price'),
                product_dict.get('sale_price'),
                product_dict.get('discount'),
                product_dict.get('product_main_image_url'),
                product_dict.get('local_image_path'),
                ', '.join(product_dict.get('product_small_image_urls', [])),
                product_dict.get('product_video_url'),
                product_dict.get('local_video_path'),
                product_dict.get('first_level_category_id'),
                product_dict.get('first_level_category_name'),
                product_dict.get('second_level_category_id'),
                product_dict.get('second_level_category_name'),
                product_dict.get('target_sale_price'),
                product_dict.get('target_sale_price_currency'),
                product_dict.get('target_app_sale_price_currency'),
                product_dict.get('target_original_price_currency'),
                product_dict.get('original_price_currency'),
                product_dict.get('evaluate_rate'),
                product_dict.get('shop_url'),
                product_dict.get('shop_id'),
                ', '.join(product_dict.get('tags', []))
            ])

        for index, row in enumerate(row_data, start=2):
             ws.update(f'A{index}:Y{index}', [row])
             logger.info(f"Products updated row {index} .")


    def _format_categories_worksheet(self, ws: Worksheet):
        """
        Форматирует лист 'categories'.

        Args:
            ws (Worksheet): Лист Google Sheets для форматирования.
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

        Args:
            ws (Worksheet): Лист Google Sheets для форматирования.
        """
        try:
            # Установка ширины столбцов
            set_column_width(ws, 'A:A', 250)
            set_column_width(ws, 'B:B', 220)
            set_column_width(ws, 'C:C', 220)
            set_column_width(ws, 'D:D', 220)
            set_column_width(ws, 'E:E', 200)
            set_column_width(ws, 'F:F', 200)
            set_column_width(ws, 'G:G', 200)
            set_column_width(ws, 'H:H', 200)
            set_column_width(ws, 'I:I', 200)
            set_column_width(ws, 'J:J', 200)
            set_column_width(ws, 'K:K', 200)
            set_column_width(ws, 'L:L', 200)
            set_column_width(ws, 'M:M', 200)
            set_column_width(ws, 'N:N', 200)
            set_column_width(ws, 'O:O', 200)
            set_column_width(ws, 'P:P', 200)
            set_column_width(ws, 'Q:Q', 200)
            set_column_width(ws, 'R:R', 200)
            set_column_width(ws, 'S:S', 200)
            set_column_width(ws, 'T:T', 200)
            set_column_width(ws, 'U:U', 200)
            set_column_width(ws, 'V:V', 200)
            set_column_width(ws, 'W:W', 200)
            set_column_width(ws, 'X:X', 200)
            set_column_width(ws, 'Y:Y', 200)
            # Установка высоты строк
            set_row_height(ws, '1:1', 40)

            # Форматирование заголовков
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