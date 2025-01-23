## \file /src/goog/spreadsheet/spreadsheet.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.goog.spreadsheet 
	:platform: Windows, Unix
	:synopsis: Minimal library for working with Google Sheets.

```python
# Example usage of the class
if __name__ == "__main__":
    from pathlib import Path

    data_file = Path('/mnt/data/google_extracted/your_data_file.csv')  # Replace with actual data file
    sheet_name = 'Sheet1'  # Replace with actual sheet name in Google Sheets

    # Create a new Spreadsheet if spreadsheet_id is not specified
    google_sheet_handler = SpreadSheet(
        spreadsheet_id=None,  # Specify None to create a new Spreadsheet
        sheet_name=sheet_name,
        spreadsheet_name='My New Spreadsheet'  # Name of the new Spreadsheet if spreadsheet_id is not specified
    )
    google_sheet_handler.upload_data_to_sheet()
```
"""


""" 
"""

from pathlib import Path
import gspread
from gspread import Spreadsheet, Worksheet
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from src.logger.logger import logger
from src import gs
from src.utils.printer import pprint


class SpreadSheet:
    """ Class for working with Google Sheets.

    This class provides basic methods for accessing the Google Sheets API, creating and managing spreadsheets,
    and uploading data from a CSV file to Google Sheets.
    """

    # Path to the credentials file for accessing Google Sheets.
    #creds_file = gs.path.root / 'secrets' / 'hypo69-c32c8736ca62.json'

    """ оригинал файла хранится в базе данных вместе с паролями
    @todo организовать копирование файла в прогамно созаданом `tmp`,чтобы не хранить файл в физической директории
    """
    
    # Class variable declarations
    spreadsheet_id: str | None
    spreadsheet_name: str | None
    spreadsheet: Spreadsheet
    data_file: Path
    sheet_name: str
    credentials: ServiceAccountCredentials
    client: gspread.Client
    worksheet: Worksheet
    create_sheet: bool

    def __init__(self, 
                 spreadsheet_id: str, *args, **kwards):  # Name of the sheet in Google Sheets
        """ Initialize GoogleSheetHandler with specified credentials and data file.
        
        @param spreadsheet_id ID of the Google Sheets spreadsheet. Specify None to create a new Spreadsheet.
        @param spreadsheet_name Name of the new Spreadsheet if spreadsheet_id is not specified.
        @param sheet_name Name of the sheet in Google Sheets.
        """
        self.spreadsheet_id = spreadsheet_id
        self.credentials = self._create_credentials()
        self.client = self._authorize_client()
        
        try:
            self.spreadsheet = self.client.open_by_key(self.spreadsheet_id)
            #logger.debug(f"Opened existing spreadsheet with ID: {self.spreadsheet_id}")
        except gspread.exceptions.SpreadsheetNotFound:
            logger.error(f"Spreadsheet with ID '{self.spreadsheet_id}' does not exist.")
            raise
   
    def _create_credentials(self):
        """ Create credentials from a JSON file.

        Creates credentials for accessing the Google Sheets API based on the key file.
        @return Credentials for accessing Google Sheets.
        """
        try:
            creds_file:Path = gs.path.secrets / 'e-cat-346312-137284f4419e.json' # <-  e.cat.co.il@gmail.com
            SCOPES: list = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
            credentials = ServiceAccountCredentials.from_json_keyfile_name(
                creds_file, SCOPES
            )
            #logger.debug("Credentials created successfully.")
            return credentials
        except Exception as ex:
            logger.error("Error creating credentials.", ex, exc_info=True)
            raise

    def _authorize_client(self):
        """ Authorize client to access the Google Sheets API.

        Creates and authorizes a client for the Google Sheets API based on the provided credentials.
        @return Authorized client for working with Google Sheets.
        """
        try:
            client = gspread.authorize(self.credentials)
            #logger.debug("Client authorized successfully.")
            return client
        except Exception as ex:
            logger.error("Error authorizing client.", ex, exc_info=True)
            raise

    def get_worksheet(self, worksheet_name: str | Worksheet) -> Worksheet | None:
        """ Get the worksheet by name.

        If the sheet with the specified name does not exist and the `create_if_not_present` flag is set to True, a new sheet is created.

        @param worksheet Name of the sheet in Google Sheets.
        @param create_if_not_present Flag to create a new sheet if it does not exist. If False and the sheet does not exist, an exception is raised.
        @return Worksheet for working with data.
        """

        try:
            ws: Worksheet = self.spreadsheet.worksheet(worksheet_name) 
        except gspread.exceptions.WorksheetNotFound:
            ws: Worksheet  = self.create_worksheet(worksheet_name)
        return ws
        
    def create_worksheet(self, title:str, dim:dict = {'rows':100,'cols':10}) -> Worksheet | None:
        """ функция создает новую страницу с именем `title` и размерностью `dim`"""
        try:
            ws: Worksheet = self.spreadsheet.add_worksheet(title=title, rows=dim['rows'], cols=dim['cols']) 
            return(ws)
        except Exception as ex:
            logger.error(f"Ошибка создания нового листа {title}")
            
    
    def copy_worksheet(self, from_worksheet: str, to_worksheet: str):
        """ Copy worksheet by name."""
        ...
        worksheet: Worksheet = self.spreadsheet.worksheet(from_worksheet)
        worksheet.duplicate(new_sheet_name=to_worksheet)
        return worksheet

    def upload_data_to_sheet(self):
        """ Upload data from a CSV file to Google Sheets.

        Uploads data from the CSV file specified in `self.data_file` to the specified sheet in Google Sheets.
        """
        try:
            if not self.data_file or not self.data_file.exists():
                raise ValueError("Data file path is not set or the file does not exist.")
            
            data = pd.read_csv(self.data_file)  # Read data from the CSV file
            data_list = [data.columns.values.tolist()] + data.values.tolist()  # Prepare data for writing to Google Sheets
            self.worksheet.update('A1', data_list)  # Write data to Google Sheets
            #logger.debug("Data has been uploaded to Google Sheets successfully.")
        except Exception as ex:
            logger.error("Error uploading data to Google Sheets.", ex, exc_info=True)
            raise
