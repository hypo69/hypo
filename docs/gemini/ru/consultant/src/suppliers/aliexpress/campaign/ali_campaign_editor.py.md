## Анализ кода модуля `ali_campaign_editor.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и разбит на логические блоки.
    - Используются `SimpleNamespace` для представления данных, что улучшает читаемость и упрощает доступ к атрибутам.
    - Применяется логирование для отслеживания ошибок и предупреждений.
    - Использование `j_loads_ns`, `j_loads`, `j_dumps` вместо стандартных `json` функций.
    - Наличие docstring для каждого класса, метода и функции, что соответствует стандартам оформления кода.

-  Минусы
    - Не все docstring содержат полные описания.
    - Не используется единый подход к обработке ошибок, некоторые `try-except` блоки можно заменить на логирование.
    -  Присутствуют не используемые закомментированные строки кода.
    -  В некоторых местах не хватает подробных комментариев к коду.
    -  Использование `...` в коде, что может затруднить отладку.
    -  В некоторых функциях не возвращается значение в случае возникновения исключения, что может приводить к неоднозначному поведению.
    -  Не все функции имеют примеры использования в docstring.
    - Не все исключения обрабатываются с помощью `exc_info=True`, что может затруднить отладку.
    -  В коде используются литеральные значения для путей, что может привести к ошибкам.
    -  Отсутствуют проверки на корректность аргументов функций.

**Рекомендации по улучшению**
1. **Документация**:
   - Дополнить docstring для всех функций и методов, добавив более подробное описание параметров, возвращаемых значений и примеров использования.
   - Улучшить описания классов, добавить примеры использования.
   - Привести документацию в соответствие с reStructuredText (RST).
2. **Обработка ошибок**:
   - Заменить `try-except` блоки на `logger.error` с `exc_info=True` для более информативного логирования.
   - Добавить возвращаемые значения в случаях ошибок для большей предсказуемости.
3. **Рефакторинг**:
    - Убрать неиспользуемые импорты и закомментированные строки кода.
    -  Использовать константы или переменные для путей к файлам.
    -  Добавить проверки на валидность аргументов функций.
    -  Удалить  `...`  в коде.
4. **Логирование**:
   - Добавить больше уровней логирования (например, debug, info).
   - Включить `exc_info=True` в `logger.error` для подробного логирования ошибок.
5. **Общие улучшения**:
   -  Добавить проверки на наличие файлов перед их открытием.
   -  Улучшить читаемость кода путем добавления комментариев к сложным участкам.
   -  Убрать  `...`  из кода.

