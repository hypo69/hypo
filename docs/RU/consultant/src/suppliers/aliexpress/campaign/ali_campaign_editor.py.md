# Анализ кода модуля `ali_campaign_editor`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован, с использованием классов и методов для управления кампаниями.
    - Присутствует базовая документация для классов и методов в формате docstring.
    - Используется `SimpleNamespace` для представления данных, что упрощает доступ к атрибутам.
    - Присутствуют проверки на наличие атрибутов перед их использованием.
    - Активно используется асинхронность.
    - Добавлены логирование через `logger`.

- Минусы
    - Не везде используется `logger.error` для обработки исключений, иногда используется `print(ex)`.
    - Некоторые docstring не соответствуют стандарту reStructuredText (RST), например нет разделения на Args, Returns, Examples.
    - В некоторых методах отсутствуют docstring.
    - Есть избыточное использование `try-except` блоков без `logger.error`.
    - Отсутствуют проверки типов данных.
    - Использование `...` как заглушки.
    - Не все комментарии достаточно информативные.
    - В некоторых местах используются двойные кавычки в коде, где должны быть одинарные.
    - Не все импорты отсортированы и сгруппированы.

**Рекомендации по улучшению**

1.  **Импорты**:
    -   Сгруппировать импорты: сначала стандартные библиотеки, затем сторонние, затем локальные.
    -   Добавить недостающие импорты, например `from src.logger import logger`.
2.  **Документация**:
    -   Привести docstring к стандарту RST.
    -   Добавить docstring для всех методов, включая `__init__` и `update_campaign`, с примерами использования.
    -   Более подробно описать аргументы и возвращаемые значения функций.
3.  **Обработка ошибок**:
    -   Заменить `print(ex)` на `logger.error(f"Описание ошибки", ex, exc_info=True)`.
    -   Убрать лишние try-except блоки, где это возможно, и заменить их на более конкретную обработку ошибок.
4.  **Форматирование кода**:
    -   Использовать одинарные кавычки в коде, кроме строк, предназначенных для вывода (например, в `print()` и `logger.error()`).
    -   Привести код в соответствие с PEP8.
5.  **Комментарии**:
    -   Добавить комментарии, объясняющие назначение каждого блока кода.
6.  **Общее**:
    -   Избегать использования `...` в коде.
    -   Добавить проверки типов данных там где это нужно.
    -   Разделить длинные строки на несколько.
    -   Использовать константы вместо магических значений.

**Оптимизированный код**

