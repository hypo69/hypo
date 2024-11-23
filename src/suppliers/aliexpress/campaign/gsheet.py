## \file hypotez/src/suppliers/aliexpress/campaign/gsheet.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.suppliers.aliexpress.campaign 
	:platform: Windows, Unix
	:synopsis:  Редактор рекламной кампании через гугл таблицами

"""
MODE = 'dev'

import time
from types import SimpleNamespace
from typing import Optional, Any
#from src.webdriver import Driver, Chrome, Firefox, Edge
from gspread.worksheet import Worksheet
from src.goog.spreadsheet.spreadsheet import SpreadSheet
from src.utils import j_dumps
from src.utils import pprint
from src.logger import logger


from src.ai.openai import translate
from types import SimpleNamespace
from typing import Optional, List, Dict
# from gspread.worksheet import Worksheet
# from gspread_formatting import (
#     cellFormat, 
#     textFormat, 
#     numberFormat, 
#     format_cell_range,
#     set_column_width,
#     set_row_height,
#     Color
# )
# from src.goog.spreadsheet.spreadsheet import SpreadSheet
from src.utils import pprint
from src.logger import logger

class AliCampaignGoogleSheet(SpreadSheet):
    """ Класс для работы с Google Sheets в рамках кампаний AliExpress.
    
    Наследует класс SpreadSheet и предоставляет дополнительные методы для управления листами Google Sheets,
    записи данных о категориях и продуктах, и форматирования листов.
    """
    
    spreadsheet_id = '1nu4mNNFMzSePlggaaL_QM2vdKVP_NNBl2OG7R9MNrs0'
    spreadsheet: SpreadSheet = None
    worksheet: Worksheet = None
   

    def __init__(self, campaign_name: str, language: str | dict = None, currency: str = None):
        """ Initialize AliCampaignGoogleSheet with specified Google Sheets spreadsheet ID and additional parameters.
        @param campaign_name `str`: The name of the campaign.
        @param category_name `str`: The name of the category.   
        @param language `str`: The language for the campaign.
        @param currency `str`: The currency for the campaign.
        """
        # Initialize SpreadSheet with the spreadsheet ID
        super().__init__(spreadsheet_id = self.spreadsheet_id)
        #self.capmaign_editor = AliCampaignEditor(campaign_name=campaign_name, language=language, currency=currency)
        # if campaign_editor:
        #     self.set_campaign_worksheet(campaign_editor.campaign)
        #     self.set_categories_worksheet(campaign_editor.campaign.category)
        
        
    def clear(self):
        """ Clear contents.
        Delete product sheets and clear data on the categories and other specified sheets.
        """
        try:
            self.delete_products_worksheets()
        except Exception as ex:
            logger.error("Ошибка очистки", ex)
            
    def delete_products_worksheets(self):
        """ Delete all sheets from the Google Sheets spreadsheet except 'categories' and 'product_template'.
        """
        excluded_titles = {'categories', 'product', 'category', 'campaign'}
        try:
            worksheets = self.spreadsheet.worksheets()
            for sheet in worksheets:
                if sheet.title not in excluded_titles:
                    self.spreadsheet.del_worksheet_by_id(sheet.id)
                    logger.success(f"Worksheet '{sheet.title}' deleted.")
        except Exception as ex:
            logger.error("Error deleting all worksheets.", ex, exc_info=True)
            raise
        
    def set_campaign_worksheet(self, campaign: SimpleNamespace):
        """ Write campaign data to a Google Sheets worksheet.
        @param campaign `SimpleNamespace | str`: SimpleNamespace object with campaign data fields for writing.
        @param language `str`: Optional language parameter.
        @param currency `str`: Optional currency parameter.
        """
        try:
            ws: Worksheet = self.get_worksheet('campaign')  # Clear the 'campaign' worksheet
        
            # Prepare data for vertical writing
            updates = []
            vertical_data = [
                ('A1', 'Campaign Name', campaign.campaign_name),
                ('A2', 'Campaign Title', campaign.title),
                ('A3', 'Campaign Language', campaign.language),
                ('A4', 'Campaign Currency', campaign.currency),
                ('A5', 'Campaign Description', campaign.description),              
                
            ]
        
            # Add update operations to batch_update list
            for cell, header, value in vertical_data:
                updates.append({'range': cell, 'values': [[header]]})
                updates.append({'range': f'B{cell[1]}', 'values': [[str(value)]]})
        
            # Perform batch update
            if updates:
                ws.batch_update(updates)
        
            logger.info("Campaign data written to 'campaign' worksheet vertically.")
        
        except Exception as ex:
            logger.error("Error setting campaign worksheet.", ex, exc_info=True)
            raise
        
    def set_products_worksheet(self, category_name: str):
        """ Write data from a list of SimpleNamespace objects to Google Sheets cells.
        @param category_name `str`: The name of the category to fetch products from.
        """
        if category_name:
            category: SimpleNamespace = getattr(self.editor.campaign.category, category_name)
            products: list[SimpleNamespace] = category.products
        else:
            logger.warning(f"No products found for {category=}\n{products=}.")
            return
    
        ws = self.copy_worksheet('product', category_name)
    
        try:
            # headers = [
            #     'product_id', 'app_sale_price', 'original_price', 'sale_price', 'discount',
            #     'product_main_image_url', 'local_saved_image', 'product_small_image_urls',
            #     'product_video_url', 'local_saved_video', 'first_level_category_id',
            #     'first_level_category_name', 'second_level_category_id', 'second_level_category_name',
            #     'target_sale_price', 'target_sale_price_currency', 'target_app_sale_price_currency',
            #     'target_original_price_currency', 'original_price_currency', 'product_title',
            #     'evaluate_rate', 'promotion_link', 'shop_url', 'shop_id', 'tags'
            # ]
            # updates = [{'range': 'A1:Y1', 'values': [headers]}]  # Add headers to the worksheet

            row_data = []
            for product in products:
                _ = product.__dict__
                row_data.append([
                    str(_.get('product_id')),
                    _.get('product_title'),
                    _.get('promotion_link'),
                    str(_.get('app_sale_price')),
                    _.get('original_price'),
                    _.get('sale_price'),
                    _.get('discount'),
                    _.get('product_main_image_url'),
                    _.get('local_saved_image'),
                    ', '.join(_.get('product_small_image_urls', [])),
                    _.get('product_video_url'),
                    _.get('local_saved_video'),
                    _.get('first_level_category_id'),
                    _.get('first_level_category_name'),
                    _.get('second_level_category_id'),
                    _.get('second_level_category_name'),
                    _.get('target_sale_price'),
                    _.get('target_sale_price_currency'),
                    _.get('target_app_sale_price_currency'),
                    _.get('target_original_price_currency'),
                    _.get('original_price_currency'),
                    
                    _.get('evaluate_rate'),
                    
                    _.get('shop_url'),
                    _.get('shop_id'),
                    ', '.join(_.get('tags', []))
                ])
            
            for index, row in enumerate(row_data, start=2):
                ws.update(f'A{index}:Y{index}', [row])
                logger.info(f"Products {str(_.get('product_id'))} updated .")

            self._format_category_products_worksheet(ws)

            logger.info("Products updated in worksheet.")


        except Exception as ex:
            logger.error("Error setting products worksheet.", ex, exc_info=True)
            raise

    def set_categories_worksheet(self, categories: SimpleNamespace):
        """ Запись данных из объекта SimpleNamespace с категориями в ячейки Google Sheets.
        @param categories `SimpleNamespace`: Объект, где ключи — это категории с данными для записи.
        """
        ws: Worksheet = self.get_worksheet('categories')
        ws.clear()  # Очистка рабочей таблицы перед записью данных
    
        try:
            # Получение всех ключей (категорий) и соответствующих значений
            category_data = categories.__dict__
        
            # Проверка, что все объекты категории имеют необходимые атрибуты
            required_attrs = ['name', 'title', 'description', 'tags', 'products_count']
        
            if all(all(hasattr(category, attr) for attr in required_attrs) for category in category_data.values()):
                # Заголовки для таблицы
                headers = ['Name', 'Title', 'Description', 'Tags', 'Products Count']
                ws.update('A1:E1', [headers])
            
                # Подготовка данных для записи
                rows = []
                for category in category_data.values():
                    row_data = [
                        category.name,
                        category.title,
                        category.description,
                        ', '.join(category.tags),
                        category.products_count,
                    ]
                    rows.append(row_data)
            
                # Обновляем строки данных
                ws.update(f'A2:E{1 + len(rows)}', rows)
            
                # Форматируем таблицу
                self._format_categories_worksheet(ws)
            
                logger.info("Category fields updated from SimpleNamespace object.")
            else:
                logger.warning("One or more category objects do not contain all required attributes.")
    
        except Exception as ex:
            logger.error("Error updating fields from SimpleNamespace object.", ex, exc_info=True)
            raise


    def get_categories(self):
        """ Получение данных из таблицы Google Sheets.
        @return Данные из таблицы в виде списка словарей.
        """
        ws = self.get_worksheet('categories') 
        data = ws.get_all_records()
        logger.info("Categories data retrieved from worksheet.")
        return data

    def set_category_products(self, category_name: str, products: dict):
        """ Запись данных о продуктах в новую таблицу Google Sheets.
        @param category_name Название категории.
        @param products Словарь с данными о продуктах.
        """
        if category_name:
            category_ns: SimpleNamespace = getattr(self.editor.campaign.category, category_name)
            products_ns: list[SimpleNamespace] = category_ns.products
        else:
            logger.warning("No products found for category.")
            return
    
        ws = self.copy_worksheet('product', category_name)
        try:
            headers = [
                'product_id', 'app_sale_price', 'original_price', 'sale_price', 'discount',
                'product_main_image_url', 'local_saved_image', 'product_small_image_urls',
                'product_video_url', 'local_saved_video', 'first_level_category_id',
                'first_level_category_name', 'second_level_category_id', 'second_level_category_name',
                'target_sale_price', 'target_sale_price_currency', 'target_app_sale_price_currency',
                'target_original_price_currency', 'original_price_currency', 'product_title',
                'evaluate_rate', 'promotion_link', 'shop_url', 'shop_id', 'tags'
            ]
            updates = [{'range': 'A1:Y1', 'values': [headers]}]  # Add headers to the worksheet

            row_data = []
            for product in products:
                _ = product.__dict__
                row_data.append([
                    str(_.get('product_id')),
                    str(_.get('app_sale_price')),
                    _.get('original_price'),
                    _.get('sale_price'),
                    _.get('discount'),
                    _.get('product_main_image_url'),
                    _.get('local_saved_image'),
                    ', '.join(_.get('product_small_image_urls', [])),
                    _.get('product_video_url'),
                    _.get('local_saved_video'),
                    _.get('first_level_category_id'),
                    _.get('first_level_category_name'),
                    _.get('second_level_category_id'),
                    _.get('second_level_category_name'),
                    _.get('target_sale_price'),
                    _.get('target_sale_price_currency'),
                    _.get('target_app_sale_price_currency'),
                    _.get('target_original_price_currency'),
                    _.get('original_price_currency'),
                    _.get('product_title'),
                    _.get('evaluate_rate'),
                    _.get('promotion_link'),
                    _.get('shop_url'),
                    _.get('shop_id'),
                    ', '.join(_.get('tags', []))
                ])
            
            for index, row in enumerate(row_data, start=2):
                ws.update(f'A{index}:Y{index}', [row])
                logger.info(f"Products {str(_.get('product_id'))} updated .")

            self._format_category_products_worksheet(ws)

            logger.info("Products updated in worksheet.")
        except Exception as ex:
            logger.error("Error updating products in worksheet.", ex, exc_info=True)
            raise

    def _format_categories_worksheet(self, ws: Worksheet):
        """ Форматирование листа 'categories'.
        @param ws Лист Google Sheets для форматирования.
        """
        try:
            # Установка ширины столбцов
            set_column_width(ws, 'A:A', 150)  # Ширина столбца A
            set_column_width(ws, 'B:B', 200)  # Ширина столбца B
            set_column_width(ws, 'C:C', 300)  # Ширина столбца C
            set_column_width(ws, 'D:D', 200)  # Ширина столбца D
            set_column_width(ws, 'E:E', 150)  # Ширина столбца E
            
            # Установка высоты строк
            set_row_height(ws, '1:1', 40)  # Высота заголовков

            # Форматирование заголовков
            header_format = cellFormat(
                textFormat=textFormat(bold=True, fontSize=12),
                horizontalAlignment='CENTER',
                verticalAlignment='MIDDLE',  # Добавлено вертикальное выравнивание
                backgroundColor=Color(0.8, 0.8, 0.8)  # Используем Color для задания цвета
            )
            format_cell_range(ws, 'A1:E1', header_format)

            logger.info("Categories worksheet formatted.")
        except Exception as ex:
            logger.error("Error formatting categories worksheet.", ex, exc_info=True)
            raise

    def _format_category_products_worksheet(self, ws: Worksheet):
        """ Форматирование листа с продуктами категории.
        @param ws Лист Google Sheets для форматирования.
        """
        try:
            # Установка ширины столбцов
            set_column_width(ws, 'A:A', 250)  # Ширина столбца A
            set_column_width(ws, 'B:B', 220)  # Ширина столбца B
            set_column_width(ws, 'C:C', 220)  # Ширина столбца C
            set_column_width(ws, 'D:D', 220)  # Ширина столбца D
            set_column_width(ws, 'E:E', 200)  # Ширина столбца E
            set_column_width(ws, 'F:F', 200)  # Ширина столбца F
            set_column_width(ws, 'G:G', 200)  # Ширина столбца G
            set_column_width(ws, 'H:H', 200)  # Ширина столбца H
            set_column_width(ws, 'I:I', 200)  # Ширина столбца I
            set_column_width(ws, 'J:J', 200)  # Ширина столбца J
            set_column_width(ws, 'K:K', 200)  # Ширина столбца K
            set_column_width(ws, 'L:L', 200)  # Ширина столбца L
            set_column_width(ws, 'M:M', 200)  # Ширина столбца M
            set_column_width(ws, 'N:N', 200)  # Ширина столбца N
            set_column_width(ws, 'O:O', 200)  # Ширина столбца O
            set_column_width(ws, 'P:P', 200)  # Ширина столбца P
            set_column_width(ws, 'Q:Q', 200)  # Ширина столбца Q
            set_column_width(ws, 'R:R', 200)  # Ширина столбца R
            set_column_width(ws, 'S:S', 200)  # Ширина столбца S
            set_column_width(ws, 'T:T', 200)  # Ширина столбца T
            set_column_width(ws, 'U:U', 200)  # Ширина столбца U
            set_column_width(ws, 'V:V', 200)  # Ширина столбца V
            set_column_width(ws, 'W:W', 200)  # Ширина столбца W
            set_column_width(ws, 'X:X', 200)  # Ширина столбца X
            set_column_width(ws, 'Y:Y', 200)  # Ширина столбца Y

            # Установка высоты строк
            set_row_height(ws, '1:1', 40)  # Высота заголовков

            # Форматирование заголовков
            header_format = cellFormat(
                textFormat=textFormat(bold=True, fontSize=12),
                horizontalAlignment='CENTER',
                verticalAlignment='TOP',  # Добавлено вертикальное выравнивание
                backgroundColor=Color(0.8, 0.8, 0.8)  # Используем Color для задания цвета
            )
            format_cell_range(ws, 'A1:Y1', header_format)

            logger.info("Category products worksheet formatted.")
        except Exception as ex:
            logger.error("Error formatting category products worksheet.", ex, exc_info=True)
            raise
        
    # def set_category_products(self, category_name: str, products: dict):
    #     """ Write product data to a new Google Sheets spreadsheet.
    #     @param category_name Category name.
    #     @param products Dictionary with product data.
    #     """
    #     time.sleep(10)
    #     ws = self.copy_worksheet('product_template', category_name)  # Copy 'product_template' to new worksheet
    #     try:
    #         headers = [
    #             'product_id', 'app_sale_price', 'original_price', 'sale_price', 'discount',
    #             'product_main_image_url', 'local_saved_image', 'product_small_image_urls',
    #             'product_video_url', 'local_saved_video', 'first_level_category_id',
    #             'first_level_category_name', 'second_level_category_id', 'second_level_category_name',
    #             'target_sale_price', 'target_sale_price_currency', 'target_app_sale_price_currency',
    #             'target_original_price_currency', 'original_price_currency', 'product_title',
    #             'evaluate_rate', 'promotion_link', 'shop_url', 'shop_id', 'tags'
    #         ]
    #         ws.update('A1:Y1', [headers])

    #         updates = []
    #         for index, product in enumerate(products, start=2):
    #             _ = product.__dict__
    #             row_data = [
    #                 str(_.get('product_id')),
    #                 str(_.get('app_sale_price')),
    #                 str(_.get('original_price')),
    #                 str(_.get('sale_price')),
    #                 str(_.get('discount')),
    #                 str(_.get('product_main_image_url')),
    #                 str(_.get('local_saved_image')),
    #                 ', '.join(map(str, _.get('product_small_image_urls', []))),
    #                 str(_.get('product_video_url')),
    #                 str(_.get('local_saved_video')),
    #                 str(_.get('first_level_category_id')),
    #                 str(_.get('first_level_category_name')),
    #                 str(_.get('second_level_category_id')),
    #                 str(_.get('second_level_category_name')),
    #                 str(_.get('target_sale_price')),
    #                 str(_.get('target_sale_price_currency')),
    #                 str(_.get('target_app_sale_price_currency')),
    #                 str(_.get('target_original_price_currency')),
    #                 str(_.get('original_price_currency')),
    #                 str(_.get('product_title')),
    #                 str(_.get('evaluate_rate')),
    #                 str(_.get('promotion_link')),
    #                 str(_.get('shop_url')),
    #                 str(_.get('shop_id')),
    #                 ', '.join(map(str, _.get('tags', [])))
    #             ]
    #             updates.append({
    #                 'range': f'A{index}:Y{index}',
    #                 'values': [row_data]
    #             })
            
    #         ws.batch_update(updates)

    #         logger.info("Products updated in worksheet.")
    #     except Exception as ex:
    #         logger.error("Error updating products in worksheet.", ex, exc_info=True)
    #         raise