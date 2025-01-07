# Анализ кода модуля `gsheet.py`

**Качество кода: 7/10**

-   **Плюсы:**
    *   Код разбит на логические блоки, что облегчает чтение и понимание.
    *   Используется класс `SpreadSheet`, что указывает на использование принципов ООП.
    *   Присутствует логирование ошибок и действий, что способствует отладке и мониторингу.
    *   Используются `SimpleNamespace` для хранения данных, что упрощает доступ к атрибутам.
    *   Есть форматирование Google Sheets, что улучшает читаемость данных.
-   **Минусы:**
    *   Не все функции и методы имеют подробные docstring в формате reStructuredText (RST).
    *   Присутствует избыточное использование try-except блоков, которые можно заменить на более лаконичные проверки с логированием.
    *   В некоторых местах можно улучшить читаемость кода, например, за счет более точных названий переменных и функций.
    *   Используется устаревший формат комментариев #, вместо docstring.

**Рекомендации по улучшению:**

1.  **Документация:**
    *   Добавить подробные docstring в формате RST ко всем функциям, методам и классам, включая описание параметров и возвращаемых значений.
2.  **Обработка ошибок:**
    *   Избегать избыточного использования try-except блоков, заменяя их на логирование ошибок через `logger.error`.
3.  **Импорты:**
    *   Удалить неиспользуемые импорты.
4.  **Код:**
    *   Улучшить читаемость кода, переписав не совсем понятные места.
    *   Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов, если это потребуется.
    *   Убедиться, что все имена функций, переменных и импортов соответствуют ранее обработанным файлам.

**Оптимизированный код:**

