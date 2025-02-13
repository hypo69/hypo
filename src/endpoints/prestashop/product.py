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
from src.utils.convertors.any import any2dict
from src.utils.jjson import j_dumps
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


    def get_parent_categories(self, id_category: int, _parents:list[dict] = []) -> List[Dict[str, int]]:
        """Retrieve parent categories from PrestaShop for a given category recursively.

        Args:
            id_category (int): The category ID.

        Returns:
            List[Dict[str, int]]: A list of parent category dictionaries (each with an 'id' key),
                                   excluding root categories (ID 1 and 2).
        """
        try:
            category_response: dict = self.read(
                'categories', resource_id=id_category, display='full', io_format='JSON'
            )['categories'][0]
        except Exception as e:
            logger.error(f"Error retrieving category with ID {id_category}: {e}")
            return []

        if not category_response:
            logger.error(f"No category found with ID {id_category}.")
            return []

        _parent_category = int(category_response['id_parent']) or 0

        if _parent_category <= 2:  # Categories with id 1 and 2 are root categories
            return _parents  # Base case: stop recursion at root categories
        else:
            _parents.append({'id': _parent_category})
            self.get_parent_categories(_parent_category, _parents)  # Recursive call

        return _parents

    def add_new_product(self, f: ProductFields) -> dict:
        """
        Add a new product to PrestaShop.

        Args:
            f (ProductFields): An instance of the ProductFields data class containing the product information.

        Returns:
            ProductFields | None: Returns the `ProductFields` object with `id_product` set, if the product was added successfully, `None` otherwise.
        """
        
        # Дополняю категории в поле `additional_categories`
        calculated_categories:list = []
        additional_categories:list[dict] = f.additional_categories['category']
        additional_categories.append({"id":f.id_category_default})  # <- -- Добавляю основную категорию
        for c in additional_categories:
            for key, cat_id in c.items():
                try:
                    cat_id=int(cat_id)
                    parents = self.get_parent_categories(cat_id)
                    if parents:
                        calculated_categories.extend(parents)

                except ValueError as ex:
                    logger.error(f"Ошибка формата категории. Должно быть число. Плучил {cat_id}",ex)
                    continue



        presta_product_dict:dict = f.to_dict()
        presta_product_dict['name'] = presta_product_dict['name'][0]['value']
        presta_product_dict['description'] = presta_product_dict['description'][0]['value']

        # ~~~~~~~~~~~~~~~~~~ DEBUG ~~~~~~~~~~~~~~~~~~
        schema = j_dumps(presta_product_dict, gs.path.endpoints / 'emil' / '_experiments' / 'product_schema_new.json')

        response = self.create('products', data={'product': presta_product_dict}, io_format='JSON')
        if response:
            try:
                f.id_product = int(response['product']['id'])
                logger.info(f"Product added: {presta_product_dict.get('name')}")
                return f
            except (KeyError, TypeError) as ex:
                logger.error(f"Ошибка при разборе ответа от сервера: {ex}", exc_info=True)
                return {}
        else:
            logger.error(f"Ошибка при добавлении товара:\n{print(print_data=presta_product_dict, text_color='yellow')}", exc_info=True)
            return {}


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
        check_prod_presence: Union[None, dict] = presta_client.get('products', search_filter=search_filter)
        """! 
        - If the product does not yet exist in the database, an empty value will be returned.  (None)
        - If the product already exists, I get a dictionary of fields and edit the fields if they have changed (price, description, etc.)
        - If there was an error adding the product to prestashop, False will be returned.        
        @todo - write the logic for saving price history
        """

        """! @debug """
        def create_debug_files():
            j_dumps(dict_presta_fields, Path(gs.dir_tmp, f'{dict_presta_fields["reference"]}_dict_presta_fields.json'))
            j_dumps(dict_assist_fields, Path(gs.dir_tmp, f'{dict_presta_fields["reference"]}_dict_assist_fields.json'))
        create_debug_files()
        ...

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
                new_product_dict: Union[dict, False] = presta_client.add(resource='products', data={'product': dict_presta_fields}, io_format='JSON')[0]
                logger.success(f"""Product successfully added reference: - {new_product_dict['reference']}""")
                ...

            except Exception as ex:
                logger.error(f""" Error adding a new product """, ex, True)
                return False

            #############################################################################
            #                                                                           #
            #                   IMAGES                                                #
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



async def main():
    # Example usage
    product = PrestaProduct()
    product_fields = ProductFields(
        lang_index = 1,
        name='Test Product Async',
        price=19.99,
        description='This is an asynchronous test product.',
    )
    


    new_product = product.add_new_product(product_fields)
    if new_product:
        print(f'New product id = {new_product.id_product}')
    else:
        print(f'Error add new product')

    product.fetch_data_async()

if __name__ == '__main__':
    asyncio.run(main())