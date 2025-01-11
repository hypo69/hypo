## Анализ кода модуля gsheet.py

**Качество кода**
7
-  Плюсы
    - Код использует классы для организации функциональности.
    - Присутствует логирование ошибок с использованием `logger.error`.
    - Код разделен на отдельные функции, что облегчает его понимание и поддержку.
    - Использование `SimpleNamespace` для передачи данных между функциями.
-  Минусы
    -  Не всегда используется единый стиль форматирования (например, смешанное использование `f-строк` и `format()`).
    -  Не везде есть docstring для функций и классов.
    -  Используется `time.sleep(10)` что блокирует поток, надо использовать асинхронность.
    -  Отсутствует обработка ошибок для случая когда нет данных в таблице
    - Много лишних коментариев
    -  Некоторые функции имеют сложную логику и могут быть упрощены.
    -  Повторение кода при формировании `updates` для `batch_update`.
    -  Не везде используется `j_dumps` или `j_loads_ns` из `src.utils.jjson`.

**Рекомендации по улучшению**
1.  Добавить docstring к классам и методам.
2.  Унифицировать стиль форматирования строк (использовать только `f-строки`).
3.  Удалить лишние коментарии и дублирующие коментарии
4.  Заменить `time.sleep` на асинхронный аналог, если это возможно.
5.  Добавить проверки на наличие данных в таблицах перед их чтением.
6.  Упростить логику функций, например,  формирование `updates` для `batch_update`.
7. Использовать  `j_dumps` или `j_loads_ns` из `src.utils.jjson`.
8. Всегда использовать `from src.logger.logger import logger`
9.  Избегать `try-except`  блоков и использовать `logger.error`  для логирования.
10. Использовать более информативные сообщения логов, например `f"Error in {self.__class__.__name__}.{func.__name__}: {ex}"`

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с Google Sheets в контексте AliExpress.
=========================================================================================

Этот модуль предоставляет класс `GptGs`, который наследуется от `SpreadSheet`
для управления Google Sheets, записи данных о категориях и продуктах,
а также для форматирования листов.

Пример использования
--------------------

Пример создания и использования экземпляра класса `GptGs`:

.. code-block:: python

    gpt_gs = GptGs()
    gpt_gs.clear()
