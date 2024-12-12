## Анализ кода модуля gsheet.py

**Качество кода**
8
-  Плюсы
    -  Используется  логгер для записи ошибок и отладочной информации.
    -  Код разбит на методы, что улучшает читаемость и повторное использование.
    -  Присутствует базовая обработка ошибок с использованием `try-except`.
    -  Используются `SimpleNamespace` для хранения и передачи данных.
-  Минусы
    -  Не везде используется `logger.error` с `exc_info=True` для более детального логирования ошибок.
    -  Присутствует избыточное использование `try-except` блоков.
    -  Отсутствует документация в формате reStructuredText (RST) для всех функций, методов и класса.
    -  Используется time.sleep(10) вместо более гибкого ожидания.
    -  Не все переменные и функции имеют  описательные названия.
    -  Отсутствует проверка типа данных для многих входных параметров.
    -  Не хватает обработки ошибок при чтении данных из Google Sheets.
    -  Некоторые docstring не соответствуют стандарту.

**Рекомендации по улучшению**

1. **Документация**:
   - Добавить docstring в формате reStructuredText (RST) для всех функций, методов и классов.

2. **Импорты**:
   - Проверить и добавить отсутствующие импорты, такие как `Any`, `Union`, `Optional`.
   - Убедиться, что все импорты соответствуют ранее обработанным файлам.

3. **Логирование**:
   - Использовать `logger.error(..., exc_info=True)` для более информативного логирования исключений.
   - Избегать избыточного использования `try-except`, когда можно использовать `logger.error`.

4. **Обработка данных**:
    - Проверять типы данных перед использованием и обрабатывать возможные ошибки.
    - Использовать более описательные переменные для улучшения читаемости кода.

5. **Рефакторинг**:
    - Упростить код, где это возможно, например, убрать лишние проверки.
    - Использовать более конкретные имена переменных для повышения читаемости.
    - Переименовать функции и методы в более понятные и описательные.

6. **Улучшение производительности**:
    - Заменить `time.sleep(10)` на более адаптивное ожидание, если требуется.

7. **Структура кода**:
    -  Улучшить структуру кода, разделив логику на более мелкие функции.

**Оптимизиробанный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для управления Google Sheets в контексте рекламных кампаний AliExpress.
=========================================================================================

Этот модуль предоставляет класс :class:`GptGs`, который наследуется от :class:`src.goog.spreadsheet.spreadsheet.SpreadSheet`
и обеспечивает функциональность для работы с Google Sheets, включая чтение, запись и управление данными
категорий, продуктов и кампаний. Модуль использует ``gspread`` для взаимодействия с Google Sheets API,
``SimpleNamespace`` для хранения данных, ``j_dumps`` и ``logger`` для сериализации данных и логирования.

Пример использования
--------------------

.. code-block:: python

    from src.suppliers.chat_gpt.gsheet import GptGs
    
    gsheet_manager = GptGs()
    # Используйте методы класса для работы с Google Sheets
    
