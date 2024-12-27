## Анализ кода модуля gsheet.py

**Качество кода**
1.  **Соответствие требованиям по оформлению кода**: 6/10
    *   **Плюсы**:
        *   Используется `logger` для логирования ошибок.
        *   Присутствует базовая структура класса.
        *   Есть разделение на методы для чтения и записи данных.
    *   **Минусы**:
        *   Отсутствует docstring для модуля.
        *   Не все функции и методы имеют docstring.
        *   Используются конструкции `try-except` без необходимости, когда можно использовать `logger.error`.
        *   Некоторые комментарии не соответствуют стандарту RST.
        *   Используется `time.sleep(10)` без объяснения.
        *   Не везде используется `j_loads` или `j_loads_ns`.
        *   Много `...` в коде, которые необходимо убрать.

**Рекомендации по улучшению**

1.  **Документация**:
    *   Добавить docstring для модуля.
    *   Добавить подробные docstring для всех функций, методов и классов в формате RST.
    *   Улучшить существующие docstring, чтобы они соответствовали стандартам RST.
2.  **Импорты**:
    *   Удалить лишние импорты, добавить недостающие (`from src.utils.jjson import j_loads`, `from typing import Any`).
3.  **Обработка ошибок**:
    *   Заменить избыточные `try-except` блоки на `logger.error`.
4.  **Именование**:
    *   Привести имена переменных и функций в соответствие с общим стилем.
5.  **Рефакторинг**:
    *   Удалить лишние комментарии и пустые строки.
    *   Удалить магические значения.
    *   Убрать `time.sleep(10)` и найти более корректный способ решения проблемы задержки.
6.  **Использование `j_loads`**:
    *   Убедиться, что все операции чтения файлов используют `j_loads` или `j_loads_ns`.
7.  **Логирование**:
    *   Добавить более информативные сообщения при логировании.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с Google Sheets в контексте AliExpress кампаний.
====================================================================

Этот модуль предоставляет класс :class:`GptGs`, который наследует функциональность
:class:`src.goog.spreadsheet.spreadsheet.SpreadSheet` для управления Google Sheets,
записи данных о категориях и продуктах, а также форматирования листов.

Пример использования
--------------------

.. code-block:: python

    gsheet = GptGs()
    gsheet.clear()
    campaign_data = gsheet.get_campaign_worksheet()
    categories_data = gsheet.get_categories_worksheet()
