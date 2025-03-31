## \file /src/endpoints/prestashop/product.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
```rst
.. module:: src.endopoints.prestashop.product
```

Модуль для взаимодействия с товарами в PrestaShop.
======================================================
Определяет логику взаимодействия с товарами в проекте.
"""
import asyncio
import os
from dataclasses import dataclass, field
# from re import U
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
from src.utils.printer import pprint as print
from src.logger.logger import logger
from src import USE_ENV  # <- True - использую переменные окружения, False - использую параметры из keepass


class Config:
    """Configuration class for PrestaShop product settings."""

    # 1. Конфигурация API
    USE_ENV: bool = False

    MODE: str = 'dev'
    POST_FORMAT = 'XML'
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
    """Manipulations with the product.

    Initially, I instruct the grabber to fetch data from the product page,
    and then work with the PrestaShop API.
    """

    def __init__(self, api_key: Optional[str] = '', api_domain: Optional[str] = '', *args, **kwargs) -> None:
        """Initializes a Product object.

        Args:
            api_key (Optional[str], optional): PrestaShop API key. Defaults to ''.
            api_domain (Optional[str], optional): PrestaShop API domain. Defaults to ''.

        Returns:
            None
        """
        super().__init__(
            api_key=api_key if api_key else Config.API_KEY,
            api_domain=api_domain if api_domain else Config.API_DOMAIN,
            *args,
            **kwargs,
        )

    def get_product_schema(self, resource_id: Optional[str | int] = None, schema: Optional[str] = 'blank') -> dict:
        """Get the schema for the product resource from PrestaShop.

        Args:
            resource_id (Optional[str  |  int], optional): The ID of the product resource. Defaults to None.
            schema (Optional[str], optional): The schema type. Defaults to 'blank'.

        Returns:
            dict: The schema for the product resource.
        """
        return self.get_schema(resource='products', resource_id=resource_id, schema=schema, display='full')

    def get_parent_category(self, id_category: int) -> Optional[int]:
        """Retrieve parent categories from PrestaShop for a given category recursively.

        Args:
            id_category (int): The category ID.

        Returns:
            Optional[int]: parent category id (int).
        """
        try:
            category_response: dict = self.read(
                'categories', resource_id=id_category, display='full', data_format='JSON'
            )['categories'][0]

            return int(category_response['id_parent'])
        except Exception as ex:
            logger.error(f'Error retrieving category with ID {id_category}: ', ex)
            return

        if not category_response:
            logger.error(f'No category found with ID {id_category}.')
            return

    def _add_parent_categories(self, f: ProductFields) -> None:
        """Calculates and appends all parent categories for a list of category IDs to the ProductFields object.

        Args:
            f (ProductFields): The ProductFields object to append parent categories to.
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
        """Возваращает словарь полей товара из магазина Prestasop

        Args:
            id_product (int): значение поля ID в таблице `product` Preastashop

        Returns:
            dict:
            {
                'product':
                    {... product fields}
            }
        """
        kwards = {'data_format': 'JSON'}
        kwards = {'data_format': 'JSON'}
        return self.read(resource='products', resource_id=id_product, **kwards)

    def add_new_product(self, f: ProductFields) -> dict:
        """Add a new product to PrestaShop.

        Преобразовывает объект `ProducFields` в словарь формата `Prestashop` и отрапавлет его в API Престашоп

        Args:
            f (ProductFields): An instance of the ProductFields data class containing the product information.

        Returns:
            dict: Returns the `ProductFields` object with `id_product` set, if the product was added successfully, `None` otherwise.
        """

        # Дополняю id_category_default в поле `additional_categories` для поиска её родительских категорий
        f.additional_category_append(f.id_category_default)

        self._add_parent_categories(f)

        presta_product_dict: dict = f.to_dict()

        ...
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
        j_dumps(
            response,
            gs.path.endpoints / 'emil' / '_experiments' / f'{gs.now}_presta_response_new_product_added.json',
        )

        # Upload the product image to PrestaShop.
        if response:
            added_product_ns: SimpleNamespace = j_loads_ns(response)
            added_product_ns = added_product_ns.product
            ...
            try:
                # f.reference = response['product']['reference'] if isinstance(response['product']['reference'], str) else int(response['product']['reference'])
                img_data = self.create_binary(
                    resource=f'products/{added_product_ns.id}',
                    file_path=f.local_image_path,
                    file_name=f'{gs.now}.png',
                )

                logger.info(f'Product added: /n {print(added_product_ns)}')
                return f
            except (KeyError, TypeError) as ex:
                logger.error(f'Ошибка при разборе ответа от сервера: {ex}', exc_info=True)
                return {}
        else:
            logger.error(
                f"Ошибка при добавлении товара:\n{print(print_data=presta_product_dict, text_color='yellow')}",
                exc_info=True,
            )
            return {}










# ##################################################   EXAMPLES ##################################################


def example_add_new_product() -> None:
    """Пример для добавления товара в Prestashop"""

    p = PrestaProduct(API_KEY=Config.API_KEY, API_DOMAIN=Config.API_DOMAIN)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # resource_id = 2191
    # schema = p.get_product_schema(resource_id = resource_id)
    # j_dumps(schema, gs.path.endpoints / 'emil' / '_experiments' / f'product_schema.{resource_id}_{gs.now}.json')
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    example_data: dict = j_loads(
        gs.path.endpoints / 'emil' / '_experiments' / 'product_schema.2191_250319224027026.json'
    )  # <- XML like
    """"""
    if not example_data:
        logger.error(f'Файл не существует или неправильный формат файла')
        ...
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
    # response = p.create('products', data=presta_product_dict  if kwards['io_format'] == 'JSON' else presta_product_xml, **kwards)
    # j_dumps(response if kwards['io_format'] == 'JSON' else xml2dict(response), gs.path.endpoints / 'emil' / '_experiments' / f"{gs.now}_presta_response_new_product_added.json")

    print(response)
    ...


def example_get_product(id_product: int, **kwards) -> None:
    """"""

    p = PrestaProduct(API_KEY=Config.API_KEY, API_DOMAIN=Config.API_DOMAIN)
    kwards: dict = {
        'data_format': 'JSON',
        'display': 'full',
        'schema': 'blank',
    }
    presta_product = p.get_product(id_product, **kwards)
    presta_product = presta_product[0] if isinstance(presta_product, list) else presta_product
    ...
    j_dumps(
        presta_product, gs.path.endpoints / 'emil' / '_experiments' / f'presta_response_product_{id_product}.json'
    )
    ...


if __name__ == '__main__':
    """"""
    #example_add_new_product()
    example_get_product(2191)
    ...