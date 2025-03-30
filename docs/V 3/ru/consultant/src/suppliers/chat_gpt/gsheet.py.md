## Анализ кода модуля `gsheet`

**Качество кода:**

- **Соответствие стандартам**: 6/10
- **Плюсы**:
  - Использование `logger` для логирования операций.
  - Наличие базовой структуры класса для работы с Google Sheets.
  - Разбиение на методы для выполнения конкретных задач (чтение, запись, удаление данных).
- **Минусы**:
  - Непоследовательное использование docstrings и комментариев.
  - Отсутствие аннотации типов для параметров и возвращаемых значений во многих методах.
  - Использование устаревших стилей кодирования (например, отсутствие пробелов вокруг операторов присваивания).
  - Смешение ответственности (класс выполняет и управление Google Sheets, и является частью AliExpress кампании).
  - Не везде используется `j_loads` или `j_loads_ns` для загрузки JSON-данных.

**Рекомендации по улучшению:**

1. **Документация**:
   - Добавить docstrings ко всем методам и классам, описывающие параметры, возвращаемые значения и возможные исключения.
   - Использовать единый стиль документирования (примеры приведены в инструкции).
   - В docstrings добавить примеры использования.

2. **Аннотация типов**:
   - Добавить аннотацию типов для всех параметров и возвращаемых значений методов. Это улучшит читаемость и поможет избежать ошибок.

3. **Форматирование кода**:
   - Привести код в соответствие со стандартами PEP8.
   - Использовать пробелы вокруг операторов присваивания.
   - Использовать одинарные кавычки для строк.

4. **Использование `j_loads` и `j_loads_ns`**:
   - Рассмотреть возможность использования `j_loads` или `j_loads_ns` для загрузки конфигурационных данных, если это применимо.

5. **Логирование**:
   - Убедиться, что все исключения логируются с использованием `logger.error` и включают `exc_info=True` для трассировки стека.

6. **Рефакторинг**:
   - Разделить класс на более мелкие, чтобы каждый класс выполнял только одну задачу.
   - Улучшить обработку ошибок, чтобы они были более информативными.

7. **Улучшение обработки данных**:
   - В методах `set_categories_worksheet` и `set_products_worksheet` добавить проверки на существование атрибутов в объектах `SimpleNamespace`, чтобы избежать ошибок при отсутствии данных.
   - В методе `get_categories_worksheet` добавить обработку исключений при преобразовании данных.

**Оптимизированный код:**

