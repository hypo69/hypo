### Анализ кода модуля `gsheet`

**Качество кода**:
- **Соответствие стандартам**: 6/10
- **Плюсы**:
    - Код разбит на функции, что улучшает читаемость и поддержку.
    - Используется класс `SimpleNamespace` для представления данных, что упрощает работу с атрибутами.
    - Присутствует логирование ошибок с использованием `logger.error`.
- **Минусы**:
    - Не везде используется `logger.error` с параметром `exc_info=True` для более детального логирования ошибок.
    - Есть `time.sleep(10)` без объяснения причины, что может привести к задержкам.
    - Много дублирования кода в `set_` и `get_` методах, особенно в части работы с `SimpleNamespace`.
    - Не всегда используется `j_dumps` или `j_loads`, как указано в требованиях.
    - Отсутствуют RST комментарии для многих функций и классов.
    - Есть неявные зависимости от глобального `self.campaign`, что может вызвать проблемы при рефакторинге.

**Рекомендации по улучшению**:

1.  **Форматирование:**
    *   Использовать одинарные кавычки для строк, как требуется в инструкции.
    *   Выровнять импорты, переменные и названия функций в соответствии с ранее обработанными файлами.
2.  **Логирование**:
    *   Использовать `logger.error(..., exc_info=True)` во всех блоках `except` для более полного логирования ошибок.
    *   Убрать `print` и заменить на `logger.info`.
    *   Импортировать `logger` из `src.logger.logger`.
3.  **Обработка данных**:
    *   Использовать `j_dumps` или `j_loads` из `src.utils.jjson` вместо `json.load`.
    *   Убедиться, что все `...` в коде остаются неизменными.
4.  **Рефакторинг**:
    *   Устранить дублирование кода в `set_` и `get_` методах, вынеся общую логику в отдельные функции.
    *   Убрать `time.sleep(10)` или добавить комментарий о причине использования задержки.
    *   Добавить RST комментарии для всех функций, методов и классов.
    *   Пересмотреть использование `self.campaign` и сделать его более явным.
    *   Переписать все `try ... except` блоки с использованием `logger.error` и `raise`, чтобы обрабатывать исключения в вызывающем коде.
5.  **Документация**:
    *   Добавить описание модуля в формате RST.
    *   Улучшить документацию функций, используя RST-формат с описанием параметров, возвращаемых значений и примерами.
6.  **Общее**:
    *   Следовать стандартам PEP8 для форматирования.
    *   Избегать неясных формулировок в комментариях.

**Оптимизированный код**:

