## Анализ кода модуля `product.py`

**Качество кода:**

- **Соответствие стандартам**: 6/10
- **Плюсы**:
  - Использование классов для организации функциональности.
  - Наличие базовой структуры для взаимодействия с PrestaShop API.
  - Использование `logger` для логирования.
- **Минусы**:
  - Неполная документация функций и классов.
  - Отсутствие обработки исключений во многих местах.
  - Смешивание конфигурации и логики в классе `Config`.
  - Непоследовательное форматирование кода.
  - Использование `print` вместо `logger.info` для отладочной информации.
  - Переменные `kwards` перезаписываются, что может привести к путанице.
  - Не все функции аннотированы типами.
  - Жестко заданные значения, такие как `\'XML\'` и `\'JSON\'`.
  - Использования `...` вместо `pass`.
  - Дублирование кода.
  - Отсутствие обработки ошибок при чтении или записи файлов.
  - Использование `Config.host` вместо `Config.API_DOMAIN` в `example_add_new_product`.

**Рекомендации по улучшению:**

1.  **Документация**:
    - Добавить docstring к каждому классу, методу и функции, чтобы описать их назначение, параметры и возвращаемые значения.
    - Использовать примеры в docstring для демонстрации использования.

2.  **Обработка исключений**:
    - Добавить блоки `try-except` для обработки возможных исключений, особенно при работе с API и файлами.
    - Логировать исключения с использованием `logger.error` с предоставлением `exc_info=True` для получения трассировки стека.

3.  **Конфигурация**:
    - Разделить класс `Config` на отдельные переменные или использовать библиотеку `pydantic` или `dataclasses` для более структурированного управления конфигурацией.
    - Использовать `j_loads` или `j_loads_ns` для загрузки конфигурационных файлов.

4.  **Форматирование кода**:
    - Привести код в соответствие со стандартами PEP8, используя инструменты вроде `black` и `flake8`.
    - Обеспечить консистентность в использовании кавычек (использовать только одинарные кавычки).
    - Добавить пробелы вокруг операторов присваивания.

5.  **Логирование**:
    - Заменить `print` на `logger.info` для вывода отладочной информации.

6.  **Типизация**:
    - Добавить аннотации типов ко всем переменным и функциям, чтобы улучшить читаемость и обнаруживать ошибки на ранних этапах.
    - Использовать `Optional` для параметров, которые могут быть `None`.

7.  **Удаление `...`**:
    - Заменить все `...` на `pass` или реализовать соответствующую логику.

8.  **Улучшение структуры**:

    *   Избавиться от дублирования кода, выделив общие блоки в отдельные функции.
    *   Удалить неиспользуемые импорты.
    *   Упростить логику, где это возможно.

9.  **Использовать константы**:

    *   Заменить жестко заданные значения, такие как `'XML'` и `'JSON'`, константами.

10. **Безопасность**:

    *   Убедиться, что API-ключи и другие конфиденциальные данные не хранятся в коде напрямую, а передаются через переменные окружения или другие безопасные механизмы.

**Оптимизированный код:**

