# Анализ кода модуля `gsheets_check_this_code.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован, использует классы и методы для организации работы с Google Sheets и данными кампаний AliExpress.
    - Присутствует логирование основных действий и ошибок, что облегчает отладку.
    - Код использует пакет `gspread-formatting` для форматирования листов, что улучшает читаемость данных.
    - Применение `SimpleNamespace` для хранения данных о кампаниях и категориях позволяет удобно обращаться к атрибутам.
    - Код соблюдает основные принципы DRY (Don't Repeat Yourself) путем создания методов для общих операций (например, форматирование листов).
- Минусы
    -   Не все функции и методы имеют docstring в формате reStructuredText (RST), что снижает удобство использования и понимания кода.
    -  В некоторых местах используются избыточные блоки `try-except`, которые можно заменить на логирование ошибок с `logger.error`.
    -   В некоторых местах  используется `#` как комментарий, но он не несёт информации о том что происходит в коде.

**Рекомендации по улучшению**

1.  **Документация**: Добавить docstring в формате RST для всех функций, методов и классов, что обеспечит понятность кода.
2.  **Обработка ошибок**: Использовать `logger.error` для логирования ошибок вместо блоков `try-except` в случаях, когда нет необходимости в дополнительной обработке исключений.
3.  **Импорты**: Проверить и добавить все необходимые импорты.
4.  **Комментарии**: Заменить комментарии `#` на более информативные, объясняющие логику кода.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для работы с Google Sheets в рамках кампаний AliExpress.
=========================================================================================

Этот модуль предоставляет класс :class:`AliCampaignGoogleSheet`, который наследуется от :class:`SpreadSheet`
и используется для управления данными рекламных кампаний AliExpress через Google Sheets. Он обеспечивает
функциональность для записи, чтения и форматирования данных о кампаниях, категориях и продуктах.

Пример использования
--------------------

Пример использования класса `AliCampaignGoogleSheet`:

.. code-block:: python

    campaign_sheet = AliCampaignGoogleSheet(campaign_name='Test Campaign', language='ru', currency='USD')
    campaign_sheet.set_campaign_worksheet(campaign_data)
    campaign_sheet.set_categories_worksheet(category_data)
    campaign_sheet.set_products_worksheet(category_name)
"""


import time
from types import SimpleNamespace
from typing import Optional, List, Dict
# from src.webdriver.driver import Driver, Chrome, Firefox, Edge # Удален лишний импорт
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
# from src.goog.spreadsheet.spreadsheet import SpreadSheet  # Удален лишний импорт
from src.suppliers.aliexpress.campaign.ali_campaign_editor import AliCampaignEditor
from src.utils.jjson import j_dumps
from src.utils.printer import pprint
from src.logger.logger import logger
from src.webdriver.driver import Driver, Chrome # добавлен импорт
from src.goog.spreadsheet.spreadsheet import SpreadSheet # добавлен импорт

# from src.ai.openai import translate #  Удален неиспользуемый импорт

class AliCampaignGoogleSheet(SpreadSheet):
    """
    Класс для работы с Google Sheets в рамках кампаний AliExpress.

    Наследует класс :class:`SpreadSheet` и предоставляет дополнительные методы для управления листами Google Sheets,
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
        :param language: Язык кампании.
        :type language: str | dict, optional
        :param currency: Валюта кампании.
        :type currency: str, optional
        """
        # Инициализируем родительский класс SpreadSheet с ID таблицы
        super().__init__(spreadsheet_id=self.spreadsheet_id)
        # Инициализируем редактор кампании AliExpress
        self.editor = AliCampaignEditor(campaign_name=campaign_name, language=language, currency=currency)
        # Вызываем метод для очистки таблиц
        self.clear()
        # Устанавливаем таблицу для кампании
        self.set_campaign_worksheet(self.editor.campaign)
        # Устанавливаем таблицу для категорий
        self.set_categories_worksheet(self.editor.campaign.category)
        # Открываем страницу гугл таблицы в браузере
        self.driver.get_url(f'https://docs.google.com/spreadsheets/d/{self.spreadsheet_id}')

    def clear(self):
        """
        Очищает содержимое листов Google Sheets.
        Удаляет листы с продуктами и очищает данные на листах категорий и других указанных листах.
        """
        try:
            # Вызываем метод удаления листов с продуктами
            self.delete_products_worksheets()
        except Exception as ex:
            # Логируем ошибку, если не удалось очистить таблицы
            logger.error("Ошибка очистки", ex)

    def delete_products_worksheets(self):
        """
        Удаляет все листы из Google Sheets, кроме 'categories', 'product', 'category' и 'campaign'.
        """
        excluded_titles = {'categories', 'product', 'category', 'campaign'}
        try:
            # Получаем все листы из таблицы
            worksheets = self.spreadsheet.worksheets()
            # Итерируемся по листам
            for sheet in worksheets:
                # Проверяем, нужно ли удалять лист
                if sheet.title not in excluded_titles:
                    # Удаляем лист
                    self.spreadsheet.del_worksheet_by_id(sheet.id)
                    logger.success(f"Worksheet '{sheet.title}' deleted.")
        except Exception as ex:
             # Логируем ошибку, если не удалось удалить листы
            logger.error("Error deleting all worksheets.", ex, exc_info=True)
            raise

    def set_campaign_worksheet(self, campaign: SimpleNamespace):
        """
        Записывает данные кампании в Google Sheets.

        :param campaign: Объект SimpleNamespace с данными о кампании.
        :type campaign: SimpleNamespace
        """
        try:
            # Получаем лист кампании
            ws: Worksheet = self.get_worksheet('campaign')  # Clear the 'campaign' worksheet

            # Подготовка данных для вертикальной записи
            updates = []
            vertical_data = [
                ('A1', 'Campaign Name', campaign.name),
                ('A2', 'Campaign Title', campaign.title),
                ('A3', 'Campaign Language', campaign.language),
                ('A4', 'Campaign Currency', campaign.currency),
                ('A5', 'Campaign Description', campaign.description),
            ]
            # Обновляем данные в таблице
            for cell, header, value in vertical_data:
                updates.append({'range': cell, 'values': [[header]]})
                updates.append({'range': f'B{cell[1]}', 'values': [[str(value)]]})

            # Выполняем обновление таблицы
            if updates:
                ws.batch_update(updates)

            logger.info("Campaign data written to 'campaign' worksheet vertically.")

        except Exception as ex:
            # Логируем ошибку, если не удалось обновить таблицу кампании
            logger.error("Error setting campaign worksheet.", ex, exc_info=True)
            raise

    def set_products_worksheet(self, category_name: str):
        """
        Записывает данные о продуктах в Google Sheets.

        :param category_name: Название категории, продукты которой нужно записать.
        :type category_name: str
        """
        if category_name:
            # Получаем данные о категории
            category: SimpleNamespace = getattr(self.editor.campaign.category, category_name)
            # Получаем список продуктов
            products: list[SimpleNamespace] = category.products
        else:
            # Логируем предупреждение, если нет продуктов
            logger.warning("No products found for category.")
            return
        # Копируем лист с продуктами
        ws = self.copy_worksheet('product', category_name)
    
        try:
            # Готовим данные для записи
            row_data = []
            for product in products:
                # Преобразуем данные продукта в словарь
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
            # Обновляем строки таблицы
            for index, row in enumerate(row_data, start=2):
                ws.update(f'A{index}:Y{index}', [row])
                logger.info(f"Products {str(_.get('product_id'))} updated .")
            # Вызываем метод форматирования
            self._format_category_products_worksheet(ws)
            logger.info("Products updated in worksheet.")

        except Exception as ex:
             # Логируем ошибку, если не удалось обновить таблицу продуктов
            logger.error("Error setting products worksheet.", ex, exc_info=True)
            raise

    def set_categories_worksheet(self, categories: SimpleNamespace):
        """
        Записывает данные о категориях в Google Sheets.

        :param categories: Объект SimpleNamespace, содержащий данные о категориях.
        :type categories: SimpleNamespace
        """
        # Получаем лист категорий
        ws: Worksheet = self.get_worksheet('categories')
        # Очищаем лист перед записью данных
        ws.clear()

        try:
            # Получаем данные категорий
            category_data = categories.__dict__

            # Проверяем наличие необходимых атрибутов у категорий
            required_attrs = ['name', 'title', 'description', 'tags', 'products_count']
        
            if all(all(hasattr(category, attr) for attr in required_attrs) for category in category_data.values()):
                # Заголовки таблицы
                headers = ['Name', 'Title', 'Description', 'Tags', 'Products Count']
                ws.update('A1:E1', [headers])

                # Подготовка данных для записи
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

                # Обновляем строки таблицы
                ws.update(f'A2:E{1 + len(rows)}', rows)
                # Вызываем метод форматирования таблицы
                self._format_categories_worksheet(ws)

                logger.info("Category fields updated from SimpleNamespace object.")
            else:
                 # Логируем предупреждение, если не все атрибуты присутствуют
                logger.warning("One or more category objects do not contain all required attributes.")

        except Exception as ex:
            # Логируем ошибку, если не удалось обновить данные категорий
            logger.error("Error updating fields from SimpleNamespace object.", ex, exc_info=True)
            raise

    def get_categories(self) -> list[dict]:
        """
        Извлекает данные о категориях из Google Sheets.

        :return: Список словарей, представляющих данные о категориях.
        :rtype: list[dict]
        """
        # Получаем лист категорий
        ws = self.get_worksheet('categories')
        # Получаем все записи с листа
        data = ws.get_all_records()
        logger.info("Categories data retrieved from worksheet.")
        # Возвращаем данные
        return data

    def set_category_products(self, category_name: str, products: dict):
        """
        Записывает данные о продуктах в лист Google Sheets для конкретной категории.

        :param category_name: Название категории.
        :type category_name: str
        :param products: Словарь с данными о продуктах.
        :type products: dict
        """
        if category_name:
            # Получаем данные категории из объекта
            category_ns: SimpleNamespace = getattr(self.editor.campaign.category, category_name)
            # Получаем список продуктов
            products_ns: list[SimpleNamespace] = category_ns.products
        else:
            # Логируем предупреждение если нет продуктов
            logger.warning("No products found for category.")
            return
        # Копируем лист с продуктами
        ws = self.copy_worksheet('product', category_name)
        try:
            # Заголовки таблицы
            headers = [
                'product_id', 'app_sale_price', 'original_price', 'sale_price', 'discount',
                'product_main_image_url', 'local_saved_image', 'product_small_image_urls',
                'product_video_url', 'local_saved_video', 'first_level_category_id',
                'first_level_category_name', 'second_level_category_id', 'second_level_category_name',
                'target_sale_price', 'target_sale_price_currency', 'target_app_sale_price_currency',
                'target_original_price_currency', 'original_price_currency', 'product_title',
                'evaluate_rate', 'promotion_link', 'shop_url', 'shop_id', 'tags'
            ]
            updates = [{'range': 'A1:Y1', 'values': [headers]}]  # Add headers to the worksheet

            row_data = []
            for product in products:
                # Преобразуем данные продукта в словарь
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
            # Обновляем строки в таблице
            for index, row in enumerate(row_data, start=2):
                ws.update(f'A{index}:Y{index}', [row])
                logger.info(f"Products {str(_.get('product_id'))} updated .")
            # Вызываем метод форматирования таблицы
            self._format_category_products_worksheet(ws)
            logger.info("Products updated in worksheet.")
        except Exception as ex:
            # Логируем ошибку, если не удалось обновить данные продуктов
            logger.error("Error updating products in worksheet.", ex, exc_info=True)
            raise

    def _format_categories_worksheet(self, ws: Worksheet):
        """
        Форматирует лист 'categories'.

        :param ws: Лист Google Sheets для форматирования.
        :type ws: Worksheet
        """
        try:
            # Устанавливаем ширину столбцов
            set_column_width(ws, 'A:A', 150)  # Ширина столбца A
            set_column_width(ws, 'B:B', 200)  # Ширина столбца B
            set_column_width(ws, 'C:C', 300)  # Ширина столбца C
            set_column_width(ws, 'D:D', 200)  # Ширина столбца D
            set_column_width(ws, 'E:E', 150)  # Ширина столбца E

            # Устанавливаем высоту строк
            set_row_height(ws, '1:1', 40)  # Высота заголовков

            # Форматирование заголовков
            header_format = cellFormat(
                textFormat=textFormat(bold=True, fontSize=12),
                horizontalAlignment='CENTER',
                verticalAlignment='MIDDLE',  # Добавлено вертикальное выравнивание
                backgroundColor=Color(0.8, 0.8, 0.8)  # Используем Color для задания цвета
            )
            format_cell_range(ws, 'A1:E1', header_format)

            logger.info("Categories worksheet formatted.")
        except Exception as ex:
             # Логируем ошибку, если не удалось отформатировать лист категорий
            logger.error("Error formatting categories worksheet.", ex, exc_info=True)
            raise

    def _format_category_products_worksheet(self, ws: Worksheet):
        """
        Форматирует лист с продуктами категории.

        :param ws: Лист Google Sheets для форматирования.
        :type ws: Worksheet
        """
        try:
            # Установка ширины столбцов
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

            # Установка высоты строк
            set_row_height(ws, '1:1', 40)  # Высота заголовков

            # Форматирование заголовков
            header_format = cellFormat(
                textFormat=textFormat(bold=True, fontSize=12),
                horizontalAlignment='CENTER',
                verticalAlignment='TOP',  # Добавлено вертикальное выравнивание
                backgroundColor=Color(0.8, 0.8, 0.8)  # Используем Color для задания цвета
            )
            format_cell_range(ws, 'A1:Y1', header_format)

            logger.info("Category products worksheet formatted.")
        except Exception as ex:
            # Логируем ошибку, если не удалось отформатировать лист продуктов
            logger.error("Error formatting category products worksheet.", ex, exc_info=True)
            raise
```