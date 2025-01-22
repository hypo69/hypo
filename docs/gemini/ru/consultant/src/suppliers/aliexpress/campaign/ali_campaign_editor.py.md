### Анализ кода модуля `ali_campaign_editor`

**Качество кода**:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код в целом структурирован и разбит на логические блоки.
    - Используется `SimpleNamespace` для представления данных, что удобно.
    - Присутствует начальная документация в формате docstring.
    - Используется асинхронность там, где это необходимо (например, `get_category_products`).
- **Минусы**:
    - Используются двойные кавычки для строк, за исключением некоторых мест, где используются одинарные.
    - В некоторых местах отсутствуют комментарии, особенно в сложных блоках кода, где требуется пояснение логики.
    - Некоторые блоки `try-except` могли бы быть более гранулярными и информативными в логах.
    - Не везде используется `logger.error` с `exc_info=True` для отслеживания ошибок.
    - Есть смешивание стилей импорта.

**Рекомендации по улучшению**:

1. **Форматирование строк**:
   - Заменить все двойные кавычки на одинарные, кроме случаев вывода в лог или `print`.
2. **Комментарии**:
   - Добавить комментарии к сложным участкам кода, например, в цикле `for` в методе `delete_product`.
   - Использовать RST-документацию для всех методов и классов для более чёткого описания.
3. **Обработка ошибок**:
   - Использовать `logger.error` с `exc_info=True` для более полной информации об ошибках.
   - Уточнить сообщения об ошибках, чтобы они были более информативными.
   - Улучшить обработку исключений в методе `delete_product`, более чётко указывая, какая ошибка произошла.
4. **Логирование**:
   -  Импортировать `logger` из `src.logger.logger`.
5. **Импорты**:
   - Упорядочить импорты согласно PEP8.
6. **Именование**:
    -  Использовать `_product_id` в методе `delete_product` только в случае, если это действительно внутренняя переменная, иначе стоит использовать `product_id`.
7. **Общая структура**:
    - В методе `delete_product` стоит пересмотреть логику обработки, если продукт есть в `sources.txt` или нет, разделив на отдельные блоки.
8. **Проверка наличия файлов**:
   - Перед переименованием файла в методе `delete_product`, стоит проверить, существует ли он.

**Оптимизированный код**:

