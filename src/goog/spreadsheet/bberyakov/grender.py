## \file /src/goog/spreadsheet/bberyakov/grender.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.goog.spreadsheet.bberyakov 
	:platform: Windows, Unix
	:synopsis:

"""


"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""
  
""" module: src.goog.spreadsheet.bberyakov """


"""  Render Google Table

 
 @section libs imports:
  - json 
  - typing 
  - gspread_formatting 
  - gspread 
  - goog.helpers 
  - gspread.utils 
  
Author(s):
  - Created by [Davidka] [BenAvraham] on 08.11.2023 .
"""
# ------------------------------
from src import gs
from src.helpers import logger, WebDriverException,  pprint

# -------------------------------

import json
from typing import List, Type, Union
from spread_formatting import *
from spread import Spreadsheet, Worksheet
from goog.helpers import hex_color_to_decimal, decimal_color_to_hex, hex_to_rgb

from spread.utils import ValueInputOption, ValueRenderOption


class GSRender():
    """
     [Class's description]


    """
    """
     Table Render
    Украшательства. \n
    ------------------------------\n
    class CellFormat(\n
        \t numberFormat: Any | None = None,\n
        \t backgroundColor: Any | None = None,\n
        \t borders: Any | None = None,\n
        \t padding: Any | None = None,\n
        \t horizontalAlignment: Any | None = None,\n
        \t verticalAlignment: Any | None = None,\n
        \t wrapStrategy: Any | None = None,\n
        \t textDirection: Any | None = None,\n
        \t textFormat: Any | None = None,\n
        \t hyperlinkDisplayType: Any | None = None,\n
        \t textRotation: Any | None = None,\n
        \t backgroundColorStyle: Any | None = None\n
    )
    """
    render_schemas: dict
    
    

    def __init__ (self, *args, **kwards) -> None:
        """
         [Function's description]

        Parameters : 
             self : [description]
             *args : [description]
             **kwards : [description]
        Returns : 
             None : [description]

        """
        #self.render_schemas = json.loads('goog\\schema.json')
        ...
    
    def render_header (self, ws: Worksheet, world_title: str, range: str = 'A1:Z1', merge_type: str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') = 'MERGE_ALL' ) -> None:
        """
         Рисую заголовок таблицы в первой строке

        Parameters : 
             self : [description]
             ws : Worksheet : таблица в книге
             world_title : str : заголовок гугл таблицы
             range : 'A1:Z1' : диапазон ячеек
             merge_type : str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') = 'MERGE_ALL' : 'MERGE_ALL' | 'MERGE_COLUMNS' | 'MERGE_ROWS'
        Returns : 
             None : [description]

        """
        bg_color = hex_to_rgb ('#FFAAAA') 
        fg_color = hex_to_rgb ('#AAAAAA')
        
        fmt = CellFormat(
            backgroundColor = Color (bg_color[0]/255, bg_color[1]/255, bg_color[2]/255 ),
            horizontalAlignment =  "RIGHT",
            textDirection = 'RIGHT_TO_LEFT',
            textFormat=TextFormat (bold=True, 
                                   foregroundColor =  Color (fg_color[0]/255, fg_color[1]/255, fg_color[2]/255 ),
                                   fontSize = 24),
        )
        # Apply formatting to cells A1:C10 if their values are greater than 50
        rule = ConditionalFormatRule(
            ranges=[GridRange.from_a1_range(range, ws)],
            booleanRule=BooleanRule(
                condition=BooleanCondition('NUMBER_GREATER', ['50']),
                format=fmt
            )
        )

        set_row_height (ws, '1', 50)
        #format_cell_ranges(ws, [range], rule)
        format_cell_range (ws, range, fmt)
        self.merge_range (ws, range, merge_type)
        
    def merge_range (self, ws: Worksheet, range: str, merge_type: str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') =  'MERGE_ALL') -> None:
        """
         [Function's description]

        Parameters : 
             self : [description]
             ws : Worksheet : [description]
             range : str : [description]
             merge_type : str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') = 'MERGE_ALL' : [description]
        Returns : 
             None : [description]

        """
        """
        Обьединение колонок / строк \n
        `ws` (gspread.Worksheet) - таблица (worksheet) \n
        `merge_type` `str`  :  \n\t 'MERGE_ALL' | 'MERGE_COLUMNS' | 'MERGE_ROWS'
        """
        ws.merge_cells(range, merge_type)
        #ws.merge_range(ws, range, merge_type)

    def set_worksheet_direction (self, sh: Spreadsheet, ws: Worksheet, direction: str ('ltr') | str ('rtl') = 'rtl' ):
        """
         [Function's description]

        Parameters : 
             self : [description]
             sh : Spreadsheet : [description]
             ws : Worksheet : [description]
             direction : str('ltr') | str('rtl') = 'rtl' : [description]

        """
        data: dict = {
            "requests": [
                    {
                        "updateSheetProperties": {
                            "properties": {
                                "sheetId": int(ws.id),
                                "rightToLeft": True 
                                
                                },
                            "fields": "rightToLeft",
                        }
                    }
                ]
            }
        sh.batch_update(data)

################################################################################################################

    def header(self, ws: Worksheet, ws_header: str | list, row: int = None):
        """
         [Function's description]

        Parameters : 
             self : [description]
             ws : Worksheet : [description]
             ws_header : str | list : [description]
             row : int = None : [description]

        """
        row: int = (self.get_first_empty_row (ws) ) if not row else row
        table_range: str = f'A{ row }'
        ws_header = [ws_header] if isinstance(ws_header, str) else ws_header
        ws.append_row (values = ws_header, table_range = table_range)
        
        table_range = f'{ table_range }:E{ row }'

        self.render_header(ws, ws_header, table_range, 'MERGE_COLUMNS')
        #self.merge_range(ws, table_range, )
        ...

    def write_category_title (self, ws: Worksheet, ws_category_title: str | list, row: int = None):
        """
         [Function's description]

        Parameters : 
             self : [description]
             ws : Worksheet : [description]
             ws_category_title : str | list : [description]
             row : int = None : [description]

        """
        #row: int = (self.get_first_empty_row(ws)) if not row else row
        table_range: str = f'B{ row }'
        ws_category_title = [ws_category_title] if isinstance(ws_category_title, str) else ws_category_title
        ws.append_row (values = ws_category_title, table_range = table_range )
        merge_range = f'{ table_range }:E{ row }'
        self.merge_range (ws, merge_range)
        ...

    def get_first_empty_row (self, ws: Worksheet, by_col: int = None) -> int:
        """
         [Function's description]

        Parameters : 
             self : [description]
             ws : Worksheet : [description]
             by_col : int = None : [description]
        Returns : 
             int : [description]

        """
        """ 
        Возвращает номер последней заполненной ячейки в колонке если в таблице есть значения, иначе 1 \n
        `worksheet` (gspread.Worksheet) - таблица (worksheet)  \n
        `by_col` (int) - по какой колонке считать (если by_col == None по последней заполненной в таблице) 
        """
        str_list = list (filter (None, ws.col_values (1))) if not by_col is None else list (filter (None, ws.get_all_values ()))
        return len (str_list) +1     