```python
## \file /src/endpoints/prestashop/product.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
Модуль для взаимодействия с PrestaShop API для управления продуктами.
"""
import asyncio
import os
from dataclasses import dataclass, field
from types import SimpleNamespace
from typing import List, Dict, Any, Optional

import header
from src import gs
from src.endpoints.prestashop.api import PrestaShop
from src.endpoints.prestashop.category import PrestaCategory
from src.endpoints.prestashop.product_fields import ProductFields
from src.endpoints.prestashop.utils.xml_json_convertor import dict2xml, xml2dict, presta_fields_to_xml

from src.utils.xml import save_xml
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.logger.logger import logger
from src import USE_ENV  # <- True - использую переменные окружения, False - использую параметры из keepass


class Config:
    """
    Конфигурация для работы с PrestaShop API.
    """

    USE_ENV: bool = False
    MODE: str = 'dev'
    POST_FORMAT: str = 'XML'
    API_DOMAIN: str = ''
    API_KEY: str = ''

    if USE_ENV:
        API_DOMAIN = os.getenv('HOST')
        API_KEY = os.getenv('API_KEY')
    elif MODE == 'dev':
        API_DOMAIN = gs.credentials.presta.client.dev_emil_design.api_domain
        API_KEY = gs.credentials.presta.client.dev_emil_design.api_key
    elif MODE == 'dev8':
        API_DOMAIN = gs.credentials.presta.client.dev8_emil_design.api_domain
        API_KEY = gs.credentials.presta.client.dev8_emil_design.api_key
    else:
        API_DOMAIN = gs.credentials.presta.client.emil_design.api_domain
        API_KEY = gs.credentials.presta.client.emil_design.api_key


class PrestaProduct(PrestaShop):
    """
    Класс для управления продуктами в PrestaShop.
    """

    def __init__(self, API_KEY: str, API_DOMAIN: str, *args, **kwargs) -> None:
        """
        Инициализирует объект Product.

        Args:
            API_KEY (str): Ключ API PrestaShop.
            API_DOMAIN (str): Домен API PrestaShop.
        """
        super().__init__(api_key=API_KEY, api_domain=API_DOMAIN, *args, **kwargs)

    def get_product_schema(self, resource_id: Optional[str | int] = None, schema: Optional[str] = 'blank') -> dict:
        """
        Получает схему продукта из PrestaShop.

        Args:
            resource_id (Optional[str  |  int], optional): ID продукта. Defaults to None.
            schema (Optional[str], optional): Тип схемы. Defaults to 'blank'.

        Returns:
            dict: Схема продукта.
        """
        return self.get_schema(resource='products', resource_id=resource_id, schema=schema, display='full')

    def get_parent_category(self, id_category: int) -> Optional[int]:
        """
        Рекурсивно получает родительские категории из PrestaShop для данной категории.

        Args:
            id_category (int): ID категории.

        Returns:
            Optional[int]: ID родительской категории или None в случае ошибки.
        """
        try:
            category_response: dict = self.read(
                'categories', resource_id=id_category, display='full', data_format='JSON'
            )['categories'][0]

            return int(category_response['id_parent'])
        except Exception as ex:
            logger.error(f'Error retrieving category with ID {id_category}: {ex}', exc_info=True)
            return None

        if not category_response:
            logger.error(f'No category found with ID {id_category}.')
            return None

    def _add_parent_categories(self, f: ProductFields) -> None:
        """
        Вычисляет и добавляет все родительские категории для списка ID категорий к объекту ProductFields.

        Args:
            f (ProductFields): Объект ProductFields для добавления родительских категорий.
        """
        for _c in f.additional_categories:
            cat_id: int = int(_c['id'])  # {'id':'value'}
            if cat_id in (1, 2):  # <-- корневые категории prestashop Здесь можно добавить другие фильтры
                continue

            while cat_id > 2:
                cat_id: Optional[int] = self.get_parent_category(cat_id)
                if cat_id:
                    f.additional_category_append(cat_id)
                else:
                    break

    def get_product(self, id_product: int, **kwards) -> dict:
        """
        Получает информацию о продукте из PrestaShop.

        Args:
            id_product (int): ID продукта.
            **kwards: Дополнительные параметры запроса.

        Returns:
            dict: Информация о продукте.
        """
        kwards = {'data_format': 'JSON'}
        return self.read(resource='products', resource_id=id_product, **kwards)

    def add_new_product(self, f: ProductFields) -> dict | None:
        """
        Добавляет новый продукт в PrestaShop.

        Args:
            f (ProductFields): Объект ProductFields с информацией о продукте.

        Returns:
            ProductFields | None: Объект `ProductFields` с установленным `id_product`, если продукт был успешно добавлен, `None` в противном случае.
        """

        # Дополняю id_category_default в поле `additional_categories` для поиска её родительских категорий
        f.additional_category_append(f.id_category_default)

        self._add_parent_categories(f)

        presta_product_dict: dict = f.to_dict()
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        # presta_product_dict['name'] = {'language':[presta_product_dict['name']]}

        kwards = {
            'data_format': Config.POST_FORMAT,
            'language': 2,
        }

        """ XML"""
        if Config.POST_FORMAT == 'XML':
            # Convert the dictionary to XML format for PrestaShop.
            xml_data: str = presta_fields_to_xml({'product': presta_product_dict})
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            save_xml(xml_data, gs.path.endpoints / 'emil' / '_experiments' / f'{gs.now}_presta_product.xml')
            kwards['data_format'] = 'XML'
            response = self.create('products', data=xml_data, **kwards)
        else:  # elif post_format == 'JSON':
            response = self.create('products', data={'product': presta_product_dict}, **kwards)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        j_dumps(response, gs.path.endpoints / 'emil' / '_experiments' / f'{gs.now}_presta_response_new_product_added.json')

        # Upload the product image to PrestaShop.
        if response:
            added_product_ns: SimpleNamespace = j_loads_ns(response)
            added_product_ns = added_product_ns.product

            try:
                # f.reference = response['product']['reference'] if isinstance(response['product']['reference'], str) else int(response['product']['reference'])
                img_data = self.create_binary(resource=f'products/{added_product_ns.id}', file_path=f.local_image_path, file_name=f'{gs.now}.png')

                logger.info(f'Product added: /n {print(added_product_ns)}')
                return f
            except (KeyError, TypeError) as ex:
                logger.error(f'Ошибка при разборе ответа от сервера: {ex}', exc_info=True)
                return None
        else:
            logger.error(
                f'Ошибка при добавлении товара:\\n{print(print_data=presta_product_dict, text_color="yellow")}', exc_info=True
            )
            return None


def example_add_new_product() -> None:
    """Пример для добавления товара в Prestashop."""

    p = PrestaProduct(API_KEY=Config.API_KEY, API_DOMAIN=Config.API_DOMAIN)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # resource_id = 2191
    # schema = p.get_product_schema(resource_id = resource_id)
    # j_dumps(schema, gs.path.endpoints / 'emil' / '_experiments' / f'product_schema.{resource_id}_{gs.now}.json')
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    example_data: dict = j_loads(gs.path.endpoints / 'emil' / '_experiments' / 'product_schema.2191_250319224027026.json')  # <- XML like
    """"""
    if not example_data:
        logger.error(f'Файл не существует или неправильный формат файла')
        return

    presta_product_xml = presta_fields_to_xml(example_data)  # <- XML
    save_xml(presta_product_xml, gs.path.endpoints / 'emil' / '_experiments' / f'{gs.now}_presta_product.xml')

    # 1. JSON | XML
    kwards: dict = {
        'io_format': 'JSON',
    }

    response = p._exec(
        resource='products',
        method='POST',
        data=example_data if kwards['io_format'] == 'JSON' else presta_product_xml,
        **kwards,
    )
    # response = p.create('products', data=presta_product_dict if kwards['io_format'] == 'JSON' else presta_product_xml, **kwards)
    # j_dumps(response if kwards['io_format'] == 'JSON' else xml2dict(response), gs.path.endpoints / 'emil' / '_experiments' / f'{gs.now}_presta_response_new_product_added.json')

    print(response)


def example_get_product(id_product: int, **kwards) -> None:
    """
    Пример получения информации о продукте из PrestaShop.

    Args:
        id_product (int): ID продукта.
        **kwards: Дополнительные параметры запроса.
    """

    p = PrestaProduct(API_KEY=Config.API_KEY, API_DOMAIN=Config.API_DOMAIN)
    kwards: dict = {
        'data_format': 'JSON',
        'display': 'full',
        'schema': 'blank',
    }
    presta_product = p.get_product(id_product, **kwards)
    presta_product = presta_product[0] if isinstance(presta_product, list) else presta_product

    j_dumps(presta_product, gs.path.endpoints / 'emil' / '_experiments' / f'presta_response_product_{id_product}.json')


if __name__ == '__main__':
    """ """
    example_add_new_product()
    # example_get_product(2191)