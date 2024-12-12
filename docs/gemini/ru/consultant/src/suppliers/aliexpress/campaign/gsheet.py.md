# Анализ кода модуля `gsheet.py`

**Качество кода: 7/10**
-   **Плюсы:**
    -   Используется `logger` для логирования ошибок и информационных сообщений.
    -   Класс `AliCampaignGoogleSheet` наследуется от `SpreadSheet`, что способствует переиспользованию кода.
    -   Код разбит на методы, что улучшает читаемость и поддержку.
    -   Присутствует базовая обработка исключений.
    -   Используется `SimpleNamespace` для хранения данных.
-   **Минусы:**
    -   Отсутствует docstring для модуля.
    -   Не все функции и методы имеют подробные docstring с описанием параметров и возвращаемых значений в формате RST.
    -   В некоторых местах используется `try-except` без необходимости, что усложняет код.
    -   Используется `str(_.get(...))` для преобразования всех значений к строке, что может привести к ошибкам.
    -   Используются магические значения (например, `'A1:Y1'`, `'A1:E1'`), которые лучше вынести в константы.
    -   Некоторые методы имеют избыточную логику (например, дублирование кода в методах установки категорий и продуктов).
    -   Много повторяющегося кода для установки ширины столбцов, что можно вынести в отдельную функцию.
    -   Не везде используется f-строки для форматирования строк.
    -   Используется `time.sleep(10)` что является плохой практикой, необходимо пересмотреть этот метод
    -   Не всегда понятно назначение некоторых переменных.
    -   Присутсвует неиспользуемый импорт `from types import SimpleNamespace`, который следует удалить

**Рекомендации по улучшению:**

1.  **Документирование:**
    -   Добавить docstring для модуля в формате RST.
    -   Добавить docstring для каждого метода и функции в формате RST с подробным описанием параметров, возвращаемых значений и исключений.

2.  **Обработка ошибок:**
    -   Упростить обработку ошибок, заменив избыточные `try-except` блоки на использование `logger.error` с `exc_info=True`.
    -   Убрать лишние `raise` после логирования ошибки.

3.  **Рефакторинг:**
    -   Вынести повторяющиеся блоки кода для форматирования таблиц в отдельные функции.
    -   Избавиться от дублирования кода в `set_categories_worksheet` и `set_category_products`.
    -   Использовать константы для магических значений (например, диапазоны ячеек).
    -   Использовать f-строки для форматирования строк, где это возможно.
    -   Пересмотреть и удалить `time.sleep(10)`

4.  **Улучшение кода:**
    -   Удалить неиспользуемые импорты.
    -   Убрать лишние преобразования типов.
    -   Использовать более понятные имена переменных.
    -   Добавить проверки на наличие необходимых атрибутов в объектах.
    -   Добавить проверку типов для входных аргументов.
    -   Улучшить форматирование кода для соответствия PEP 8.

5.  **Безопасность:**
    -   Проверить, что все данные, которые записываются в Google Sheets, корректно обрабатываются и не содержат потенциально опасных символов.

**Оптимизированный код:**