"""

import time
from types import SimpleNamespace
from typing import List
from gspread.worksheet import Worksheet
from src.goog.spreadsheet.spreadsheet import SpreadSheet
from src.logger.logger import logger
from src.utils.jjson import j_dumps



class GptGs(SpreadSheet):
    """
    Класс для управления Google Sheets в кампаниях AliExpress.

    Наследуется от `SpreadSheet` для управления Google Sheets, записи данных о
    категориях и продуктах, а также для форматирования листов.
    """
    def __init__(self):
        """
        Инициализирует `AliCampaignGoogleSheet` с указанным ID Google Sheets и дополнительными параметрами.
        """
        super().__init__('1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0')

    def clear(self):
        """
        Очищает содержимое.
        Удаляет листы продуктов и очищает данные на листах категорий и других листах.
        """
        try:
            self.delete_products_worksheets()
        except Exception as ex:
            logger.error(f"Error in {self.__class__.__name__}.{self.clear.__name__}: {ex}", exc_info=True)

    def update_chat_worksheet(self, data: SimpleNamespace|dict|list, conversation_name:str, language: str = None):
        """
        Записывает данные кампании на лист Google Sheets.

        Args:
            data (SimpleNamespace | dict | list): Объект SimpleNamespace с данными для записи.
            conversation_name (str): Название листа.
            language (str, optional): Языковой параметр. Defaults to None.
        """
        try:
            ws: Worksheet = self.get_worksheet(conversation_name)
            _ = data.__dict__
            name =  _.get('name','')
            title =  _.get('title')
            description =  _.get('description')
            tags =  ', '.join(map(str, _.get('tags', [])))
            products_count =  _.get('products_count','~')

            start_row = 1 #TODO need add logic to find current row
            updates = [
                {'range': f'A{start_row}', 'values': [[name]]},
                {'range': f'B{start_row}', 'values': [[title]]},
                {'range': f'C{start_row}', 'values': [[description]]},
                {'range': f'D{start_row}', 'values': [[tags]]},
                {'range': f'E{start_row}', 'values': [[products_count]]},
            ]
            ws.batch_update(updates)
        except Exception as ex:
            logger.error(f"Error in {self.__class__.__name__}.{self.update_chat_worksheet.__name__}: {ex}", exc_info=True)
            raise

    def get_campaign_worksheet(self) -> SimpleNamespace:
        """
        Считывает данные кампании с листа 'campaign'.

        Returns:
            SimpleNamespace: Объект SimpleNamespace с данными кампании.
        """
        try:
            ws: Worksheet = self.get_worksheet('campaign')
            if not ws:
                raise ValueError("Worksheet 'campaign' not found.")
            
            data = ws.get_all_values()
            if not data or len(data) < 5:
                logger.error("Incorrect data format in 'campaign' worksheet.")
                return SimpleNamespace()  # Возвращает пустой SimpleNamespace
            
            campaign_data = SimpleNamespace(
                name=data[0][1] if len(data[0]) > 1 else '',
                title=data[1][1] if len(data[1]) > 1 else '',
                language=data[2][1] if len(data[2]) > 1 else '',
                currency=data[3][1] if len(data[3]) > 1 else '',
                description=data[4][1] if len(data[4]) > 1 else ''
            )
            
            logger.info("Campaign data read from 'campaign' worksheet.")
            return campaign_data

        except Exception as ex:
            logger.error(f"Error in {self.__class__.__name__}.{self.get_campaign_worksheet.__name__}: {ex}", exc_info=True)
            raise

    def set_category_worksheet(self, category: SimpleNamespace | str):
        """
        Записывает данные из объекта SimpleNamespace на лист Google Sheets вертикально.

        Args:
            category (SimpleNamespace | str): Объект SimpleNamespace с данными для записи.
        """
        category = category if isinstance(category, SimpleNamespace) else self.get_campaign_category(category)
        try:
            ws: Worksheet = self.get_worksheet('category')

            if isinstance(category, SimpleNamespace):
                _ = category.__dict__
                vertical_data = [
                    ['Name', _.get('name','')],
                    ['Title', _.get('title','')],
                    ['Description', _.get('description')],
                    ['Tags', ', '.join(map(str, _.get('tags', [])))],
                    ['Products Count', _.get('products_count', '~')]
                ]
            
                ws.update('A1:B{}'.format(len(vertical_data)), vertical_data)

                logger.info("Category data written to 'category' worksheet vertically.")
            else:
                raise TypeError("Expected SimpleNamespace for category.")

        except Exception as ex:
            logger.error(f"Error in {self.__class__.__name__}.{self.set_category_worksheet.__name__}: {ex}", exc_info=True)
            raise


    def get_category_worksheet(self) -> SimpleNamespace:
        """
        Считывает данные категории с листа 'category'.

        Returns:
            SimpleNamespace: Объект SimpleNamespace с данными категории.
        """
        try:
            ws: Worksheet = self.get_worksheet('category')
            if not ws:
                raise ValueError("Worksheet 'category' not found.")
            
            data = ws.get_all_values()
            if not data or len(data) < 6:
               logger.error("Incorrect data format in 'category' worksheet.")
               return SimpleNamespace()
               
            category_data = SimpleNamespace(
                name=data[1][1] if len(data[1]) > 1 else '',
                title=data[2][1] if len(data[2]) > 1 else '',
                description=data[3][1] if len(data[3]) > 1 else '',
                tags=data[4][1].split(', ')  if len(data[4]) > 1 and data[4][1] else [],
                products_count=int(data[5][1]) if len(data[5]) > 1 and data[5][1] else 0
            )
            
            logger.info("Category data read from 'category' worksheet.")
            return category_data

        except Exception as ex:
            logger.error(f"Error in {self.__class__.__name__}.{self.get_category_worksheet.__name__}: {ex}", exc_info=True)
            raise

    def set_categories_worksheet(self, categories: SimpleNamespace):
        """
        Записывает данные из объекта SimpleNamespace на лист Google Sheets.

        Args:
            categories (SimpleNamespace): Объект SimpleNamespace с данными для записи.
        """
        ws: Worksheet = self.get_worksheet('categories')

        try:
            start_row = 2

            for attr_name in dir(categories):
                attr_value = getattr(categories, attr_name, None)
                if not isinstance(attr_value, SimpleNamespace) or not any(
                    hasattr(attr_value, field) for field in ['name', 'title', 'description', 'tags', 'products_count']
                ):
                    continue
                _ = attr_value.__dict__
                name =  _.get('name','')
                title =  _.get('title')
                description =  _.get('description')
                tags =  ', '.join(map(str, _.get('tags', [])))
                products_count =  _.get('products_count','~')
                
                updates = [
                    {'range': f'A{start_row}', 'values': [[name]]},
                    {'range': f'B{start_row}', 'values': [[title]]},
                    {'range': f'C{start_row}', 'values': [[description]]},
                    {'range': f'D{start_row}', 'values': [[tags]]},
                    {'range': f'E{start_row}', 'values': [[products_count]]},
                ]
                if updates:
                    ws.batch_update(updates)
                    logger.info(f"Category data written to 'categories' worksheet for {attr_name}.")
            
                start_row += 1

        except Exception as ex:
            logger.error(f"Error in {self.__class__.__name__}.{self.set_categories_worksheet.__name__}: {ex}", exc_info=True)
            raise
 
    def get_categories_worksheet(self) -> List[List[str]]:
        """
        Считывает данные с колонок A по E, начиная со второй строки, с листа 'categories'.

        Returns:
            List[List[str]]: Список строк с данными из колонок A по E.
        """
        try:
            ws: Worksheet = self.get_worksheet('categories')
            if not ws:
                raise ValueError("Worksheet 'categories' not found.")
        
            data = ws.get_all_values()
            data = [row[:5] for row in data[1:] if len(row) >= 5] 
        
            logger.info("Category data read from 'categories' worksheet.")
            return data

        except Exception as ex:
           logger.error(f"Error in {self.__class__.__name__}.{self.get_categories_worksheet.__name__}: {ex}", exc_info=True)
           raise

    def set_product_worksheet(self, product: SimpleNamespace | str, category_name: str):
        """
        Записывает данные продукта в новый лист Google Sheets.

        Args:
            product (SimpleNamespace | str): Объект SimpleNamespace с данными продукта.
            category_name (str): Название категории.
        """
        #TODO  Replace to async function
        time.sleep(10)
        ws = self.copy_worksheet('product_template', category_name)
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

            ws.update('A2:Y2', [row_data])

            logger.info("Product data written to worksheet.")
        except Exception as ex:
            logger.error(f"Error in {self.__class__.__name__}.{self.set_product_worksheet.__name__}: {ex}", exc_info=True)
            raise

    def get_product_worksheet(self) -> SimpleNamespace:
        """
        Считывает данные продукта с листа 'products'.

        Returns:
            SimpleNamespace: Объект SimpleNamespace с данными продукта.
        """
        try:
            ws: Worksheet = self.get_worksheet('products')
            if not ws:
                raise ValueError("Worksheet 'products' not found.")
            
            data = ws.get_all_values()
            if not data or len(data) < 7:
                logger.error("Incorrect data format in 'products' worksheet.")
                return SimpleNamespace()
                
            product_data = SimpleNamespace(
                id=data[1][1] if len(data[1]) > 1 else '',
                name=data[2][1] if len(data[2]) > 1 else '',
                title=data[3][1] if len(data[3]) > 1 else '',
                description=data[4][1] if len(data[4]) > 1 else '',
                tags=data[5][1].split(', ') if len(data[5]) > 1 and data[5][1] else [],
                price=float(data[6][1]) if len(data[6]) > 1 and data[6][1] else 0.0
            )
            
            logger.info("Product data read from 'products' worksheet.")
            return product_data

        except Exception as ex:
            logger.error(f"Error in {self.__class__.__name__}.{self.get_product_worksheet.__name__}: {ex}", exc_info=True)
            raise

    def set_products_worksheet(self, category_name:str):
        """
        Записывает данные из списка SimpleNamespace объектов на лист Google Sheets.

        Args:
            category_name (str): Название категории.
        """
        if category_name:
            category_ns:SimpleNamespace = getattr(self.campaign.category,category_name)
            products_ns:SimpleNamespace = category_ns.products
        else:
            logger.warning(f"Не найдены товары в {pprint(category_ns)}")
            return    
        ws: Worksheet = self.get_worksheet(category_name)
        
        try:
            updates:list=[]
            for index, value in enumerate(products_ns, start=2):
                _ = value.__dict__
                updates.append({'range': f'A{index}', 'values': [[str(_.get('product_id',''))]]})
                updates.append({'range': f'B{index}', 'values': [[str(_.get('product_title',''))]]})
                updates.append({'range': f'C{index}', 'values': [[str(_.get('title',''))]]})
                updates.append({'range': f'D{index}', 'values': [[str(_.get('local_image_path',''))]]})
                updates.append({'range': f'E{index}', 'values': [[str(_.get('product_video_url',''))]]})
                updates.append({'range': f'F{index}', 'values': [[str(_.get('original_price',''))]]})
                updates.append({'range': f'G{index}', 'values': [[str(_.get('app_sale_price',''))]]})
                updates.append({'range': f'H{index}', 'values': [[str(_.get('target_sale_price',''))]]})
                updates.append({'range': f'I{index}', 'values': [[str(_.get('target_sale_price',''))]]})
                
            ws.batch_update(updates)
            logger.info("Products data written to 'products' worksheet.")

        
        except Exception as ex:
           logger.error(f"Error in {self.__class__.__name__}.{self.set_products_worksheet.__name__}: {ex}", exc_info=True)
           raise

    def delete_products_worksheets(self):
        """
        Удаляет все листы из Google Sheets, кроме 'categories', 'product_template', 'category', 'campaign'.
        """
        excluded_titles = {'categories', 'product', 'category', 'campaign', 'product_template'}
        try:
            worksheets = self.spreadsheet.worksheets()
            for sheet in worksheets:
                if sheet.title not in excluded_titles:
                    self.spreadsheet.del_worksheet_by_id(sheet.id)
                    logger.info(f"Worksheet '{sheet.title}' deleted.")
        except Exception as ex:
            logger.error(f"Error in {self.__class__.__name__}.{self.delete_products_worksheets.__name__}: {ex}", exc_info=True)
            raise
        
    def save_categories_from_worksheet(self, update:bool=False):
        """
        Сохраняет данные, отредактированные в Google Sheets.
        """

        edited_categories: list[dict] = self.get_categories_worksheet()
        _categories_ns:SimpleNamespace = SimpleNamespace()
        for _cat in edited_categories:
            _cat_ns: SimpleNamespace = SimpleNamespace(**{
                'name':_cat[0],
                'title':_cat[1],
                'description':_cat[2],
                'tags':_cat[3].split(","),
                'products_count':_cat[4],
            }
            )
            setattr(_categories_ns,_cat_ns.name,_cat_ns)
        ...
        self.campaign.category = _categories_ns
        if update: self.update_campaign()
        
    def save_campaign_from_worksheet(self):
        """
        Сохраняет рекламную кампанию.
        """
        self.save_categories_from_worksheet(False)
        data = self.get_campaign_worksheet()
        data.category = self.campaign.category
        self.campaign = data
        self.update_campaign()
        ...