**Оптимизированный код**
```python
"""
Модуль для редактирования рекламных кампаний AliExpress.
=========================================================================================

Этот модуль предоставляет класс :class:`AliCampaignEditor`, который позволяет редактировать рекламные кампании AliExpress,
включая добавление, удаление и обновление продуктов, категорий и параметров кампаний.

Модуль использует классы :class:`AliPromoCampaign`, :class:`AliCampaignGoogleSheet` для работы с данными.

Пример использования
--------------------

Пример создания и использования класса `AliCampaignEditor`:

.. code-block:: python

    from pathlib import Path

    editor = AliCampaignEditor(campaign_name="Summer Sale", language="EN", currency="USD")

    # Удаление продукта
    editor.delete_product("12345")

    # Обновление продукта
    editor.update_product("Electronics", "EN", {"product_id": "12345", "title": "Smartphone"})

    # Обновление категории
    category = SimpleNamespace(name="New Category", description="Updated description")
    editor.update_category(Path("category.json"), category)

    # Получение списка категорий
    categories = editor.list_categories
    print(categories)

    # Получение продуктов категории
    products = editor.get_category_products("Electronics")
    print(len(products))
"""


import re
import shutil
from pathlib import Path
from types import SimpleNamespace
from typing import List, Optional, Any

import header  # TODO: check this import, can be not used
from src import gs  # TODO: check this import, can be not used
from src.suppliers.aliexpress.campaign.ali_promo_campaign import AliPromoCampaign
from src.suppliers.aliexpress.campaign.gsheet import AliCampaignGoogleSheet # TODO: check this import, can be not used
from src.suppliers.aliexpress.utils import extract_prod_ids, ensure_https # TODO: check this import, can be not used
from src.utils.jjson import j_loads_ns, j_loads, j_dumps
from src.utils.convertors.csv import csv2dict # TODO: check this import, can be not used
from src.utils.printer import pprint # TODO: check this import, can be not used
from src.utils.file import read_text_file, save_text_file, get_filenames
from src.logger.logger import logger


class AliCampaignEditor(AliPromoCampaign):
    """
    Редактор для рекламных кампаний.

    :param campaign_name: Имя кампании.
    :type campaign_name: str
    :param language: Язык кампании.
    :type language: str | dict, optional
    :param currency: Валюта кампании.
    :type currency: str, optional
    """
    def __init__(self,
                 campaign_name: str,
                 language: Optional[str | dict] = None,
                 currency: Optional[str] = None):
        """
        Инициализирует класс `AliCampaignEditor` с заданными параметрами.

        :param campaign_name: Название кампании.
        :type campaign_name: str
        :param language: Язык кампании. Может быть строкой или словарем. По умолчанию `EN`.
        :type language: str | dict, optional
        :param currency: Валюта кампании. По умолчанию `USD`.
        :type currency: str, optional
        :raises ValueError: Если ни `campaign_name`, ни `campaign_file` не предоставлены.

        Пример использования:

        .. code-block:: python

            # 1. Инициализация с параметрами кампании
            editor = AliCampaignEditor(campaign_name="Summer Sale", language="EN", currency="USD")

            # 2. Загрузка из файла
            # editor = AliCampaignEditor(campaign_name="Summer Sale", campaign_file="EN_USD.JSON")
        """
        if not campaign_name:
            logger.error('`campaign_name` is required', exc_info=True)
            raise ValueError('`campaign_name` is required')
        super().__init__(campaign_name=campaign_name, language=language, currency=currency)
        # self.google_sheet = AliCampaignGoogleSheet(campaign_name = campaign_name, language = language, currency = currency, campaign_editor = self)


    def delete_product(self, product_id: str, exc_info: bool = False) -> None:
        """
        Удаляет продукт, у которого нет партнерской ссылки.

        :param product_id: ID продукта для удаления.
        :type product_id: str
        :param exc_info: Включать ли информацию об исключении в логи. По умолчанию `False`.
        :type exc_info: bool, optional
        :raises FileNotFoundError: Если файл продукта не найден.
        :raises Exception: Если произошла ошибка при удалении файла продукта.

        Пример использования:

        .. code-block:: python

            editor = AliCampaignEditor(campaign_name="Summer Sale")
            editor.delete_product("12345")
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
                        save_text_file((products_list, '\n'), prepared_product_path)
                        break
                else:
                    if record == str(product_id):
                        products_list.remove(record)
                        save_text_file((products_list, '\n'), product_path)

        else:
            product_path = self.category_path / 'sources' / f'{product_id}.html'
            try:
                # Переименование файла продукта
                product_path.rename(self.category_path / 'sources' / f'{product_id}_.html')
                logger.info(f"Product file {product_path=} renamed successfully.")
            except FileNotFoundError as ex:
                # Логирование ошибки, если файл не найден
                logger.error(f"Product file {product_path=} not found.", exc_info=exc_info)
                return
            except Exception as ex:
                # Логирование критической ошибки
                logger.critical(f"An error occurred while deleting the product file {product_path}.", ex, exc_info=True)
                return


    def update_product(self, category_name: str, lang: str, product: dict) -> None:
        """
        Обновляет информацию о продукте в заданной категории.

        :param category_name: Название категории, в которой нужно обновить продукт.
        :type category_name: str
        :param lang: Язык кампании.
        :type lang: str
        :param product: Словарь с данными продукта.
        :type product: dict

        Пример использования:

        .. code-block:: python

            editor = AliCampaignEditor(campaign_name="Summer Sale")
            editor.update_product("Electronics", "EN", {"product_id": "12345", "title": "Smartphone"})
        """
        self.dump_category_products_files(category_name, lang, product)

    def update_campaign(self) -> None:
        """
        Обновляет свойства кампании, такие как `description`, `tags` и т.д.
        
        Пример использования:

        .. code-block:: python
        
            editor = AliCampaignEditor(campaign_name="Summer Sale")
            editor.update_campaign()
        """
        ...

    def update_category(self, json_path: Path, category: SimpleNamespace) -> bool:
        """
        Обновляет категорию в JSON файле.

        :param json_path: Путь к JSON файлу.
        :type json_path: Path
        :param category: Объект категории для обновления.
        :type category: SimpleNamespace
        :return: `True`, если обновление прошло успешно, `False` в противном случае.
        :rtype: bool

        Пример использования:

        .. code-block:: python

            category = SimpleNamespace(name="New Category", description="Updated description")
            editor = AliCampaignEditor(campaign_name="Summer Sale")
            result = editor.update_category(Path("category.json"), category)
            print(result)  # True if successful
        """
        try:
            # Чтение JSON данных из файла
            if not json_path.exists():
                 logger.error(f"File not found: {json_path}", exc_info=True)
                 return False
            data = j_loads(json_path)
            # Преобразование SimpleNamespace в словарь и обновление данных категории
            data['category'] = category.__dict__
            # Запись обновленных данных обратно в файл
            j_dumps(data, json_path)
            return True
        except Exception as ex:
            # Логирование ошибки при обновлении категории
            logger.error(f"Failed to update category {json_path}: {ex}", exc_info=True)
            return False

    def get_category(self, category_name: str) -> Optional[SimpleNamespace]:
        """
        Возвращает объект `SimpleNamespace` для заданной категории.

        :param category_name: Название категории для получения.
        :type category_name: str
        :return: Объект `SimpleNamespace`, представляющий категорию, или `None`, если категория не найдена.
        :rtype: SimpleNamespace, optional

        Пример использования:

        .. code-block:: python

            editor = AliCampaignEditor(campaign_name="Summer Sale")
            category = editor.get_category("Electronics")
            print(category)  # SimpleNamespace or None
        """
        try:
            # Проверка наличия категории в кампании
            if hasattr(self.campaign.category, category_name):
                return getattr(self.campaign.category, category_name)
            else:
                # Логирование предупреждения, если категория не найдена
                logger.warning(f"Category {category_name} not found in the campaign.")
                return
        except Exception as ex:
            # Логирование ошибки при получении категории
            logger.error(f"Error retrieving category {category_name}.", ex, exc_info=True)
            return


    @property
    def list_categories(self) -> Optional[List[str]]:
        """
        Возвращает список категорий в текущей кампании.

        :return: Список названий категорий или `None`, если категории не найдены.
        :rtype: list, optional

        Пример использования:

        .. code-block:: python

            editor = AliCampaignEditor(campaign_name="Summer Sale")
            categories = editor.list_categories
            print(categories)  # ['Electronics', 'Fashion', 'Home']
        """
        try:
            # Проверка наличия атрибута category и что он является SimpleNamespace
            if hasattr(self.campaign, 'category') and isinstance(self.campaign.category, SimpleNamespace):
                # Возвращает список ключей атрибута category
                return list(vars(self.campaign.category).keys())
            else:
                # Логирование предупреждения, если категории не найдены
                logger.warning("No categories found in the campaign.")
                return
        except Exception as ex:
            # Логирование ошибки при получении списка категорий
            logger.error(f"Error retrieving categories list: {ex}", exc_info=True)
            return


    def get_category_products(
        self, category_name: str
    ) -> Optional[List[SimpleNamespace]]:
        """
        Читает данные о товарах из JSON файлов для конкретной категории.

        :param category_name: Имя категории.
        :type category_name: str
        :return: Список объектов `SimpleNamespace`, представляющих товары.
        :rtype: list, optional

        Пример использования:

        .. code-block:: python

            products = campaign.get_category_products("Electronics")
            print(len(products))
            # 15
        """
        category_path = (
            self.base_path
            / "category"
            / category_name
            / f"{self.language}_{self.currency}"
        )
        json_filenames = get_filenames(category_path, extensions="json")
        products = []

        if json_filenames:
            for json_filename in json_filenames:
                 # Чтение данных из JSON файла
                product_data = j_loads_ns(category_path / json_filename)
                if not product_data:
                   logger.error(f"Failed to load product data from {category_path / json_filename}")
                   continue
                # Преобразование данных в объект SimpleNamespace
                product = SimpleNamespace(**vars(product_data))
                products.append(product)
            return products
        else:
            # Логирование ошибки, если JSON файлы не найдены
            logger.error(
                f"No JSON files found for {category_name=} at {category_path=}. Start prepare category"
            )
            # Запуск подготовки продуктов категории
            self.process_category_products(category_name)
            return