```python
# -*- coding: utf-8 -*-

"""
Модуль для работы с Google Sheets в контексте AliExpress кампаний.
===================================================================

Модуль предоставляет класс :class:`GptGs`, который наследуется от :class:`SpreadSheet`
и используется для управления Google Sheets, записи данных о категориях и продуктах, а также
для форматирования листов.

Пример использования
--------------------
.. code-block:: python

    gs = GptGs()
    gs.clear()
    campaign_data = gs.get_campaign_worksheet()
"""
import time
from types import SimpleNamespace
from typing import List
from pathlib import Path
from gspread.worksheet import Worksheet

from src.goog.spreadsheet.spreadsheet import SpreadSheet
from src.utils.jjson import j_dumps
from src.logger.logger import logger  # Исправлено: импорт logger
from src.utils.printer import pprint  # Исправлено: импорт pprint


class GptGs(SpreadSheet):
    """
    Класс для управления Google Sheets в контексте AliExpress кампаний.

    Наследуется от :class:`SpreadSheet` для управления Google Sheets, записи
    данных о категориях и продуктах, а также для форматирования листов.
    """
    def __init__(self):
        """
        Инициализирует экземпляр класса GptGs.

        Устанавливает ID Google Sheets таблицы.
        """
        super().__init__('1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0') #  Initialize SpreadSheet with the spreadsheet ID

    def clear(self) -> None:
        """
        Очищает содержимое Google Sheets.

        Удаляет листы с продуктами и очищает данные на листах
        категорий и других указанных листах.
        """
        try:
            self.delete_products_worksheets() # Delete product sheets
            # ws_to_clear = ['category','categories','campaign'] # delete ws list
            # for ws in self.spreadsheet.worksheets():
            #     self.get_worksheet(ws).clear()
        except Exception as ex:
            logger.error('Ошибка очистки', exc_info=True) #  Error log and show exc

    def update_chat_worksheet(self, data: SimpleNamespace | dict | list, conversation_name: str, language: str = None) -> None:
        """
        Записывает данные кампании в лист Google Sheets.

        :param data: Данные для записи в виде SimpleNamespace, dict или list.
        :type data: SimpleNamespace | dict | list
        :param conversation_name: Имя листа для записи.
        :type conversation_name: str
        :param language: Необязательный параметр языка.
        :type language: str, optional
        :raises Exception: В случае ошибки при записи данных.
        """
        try:
            ws: Worksheet = self.get_worksheet(conversation_name) # Get a worksheet

            if isinstance(data, SimpleNamespace):
                _ = data.__dict__
            elif isinstance(data, dict):
                _ = data
            elif isinstance(data, list):
                _ = data[0]
            else:
                 raise TypeError(f'Expected SimpleNamespace, dict or list, but got {type(data)}') # show TypeError

            name =  _.get('name', '') # get name
            title =  _.get('title') # get title
            description =  _.get('description') # get description
            tags =  ', '.join(map(str, _.get('tags', []))) # get tags
            products_count =  _.get('products_count', '~') # get products_count

            # Prepare updates for the given SimpleNamespace object
            updates = [
                {'range': f'A1', 'values': [[name]]},
                {'range': f'B1', 'values': [[title]]},
                {'range': f'C1', 'values': [[description]]},
                {'range': f'D1', 'values': [[tags]]},
                {'range': f'E1', 'values': [[products_count]]},
            ]
            ws.batch_update(updates)  # Write data to a worksheet
        except Exception as ex:
            logger.error('Error writing campaign data to worksheet.', exc_info=True) #  Error log and show exc
            raise

    def get_campaign_worksheet(self) -> SimpleNamespace:
        """
        Считывает данные кампании с листа 'campaign'.

        :return: Объект SimpleNamespace с данными кампании.
        :rtype: SimpleNamespace
        :raises ValueError: Если лист 'campaign' не найден.
        :raises Exception: В случае ошибки при чтении данных.
        """
        try:
            ws: Worksheet = self.get_worksheet('campaign')  # Get a worksheet
            if not ws:
                raise ValueError("Worksheet 'campaign' not found.") # show ValueError
            
            data = ws.get_all_values() # Get all values
            campaign_data = SimpleNamespace(
                name=data[0][1], # get name
                title=data[1][1], # get title
                language=data[2][1], # get language
                currency=data[3][1], # get currency
                description=data[4][1] # get description
            )
            
            logger.info("Campaign data read from 'campaign' worksheet.") #  Log info
            return campaign_data # Return SimpleNamespace data
        except Exception as ex:
            logger.error('Error getting campaign worksheet data.', exc_info=True) # Error log and show exc
            raise

    def set_category_worksheet(self, category: SimpleNamespace | str) -> None:
        """
        Записывает данные категории в лист 'category' вертикально.

        :param category: Объект SimpleNamespace с данными категории или название категории.
        :type category: SimpleNamespace | str
        :raises TypeError: Если передан не SimpleNamespace для категории.
        :raises Exception: В случае ошибки при записи данных.
        """
        category = category if isinstance(category, SimpleNamespace) else self.get_campaign_category(category) # Check type
        try:
            ws: Worksheet = self.get_worksheet('category') # Get a worksheet

            if isinstance(category, SimpleNamespace):
                # Prepare data for vertical writing
                _ = category.__dict__ # Get dict from SimpleNamespace
                vertical_data = [
                    ['Name', _.get('name', '')], # Get name
                    ['Title', _.get('title', '')], # Get title
                    ['Description', _.get('description')], # Get description
                    ['Tags', ', '.join(map(str, _.get('tags', [])))], # Get tags
                    ['Products Count', _.get('products_count', '~')] # Get products_count
                ]
            
                # Write data vertically
                ws.update('A1:B{}'.format(len(vertical_data)), vertical_data) # Write data to a worksheet
                logger.info("Category data written to 'category' worksheet vertically.") #  Log info
            else:
                raise TypeError("Expected SimpleNamespace for category.") #  show TypeError
        except Exception as ex:
             logger.error("Error setting category worksheet.", exc_info=True) #  Error log and show exc
             raise

    def get_category_worksheet(self) -> SimpleNamespace:
        """
        Считывает данные категории с листа 'category'.

        :return: Объект SimpleNamespace с данными категории.
        :rtype: SimpleNamespace
        :raises ValueError: Если лист 'category' не найден.
        :raises Exception: В случае ошибки при чтении данных.
        """
        try:
            ws: Worksheet = self.get_worksheet('category') # Get a worksheet
            if not ws:
                raise ValueError("Worksheet 'category' not found.") # show ValueError
            
            data = ws.get_all_values() # Get all values
            category_data = SimpleNamespace(
                name=data[1][1], # get name
                title=data[2][1], # get title
                description=data[3][1], # get description
                tags=data[4][1].split(', '), # get tags
                products_count=int(data[5][1]) # get products_count
            )
            
            logger.info("Category data read from 'category' worksheet.") # Log info
            return category_data # Return SimpleNamespace data
        except Exception as ex:
            logger.error('Error getting category worksheet data.', exc_info=True) # Error log and show exc
            raise
        
    def set_categories_worksheet(self, categories: SimpleNamespace) -> None:
        """
        Записывает данные из объекта SimpleNamespace в лист 'categories'.

        :param categories: Объект SimpleNamespace с данными категорий.
        :type categories: SimpleNamespace
        :raises Exception: В случае ошибки при записи данных.
        """
        ws: Worksheet = self.get_worksheet('categories') # Get a worksheet
        # ws.clear()  # Clear the 'categories' worksheet

        try:
            # Initialize the starting row
            start_row = 2
            
            # Iterate over all attributes of the categories object
            for attr_name in dir(categories):
                attr_value = getattr(categories, attr_name, None) # Get attr value
            
                # Skip non-SimpleNamespace attributes or attributes with no data
                if not isinstance(attr_value, SimpleNamespace) or not any(
                    hasattr(attr_value, field) for field in ['name', 'title', 'description', 'tags', 'products_count']
                ):
                    continue
                
                _ = attr_value.__dict__ # Get dict from SimpleNamespace
                # Extract data from the SimpleNamespace attribute
                name =  _.get('name', '') # get name
                title =  _.get('title') # get title
                description =  _.get('description') # get description
                tags =  ', '.join(map(str, _.get('tags', []))) # get tags
                products_count =  _.get('products_count', '~') # get products_count

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
                   ws.batch_update(updates) # Write data to a worksheet
                   logger.info(f"Category data written to 'categories' worksheet for {attr_name}.") #  Log info
                
                # Move to the next row
                start_row += 1
        except Exception as ex:
            logger.error("Error setting categories worksheet.", exc_info=True)  # Error log and show exc
            raise
    
    def get_categories_worksheet(self) -> List[List[str]]:
        """
        Считывает данные из листа 'categories' с столбцов A по E, начиная со второй строки.

        :return: Список строк с данными из столбцов A-E.
        :rtype: List[List[str]]
        :raises ValueError: Если лист 'categories' не найден.
        :raises Exception: В случае ошибки при чтении данных.
        """
        try:
            ws: Worksheet = self.get_worksheet('categories') # Get a worksheet
            if not ws:
                raise ValueError("Worksheet 'categories' not found.") # show ValueError
        
            # Read all values from the worksheet
            data = ws.get_all_values() # Get all values
        
            # Extract data from columns A to E, starting from the second row
            data = [row[:5] for row in data[1:] if len(row) >= 5]  # Get data from columns A to E, starting from the second row
        
            logger.info("Category data read from 'categories' worksheet.") # Log info
            return data # Return data
        except Exception as ex:
            logger.error("Error getting category data from worksheet.", exc_info=True) # Error log and show exc
            raise

    def set_product_worksheet(self, product: SimpleNamespace | str, category_name: str) -> None:
        """
        Записывает данные продукта в новый лист Google Sheets.

        :param product: Объект SimpleNamespace с данными продукта.
        :type product: SimpleNamespace
        :param category_name: Название категории.
        :type category_name: str
        :raises Exception: В случае ошибки при записи данных.
        """
        time.sleep(1) # TODO: Add description
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
            ws.update('A1:Y1', [headers]) # Write headers to a worksheet

            if isinstance(product, SimpleNamespace):
                _ = product.__dict__
            elif isinstance(product, dict):
                _ = product
            else:
                 raise TypeError(f'Expected SimpleNamespace or dict, but got {type(product)}') # show TypeError
            row_data = [
                str(_.get('product_id')), # get product_id
                str(_.get('app_sale_price')), # get app_sale_price
                str(_.get('original_price')), # get original_price
                str(_.get('sale_price')), # get sale_price
                str(_.get('discount')), # get discount
                str(_.get('product_main_image_url')), # get product_main_image_url
                str(_.get('local_image_path')), # get local_image_path
                ', '.join(map(str, _.get('product_small_image_urls', []))), # get product_small_image_urls
                str(_.get('product_video_url')), # get product_video_url
                str(_.get('local_video_path')), # get local_video_path
                str(_.get('first_level_category_id')), # get first_level_category_id
                str(_.get('first_level_category_name')), # get first_level_category_name
                str(_.get('second_level_category_id')), # get second_level_category_id
                str(_.get('second_level_category_name')), # get second_level_category_name
                str(_.get('target_sale_price')), # get target_sale_price
                str(_.get('target_sale_price_currency')), # get target_sale_price_currency
                str(_.get('target_app_sale_price_currency')), # get target_app_sale_price_currency
                str(_.get('target_original_price_currency')), # get target_original_price_currency
                str(_.get('original_price_currency')), # get original_price_currency
                str(_.get('product_title')), # get product_title
                str(_.get('evaluate_rate')), # get evaluate_rate
                str(_.get('promotion_link')), # get promotion_link
                str(_.get('shop_url')), # get shop_url
                str(_.get('shop_id')), # get shop_id
                ', '.join(map(str, _.get('tags', []))) # get tags
            ]

            ws.update('A2:Y2', [row_data])  # Update row data in a single row

            logger.info("Product data written to worksheet.") # Log info
        except Exception as ex:
            logger.error("Error updating product data in worksheet.", exc_info=True) # Error log and show exc
            raise

    def get_product_worksheet(self) -> SimpleNamespace:
        """
        Считывает данные продукта с листа 'products'.

        :return: Объект SimpleNamespace с данными продукта.
        :rtype: SimpleNamespace
        :raises ValueError: Если лист 'products' не найден.
        :raises Exception: В случае ошибки при чтении данных.
        """
        try:
            ws: Worksheet = self.get_worksheet('products') # Get a worksheet
            if not ws:
                raise ValueError("Worksheet 'products' not found.") # show ValueError
            
            data = ws.get_all_values() # Get all values
            product_data = SimpleNamespace(
                id=data[1][1], # get id
                name=data[2][1], # get name
                title=data[3][1], # get title
                description=data[4][1], # get description
                tags=data[5][1].split(', '), # get tags
                price=float(data[6][1]) # get price
            )
            
            logger.info("Product data read from 'products' worksheet.") # Log info
            return product_data # Return SimpleNamespace data
        except Exception as ex:
            logger.error('Error getting product worksheet data.', exc_info=True) # Error log and show exc
            raise

    def set_products_worksheet(self, category_name: str) -> None:
        """
        Записывает данные из списка SimpleNamespace в лист Google Sheets.

        :param category_name: Название категории.
        :type category_name: str
        :raises Exception: В случае ошибки при записи данных.
        """
        if category_name:
            category_ns: SimpleNamespace = getattr(self.campaign.category, category_name) # Get category
            products_ns: SimpleNamespace = category_ns.products # Get products
        else:
            logger.warning(f"На ашел товары в {pprint(category_ns)}") # Log warning
            return
        ws: Worksheet = self.get_worksheet(category_name) # Get a worksheet
        
        try:
            updates: list = [] # Init updates list
            for index, value in enumerate(products_ns, start=2):
                if isinstance(value, SimpleNamespace):
                   _ = value.__dict__
                elif isinstance(value, dict):
                   _ = value
                else:
                    raise TypeError(f'Expected SimpleNamespace or dict, but got {type(value)}') # show TypeError
                updates.append({'range': f'A{index}', 'values': [[str(_.get('product_id', ''))]]}) # add product_id to updates
                updates.append({'range': f'B{index}', 'values': [[str(_.get('product_title', ''))]]}) # add product_title to updates
                updates.append({'range': f'C{index}', 'values': [[str(_.get('title', ''))]]}) # add title to updates
                updates.append({'range': f'D{index}', 'values': [[str(_.get('local_image_path', ''))]]}) # add local_image_path to updates
                updates.append({'range': f'D{index}', 'values': [[str(_.get('product_video_url', ''))]]}) # add product_video_url to updates
                updates.append({'range': f'F{index}', 'values': [[str(_.get('original_price', ''))]]}) # add original_price to updates
                updates.append({'range': f'F{index}', 'values': [[str(_.get('app_sale_price', ''))]]}) # add app_sale_price to updates
                updates.append({'range': f'F{index}', 'values': [[str(_.get('target_sale_price', ''))]]}) # add target_sale_price to updates
                updates.append({'range': f'F{index}', 'values': [[str(_.get('target_sale_price', ''))]]}) # add target_sale_price to updates
                
            ws.batch_update(updates) # Write data to a worksheet
            logger.info("Products data written to 'products' worksheet.") # Log info
        except Exception as ex:
            logger.error("Error setting products worksheet.", exc_info=True) # Error log and show exc
            raise

    def delete_products_worksheets(self) -> None:
        """
        Удаляет все листы, кроме 'categories', 'product_template', 'category', 'campaign'

        :raises Exception: В случае ошибки при удалении листов.
        """
        excluded_titles = {'categories', 'product', 'category', 'campaign'} #  List of excluded sheet titles
        try:
            worksheets = self.spreadsheet.worksheets() # Get all worksheets
            for sheet in worksheets:
                if sheet.title not in excluded_titles:
                    self.spreadsheet.del_worksheet_by_id(sheet.id) # Delete worksheet by id
                    logger.info(f"Worksheet '{sheet.title}' deleted.") #  Log info
        except Exception as ex:
            logger.error("Error deleting all worksheets.", exc_info=True) # Error log and show exc
            raise
        
    def save_categories_from_worksheet(self, update: bool = False) -> None:
        """
        Сохраняет данные категорий из Google Sheets в self.campaign.

        :param update: Флаг обновления кампании.
        :type update: bool, optional
        """
        edited_categories: list[dict] = self.get_categories_worksheet() # Get categories from worksheet
        _categories_ns: SimpleNamespace = SimpleNamespace() # Init SimpleNamespace
        for _cat in edited_categories:
            _cat_ns: SimpleNamespace = SimpleNamespace(**{
                'name': _cat[0], # get name
                'title': _cat[1], # get title
                'description': _cat[2], # get description
                'tags': _cat[3].split(','), # get tags
                'products_count': _cat[4], # get products_count
            }
            )
            setattr(_categories_ns, _cat_ns.name, _cat_ns) # set attr to SimpleNamespace
        ...
        self.campaign.category = _categories_ns # set category to campaign
        if update:
            self.update_campaign() # Update campaign
        
    def save_campaign_from_worksheet(self) -> None:
        """
        Сохраняет данные кампании из Google Sheets в self.campaign.
        """
        self.save_categories_from_worksheet(False) # save categories
        data = self.get_campaign_worksheet() # get campaign from worksheet
        data.category = self.campaign.category # set category
        self.campaign = data # set campaign to self
        self.update_campaign() # Update campaign
        ...