```python
## \file /src/suppliers/chat_gpt/gsheet.py
# -*- coding: utf-8 -*-

"""
Модуль для работы с Google Sheets в контексте AliExpress кампаний.
=================================================================

Модуль содержит класс :class:`GptGs`, который наследуется от :class:`SpreadSheet`
и предназначен для управления Google Sheets, записи данных о категориях и продуктах,
а также для форматирования листов.

Пример использования
----------------------

>>> gpt_gs = GptGs()
>>> campaign_data = gpt_gs.get_campaign_worksheet()
>>> if campaign_data:
...     print(f'Campaign Name: {campaign_data.name}')
"""

import time
from typing import List, Optional, Generator
from types import SimpleNamespace
from pathlib import Path

from gspread.worksheet import Worksheet

from src.goog.spreadsheet.spreadsheet import SpreadSheet
from src.utils.jjson import j_dumps
from src.utils.printer import pprint
from src.logger.logger import logger


class GptGs(SpreadSheet):
    """
    Класс для управления Google Sheets в AliExpress кампаниях.

    Наследуется от `SpreadSheet` для управления Google Sheets,
    записи данных о категориях и продуктах, а также форматирования листов.
    """

    def __init__(self) -> None:
        """
        Инициализирует AliCampaignGoogleSheet с указанным ID Google Sheets таблицы и дополнительными параметрами.
        """
        # Инициализация SpreadSheet с ID таблицы
        super().__init__('1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0')
        self.campaign = SimpleNamespace()

    def clear(self) -> None:
        """
        Очищает содержимое Google Sheets.
        Удаляет листы продуктов и очищает данные на листах категорий и других указанных листах.
        """
        try:
            self.delete_products_worksheets()
            # ws_to_clear = ['category','categories','campaign']
            # for ws in self.spreadsheet.worksheets():
            #     self.get_worksheet(ws).clear()
        except Exception as ex:
            logger.error('Ошибка очистки', ex, exc_info=True)

    def update_chat_worksheet(self, data: SimpleNamespace | dict | list, conversation_name: str, language: Optional[str] = None) -> None:
        """
        Записывает данные кампании в Google Sheets worksheet.

        Args:
            data (SimpleNamespace | dict | list): Объект SimpleNamespace или словарь с данными кампании для записи.
            conversation_name (str): Имя worksheet.
            language (Optional[str], optional): Опциональный параметр языка. Defaults to None.

        Raises:
            Exception: В случае ошибки при записи данных в worksheet.
        """
        try:
            ws: Worksheet = self.get_worksheet(conversation_name)
            _ = data.__dict__
            # Extract data from the SimpleNamespace attribute
            name =  _.get('name','')
            title =  _.get('title')
            description =  _.get('description')
            tags =  ', '.join(map(str, _.get('tags', [])))
            products_count =  _.get('products_count','~')

            # Prepare updates for the given SimpleNamespace object
            start_row = 2 #todo fix

            updates = [
                {'range': f'A{start_row}', 'values': [[name]]},
                {'range': f'B{start_row}', 'values': [[title]]},
                {'range': f'C{start_row}', 'values': [[description]]},
                {'range': f'D{start_row}', 'values': [[tags]]},
                {'range': f'E{start_row}', 'values': [[products_count]]},
            ]

            if updates:
                ws.batch_update(updates)
                logger.info(f"Category data written to \'{conversation_name}\' worksheet for {name}.")
                # Move to the next row

        except Exception as ex:
            logger.error('Error writing campaign data to worksheet.', ex, exc_info=True)
            raise

    def get_campaign_worksheet(self) -> SimpleNamespace:
        """
        Читает данные кампании из worksheet 'campaign'.

        Returns:
            SimpleNamespace: Объект SimpleNamespace с полями данных кампании.

        Raises:
            ValueError: Если worksheet 'campaign' не найден.
            Exception: В случае ошибки при чтении данных из worksheet.
        """
        try:
            ws: Worksheet = self.get_worksheet('campaign')
            if not ws:
                raise ValueError('Worksheet \'campaign\' not found.')

            data = ws.get_all_values()
            campaign_data = SimpleNamespace(
                name=data[0][1],
                title=data[1][1],
                language=data[2][1],
                currency=data[3][1],
                description=data[4][1]
            )

            logger.info('Campaign data read from \'campaign\' worksheet.')
            return campaign_data

        except Exception as ex:
            logger.error('Error getting campaign worksheet data.', ex, exc_info=True)
            raise

    def set_category_worksheet(self, category: SimpleNamespace | str) -> None:
        """
        Записывает данные из объекта SimpleNamespace в ячейки Google Sheets вертикально.

        Args:
            category (SimpleNamespace | str): Объект SimpleNamespace с полями данных для записи или имя категории.

        Raises:
            TypeError: Если передан не SimpleNamespace для category.
            Exception: В случае ошибки при записи данных в worksheet.
        """
        category = category if isinstance(category, SimpleNamespace) else self.get_campaign_category(category)
        try:
            ws: Worksheet = self.get_worksheet('category')

            if isinstance(category, SimpleNamespace):
                # Prepare data for vertical writing
                _ = category.__dict__
                vertical_data = [
                    ['Name', _.get('name','')],
                    ['Title', _.get('title','')],
                    ['Description', _.get('description')],
                    ['Tags', ', '.join(map(str, _.get('tags', [])))],
                    ['Products Count', _.get('products_count', '~')]
                ]

                # Write data vertically
                ws.update('A1:B{}'.format(len(vertical_data)), vertical_data)

                logger.info('Category data written to \'category\' worksheet vertically.')
            else:
                raise TypeError('Expected SimpleNamespace for category.')

        except Exception as ex:
            logger.error('Error setting category worksheet.', ex, exc_info=True)
            raise

    def get_category_worksheet(self) -> SimpleNamespace:
        """
        Читает данные категории из worksheet 'category'.

        Returns:
            SimpleNamespace: Объект SimpleNamespace с полями данных категории.

        Raises:
            ValueError: Если worksheet 'category' не найден.
            Exception: В случае ошибки при чтении данных из worksheet.
        """
        try:
            ws: Worksheet = self.get_worksheet('category')
            if not ws:
                raise ValueError('Worksheet \'category\' not found.')

            data = ws.get_all_values()
            category_data = SimpleNamespace(
                name=data[1][1],
                title=data[2][1],
                description=data[3][1],
                tags=data[4][1].split(', '),
                products_count=int(data[5][1])
            )

            logger.info('Category data read from \'category\' worksheet.')
            return category_data

        except Exception as ex:
            logger.error('Error getting category worksheet data.', ex, exc_info=True)
            raise

    def set_categories_worksheet(self, categories: SimpleNamespace) -> None:
        """
        Записывает данные из объекта SimpleNamespace в ячейки Google Sheets.

        Args:
            categories (SimpleNamespace): Объект SimpleNamespace с полями данных для записи.

        Raises:
            Exception: В случае ошибки при записи данных в worksheet.
        """
        ws: Worksheet = self.get_worksheet('categories')
        # ws.clear()  # Clear the 'categories' worksheet

        try:
            # Initialize the starting row
            start_row = 2

            # Iterate over all attributes of the categories object
            for attr_name in dir(categories):
                attr_value = getattr(categories, attr_name, None)

                # Skip non-SimpleNamespace attributes or attributes with no data
                if not isinstance(attr_value, SimpleNamespace) or not any(
                    hasattr(attr_value, field) for field in ['name', 'title', 'description', 'tags', 'products_count']
                ):
                    continue
                _ = attr_value.__dict__
                # Extract data from the SimpleNamespace attribute
                name =  _.get('name','')
                title =  _.get('title')
                description =  _.get('description')
                tags =  ', '.join(map(str, _.get('tags', [])))
                products_count =  _.get('products_count','~')

                # Prepare updates for the given SimpleNamespace object
                updates = [
                    {'range': f'A{start_row}', 'values': [[name]]},
                    {'range': f'B{start_row}', 'values': [[title]]},
                    {'range': f'C{start_row}', 'values': [[description]]},
                    {'range': f'D{start_row}', 'values': [[tags]]},
                    {'range': f'E{start_row}', 'values': [[products_count]]},
                ]

                # Perform batch update
                if updates:
                    ws.batch_update(updates)
                    logger.info(f"Category data written to \'categories\' worksheet for {attr_name}.")

                # Move to the next row
                start_row += 1

        except Exception as ex:
            logger.error('Error setting categories worksheet.', ex, exc_info=True)
            raise

    def get_categories_worksheet(self) -> List[List[str]]:
        """
        Читает данные из столбцов A по E, начиная со второй строки, из worksheet 'categories'.

        Returns:
            List[List[str]]: Список строк с данными из столбцов A по E.

        Raises:
            ValueError: Если worksheet 'categories' не найден.
            Exception: В случае ошибки при чтении данных из worksheet.
        """
        try:
            ws: Worksheet = self.get_worksheet('categories')
            if not ws:
                raise ValueError('Worksheet \'categories\' not found.')

            # Read all values from the worksheet
            data = ws.get_all_values()

            # Extract data from columns A to E, starting from the second row
            data = [row[:5] for row in data[1:] if len(row) >= 5]

            logger.info('Category data read from \'categories\' worksheet.')
            return data

        except Exception as ex:
            logger.error('Error getting category data from worksheet.', ex, exc_info=True)
            raise

    def set_product_worksheet(self, product: SimpleNamespace | str, category_name: str) -> None:
        """
        Записывает данные продукта в новый Google Sheets spreadsheet.

        Args:
            category_name (str): Имя категории.
            product (SimpleNamespace): Объект SimpleNamespace с полями данных продукта для записи.

        Raises:
            Exception: В случае ошибки при обновлении данных продукта в worksheet.
        """
        time.sleep(10)
        ws = self.copy_worksheet('product_template', category_name)  # Copy 'product_template' to new worksheet
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
            ws.update('A1:Y1', [headers])

            _ = product.__dict__
            row_data = [
                str(_.get('product_id')),
                str(_.get('app_sale_price')),
                str(_.get('original_price')),
                str(_.get('sale_price')),
                str(_.get('discount')),
                str(_.get('product_main_image_url')),
                str(_.get('local_image_path')),
                ', '.join(map(str, _.get('product_small_image_urls', []))),
                str(_.get('product_video_url')),
                str(_.get('local_video_path')),
                str(_.get('first_level_category_id')),
                str(_.get('first_level_category_name')),
                str(_.get('second_level_category_id')),
                str(_.get('second_level_category_name')),
                str(_.get('target_sale_price')),
                str(_.get('target_sale_price_currency')),
                str(_.get('target_app_sale_price_currency')),
                str(_.get('target_original_price_currency')),
                str(_.get('original_price_currency')),
                str(_.get('product_title')),
                str(_.get('evaluate_rate')),
                str(_.get('promotion_link')),
                str(_.get('shop_url')),
                str(_.get('shop_id')),
                ', '.join(map(str, _.get('tags', [])))
            ]

            ws.update('A2:Y2', [row_data])  # Update row data in a single row

            logger.info('Product data written to worksheet.')
        except Exception as ex:
            logger.error('Error updating product data in worksheet.', ex, exc_info=True)
            raise

    def get_product_worksheet(self) -> SimpleNamespace:
        """
        Читает данные продукта из worksheet 'products'.

        Returns:
            SimpleNamespace: Объект SimpleNamespace с полями данных продукта.

        Raises:
            ValueError: Если worksheet 'products' не найден.
            Exception: В случае ошибки при чтении данных из worksheet.
        """
        try:
            ws: Worksheet = self.get_worksheet('products')
            if not ws:
                raise ValueError('Worksheet \'products\' not found.')

            data = ws.get_all_values()
            product_data = SimpleNamespace(
                id=data[1][1],
                name=data[2][1],
                title=data[3][1],
                description=data[4][1],
                tags=data[5][1].split(', '),
                price=float(data[6][1])
            )

            logger.info('Product data read from \'products\' worksheet.')
            return product_data

        except Exception as ex:
            logger.error('Error getting product worksheet data.', ex, exc_info=True)
            raise

    def set_products_worksheet(self, category_name: str) -> None:
        """
        Записывает данные из списка объектов SimpleNamespace в ячейки Google Sheets.

        Args:
            category_name (str): Имя категории.

        Raises:
            Exception: В случае ошибки при записи данных в worksheet.
        """
        if category_name:
            category_ns: SimpleNamespace = getattr(self.campaign.category, category_name)
            products_ns: SimpleNamespace = category_ns.products
        else:
            logger.warning(f'На ашел товары в {pprint(category_ns)}')
            return
        ws: Worksheet = self.get_worksheet(category_name)

        try:
            updates: list = []
            for index, value in enumerate(products_ns, start=2):
                _ = value.__dict__
                updates.append({'range': f'A{index}', 'values': [[str(_.get('product_id', ''))]]})
                updates.append({'range': f'B{index}', 'values': [[str(_.get('product_title', ''))]]})
                updates.append({'range': f'C{index}', 'values': [[str(_.get('title', ''))]]})
                updates.append({'range': f'D{index}', 'values': [[str(_.get('local_image_path', ''))]]})
                updates.append({'range': f'D{index}', 'values': [[str(_.get('product_video_url', ''))]]})
                updates.append({'range': f'F{index}', 'values': [[str(_.get('original_price', ''))]]})
                updates.append({'range': f'F{index}', 'values': [[str(_.get('app_sale_price', ''))]]})
                updates.append({'range': f'F{index}', 'values': [[str(_.get('target_sale_price', ''))]]})
                updates.append({'range': f'F{index}', 'values': [[str(_.get('target_sale_price', ''))]]})

            ws.batch_update(updates)
            logger.info('Products data written to \'products\' worksheet.')

        except Exception as ex:
            logger.error('Error setting products worksheet.', ex, exc_info=True)
            raise

    def delete_products_worksheets(self) -> None:
        """
        Удаляет все листы из Google Sheets spreadsheet, кроме 'categories' и 'product_template'.

        Raises:
            Exception: В случае ошибки при удалении worksheets.
        """
        excluded_titles = {'categories', 'product', 'category', 'campaign'}
        try:
            worksheets = self.spreadsheet.worksheets()
            for sheet in worksheets:
                if sheet.title not in excluded_titles:
                    self.spreadsheet.del_worksheet_by_id(sheet.id)
                    logger.success(f"Worksheet '{sheet.title}' deleted.")
        except Exception as ex:
            logger.error('Error deleting all worksheets.', ex, exc_info=True)
            raise

    def save_categories_from_worksheet(self, update: bool = False) -> None:
        """
        Сохраняет данные, отредактированные в гугл таблице.

        Args:
            update (bool, optional): Флаг для обновления кампании. Defaults to False.
        """
        edited_categories: list[dict] = self.get_categories_worksheet()
        _categories_ns: SimpleNamespace = SimpleNamespace()
        for _cat in edited_categories:
            _cat_ns: SimpleNamespace = SimpleNamespace(**{
                'name': _cat[0],
                'title': _cat[1],
                'description': _cat[2],
                'tags': _cat[3].split(","),
                'products_count': _cat[4],
            }
            )
            setattr(_categories_ns, _cat_ns.name, _cat_ns)
        ...
        self.campaign.category = _categories_ns
        if update:
            self.update_campaign()

    def save_campaign_from_worksheet(self) -> None:
        """Сохраняет рекламную кампанию."""
        self.save_categories_from_worksheet(False)
        data = self.get_campaign_worksheet()
        data.category = self.campaign.category
        self.campaign = data
        self.update_campaign()
        ...