"""
import time
from types import SimpleNamespace
from typing import List, Any

from gspread.worksheet import Worksheet

from src.goog.spreadsheet.spreadsheet import SpreadSheet
from src.utils.jjson import j_dumps
from src.utils.printer import pprint
from src.logger.logger import logger


class GptGs(SpreadSheet):
    """
    Управляет Google Sheets в рамках кампаний AliExpress.

    Наследует :class:`SpreadSheet` для управления Google Sheets,
    записи данных о категориях и продуктах, а также форматирования листов.
    """

    def __init__(self):
        """
        Инициализирует класс GptGs с указанным ID Google Sheets.

        Вызывает конструктор родительского класса :class:`SpreadSheet`
        с ID таблицы Google Sheets.
        """
        super().__init__('1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0')

    def clear(self):
        """
        Очищает содержимое Google Sheets.

        Удаляет листы продуктов и очищает данные на листах категорий и других указанных листах.
        """
        try:
            # код исполняет удаление всех листов продуктов
            self.delete_products_worksheets()
        except Exception as ex:
            logger.error('Ошибка очистки листов Google Sheets', ex, exc_info=True)

    def update_chat_worksheet(self, data: SimpleNamespace | dict | list, conversation_name: str, language: str = None):
        """
        Записывает данные чата в лист Google Sheets.

        :param data: Объект SimpleNamespace, словарь или список с данными для записи.
        :param conversation_name: Имя листа для записи данных.
        :param language: Необязательный параметр языка.
        """
        try:
            ws: Worksheet = self.get_worksheet(conversation_name)
            if not ws:
                logger.error(f'Лист {conversation_name} не найден', exc_info=True)
                return
            _ = data.__dict__
            name = _.get('name', '')
            title = _.get('title')
            description = _.get('description')
            tags = ', '.join(map(str, _.get('tags', [])))
            products_count = _.get('products_count', '~')

            start_row = 2
            updates = [
                {'range': f'A{start_row}', 'values': [[name]]},
                {'range': f'B{start_row}', 'values': [[title]]},
                {'range': f'C{start_row}', 'values': [[description]]},
                {'range': f'D{start_row}', 'values': [[tags]]},
                {'range': f'E{start_row}', 'values': [[products_count]]},
            ]
            ws.batch_update(updates)
            logger.info(f'Данные чата записаны в лист "{conversation_name}"')


        except Exception as ex:
            logger.error('Ошибка записи данных чата в лист', ex, exc_info=True)
            raise

    def get_campaign_worksheet(self) -> SimpleNamespace:
        """
        Читает данные кампании из листа 'campaign'.

        :return: Объект SimpleNamespace с данными кампании.
        """
        try:
            ws: Worksheet = self.get_worksheet('campaign')
            if not ws:
                logger.error('Лист "campaign" не найден')
                return None

            data = ws.get_all_values()
            campaign_data = SimpleNamespace(
                name=data[0][1],
                title=data[1][1],
                language=data[2][1],
                currency=data[3][1],
                description=data[4][1],
            )

            logger.info('Данные кампании прочитаны из листа "campaign".')
            return campaign_data

        except Exception as ex:
            logger.error('Ошибка чтения данных кампании из листа', ex, exc_info=True)
            raise

    def set_category_worksheet(self, category: SimpleNamespace | str):
        """
        Записывает данные категории в лист 'category' вертикально.

        :param category: Объект SimpleNamespace с данными категории или имя категории.
        """
        category = category if isinstance(category, SimpleNamespace) else self.get_campaign_category(category)
        try:
            ws: Worksheet = self.get_worksheet('category')
            if not ws:
                logger.error('Лист "category" не найден')
                return

            if isinstance(category, SimpleNamespace):
                _ = category.__dict__
                vertical_data = [
                    ['Name', _.get('name', '')],
                    ['Title', _.get('title', '')],
                    ['Description', _.get('description')],
                    ['Tags', ', '.join(map(str, _.get('tags', [])))],
                    ['Products Count', _.get('products_count', '~')],
                ]

                ws.update('A1:B{}'.format(len(vertical_data)), vertical_data)
                logger.info('Данные категории записаны в лист "category" вертикально.')
            else:
                logger.error('Ожидается SimpleNamespace для категории', exc_info=True)
                raise TypeError('Ожидается SimpleNamespace для категории.')

        except Exception as ex:
            logger.error('Ошибка записи данных категории в лист', ex, exc_info=True)
            raise

    def get_category_worksheet(self) -> SimpleNamespace:
        """
        Читает данные категории из листа 'category'.

        :return: Объект SimpleNamespace с данными категории.
        """
        try:
            ws: Worksheet = self.get_worksheet('category')
            if not ws:
                logger.error('Лист "category" не найден')
                return None
            data = ws.get_all_values()
            category_data = SimpleNamespace(
                name=data[1][1],
                title=data[2][1],
                description=data[3][1],
                tags=data[4][1].split(', '),
                products_count=int(data[5][1]),
            )

            logger.info('Данные категории прочитаны из листа "category".')
            return category_data

        except Exception as ex:
            logger.error('Ошибка чтения данных категории из листа', ex, exc_info=True)
            raise

    def set_categories_worksheet(self, categories: SimpleNamespace):
        """
        Записывает данные категорий в лист 'categories'.

        :param categories: Объект SimpleNamespace с данными категорий.
        """
        ws: Worksheet = self.get_worksheet('categories')
        if not ws:
            logger.error('Лист "categories" не найден')
            return
        try:
            start_row = 2
            for attr_name in dir(categories):
                attr_value = getattr(categories, attr_name, None)

                if not isinstance(attr_value, SimpleNamespace) or not any(
                    hasattr(attr_value, field) for field in ['name', 'title', 'description', 'tags', 'products_count']
                ):
                    continue

                _ = attr_value.__dict__
                name = _.get('name', '')
                title = _.get('title')
                description = _.get('description')
                tags = ', '.join(map(str, _.get('tags', [])))
                products_count = _.get('products_count', '~')

                updates = [
                    {'range': f'A{start_row}', 'values': [[name]]},
                    {'range': f'B{start_row}', 'values': [[title]]},
                    {'range': f'C{start_row}', 'values': [[description]]},
                    {'range': f'D{start_row}', 'values': [[tags]]},
                    {'range': f'E{start_row}', 'values': [[products_count]]},
                ]

                if updates:
                    ws.batch_update(updates)
                    logger.info(f'Данные категории записаны в лист "categories" для {attr_name}.')

                start_row += 1

        except Exception as ex:
            logger.error('Ошибка записи данных категорий в лист', ex, exc_info=True)
            raise

    def get_categories_worksheet(self) -> List[List[str]]:
        """
        Читает данные категорий из листа 'categories'.

         :return: Список строк с данными из столбцов A-E.
        """
        try:
            ws: Worksheet = self.get_worksheet('categories')
            if not ws:
                 logger.error('Лист "categories" не найден')
                 return None
            data = ws.get_all_values()
            data = [row[:5] for row in data[1:] if len(row) >= 5]
            logger.info('Данные категорий прочитаны из листа "categories".')
            return data

        except Exception as ex:
            logger.error('Ошибка чтения данных категорий из листа', ex, exc_info=True)
            raise

    def set_product_worksheet(self, product: SimpleNamespace | str, category_name: str):
        """
        Записывает данные продукта в новый лист Google Sheets.

        :param category_name: Имя категории.
        :param product: Объект SimpleNamespace с данными продукта.
        """
        time.sleep(1)
        ws = self.copy_worksheet('product_template', category_name)
        try:
            headers = [
                'product_id',
                'app_sale_price',
                'original_price',
                'sale_price',
                'discount',
                'product_main_image_url',
                'local_saved_image',
                'product_small_image_urls',
                'product_video_url',
                'local_saved_video',
                'first_level_category_id',
                'first_level_category_name',
                'second_level_category_id',
                'second_level_category_name',
                'target_sale_price',
                'target_sale_price_currency',
                'target_app_sale_price_currency',
                'target_original_price_currency',
                'original_price_currency',
                'product_title',
                'evaluate_rate',
                'promotion_link',
                'shop_url',
                'shop_id',
                'tags',
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
                ', '.join(map(str, _.get('tags', []))),
            ]

            ws.update('A2:Y2', [row_data])
            logger.info('Данные продукта записаны в лист.')

        except Exception as ex:
            logger.error('Ошибка записи данных продукта в лист', ex, exc_info=True)
            raise

    def get_product_worksheet(self) -> SimpleNamespace:
        """
        Читает данные продукта из листа 'products'.

        :return: Объект SimpleNamespace с данными продукта.
        """
        try:
            ws: Worksheet = self.get_worksheet('products')
            if not ws:
                logger.error('Лист "products" не найден')
                return None

            data = ws.get_all_values()
            product_data = SimpleNamespace(
                id=data[1][1],
                name=data[2][1],
                title=data[3][1],
                description=data[4][1],
                tags=data[5][1].split(', '),
                price=float(data[6][1]),
            )

            logger.info('Данные продукта прочитаны из листа "products".')
            return product_data

        except Exception as ex:
            logger.error('Ошибка чтения данных продукта из листа', ex, exc_info=True)
            raise

    def set_products_worksheet(self, category_name: str):
        """
        Записывает данные продуктов в лист.

        :param category_name: Имя категории.
        """
        if not category_name:
             logger.warning(f'Не найдена категория')
             return

        category_ns: SimpleNamespace = getattr(self.campaign.category, category_name,None)
        if not category_ns:
            logger.warning(f'Не найдена категория {category_name}')
            return
        products_ns: SimpleNamespace = category_ns.products
        ws: Worksheet = self.get_worksheet(category_name)
        if not ws:
            logger.error(f'Не найден лист {category_name}')
            return

        try:
            updates: list = []
            for index, value in enumerate(products_ns, start=2):
                _ = value.__dict__
                updates.append({'range': f'A{index}', 'values': [[str(_.get('product_id', ''))]]})
                updates.append({'range': f'B{index}', 'values': [[str(_.get('product_title', ''))]]})
                updates.append({'range': f'C{index}', 'values': [[str(_.get('title', ''))]]})
                updates.append({'range': f'D{index}', 'values': [[str(_.get('local_saved_image', ''))]]})
                updates.append({'range': f'E{index}', 'values': [[str(_.get('product_video_url', ''))]]})
                updates.append({'range': f'F{index}', 'values': [[str(_.get('original_price', ''))]]})
                updates.append({'range': f'G{index}', 'values': [[str(_.get('app_sale_price', ''))]]})
                updates.append({'range': f'H{index}', 'values': [[str(_.get('target_sale_price', ''))]]})
                updates.append({'range': f'I{index}', 'values': [[str(_.get('target_sale_price', ''))]]})

            ws.batch_update(updates)
            logger.info('Данные продуктов записаны в лист.')

        except Exception as ex:
            logger.error('Ошибка записи данных продуктов в лист', ex, exc_info=True)
            raise

    def delete_products_worksheets(self):
        """
        Удаляет все листы, кроме 'categories', 'product', 'category' и 'campaign'.
        """
        excluded_titles = {'categories', 'product', 'category', 'campaign'}
        try:
            worksheets = self.spreadsheet.worksheets()
            for sheet in worksheets:
                if sheet.title not in excluded_titles:
                    self.spreadsheet.del_worksheet_by_id(sheet.id)
                    logger.info(f"Лист '{sheet.title}' удален.")
        except Exception as ex:
            logger.error('Ошибка удаления листов', ex, exc_info=True)
            raise

    def save_categories_from_worksheet(self, update: bool = False):
        """
        Сохраняет данные категорий из листа Google Sheets.

        :param update: Флаг для обновления кампании.
        """
        edited_categories: list[dict] = self.get_categories_worksheet()
        if not edited_categories:
            logger.warning(f"Нет данных категорий для сохранения")
            return

        _categories_ns: SimpleNamespace = SimpleNamespace()
        for _cat in edited_categories:
            _cat_ns: SimpleNamespace = SimpleNamespace(
                **{
                    'name': _cat[0],
                    'title': _cat[1],
                    'description': _cat[2],
                    'tags': _cat[3].split(','),
                    'products_count': _cat[4],
                }
            )
            setattr(_categories_ns, _cat_ns.name, _cat_ns)
        self.campaign.category = _categories_ns
        if update:
            self.update_campaign()

    def save_campaign_from_worksheet(self):
        """
        Сохраняет данные кампании из листа Google Sheets.
        """
        self.save_categories_from_worksheet(False)
        data = self.get_campaign_worksheet()
        if not data:
            logger.warning("Нет данных кампании для сохранения")
            return

        data.category = self.campaign.category
        self.campaign = data
        self.update_campaign()