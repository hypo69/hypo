## \file /src/endpoints/prestashop/product.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
.. module:: src.endopoints.prestashop.product
    :platform: Windows, Unix
    :synopsis: Interaction between website, product, and PrestaShop.
Defines the behavior of a product in the project.

"""
import asyncio
from dataclasses import dataclass, field
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




class PrestaProduct(PrestaShop):
    """Manipulations with the product.
    Initially, I instruct the grabber to fetch data from the product page,
    and then work with the PrestaShop API.
    """

    def __init__(self, api_key:str, api_domain:str, *args, **kwargs):
        """
        Initializes a Product object.

        """

        super().__init__( api_key = api_key, api_domain = api_domain, *args, **kwargs)

    def get_schema(self):
        """Get the schema for the product resource from PrestaShop.
        Returns:
            dict: The schema for the product resource.
        """
        return self.get('products', schema=True)

    def get_parent_category(self, id_category: int) -> Optional[int]:
        """Retrieve parent categories from PrestaShop for a given category recursively.

        Args:
            id_category (int): The category ID.

        Returns:
            parent category id (int).
        """
        try:
            category_response: dict = self.read(
                'categories', resource_id=id_category, display='full', io_format='JSON'
            )['categories'][0]

            return int(category_response['id_parent'])
        except Exception as ex:
            logger.error(f"Error retrieving category with ID {id_category}: ",ex)
            return

        if not category_response:
            logger.error(f"No category found with ID {id_category}.")
            return



    def _add_parent_categories(self, f: ProductFields) -> None:
            """Calculates and appends all parent categories for a list of category IDs to the ProductFields object.

            Args:
                f (ProductFields): The ProductFields object to append parent categories to.
                category_ids (List[int]): List of category IDs.
            """

            for _c in f.additional_categories :
                cat_id:int = int(_c['id']) #   {'id':'value'}
                if cat_id in (1,2): # <-- корневые категории prestashop Здесь можно добавить другие фильтры
                    continue

                while cat_id > 2:
                    cat_id:Optional[int] = self.get_parent_category(cat_id)
                    if cat_id:
                       f.additional_category_append(cat_id)
                    else:
                        break

    def get_product(self, id_product:int, **kwards):
        """"""
        return self.read(resource = 'products', resource_id = id_product, **kwards)

    def add_new_product(self, f: ProductFields) -> dict:
        """
        Add a new product to PrestaShop.

        Args:
            f (ProductFields): An instance of the ProductFields data class containing the product information.

        Returns:
            ProductFields | None: Returns the `ProductFields` object with `id_product` set, if the product was added successfully, `None` otherwise.
        """

        #  Дополняю id_category_default в поле `additional_categories` для поиска её родительских категорий
        f.additional_category_append(f.id_category_default)

        self._add_parent_categories(f)

        presta_product_dict: dict = f.to_dict()

        ...
        kwards = {
            'io_format': 'JSON', # may be 'XML' or 'JSON'
            'language': 2,
        }

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ DEBUG Try sending data in XML format ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #          Convert the dictionary to XML format for PrestaShop.
        # j_dumps(presta_product_dict, gs.path.endpoints / 'emil' / '_experiments' / f'presta_product_dict.{gs.now}.json')
        # xml_data: str = presta_fields_to_xml({"product": presta_product_dict})
        # kwards['io_format'] = 'XML'
        # response = self._exec(resource='products', method='POST', data=xml_data, **kwards)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        response = self.create('products', data={'products': presta_product_dict}, **kwards)

        if response:
            try:
                f.reference = response['product']['reference'] if isinstance(response['product']['reference'], str) else int(response['product']['reference'])

                logger.info(f"Product added: {presta_product_dict.get('name')}")
                return f
            except (KeyError, TypeError) as ex:
                logger.error(f"Ошибка при разборе ответа от сервера: {ex}", exc_info=True)
                return {}
        else:
            logger.error(f"Ошибка при добавлении товара:\n{print(print_data=presta_product_dict, text_color='yellow')}", exc_info=True)
            return {}

    async def add_new_product_async(self, f: ProductFields) -> dict:
        """
        Asynchronously add a new product to PrestaShop.

        Args:
            f (ProductFields): An instance of the ProductFields data class containing the product information.

        Returns:
            ProductFields | None: Returns the `ProductFields` object with `id_product` set, if the product was added successfully, `None` otherwise.
        """

        #  Дополняю id_category_default в поле `additional_categories` для поиска её родительских категорий
        f.additional_category_append(f.id_category_default)

        self._add_parent_categories(f)

        presta_product_dict: dict = f.to_dict()

        kwards = {
            'io_format': 'XML',
            'language': 2,
        }

        # Convert the dictionary to XML format for PrestaShop.
        data: str = presta_fields_to_xml({"product": presta_product_dict})

        try:
            response = await self._exec_async(resource='products', method='POST', data=data, io_format = kwards['io_format'], **kwards)
            #response = self.create('products', data={'product': presta_product_dict}, **kwards)

            if response:
                try:
                    f.reference = response['product']['reference'] if isinstance(response['product']['reference'], str) else int(response['product']['reference'])
                    logger.info(f"Product added: {presta_product_dict.get('name')}")
                    return f
                except (KeyError, TypeError) as ex:
                    logger.error(f"Ошибка при разборе ответа от сервера: {ex}", exc_info=True)
                    return {}
            else:
                logger.error(f"Ошибка при добавлении товара:\n{print(print_data=presta_product_dict, text_color='yellow')}", exc_info=True)
                return {}

        except Exception as e:
            logger.exception(f"An exception occurred while adding product asynchronously: {e}")
            return {}


def example_add_new_product():
    """ Пример для добавления товара в Prestashop """

    # 1. Конфигурация API
    USE_ENV:bool = False # <- True - использую переменные окружения, False - использую параметры из keepass

    MODE:str = 'dev8'

    if MODE == 'dev':
        host = gs.credentials.presta.client.dev_emil_design.api_domain
        api_key = gs.credentials.presta.client.dev_emil_design.api_key
    if MODE == 'dev8':
        host = gs.credentials.presta.client.dev8_emil_design.api_domain
        api_key = gs.credentials.presta.client.dev8_emil_design.api_key
    else:
        host = gs.credentials.presta.client.emil_design.api_domain if USE_ENV else os.getenv('HOST')
        api_key = gs.credentials.presta.client.emil_design.api_key if USE_ENV else os.getenv('API_KEY')


    p = PrestaProduct(api_key=api_key, api_domain=host)

    # schema = p.get_schema()
    # j_dumps(schema, gs.path.endpoints / 'emil' / '_experiments' / f'product_schema.{gs.now}.json')


    #example_data:dict = j_loads(gs.path.endpoints / 'emil' / '_experiments' / 'example_input.json')
    example_data:dict = j_loads(gs.path.endpoints / 'emil' / '_experiments' / 'example_input_2.json') # <- XML like

    if not example_data:
        logger.error(f"Файл не существует или неправильный формат файла")
        ...
        return
    presta_product_dict:dict = {'product':example_data}
    presta_product_xml = presta_fields_to_xml(presta_product_dict) # <- XML

    # 1. JSON
    kwards:dict = {
    'io_format':'XML',
    }
    response = p._exec(resource='products', method='POST', data= presta_product_dict  if kwards['io_format'] == 'JSON' else presta_product_xml,  **kwards)
    #response = p.create('products', data=presta_product_dict  if kwards['io_format'] == 'JSON' else presta_product_xml, **kwards)
    #j_dumps(response if kwards['io_format'] == 'JSON' else xml2dict(response), gs.path.endpoints / 'emil' / '_experiments' / f"{gs.now}_presta_response_new_product_added.json")

    print(response)
    ...

def example_get_product(id_product:int, **kwards):
    """"""
    USE_ENV:bool = False # <- True - использую переменные окружения, False - использую параметры из keepass
    MODE:str = 'dev8'

    if MODE == 'dev':
        host = gs.credentials.presta.client.dev_emil_design.api_domain
        api_key = gs.credentials.presta.client.dev_emil_design.api_key
    if MODE == 'dev8':
        host = gs.credentials.presta.client.dev8_emil_design.api_domain
        api_key = gs.credentials.presta.client.dev8_emil_design.api_key
    else:
        host = gs.credentials.presta.client.emil_design.api_domain if USE_ENV else os.getenv('HOST')
        api_key = gs.credentials.presta.client.emil_design.api_key if USE_ENV else os.getenv('API_KEY')


    p = PrestaProduct(api_key=api_key, api_domain=host)
    kwards:dict = {
    'io_format':'JSON',

    }
    presta_product = p.get_product(id_product, **kwards)
    presta_product = presta_product[0] if isinstance(presta_product, list) else presta_product
    ...
    j_dumps(presta_product, gs.path.endpoints / 'emil' / '_experiments' / f'presta_response_product_{id_product}.json')
    ...



if __name__ == '__main__':
    """"""
    example_add_new_product()

    #example_get_product(4)
    ...











# --- executor.py --- from scenario module

async def execute_prestashop_insert(dict_presta_fields: Dict, dict_assist_fields: Dict) -> bool:
    """!
    Adds or checks for the existence of a product. Makes sequential connection to the PrestaShop API.

    @param dict_presta_fields Dictionary of product fields for addition.
    @param dict_assist_fields Dictionary of auxiliary fields.

    @return True if the product was successfully added or checked, False in case of an error.

     This is a very bad solution. But this is not a hack, but a check of operability.
    @note In this solution, I sequentially connect to the prestashop connectors emil-design.com / e-cat.co.il.
    @todo Make multithreading (or asynchronous) here.
    @todo The nose for the caribou.
    """

    """! For each product, I redefine the `Product` class anew, otherwise garbage (data from the previous product) may end up """
    ...

    # 5.1 build API request filter
    reference = dict_presta_fields["reference"]
    search_filter: Dict = {'filter[reference]': '[' + reference + ']'}
    """! For `V3` I can pass the filter as a string `filter[id] = [5]` and as a dictionary `{'filter[id]':'[5]'}`.
    By default, I use a dictionary."""
    display: Dict = {'display': 'full'}
    search_filter.update(display)

    # 5.2 check for the presence of the product in the client's database
    """! @todo Bad solution. I'm making too many connections """
    for api_credentials in gs.list_prestashop_api_credentials:  ## <- I'm working with several clients (emil-design, e-cat, sergey.mymaster)
        """! Connecting to each!!! client in turn. @todo Good only for testing, bad in production """

        #p = Product (api_credentials)
        presta_client = PrestaClient(api_credentials)
        logger.info(f"""Presta client: {api_credentials['API_DOMAIN']}""")

        # 5.2.1 Get response from prestashop.
        check_prod_presence: dict = presta_client.get('products', search_filter=search_filter)
        """!
        - If the product does not yet exist in the database, an empty value will be returned.  (None)
        - If the product already exists, I get a dictionary of fields and edit the fields if they have changed (price, description, etc.)
        - If there was an error adding the product to prestashop, False will be returned.
        @todo - write the logic for saving price history
        """



        if not check_prod_presence or len(check_prod_presence) == 0:
            """! An empty response came back from the server. Adding a new product to the client's database """

            # 6.1 Translations
            try:
                """! I get a dictionary with all translations of product fields into all client languages """
                ...
                client_languages_schema = presta_client.get_languages_schema()
                dict_presta_fields = translate_dict_presta_fields(dict_presta_fields, dict_assist_fields['page_lang'], client_languages_schema)
                ...

            except Exception as ex:
                logger.error(f'Error translating product fields', ex)
                ...

            try:
                """! Add a new product to the client's prestashop database
                I get a dictionary with the parameters of the added product in response
                - get a dictionary of fields of the newly added product
                - If there was an error adding the product to prestashop, False will be returned"""
                new_product_dict: dict = presta_client.add(resource='products', data={'product': dict_presta_fields}, io_format='JSON')[0]
                logger.success(f"""Product successfully added reference: - {new_product_dict['reference']}""")
                ...

            except Exception as ex:
                logger.error(f""" Error adding a new product """, ex, True)
                return False

            #############################################################################
            #                                                                           #
            #                   IMAGES                                                  #
            #                                                                           #
            #############################################################################

            _start_time = int(time.time())
            uploaded_image_dict: dict = presta_client.upload_image('products', product_id, dict_assist_fields['product_image_default_url'], f"{new_product_dict['reference']}_main")
            """! @code
            {
                'product_id':'int',
                'image_id':'int',
                'cover':'int',
                'position':'int',
                'legend':'{dict}'}

            @endcode
            """
            if not uploaded_image_dict:
                logger.error(f"Image did not add\n{dict_assist_fields['product_image_default_url']}")
                ...
            logger.warning(f""" ... one image was added in {int(time.time()) - _start_time} seconds """)
            # 7.2.2 add the default image id to the product
            new_product_dict['id_default_image'] = uploaded_image_dict['id']
            ...
            i = 0  # <- counter
            # 7.2.3 Save other images
            for url in dict_assist_fields['product_images_additional_urls']:
                i += 1
                # saved_img_dict: dict = presta_client.upload_image(product_id, url, f"{dict_presta_fields['referense']}_{i}")

                # if not 'images' in  new_product_dict['associations'].keys():
                #     new_product_dict['associations'].update({'images':{'image':[]}})

                # new_product_dict['associations']['images']['image'].append({'id': saved_img_dict['id']})
                uploaded_image_dict: dict = presta_client.upload_image('products', product_id, url, f"{dict_presta_fields['reference']}_{i}")
                new_product_dict['associations']['images']['image'].append({'id': uploaded_image_dict['id']})
            ...

            """! @debug """
            logger.warning(f"""Images successfully uploaded in {int(time.time()) - _start_time} seconds """)
            if os.path.exists(f'{dict_presta_fields["reference"]}_dict_presta_fields.json'):  # Check if the file exists
                os.remove(f'{dict_presta_fields["reference"]}_dict_presta_fields.json')
            if os.path.exists(f'{dict_presta_fields["reference"]}_dict_assist_fields.json'):  # Check if the file exists
                os.remove(f'{dict_presta_fields["reference"]}_dict_assist_fields.json')
            ...
    # 8. The product already exists in the prestashop db
    else:
        logger.success("The product is already in the client's database")
        """! @todo The product is in the db. Implement editing """
        ...