```python
"""
Модуль для работы с редактором рекламных кампаний AliExpress.
============================================================

Модуль содержит класс :class:`AliCampaignEditor`, который используется для редактирования
рекламных кампаний на AliExpress.

Пример использования
----------------------
.. code-block:: python

    editor = AliCampaignEditor(campaign_name='Summer Sale', language='EN', currency='USD')
    editor.delete_product('12345')
"""

import asyncio
import re
import shutil
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace
from typing import List, Optional

import header
from src import gs
from src.suppliers.aliexpress.campaign.ali_promo_campaign import AliPromoCampaign
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet
from src.suppliers.aliexpress.utils import extract_prod_ids, ensure_https
from src.utils.jjson import j_loads_ns, j_loads, j_dumps
from src.utils.convertors.csv import csv2dict
from src.utils.printer import pprint
from src.utils.file_async import (
    read_text_file,
    get_filenames_from_directory,
    get_directory_names,
)
from src.logger.logger import logger


class AliCampaignEditor(AliPromoCampaign):
    """
    Редактор рекламных кампаний.

    :param campaign_name: Название кампании.
    :type campaign_name: str
    :param language: Язык кампании.
    :type language: Optional[str | dict], optional
    :param currency: Валюта кампании.
    :type currency: Optional[str], optional

    :Example:
        >>> editor = AliCampaignEditor(campaign_name='Summer Sale', language='EN', currency='USD')
    """

    def __init__(
        self,
        campaign_name: str,
        language: Optional[str | dict] = None,
        currency: Optional[str] = None,
    ):
        """
        Инициализация редактора кампании.

        :param campaign_name: Название кампании.
        :type campaign_name: str
        :param language: Язык кампании.
        :type language: Optional[str | dict], optional
        :param currency: Валюта кампании.
        :type currency: Optional[str], optional
        :raises CriticalError: Если не указано ни `campaign_name`, ни `campaign_file`.

        :Example:
            # 1. by campaign parameters
            >>> editor = AliCampaignEditor(campaign_name='Summer Sale', language='EN', currency='USD')
            # 2. load fom file
            >>> editor = AliCampaignEditor(campaign_name='Summer Sale', campaign_file='EN_USD.JSON')
        """
        ...
        super().__init__(campaign_name=campaign_name, language=language, currency=currency)
        # self.google_sheet = AliCampaignGoogleSheet(campaign_name = campaign_name, language = language, currency = currency, campaign_editor = self)

    def delete_product(self, product_id: str, exc_info: bool = False):
        """
        Удаляет продукт, у которого нет партнерской ссылки.

        :param product_id: ID продукта для удаления.
        :type product_id: str
        :param exc_info: Включать ли информацию об исключении в логи.
        :type exc_info: bool, optional

        :Example:
            >>> editor = AliCampaignEditor(campaign_name='Summer Sale')
            >>> editor.delete_product('12345')
        """
        _product_id = extract_prod_ids(product_id)

        product_path = self.category_path / 'sources.txt'
        prepared_product_path = self.category_path / '_sources.txt'
        products_list = read_text_file(product_path) # Читаем список товаров из файла
        
        if products_list: # Если список товаров не пустой
            for record in products_list:
                if _product_id:
                    record_id = extract_prod_ids(record)
                    if record_id == str(product_id):
                        products_list.remove(record)
                        save_text_file((products_list, '\n'), prepared_product_path)  # Сохраняем список товаров в файл
                        break
                else:
                    if record == str(product_id):
                        products_list.remove(record)
                        save_text_file((products_list, '\n'), product_path) # Сохраняем список товаров в файл
        else:
            product_path = self.category_path / 'sources' / f'{product_id}.html'
            try:
                if product_path.exists(): # Проверяем, существует ли файл
                     product_path.rename(self.category_path / 'sources' / f'{product_id}_.html') # Переименовываем файл
                     logger.success(f"Product file {product_path=} renamed successfully.")
                else:
                     logger.warning(f"Product file {product_path=} not found.")
            except FileNotFoundError as ex:
                logger.error(f"Product file {product_path=} not found.", exc_info=exc_info)
            except Exception as ex:
                logger.critical(f"An error occurred while deleting the product file {product_path}.", exc_info=True)

    def update_product(self, category_name: str, lang: str, product: dict):
        """
        Обновляет информацию о продукте в рамках категории.

        :param category_name: Имя категории, в которой нужно обновить продукт.
        :type category_name: str
        :param lang: Язык кампании.
        :type lang: str
        :param product: Словарь с данными продукта.
        :type product: dict

        :Example:
            >>> editor = AliCampaignEditor(campaign_name='Summer Sale')
            >>> editor.update_product('Electronics', 'EN', {'product_id': '12345', 'title': 'Smartphone'})
        """
        ...
        self.dump_category_products_files(category_name, lang, product)

    def update_campaign(self):
        """
        Обновляет свойства кампании, такие как `description`, `tags` и т.д.

        :Example:
            >>> editor = AliCampaignEditor(campaign_name='Summer Sale')
            >>> editor.update_campaign()
        """
        ...

    def update_category(self, json_path: Path, category: SimpleNamespace) -> bool:
        """
        Обновляет категорию в JSON-файле.

        :param json_path: Путь к JSON-файлу.
        :type json_path: Path
        :param category: Объект категории для обновления.
        :type category: SimpleNamespace
        :return: True, если обновление успешно, иначе False.
        :rtype: bool

        :Example:
            >>> category = SimpleNamespace(name='New Category', description='Updated description')
            >>> editor = AliCampaignEditor(campaign_name='Summer Sale')
            >>> result = editor.update_category(Path('category.json'), category)
            >>> print(result)  # True if successful
        """
        try:
            data = j_loads(json_path)  # Чтение JSON-данных из файла
            data['category'] = category.__dict__  # Преобразование SimpleNamespace в dict
            j_dumps(data, json_path)  # Запись обновленных JSON-данных обратно в файл
            return True
        except Exception as ex:
            logger.error(f'Failed to update category {json_path}: {ex}', exc_info=True)
            return False

    def get_category(self, category_name: str) -> Optional[SimpleNamespace]:
        """
        Возвращает объект SimpleNamespace для заданной категории.

        :param category_name: Имя категории для получения.
        :type category_name: str
        :return: Объект SimpleNamespace, представляющий категорию, или None, если не найдена.
        :rtype: Optional[SimpleNamespace]

        :Example:
            >>> editor = AliCampaignEditor(campaign_name='Summer Sale')
            >>> category = editor.get_category('Electronics')
            >>> print(category)  # SimpleNamespace или None
        """
        try:
            if hasattr(self.campaign.category, category_name):
                return getattr(self.campaign.category, category_name)
            else:
                logger.warning(f'Category {category_name} not found in the campaign.')
                return
        except Exception as ex:
            logger.error(f'Error retrieving category {category_name}.', ex, exc_info=True)
            return

    @property
    def list_categories(self) -> Optional[List[str]]:
        """
        Получает список категорий в текущей кампании.

        :return: Список имен категорий или None, если категории не найдены.
        :rtype: Optional[List[str]]

        :Example:
            >>> editor = AliCampaignEditor(campaign_name='Summer Sale')
            >>> categories = editor.categories_list
            >>> print(categories)  # ['Electronics', 'Fashion', 'Home']
        """
        try:
            if hasattr(self.campaign, 'category') and isinstance(
                self.campaign.category, SimpleNamespace
            ):
                return list(vars(self.campaign.category).keys())
            else:
                logger.warning('No categories found in the campaign.')
                return
        except Exception as ex:
            logger.error(f'Error retrieving categories list: {ex}', exc_info=True)
            return

    async def get_category_products(
        self, category_name: str
    ) -> Optional[List[SimpleNamespace]]:
        """
        Читает данные о товарах из JSON-файлов для конкретной категории.

        :param category_name: Имя категории.
        :type category_name: str
        :return: Список объектов SimpleNamespace, представляющих товары.
        :rtype: Optional[List[SimpleNamespace]]

        :Example:
            >>> products = campaign.get_category_products('Electronics')
            >>> print(len(products))
            15
        """
        category_path = (
            self.base_path
            / 'category'
            / category_name
            / f'{self.language}_{self.currency}'
        )
        json_filenames = await get_filenames_from_directory(
            category_path, extensions='json'
        )
        products = []

        if json_filenames:
            for json_filename in json_filenames:
                product_data = j_loads_ns(category_path / json_filename)
                product = SimpleNamespace(**vars(product_data))
                products.append(product)
            return products
        else:
            logger.error(
                f'No JSON files found for {category_name=} at {category_path=}.\\nStart prepare category'
            )
            self.process_category_products(category_name)
            return