"""
import time
from typing import List, Any, Union, Optional
from types import SimpleNamespace
from gspread.worksheet import Worksheet

from src.goog.spreadsheet.spreadsheet import SpreadSheet
from src.utils.jjson import j_dumps
from src.utils.printer import pprint
from src.logger.logger import logger


MODE = 'dev'


class GptGs(SpreadSheet):
    """
    Управляет Google Sheets для кампаний AliExpress.

    Наследуется от :class:`SpreadSheet` для управления Google Sheets, записи данных
    о категориях и продуктах, а также форматирования листов.
    """
    def __init__(self):
        """
        Инициализация :class:`GptGs` с указанным ID Google Sheets.
        """
        # Инициализирует SpreadSheet с указанным ID таблицы.
        super().__init__('1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0')
    
    def clear(self):
        """
        Очищает содержимое Google Sheets.

        Удаляет листы с продуктами и очищает данные на листах категорий и других указанных листах.
        """
        try:
            #  Код удаляет все листы продуктов
            self.delete_products_worksheets()
        except Exception as ex:
            logger.error("Ошибка при очистке Google Sheets.", exc_info=True)
    
    def update_chat_worksheet(self, data: Union[SimpleNamespace, dict, list], conversation_name: str, language: Optional[str] = None):
        """
        Записывает данные кампании в Google Sheets.

        :param data: Объект SimpleNamespace, dict или list с данными для записи.
        :param conversation_name: Имя листа, в который записываются данные.
        :param language: Необязательный параметр языка.
        """
        try:
             # Получает лист по имени
            ws: Worksheet = self.get_worksheet(conversation_name)
             # Код извлекает данные из объекта SimpleNamespace
            _ = data.__dict__
            name =  _.get('name','')
            title =  _.get('title')
            description =  _.get('description')
            tags =  ', '.join(map(str, _.get('tags', [])))
            products_count =  _.get('products_count','~')

            #  Подготавливает обновления для записи в таблицу
            updates = [
                {'range': f'A{1}', 'values': [[name]]},
                {'range': f'B{1}', 'values': [[title]]},
                {'range': f'C{1}', 'values': [[description]]},
                {'range': f'D{1}', 'values': [[tags]]},
                {'range': f'E{1}', 'values': [[products_count]]},
            ]

            #  Код выполняет пакетное обновление данных в таблице
            if updates:
                ws.batch_update(updates)
                logger.info(f"Данные чата записаны на лист '{conversation_name}'.")

        except Exception as ex:
            logger.error(f"Ошибка записи данных чата на лист '{conversation_name}'.", exc_info=True)
            raise
        
    def get_campaign_worksheet(self) -> SimpleNamespace:
        """
        Считывает данные кампании из листа 'campaign'.

        :return: Объект SimpleNamespace с данными кампании.
        :raises ValueError: Если лист 'campaign' не найден.
        """
        try:
            # Код получает лист 'campaign'
            ws: Worksheet = self.get_worksheet('campaign')
            if not ws:
                raise ValueError("Лист 'campaign' не найден.")
            
             # Код получает все значения из листа
            data = ws.get_all_values()
            
            # Создает SimpleNamespace с данными кампании
            campaign_data = SimpleNamespace(
                name=data[0][1],
                title=data[1][1],
                language=data[2][1],
                currency=data[3][1],
                description=data[4][1]
            )
            
            logger.info("Данные кампании прочитаны с листа 'campaign'.")
            return campaign_data

        except Exception as ex:
            logger.error("Ошибка при получении данных кампании.", exc_info=True)
            raise

    def set_category_worksheet(self, category: Union[SimpleNamespace, str]):
        """
        Записывает данные категории в лист 'category' вертикально.

        :param category: Объект SimpleNamespace или строка с данными категории для записи.
        :raises TypeError: Если `category` не является SimpleNamespace.
        """
        # Код проверяет тип данных параметра category, если строка то получает SimpleNamespace
        category = category if isinstance(category, SimpleNamespace) else self.get_campaign_category(category)
        try:
            #  Код получает лист 'category'
            ws: Worksheet = self.get_worksheet('category')
            
            if isinstance(category, SimpleNamespace):
                # Код извлекает данные из объекта SimpleNamespace
                _ = category.__dict__
                
                # Формирует вертикальный список данных для записи
                vertical_data = [
                    ['Name', _.get('name','')],
                    ['Title', _.get('title','')],
                    ['Description', _.get('description')],
                    ['Tags', ', '.join(map(str, _.get('tags', [])))],
                    ['Products Count', _.get('products_count', '~')]
                ]
            
                # Записывает данные вертикально в лист
                ws.update('A1:B{}'.format(len(vertical_data)), vertical_data)

                logger.info("Данные категории записаны на лист 'category' вертикально.")
            else:
                raise TypeError("Ожидается SimpleNamespace для категории.")

        except Exception as ex:
            logger.error("Ошибка при записи данных категории.", exc_info=True)
            raise


    def get_category_worksheet(self) -> SimpleNamespace:
        """
        Считывает данные категории из листа 'category'.

        :return: Объект SimpleNamespace с данными категории.
        :raises ValueError: Если лист 'category' не найден.
        """
        try:
            #  Код получает лист 'category'
            ws: Worksheet = self.get_worksheet('category')
            if not ws:
                raise ValueError("Лист 'category' не найден.")
            
            #  Код получает все значения из листа
            data = ws.get_all_values()
            
            # Код формирует SimpleNamespace с данными категории
            category_data = SimpleNamespace(
                name=data[1][1],
                title=data[2][1],
                description=data[3][1],
                tags=data[4][1].split(', '),
                products_count=int(data[5][1])
            )
            
            logger.info("Данные категории прочитаны с листа 'category'.")
            return category_data

        except Exception as ex:
            logger.error("Ошибка при получении данных категории.", exc_info=True)
            raise
    
    def set_categories_worksheet(self, categories: SimpleNamespace):
        """
        Записывает данные категорий в лист 'categories'.

        :param categories: Объект SimpleNamespace с данными для записи.
        """
        # Код получает лист 'categories'
        ws: Worksheet = self.get_worksheet('categories')

        try:
            start_row = 2
            # Код итерируется по всем атрибутам объекта categories
            for attr_name in dir(categories):
                attr_value = getattr(categories, attr_name, None)
            
                # Пропускает не SimpleNamespace атрибуты или атрибуты без необходимых данных
                if not isinstance(attr_value, SimpleNamespace) or not any(
                    hasattr(attr_value, field) for field in ['name', 'title', 'description', 'tags', 'products_count']
                ):
                    continue
                # Код извлекает данные из объекта SimpleNamespace
                _ = attr_value.__dict__
                name =  _.get('name','')
                title =  _.get('title')
                description =  _.get('description')
                tags =  ', '.join(map(str, _.get('tags', [])))
                products_count =  _.get('products_count','~')

                #  Формирует обновления для записи в таблицу
                updates = [
                    {'range': f'A{start_row}', 'values': [[name]]},
                    {'range': f'B{start_row}', 'values': [[title]]},
                    {'range': f'C{start_row}', 'values': [[description]]},
                    {'range': f'D{start_row}', 'values': [[tags]]},
                    {'range': f'E{start_row}', 'values': [[products_count]]},
                ]
                
                # Код выполняет пакетное обновление данных в таблице
                if updates:
                    ws.batch_update(updates)
                    logger.info(f"Данные категории записаны на лист 'categories' для {attr_name}.")

                start_row += 1

        except Exception as ex:
            logger.error("Ошибка при записи данных категорий.", exc_info=True)
            raise
    
    def get_categories_worksheet(self) -> List[List[str]]:
        """
        Считывает данные категорий из листа 'categories'.

        :return: Список строк с данными из столбцов A-E.
        :raises ValueError: Если лист 'categories' не найден.
        """
        try:
            # Код получает лист 'categories'
            ws: Worksheet = self.get_worksheet('categories')
            if not ws:
                raise ValueError("Лист 'categories' не найден.")
            
            #  Код получает все значения из листа
            data = ws.get_all_values()
        
            #  Код извлекает данные из столбцов A-E, начиная со второй строки
            data = [row[:5] for row in data[1:] if len(row) >= 5]
            
            logger.info("Данные категорий прочитаны с листа 'categories'.")
            return data

        except Exception as ex:
             logger.error("Ошибка при получении данных категорий.", exc_info=True)
             raise

    def set_product_worksheet(self, product: SimpleNamespace, category_name: str):
        """
         Записывает данные продукта в новый лист Google Sheets.

         :param product: Объект SimpleNamespace с данными продукта для записи.
         :param category_name: Имя категории.
         """
        time.sleep(10)
         # Код копирует шаблон листа продукта
        ws = self.copy_worksheet('product_template', category_name)
        try:
            #  Код задает заголовки столбцов
            headers = [
                'product_id', 'app_sale_price', 'original_price', 'sale_price', 'discount',
                'product_main_image_url', 'local_saved_image', 'product_small_image_urls',
                'product_video_url', 'local_saved_video', 'first_level_category_id',
                'first_level_category_name', 'second_level_category_id', 'second_level_category_name',
                'target_sale_price', 'target_sale_price_currency', 'target_app_sale_price_currency',
                'target_original_price_currency', 'original_price_currency', 'product_title',
                'evaluate_rate', 'promotion_link', 'shop_url', 'shop_id', 'tags'
            ]
            #  Код записывает заголовки в первую строку
            ws.update('A1:Y1', [headers])
           
            # Код извлекает данные из объекта SimpleNamespace
            _ = product.__dict__
            # Код формирует строку данных продукта
            row_data = [
                str(_.get('product_id')),
                str(_.get('app_sale_price')),
                str(_.get('original_price')),
                str(_.get('sale_price')),
                str(_.get('discount')),
                str(_.get('product_main_image_url')),
                str(_.get('local_saved_image')),
                ', '.join(map(str, _.get('product_small_image_urls', []))),
                str(_.get('product_video_url')),
                str(_.get('local_saved_video')),
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
            # Код записывает строку данных продукта во вторую строку
            ws.update('A2:Y2', [row_data])

            logger.info("Данные продукта записаны на лист.")
        except Exception as ex:
            logger.error("Ошибка при записи данных продукта.", exc_info=True)
            raise

    def get_product_worksheet(self) -> SimpleNamespace:
        """
         Считывает данные продукта из листа 'products'.

         :return: Объект SimpleNamespace с данными продукта.
         :raises ValueError: Если лист 'products' не найден.
         """
        try:
            # Код получает лист 'products'
            ws: Worksheet = self.get_worksheet('products')
            if not ws:
                raise ValueError("Лист 'products' не найден.")
            
            #  Код получает все значения из листа
            data = ws.get_all_values()
            
             # Код формирует SimpleNamespace с данными продукта
            product_data = SimpleNamespace(
                id=data[1][1],
                name=data[2][1],
                title=data[3][1],
                description=data[4][1],
                tags=data[5][1].split(', '),
                price=float(data[6][1])
            )
            
            logger.info("Данные продукта прочитаны с листа 'products'.")
            return product_data

        except Exception as ex:
            logger.error("Ошибка при получении данных продукта.", exc_info=True)
            raise
    
    def set_products_worksheet(self, category_name: str):
        """
         Записывает данные из списка объектов SimpleNamespace в Google Sheets.

         :param category_name: Имя категории, для которой записываются данные.
         :raises ValueError: Если не передано имя категории.
         """
        if not category_name:
            logger.warning(f"Имя категории не было передано {category_name=}")
            return
        try:
            category_ns:SimpleNamespace = getattr(self.campaign.category,category_name)
            products_ns:SimpleNamespace = category_ns.products
        except Exception as ex:
            logger.error("Ошибка при получении данных категории.", exc_info=True)
            raise
        # Код получает лист с именем категории
        ws: Worksheet = self.get_worksheet(category_name)
        
        try:
            updates: list = []
            # Код итерируется по списку продуктов и формирует обновления
            for index, value in enumerate(products_ns, start=2):
                _ = value.__dict__
                updates.append({'range': f'A{index}', 'values': [[str(_.get('product_id',''))]]})
                updates.append({'range': f'B{index}', 'values': [[str(_.get('product_title',''))]]})
                updates.append({'range': f'C{index}', 'values': [[str(_.get('title',''))]]})
                updates.append({'range': f'D{index}', 'values': [[str(_.get('local_saved_image',''))]]})
                updates.append({'range': f'D{index}', 'values': [[str(_.get('product_video_url',''))]]})
                updates.append({'range': f'F{index}', 'values': [[str(_.get('original_price',''))]]})
                updates.append({'range': f'F{index}', 'values': [[str(_.get('app_sale_price',''))]]})
                updates.append({'range': f'F{index}', 'values': [[str(_.get('target_sale_price',''))]]})
                updates.append({'range': f'F{index}', 'values': [[str(_.get('target_sale_price',''))]]})
            
            # Код выполняет пакетное обновление данных в таблице
            if updates:
                ws.batch_update(updates)
                logger.info("Данные продуктов записаны на лист.")

        except Exception as ex:
            logger.error("Ошибка при записи данных продуктов.", exc_info=True)
            raise
    
    def delete_products_worksheets(self):
        """
        Удаляет все листы из Google Sheets, кроме 'categories', 'product', 'category', и 'campaign'.
        """
        excluded_titles = {'categories', 'product', 'category', 'campaign'}
        try:
            worksheets = self.spreadsheet.worksheets()
            for sheet in worksheets:
                if sheet.title not in excluded_titles:
                    self.spreadsheet.del_worksheet_by_id(sheet.id)
                    logger.info(f"Лист '{sheet.title}' удален.")
        except Exception as ex:
            logger.error("Ошибка при удалении листов.", exc_info=True)
            raise
    
    def save_categories_from_worksheet(self, update: bool = False):
        """
         Сохраняет данные категорий из Google Sheets.

         :param update: Флаг для обновления кампании после сохранения.
         """
        # Код получает отредактированные данные из таблицы
        edited_categories: list[dict] = self.get_categories_worksheet()
        _categories_ns:SimpleNamespace = SimpleNamespace()
        
        # Код итерируется по списку отредактированных категорий
        for _cat in edited_categories:
            _cat_ns: SimpleNamespace = SimpleNamespace(**{
                'name':_cat[0],
                'title':_cat[1],
                'description':_cat[2],
                'tags':_cat[3].split(","),
                'products_count':_cat[4],
            })
            setattr(_categories_ns,_cat_ns.name,_cat_ns)
        
        self.campaign.category = _categories_ns
        if update: self.update_campaign()
    
    def save_campaign_from_worksheet(self):
        """
        Сохраняет данные рекламной кампании из Google Sheets.
        """
        self.save_categories_from_worksheet(False)
        data = self.get_campaign_worksheet()
        data.category = self.campaign.category
        self.campaign = data
        self.update_campaign()