```python
"""
Модуль для работы с Google Sheets в рамках рекламных кампаний AliExpress.
======================================================================

Этот модуль предоставляет класс :class:`AliCampaignGoogleSheet`, который
наследует функциональность :class:`src.goog.spreadsheet.spreadsheet.SpreadSheet`
и расширяет ее методами для управления данными, специфичными для кампаний AliExpress.
Он включает в себя методы для записи данных о кампаниях, категориях и продуктах,
а также для форматирования таблиц Google Sheets.

Пример использования
--------------------

.. code-block:: python

    campaign_sheet = AliCampaignGoogleSheet(campaign_name='Test Campaign')
    campaign_sheet.set_campaign_worksheet(campaign_data)
    campaign_sheet.set_categories_worksheet(categories_data)
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

import time
from typing import Optional, Any, List, Dict
from types import SimpleNamespace
from gspread.worksheet import Worksheet
from src.goog.spreadsheet.spreadsheet import SpreadSheet
# from src.utils.jjson import j_dumps
from src.utils.printer import pprint
from src.logger.logger import logger
from src.ai.openai import translate
# from gspread_formatting import (
#     cellFormat,
#     textFormat,
#     numberFormat,
#     format_cell_range,
#     set_column_width,
#     set_row_height,
#     Color
# )

# from src.goog.spreadsheet.spreadsheet import SpreadSheet

# from src.utils.printer import pprint
# from src.logger.logger import logger

MODE = 'dev'


class AliCampaignGoogleSheet(SpreadSheet):
    """
    Класс для работы с Google Sheets в рамках кампаний AliExpress.

    Наследует класс :class:`src.goog.spreadsheet.spreadsheet.SpreadSheet` и предоставляет
    дополнительные методы для управления листами Google Sheets, записи данных о категориях
    и продуктах, и форматирования листов.
    """

    SPREADSHEET_ID = '1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0'
    WORKSHEET_CATEGORIES = 'categories'
    WORKSHEET_PRODUCT_TEMPLATE = 'product'
    WORKSHEET_CAMPAIGN = 'campaign'
    PRODUCT_HEADERS = [
        'product_id', 'app_sale_price', 'original_price', 'sale_price', 'discount',
        'product_main_image_url', 'local_saved_image', 'product_small_image_urls',
        'product_video_url', 'local_saved_video', 'first_level_category_id',
        'first_level_category_name', 'second_level_category_id', 'second_level_category_name',
        'target_sale_price', 'target_sale_price_currency', 'target_app_sale_price_currency',
        'target_original_price_currency', 'original_price_currency', 'product_title',
        'evaluate_rate', 'promotion_link', 'shop_url', 'shop_id', 'tags'
    ]
    CATEGORY_HEADERS = ['Name', 'Title', 'Description', 'Tags', 'Products Count']

    def __init__(self, campaign_name: str, language: Optional[str | dict] = None, currency: Optional[str] = None):
        """
        Инициализирует `AliCampaignGoogleSheet` с заданным ID Google Sheets и дополнительными параметрами.

        :param campaign_name: Название кампании.
        :type campaign_name: str
        :param language: Язык для кампании.
        :type language: Optional[str | dict]
        :param currency: Валюта для кампании.
        :type currency: Optional[str]
        """
        # Инициализирует родительский класс SpreadSheet с ID таблицы
        super().__init__(spreadsheet_id=self.SPREADSHEET_ID)
        # self.capmaign_editor = AliCampaignEditor(campaign_name=campaign_name, language=language, currency=currency)
        # if campaign_editor:
        #     self.set_campaign_worksheet(campaign_editor.campaign)
        #     self.set_categories_worksheet(campaign_editor.campaign.category)

    def clear(self):
        """
        Очищает содержимое, удаляя листы продуктов и очищая данные на листах категорий и других указанных листах.
        """
        try:
            # Код исполняет удаление листов продуктов
            self.delete_products_worksheets()
        except Exception as ex:
            logger.error('Ошибка очистки', ex, exc_info=True)
            ...
        
    def delete_products_worksheets(self):
        """
         Удаляет все листы из таблицы Google Sheets, кроме 'categories', 'product', 'category' и 'campaign'.
        """
        excluded_titles = {self.WORKSHEET_CATEGORIES, self.WORKSHEET_PRODUCT_TEMPLATE, 'category', self.WORKSHEET_CAMPAIGN}
        try:
            worksheets = self.spreadsheet.worksheets()
            for sheet in worksheets:
                if sheet.title not in excluded_titles:
                     # Код исполняет удаление листа
                    self.spreadsheet.del_worksheet_by_id(sheet.id)
                    logger.success(f"Лист '{sheet.title}' удален.")
        except Exception as ex:
            logger.error("Ошибка удаления всех листов.", ex, exc_info=True)
            ...
            
    def set_campaign_worksheet(self, campaign: SimpleNamespace):
        """
        Записывает данные кампании в лист Google Sheets.

        :param campaign: Объект SimpleNamespace с данными кампании.
        :type campaign: SimpleNamespace
        """
        try:
            # Код исполняет получение листа кампании
            ws: Worksheet = self.get_worksheet(self.WORKSHEET_CAMPAIGN)
            
            # Подготавливает данные для вертикальной записи
            updates = []
            vertical_data = [
                ('A1', 'Campaign Name', campaign.campaign_name),
                ('A2', 'Campaign Title', campaign.title),
                ('A3', 'Campaign Language', campaign.language),
                ('A4', 'Campaign Currency', campaign.currency),
                ('A5', 'Campaign Description', campaign.description),
            ]

            # Добавляет операции обновления в список batch_update
            for cell, header, value in vertical_data:
                updates.append({'range': cell, 'values': [[header]]})
                updates.append({'range': f'B{cell[1]}', 'values': [[str(value)]]})
            
            # Код исполняет пакетное обновление данных в листе
            if updates:
                ws.batch_update(updates)

            logger.info("Данные кампании записаны на лист 'campaign' вертикально.")

        except Exception as ex:
            logger.error("Ошибка установки листа кампании.", ex, exc_info=True)
            ...


    def set_products_worksheet(self, category_name: str):
        """
        Записывает данные продуктов в лист Google Sheets.

        :param category_name: Название категории, из которой необходимо получить продукты.
        :type category_name: str
        """
        if category_name:
            # Код исполняет получение объекта категории из self.editor.campaign.category
            category: SimpleNamespace = getattr(self.editor.campaign.category, category_name)
            products: list[SimpleNamespace] = category.products
        else:
            logger.warning(f"Продукты не найдены для {category=}\\n{products=}.")
            return
        # Код исполняет копирование листа продукта и его переименование
        ws = self.copy_worksheet(self.WORKSHEET_PRODUCT_TEMPLATE, category_name)

        try:
           # Код исполняет подготовку данных для записи в лист
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
            # Код исполняет запись данных по продуктам
            for index, row in enumerate(row_data, start=2):
                ws.update(f'A{index}:Y{index}', [row])
                logger.info(f"Продукты {str(_.get('product_id'))} обновлены.")
            # Код исполняет форматирование листа продуктов
            self._format_category_products_worksheet(ws)

            logger.info("Продукты обновлены в листе.")

        except Exception as ex:
            logger.error("Ошибка установки листа продуктов.", ex, exc_info=True)
            ...

    def set_categories_worksheet(self, categories: SimpleNamespace):
        """
        Записывает данные категорий из объекта SimpleNamespace в ячейки Google Sheets.

        :param categories: Объект, где ключи — это категории с данными для записи.
        :type categories: SimpleNamespace
        """
        # Код исполняет получение рабочего листа категорий
        ws: Worksheet = self.get_worksheet(self.WORKSHEET_CATEGORIES)
        ws.clear()  # Очистка рабочего листа перед записью данных

        try:
            # Код исполняет получение всех ключей (категорий) и соответствующих значений
            category_data = categories.__dict__

            # Проверка, что все объекты категории имеют необходимые атрибуты
            required_attrs = ['name', 'title', 'description', 'tags', 'products_count']

            if all(all(hasattr(category, attr) for attr in required_attrs) for category in category_data.values()):
                # Код исполняет запись заголовков в лист
                ws.update('A1:E1', [self.CATEGORY_HEADERS])

                # Код исполняет подготовку данных для записи
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

                # Код исполняет обновление строк данных
                ws.update(f'A2:E{1 + len(rows)}', rows)

                # Код исполняет форматирование листа
                self._format_categories_worksheet(ws)

                logger.info("Поля категорий обновлены из объекта SimpleNamespace.")
            else:
                logger.warning("Один или несколько объектов категорий не содержат всех необходимых атрибутов.")
                ...

        except Exception as ex:
            logger.error("Ошибка обновления полей из объекта SimpleNamespace.", ex, exc_info=True)
            ...

    def get_categories(self) -> List[Dict[str, Any]]:
        """
         Получает данные из таблицы Google Sheets.

        :return: Данные из таблицы в виде списка словарей.
        :rtype: List[Dict[str, Any]]
        """
        # Код исполняет получение листа категорий
        ws = self.get_worksheet(self.WORKSHEET_CATEGORIES)
        # Код исполняет получение всех записей
        data = ws.get_all_records()
        logger.info("Данные категорий получены из листа.")
        return data

    def set_category_products(self, category_name: str, products: list[dict]):
        """
         Записывает данные о продуктах в новый лист Google Sheets.

        :param category_name: Название категории.
        :type category_name: str
        :param products: Список словарей с данными о продуктах.
        :type products: list[dict]
        """
        if category_name:
            # Код исполняет получение объекта категории из self.editor.campaign.category
            category_ns: SimpleNamespace = getattr(self.editor.campaign.category, category_name)
            products_ns: list[SimpleNamespace] = category_ns.products
        else:
            logger.warning("Продукты не найдены для категории.")
            return
        # Код исполняет копирование листа продукта
        ws = self.copy_worksheet(self.WORKSHEET_PRODUCT_TEMPLATE, category_name)
        try:
            # Код исполняет запись заголовков
            ws.update('A1:Y1', [self.PRODUCT_HEADERS])

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
            # Код исполняет обновление строк с данными по продуктам
            for index, row in enumerate(row_data, start=2):
                ws.update(f'A{index}:Y{index}', [row])
                logger.info(f"Продукты {str(_.get('product_id'))} обновлены.")

            # Код исполняет форматирование листа продуктов
            self._format_category_products_worksheet(ws)
            logger.info("Продукты обновлены в листе.")

        except Exception as ex:
            logger.error("Ошибка обновления продуктов в листе.", ex, exc_info=True)
            ...

    def _format_categories_worksheet(self, ws: Worksheet):
        """
        Форматирует лист 'categories'.

        :param ws: Лист Google Sheets для форматирования.
        :type ws: Worksheet
        """
        try:
            # Установка ширины столбцов
            self._set_column_width(ws, {'A': 150, 'B': 200, 'C': 300, 'D': 200, 'E': 150})

            # Установка высоты строк
            self._set_row_height(ws, '1:1', 40)

            # Форматирование заголовков
            header_format = self._create_header_format()
            self._format_cell_range(ws, 'A1:E1', header_format)

            logger.info("Лист категорий отформатирован.")
        except Exception as ex:
            logger.error("Ошибка форматирования листа категорий.", ex, exc_info=True)
            ...


    def _format_category_products_worksheet(self, ws: Worksheet):
        """
        Форматирует лист с продуктами категории.

        :param ws: Лист Google Sheets для форматирования.
        :type ws: Worksheet
        """
        try:
           # Установка ширины столбцов
            self._set_column_width(ws, {
                'A': 250, 'B': 220, 'C': 220, 'D': 220, 'E': 200,
                'F': 200, 'G': 200, 'H': 200, 'I': 200, 'J': 200,
                'K': 200, 'L': 200, 'M': 200, 'N': 200, 'O': 200,
                'P': 200, 'Q': 200, 'R': 200, 'S': 200, 'T': 200,
                'U': 200, 'V': 200, 'W': 200, 'X': 200, 'Y': 200
            })

            # Установка высоты строк
            self._set_row_height(ws, '1:1', 40)

            # Форматирование заголовков
            header_format = self._create_header_format(vertical_alignment='TOP')
            self._format_cell_range(ws, 'A1:Y1', header_format)

            logger.info("Лист продуктов категории отформатирован.")
        except Exception as ex:
            logger.error("Ошибка форматирования листа продуктов категории.", ex, exc_info=True)
            ...

    def _create_header_format(self, vertical_alignment='MIDDLE'):
        """
        Создает формат для заголовков.

        :param vertical_alignment: Вертикальное выравнивание текста.
        :type vertical_alignment: str
        :return: Объект cellFormat.
        :rtype: cellFormat
        """
        from gspread_formatting import cellFormat, textFormat, Color
        return cellFormat(
            textFormat=textFormat(bold=True, fontSize=12),
            horizontalAlignment='CENTER',
            verticalAlignment=vertical_alignment,
            backgroundColor=Color(0.8, 0.8, 0.8)
        )

    def _set_column_width(self, ws: Worksheet, columns: dict):
        """
         Устанавливает ширину столбцов в листе Google Sheets.

        :param ws: Лист Google Sheets.
        :type ws: Worksheet
        :param columns: Словарь, где ключ — буква столбца, а значение — его ширина.
        :type columns: dict
        """
        from gspread_formatting import set_column_width
        for column, width in columns.items():
            set_column_width(ws, f'{column}:{column}', width)

    def _set_row_height(self, ws: Worksheet, row_range: str, height: int):
         """
        Устанавливает высоту строк в листе Google Sheets.

        :param ws: Лист Google Sheets.
        :type ws: Worksheet
        :param row_range: Диапазон строк для установки высоты.
        :type row_range: str
        :param height: Высота строк.
        :type height: int
        """
        from gspread_formatting import set_row_height
        set_row_height(ws, row_range, height)

    def _format_cell_range(self, ws: Worksheet, cell_range: str, cell_format):
         """
         Форматирует диапазон ячеек в листе Google Sheets.

        :param ws: Лист Google Sheets.
        :type ws: Worksheet
        :param cell_range: Диапазон ячеек для форматирования.
        :type cell_range: str
        :param cell_format: Формат ячеек.
        :type cell_format: cellFormat
        """
        from gspread_formatting import format_cell_range
        format_cell_range(ws, cell_range, cell_format)


    # def set_category_products(self, category_name: str, products: dict):
    #     """ Write product data to a new Google Sheets spreadsheet.
    #     @param category_name Category name.
    #     @param products Dictionary with product data.
    #     """
    #     time.sleep(10)
    #     ws = self.copy_worksheet('product_template', category_name)  # Copy 'product_template' to new worksheet
    #     try:
    #         headers = [
    #             'product_id', 'app_sale_price', 'original_price', 'sale_price', 'discount',
    #             'product_main_image_url', 'local_saved_image', 'product_small_image_urls',
    #             'product_video_url', 'local_saved_video', 'first_level_category_id',
    #             'first_level_category_name', 'second_level_category_id', 'second_level_category_name',
    #             'target_sale_price', 'target_sale_price_currency', 'target_app_sale_price_currency',
    #             'target_original_price_currency', 'original_price_currency', 'product_title',
    #             'evaluate_rate', 'promotion_link', 'shop_url', 'shop_id', 'tags'
    #         ]
    #         ws.update('A1:Y1', [headers])

    #         updates = []
    #         for index, product in enumerate(products, start=2):
    #             _ = product.__dict__
    #             row_data = [
    #                 str(_.get('product_id')),
    #                 str(_.get('app_sale_price')),
    #                 str(_.get('original_price')),
    #                 str(_.get('sale_price')),
    #                 str(_.get('discount')),
    #                 str(_.get('product_main_image_url')),
    #                 str(_.get('local_saved_image')),
    #                 ', '.join(map(str, _.get('product_small_image_urls', []))),
    #                 str(_.get('product_video_url')),
    #                 str(_.get('local_saved_video')),
    #                 str(_.get('first_level_category_id')),
    #                 str(_.get('first_level_category_name')),
    #                 str(_.get('second_level_category_id')),
    #                 str(_.get('second_level_category_name')),
    #                 str(_.get('target_sale_price')),
    #                 str(_.get('target_sale_price_currency')),
    #                 str(_.get('target_app_sale_price_currency')),
    #                 str(_.get('target_original_price_currency')),
    #                 str(_.get('original_price_currency')),
    #                 str(_.get('product_title')),
    #                 str(_.get('evaluate_rate')),
    #                 str(_.get('promotion_link')),
    #                 str(_.get('shop_url')),
    #                 str(_.get('shop_id')),
    #                 ', '.join(map(str, _.get('tags', [])))
    #             ]
    #             updates.append({
    #                 'range': f'A{index}:Y{index}',
    #                 'values': [row_data]
    #             })
            
    #         ws.batch_update(updates)

    #         logger.info("Products updated in worksheet.")
    #     except Exception as ex:
    #         logger.error("Error updating products in worksheet.", ex, exc_info=True)
    #         raise
```