```python
"""
Модуль для работы с редактором рекламных кампаний AliExpress.
=========================================================================================

Этот модуль предоставляет класс :class:`AliCampaignEditor`, который используется для управления рекламными кампаниями
на AliExpress, включая добавление, удаление и обновление товаров и категорий.

Пример использования
--------------------

Пример создания экземпляра класса `AliCampaignEditor`:

.. code-block:: python

    editor = AliCampaignEditor(campaign_name='Summer Sale', language='EN', currency='USD')
    # Или используя загрузку из файла
    editor = AliCampaignEditor(campaign_name='Summer Sale', campaign_file='EN_USD.json')
"""

import asyncio
import re
import shutil
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace
from typing import List, Optional

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
    Редактор для управления рекламными кампаниями.
    """
    def __init__(
        self,
        campaign_name: str,
        language: Optional[str | dict] = None,
        currency: Optional[str] = None,
        campaign_file: Optional[str | Path] = None,
    ):
        """
        Инициализирует редактор рекламных кампаний.

        Args:
            campaign_name (str): Название кампании.
            language (Optional[str | dict]): Язык кампании, по умолчанию 'EN'.
            currency (Optional[str]): Валюта кампании, по умолчанию 'USD'.
            campaign_file (Optional[str | Path]): Путь к файлу кампании, если загрузка из файла.

        Raises:
            ValueError: Если не указано ни `campaign_name`, ни `campaign_file`.

        Example:
            >>> editor = AliCampaignEditor(campaign_name='Summer Sale', language='EN', currency='USD')
            >>> editor = AliCampaignEditor(campaign_name='Summer Sale', campaign_file='EN_USD.json')
        """
        if not campaign_name and not campaign_file:
            logger.error("Необходимо указать либо `campaign_name`, либо `campaign_file`.")
            raise ValueError("Необходимо указать либо `campaign_name`, либо `campaign_file`.")

        super().__init__(campaign_name=campaign_name, language=language, currency=currency)
        # self.google_sheet = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency, campaign_editor=self)

    def delete_product(self, product_id: str, exc_info: bool = False):
        """
        Удаляет продукт, у которого нет партнерской ссылки.

        Args:
            product_id (str): ID удаляемого продукта.
            exc_info (bool): Включать ли информацию об исключении в логи.

        Example:
            >>> editor = AliCampaignEditor(campaign_name='Summer Sale')
            >>> editor.delete_product('12345')
        """
        _product_id = extract_prod_ids(product_id)
        
        product_path = self.category_path / 'sources.txt'
        prepared_product_path = self.category_path / '_sources.txt'
        
        products_list = read_text_file(product_path)
        
        if products_list:
            for record in products_list:
                if _product_id:
                    record_id = extract_prod_ids(record)
                    if record_id == str(product_id):
                        products_list.remove(record)
                        save_text_file(prepared_product_path, '\n'.join(products_list))
                        break
                else:
                    if record == str(product_id):
                        products_list.remove(record)
                        save_text_file(product_path, '\n'.join(products_list))
                        break # Выход из цикла после удаления
        else:
            product_path = self.category_path / 'sources' / f'{product_id}.html'
            try:
                product_path.rename(self.category_path / 'sources' / f'{product_id}_.html')
                logger.success(f"Файл продукта {product_path=} успешно переименован.")
            except FileNotFoundError as ex:
                logger.error(f"Файл продукта {product_path=} не найден.", ex, exc_info=exc_info)
            except Exception as ex:
                logger.critical(f"Возникла ошибка при удалении файла продукта {product_path}.", ex)

    def update_product(self, category_name: str, lang: str, product: dict):
        """
        Обновляет данные продукта в указанной категории.

        Args:
            category_name (str): Название категории для обновления.
            lang (str): Язык кампании.
            product (dict): Словарь с данными продукта.

        Example:
            >>> editor = AliCampaignEditor(campaign_name='Summer Sale')
            >>> editor.update_product('Electronics', 'EN', {'product_id': '12345', 'title': 'Smartphone'})
        """
        self.dump_category_products_files(category_name, lang, product)

    def update_campaign(self):
        """
        Обновляет свойства кампании, такие как описание и теги.

        Example:
            >>> editor = AliCampaignEditor(campaign_name='Summer Sale')
            >>> editor.update_campaign()
        """
        ...

    def update_category(self, json_path: Path, category: SimpleNamespace) -> bool:
        """
        Обновляет категорию в JSON-файле.

        Args:
            json_path (Path): Путь к JSON-файлу.
            category (SimpleNamespace): Объект SimpleNamespace с данными категории.

        Returns:
            bool: True, если обновление прошло успешно, False в противном случае.

        Example:
            >>> category = SimpleNamespace(name='New Category', description='Updated description')
            >>> editor = AliCampaignEditor(campaign_name='Summer Sale')
            >>> result = editor.update_category(Path('category.json'), category)
            >>> print(result)  # True, если обновление успешно
        """
        try:
            data = j_loads(json_path)  # Чтение данных JSON из файла
            data['category'] = category.__dict__  # Преобразование SimpleNamespace в словарь
            j_dumps(data, json_path)  # Запись обновленных данных JSON обратно в файл
            return True
        except Exception as ex:
            logger.error(f"Не удалось обновить категорию {json_path}: {ex}", exc_info=True)
            return False

    def get_category(self, category_name: str) -> Optional[SimpleNamespace]:
        """
        Возвращает объект SimpleNamespace для заданной категории.

        Args:
            category_name (str): Название категории.

        Returns:
             Optional[SimpleNamespace]: Объект SimpleNamespace, представляющий категорию, или None, если категория не найдена.

        Example:
             >>> editor = AliCampaignEditor(campaign_name='Summer Sale')
             >>> category = editor.get_category('Electronics')
             >>> print(category)  # SimpleNamespace или None
        """
        try:
            if hasattr(self.campaign.category, category_name):
                return getattr(self.campaign.category, category_name)
            else:
                logger.warning(f"Категория {category_name} не найдена в кампании.")
                return None
        except Exception as ex:
            logger.error(f"Ошибка при получении категории {category_name}.", ex, exc_info=True)
            return None

    @property
    def list_categories(self) -> Optional[List[str]]:
        """
        Возвращает список категорий в текущей кампании.

        Returns:
            Optional[List[str]]: Список названий категорий, или None, если категории не найдены.

        Example:
            >>> editor = AliCampaignEditor(campaign_name='Summer Sale')
            >>> categories = editor.list_categories
            >>> print(categories)  # ['Electronics', 'Fashion', 'Home']
        """
        try:
            # Проверка наличия атрибута category и его типа SimpleNamespace
            if hasattr(self.campaign, 'category') and isinstance(
                self.campaign.category, SimpleNamespace
            ):
                return list(vars(self.campaign.category).keys())
            else:
                logger.warning("В кампании не найдены категории.")
                return None
        except Exception as ex:
            logger.error(f"Ошибка при получении списка категорий: {ex}", exc_info=True)
            return None

    async def get_category_products(
        self, category_name: str
    ) -> Optional[List[SimpleNamespace]]:
        """
        Получает данные о товарах из JSON-файлов для конкретной категории.

        Args:
            category_name (str): Название категории.

        Returns:
            Optional[List[SimpleNamespace]]: Список объектов SimpleNamespace, представляющих товары, или None в случае ошибки.

        Example:
            >>> products = await editor.get_category_products("Electronics")
            >>> print(len(products))
            15
        """
        category_path = (
            self.base_path
            / 'category'
            / category_name
            / f'{self.language}_{self.currency}'
        )
        json_filenames = await get_filenames_from_directory(category_path, extensions='json')
        products = []

        if json_filenames:
            for json_filename in json_filenames:
                product_data = j_loads_ns(category_path / json_filename)
                product = SimpleNamespace(**vars(product_data))
                products.append(product)
            return products
        else:
            logger.error(
                f"Не найдены JSON-файлы для {category_name=}. {category_path=}.\\nНачата подготовка категории."
            )
            self.process_category_products(category_name)
            return None
```