```python
"""
Модуль для работы с Google Sheets в контексте рекламных кампаний AliExpress.
=========================================================================================

Этот модуль предоставляет класс :class:`AliCampaignGoogleSheet`, который наследует класс :class:`SpreadSheet`
и расширяет его функциональность для управления Google Sheets, используемых в рекламных кампаниях AliExpress.

Модуль включает в себя методы для записи данных о кампаниях, категориях и продуктах, а также для
форматирования листов Google Sheets.

Пример использования
--------------------

Пример инициализации класса `AliCampaignGoogleSheet`:

.. code-block:: python

    campaign_sheet = AliCampaignGoogleSheet(campaign_name='TestCampaign', language='ru', currency='USD')
    campaign_sheet.clear()
"""
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12



import time
from types import SimpleNamespace
from typing import Optional, Any, List, Dict
from gspread.worksheet import Worksheet
# from gspread_formatting import (
#     cellFormat,
#     textFormat,
#     numberFormat,
#     format_cell_range,
#     set_column_width,
#     set_row_height,
#     Color
# )
from src.goog.spreadsheet.spreadsheet import SpreadSheet
from src.utils.jjson import j_dumps
from src.utils.printer import pprint
from src.logger.logger import logger
from src.ai.openai import translate


class AliCampaignGoogleSheet(SpreadSheet):
    """
    Класс для работы с Google Sheets в рамках кампаний AliExpress.

    Наследует класс :class:`SpreadSheet` и предоставляет дополнительные методы
    для управления листами Google Sheets, записи данных о категориях и продуктах,
    и форматирования листов.
    """
    spreadsheet_id = '1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0'
    spreadsheet: SpreadSheet = None
    worksheet: Worksheet = None

    def __init__(self, campaign_name: str, language: str | dict = None, currency: str = None):
        """
        Инициализация объекта AliCampaignGoogleSheet.

        :param campaign_name: Имя кампании.
        :type campaign_name: str
        :param language: Язык кампании.
        :type language: str | dict, optional
        :param currency: Валюта кампании.
        :type currency: str, optional
        """
        # Инициализация родительского класса SpreadSheet
        super().__init__(spreadsheet_id=self.spreadsheet_id)
        #self.capmaign_editor = AliCampaignEditor(campaign_name=campaign_name, language=language, currency=currency)
        # if campaign_editor:
        #     self.set_campaign_worksheet(campaign_editor.campaign)
        #     self.set_categories_worksheet(campaign_editor.campaign.category)

    def clear(self):
        """
        Удаляет листы продуктов и очищает данные на листах категорий и кампании.
        """
        try:
            # Код выполняет удаление листов продуктов
            self.delete_products_worksheets()
        except Exception as ex:
            # Логирование ошибки при очистке
            logger.error("Ошибка очистки", ex)

    def delete_products_worksheets(self):
        """
        Удаляет все листы, кроме 'categories', 'product', 'category' и 'campaign'.
        """
        excluded_titles = {'categories', 'product', 'category', 'campaign'}
        try:
            # Код получает список всех листов
            worksheets = self.spreadsheet.worksheets()
            for sheet in worksheets:
                # Код проверяет, нужно ли удалять текущий лист
                if sheet.title not in excluded_titles:
                    # Код удаляет лист
                    self.spreadsheet.del_worksheet_by_id(sheet.id)
                    logger.success(f"Worksheet '{sheet.title}' deleted.")
        except Exception as ex:
            # Логирование ошибки удаления листов
            logger.error("Error deleting all worksheets.", ex, exc_info=True)
            raise

    def set_campaign_worksheet(self, campaign: SimpleNamespace):
        """
        Записывает данные кампании на лист Google Sheets.

        :param campaign: Объект SimpleNamespace с данными кампании.
        :type campaign: SimpleNamespace
        """
        try:
             # Код получает лист 'campaign'
            ws: Worksheet = self.get_worksheet('campaign')

            # Код подготавливает данные для записи
            updates = []
            vertical_data = [
                ('A1', 'Campaign Name', campaign.campaign_name),
                ('A2', 'Campaign Title', campaign.title),
                ('A3', 'Campaign Language', campaign.language),
                ('A4', 'Campaign Currency', campaign.currency),
                ('A5', 'Campaign Description', campaign.description),

            ]

             # Код добавляет операции обновления в список
            for cell, header, value in vertical_data:
                updates.append({'range': cell, 'values': [[header]]})
                updates.append({'range': f'B{cell[1]}', 'values': [[str(value)]]})

            # Код выполняет пакетное обновление
            if updates:
                ws.batch_update(updates)

            logger.info("Campaign data written to 'campaign' worksheet vertically.")

        except Exception as ex:
             # Логирование ошибки записи данных кампании
            logger.error("Error setting campaign worksheet.", ex, exc_info=True)
            raise

    def set_products_worksheet(self, category_name: str):
        """
        Записывает данные о продуктах на лист Google Sheets.

        :param category_name: Название категории продуктов.
        :type category_name: str
        """
        if category_name:
            # Код получает категорию по имени
            category: SimpleNamespace = getattr(self.editor.campaign.category, category_name)
            products: list[SimpleNamespace] = category.products
        else:
            # Логирование предупреждения об отсутствии продуктов
            logger.warning(f"No products found for {category=}\\n{products=}.")
            return
        # Код копирует лист 'product' и устанавливает имя категории
        ws = self.copy_worksheet('product', category_name)

        try:
             # Код подготавливает данные для записи
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
            # Код выполняет запись данных
            for index, row in enumerate(row_data, start=2):
                ws.update(f'A{index}:Y{index}', [row])
                logger.info(f"Products {str(_.get('product_id'))} updated .")

            self._format_category_products_worksheet(ws)
            logger.info("Products updated in worksheet.")

        except Exception as ex:
            # Логирование ошибки записи продуктов
            logger.error("Error setting products worksheet.", ex, exc_info=True)
            raise

    def set_categories_worksheet(self, categories: SimpleNamespace):
        """
        Записывает данные о категориях на лист Google Sheets.

        :param categories: Объект SimpleNamespace с данными категорий.
        :type categories: SimpleNamespace
        """
        # Код получает лист 'categories'
        ws: Worksheet = self.get_worksheet('categories')
        # Код очищает лист
        ws.clear()

        try:
             # Код получает данные категорий
            category_data = categories.__dict__

            # Код проверяет, что все объекты категории имеют необходимые атрибуты
            required_attrs = ['name', 'title', 'description', 'tags', 'products_count']

            if all(all(hasattr(category, attr) for attr in required_attrs) for category in category_data.values()):
                # Код подготавливает заголовки таблицы
                headers = ['Name', 'Title', 'Description', 'Tags', 'Products Count']
                # Код записывает заголовки
                ws.update('A1:E1', [headers])

                # Код подготавливает данные для записи
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
                # Код записывает данные на лист
                ws.update(f'A2:E{1 + len(rows)}', rows)
                # Код форматирует лист
                self._format_categories_worksheet(ws)

                logger.info("Category fields updated from SimpleNamespace object.")
            else:
                # Логирование предупреждения о неполных данных
                logger.warning("One or more category objects do not contain all required attributes.")

        except Exception as ex:
             # Логирование ошибки записи категорий
            logger.error("Error updating fields from SimpleNamespace object.", ex, exc_info=True)
            raise

    def get_categories(self) -> List[Dict[str, Any]]:
        """
        Получает данные о категориях с листа Google Sheets.

        :return: Список словарей с данными о категориях.
        :rtype: List[Dict[str, Any]]
        """
         # Код получает лист 'categories'
        ws = self.get_worksheet('categories')
        # Код получает все записи
        data = ws.get_all_records()
        logger.info("Categories data retrieved from worksheet.")
        return data

    def set_category_products(self, category_name: str, products: dict):
        """
        Записывает данные о продуктах в новый лист Google Sheets.

        :param category_name: Название категории.
        :type category_name: str
        :param products: Словарь с данными о продуктах.
        :type products: dict
        """
        if category_name:
            # Код получает категорию
            category_ns: SimpleNamespace = getattr(self.editor.campaign.category, category_name)
            products_ns: list[SimpleNamespace] = category_ns.products
        else:
             # Логирование предупреждения об отсутствии продуктов
            logger.warning("No products found for category.")
            return
        # Код копирует лист 'product' и устанавливает имя категории
        ws = self.copy_worksheet('product', category_name)
        try:
            # Код подготавливает заголовки
            headers = [
                'product_id', 'app_sale_price', 'original_price', 'sale_price', 'discount',
                'product_main_image_url', 'local_saved_image', 'product_small_image_urls',
                'product_video_url', 'local_saved_video', 'first_level_category_id',
                'first_level_category_name', 'second_level_category_id', 'second_level_category_name',
                'target_sale_price', 'target_sale_price_currency', 'target_app_sale_price_currency',
                'target_original_price_currency', 'original_price_currency', 'product_title',
                'evaluate_rate', 'promotion_link', 'shop_url', 'shop_id', 'tags'
            ]
             # Код записывает заголовки
            updates = [{'range': 'A1:Y1', 'values': [headers]}]

            # Код подготавливает данные для записи
            row_data = []
            for product in products:
                _ = product.__dict__
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

            # Код записывает данные на лист
            for index, row in enumerate(row_data, start=2):
                ws.update(f'A{index}:Y{index}', [row])
                logger.info(f"Products {str(_.get('product_id'))} updated .")
            # Код форматирует лист
            self._format_category_products_worksheet(ws)

            logger.info("Products updated in worksheet.")
        except Exception as ex:
             # Логирование ошибки записи продуктов
            logger.error("Error updating products in worksheet.", ex, exc_info=True)
            raise

    def _format_categories_worksheet(self, ws: Worksheet):
        """
        Форматирует лист 'categories'.

        :param ws: Лист Google Sheets для форматирования.
        :type ws: Worksheet
        """
        try:
            # Код устанавливает ширину столбцов
            # from gspread_formatting import set_column_width, set_row_height, cellFormat, textFormat, Color
            # TODO: сделать импорт и использовать как в _format_category_products_worksheet
            ws.set_column_width('A:A', 150)  # Ширина столбца A
            ws.set_column_width('B:B', 200)  # Ширина столбца B
            ws.set_column_width('C:C', 300)  # Ширина столбца C
            ws.set_column_width('D:D', 200)  # Ширина столбца D
            ws.set_column_width('E:E', 150)  # Ширина столбца E
            # Код устанавливает высоту строк
            ws.set_row_height('1:1', 40)  # Высота заголовков

            # Код форматирует заголовки
            header_format = cellFormat(
                textFormat=textFormat(bold=True, fontSize=12),
                horizontalAlignment='CENTER',
                verticalAlignment='MIDDLE',  # Добавлено вертикальное выравнивание
                backgroundColor=Color(0.8, 0.8, 0.8)  # Используем Color для задания цвета
            )
            # Код применяет форматирование
            format_cell_range(ws, 'A1:E1', header_format)

            logger.info("Categories worksheet formatted.")
        except Exception as ex:
             # Логирование ошибки форматирования
            logger.error("Error formatting categories worksheet.", ex, exc_info=True)
            raise

    def _format_category_products_worksheet(self, ws: Worksheet):
        """
        Форматирует лист с продуктами категории.

        :param ws: Лист Google Sheets для форматирования.
        :type ws: Worksheet
        """
        try:
            # from gspread_formatting import set_column_width, set_row_height, cellFormat, textFormat, Color
            # Код устанавливает ширину столбцов
            set_column_width(ws, 'A:A', 250)  # Ширина столбца A
            set_column_width(ws, 'B:B', 220)  # Ширина столбца B
            set_column_width(ws, 'C:C', 220)  # Ширина столбца C
            set_column_width(ws, 'D:D', 220)  # Ширина столбца D
            set_column_width(ws, 'E:E', 200)  # Ширина столбца E
            set_column_width(ws, 'F:F', 200)  # Ширина столбца F
            set_column_width(ws, 'G:G', 200)  # Ширина столбца G
            set_column_width(ws, 'H:H', 200)  # Ширина столбца H
            set_column_width(ws, 'I:I', 200)  # Ширина столбца I
            set_column_width(ws, 'J:J', 200)  # Ширина столбца J
            set_column_width(ws, 'K:K', 200)  # Ширина столбца K
            set_column_width(ws, 'L:L', 200)  # Ширина столбца L
            set_column_width(ws, 'M:M', 200)  # Ширина столбца M
            set_column_width(ws, 'N:N', 200)  # Ширина столбца N
            set_column_width(ws, 'O:O', 200)  # Ширина столбца O
            set_column_width(ws, 'P:P', 200)  # Ширина столбца P
            set_column_width(ws, 'Q:Q', 200)  # Ширина столбца Q
            set_column_width(ws, 'R:R', 200)  # Ширина столбца R
            set_column_width(ws, 'S:S', 200)  # Ширина столбца S
            set_column_width(ws, 'T:T', 200)  # Ширина столбца T
            set_column_width(ws, 'U:U', 200)  # Ширина столбца U
            set_column_width(ws, 'V:V', 200)  # Ширина столбца V
            set_column_width(ws, 'W:W', 200)  # Ширина столбца W
            set_column_width(ws, 'X:X', 200)  # Ширина столбца X
            set_column_width(ws, 'Y:Y', 200)  # Ширина столбца Y

            # Код устанавливает высоту строк
            set_row_height(ws, '1:1', 40)  # Высота заголовков

            # Код форматирует заголовки
            header_format = cellFormat(
                textFormat=textFormat(bold=True, fontSize=12),
                horizontalAlignment='CENTER',
                verticalAlignment='TOP',  # Добавлено вертикальное выравнивание
                backgroundColor=Color(0.8, 0.8, 0.8)  # Используем Color для задания цвета
            )
            # Код применяет форматирование
            format_cell_range(ws, 'A1:Y1', header_format)

            logger.info("Category products worksheet formatted.")
        except Exception as ex:
             # Логирование ошибки форматирования
            logger.error("Error formatting category products worksheet.", ex, exc_info=True)
            raise
```