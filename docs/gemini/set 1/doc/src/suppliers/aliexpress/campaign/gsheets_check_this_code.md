# Модуль `hypotez/src/suppliers/aliexpress/campaign/gsheets_check_this_code.py`

## Обзор

Модуль `gsheets_check_this_code.py` предоставляет класс `AliCampaignGoogleSheet` для работы с Google Таблицами в контексте управления рекламными кампаниями AliExpress. Он позволяет записывать данные о кампаниях, категориях и продуктах, а также форматировать листы Google Таблиц. Модуль использует библиотеки `gspread`, `gspread_formatting`, и др. для взаимодействия с Google Таблицами и предоставляет методы для очистки, копирования и форматирования листов.

## Оглавление

- [Модуль `gsheets_check_this_code.py`](#модуль-gsheets_check_this_codepy)
- [Класс `AliCampaignGoogleSheet`](#класс-alicampaigngooglesheet)
    - [`__init__`](#инициализатор-аликампайнгooglesheet)
    - [`clear`](#метод-clear)
    - [`delete_products_worksheets`](#метод-delete_products_worksheets)
    - [`set_campaign_worksheet`](#метод-set_campaign_worksheet)
    - [`set_products_worksheet`](#метод-set_products_worksheet)
    - [`set_categories_worksheet`](#метод-set_categories_worksheet)
    - [`get_categories`](#метод-get_categories)
    - [`set_category_products`](#метод-set_category_products)
    - [`_format_categories_worksheet`](#метод-_format_categories_worksheet)
    - [`_format_category_products_worksheet`](#метод-_format_category_products_worksheet)


## Класс `AliCampaignGoogleSheet`

### Описание

Класс `AliCampaignGoogleSheet` наследует от класса `SpreadSheet` и предоставляет методы для работы с Google Таблицами в контексте кампаний AliExpress.  Он позволяет создавать, обновлять и форматировать листы, содержащие данные о кампаниях, категориях и продуктах.

### Методы

#### `__init__`

```python
def __init__(self, campaign_name: str, language: str | dict = None, currency: str = None):
    """ Initialize AliCampaignGoogleSheet with specified Google Sheets spreadsheet ID and additional parameters.
    @param campaign_name `str`: The name of the campaign.
    @param category_name `str`: The name of the category.   
    @param language `str`: The language for the campaign.
    @param currency `str`: The currency for the campaign.
    """
    # Initialize SpreadSheet with the spreadsheet ID
    super().__init__(spreadsheet_id=self.spreadsheet_id)
    self.editor = AliCampaignEditor(campaign_name=campaign_name, language=language, currency=currency)
    self.clear()
    self.set_campaign_worksheet(self.editor.campaign)
    self.set_categories_worksheet(self.editor.campaign.category)
    self.driver.get_url(f'https://docs.google.com/spreadsheets/d/{self.spreadsheet_id}')
```

#### `clear`

```python
def clear(self):
    """ Clear contents.
    Delete product sheets and clear data on the categories and other specified sheets.
    """
    try:
        self.delete_products_worksheets()
    except Exception as ex:
        logger.error("Ошибка очистки", ex)
```

#### `delete_products_worksheets`

```python
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
```

**(И так далее, для остальных методов)**

**Важно:**  Полная документация требует подробных описаний аргументов, возвращаемых значений и возможных исключений для каждого метода.  Данный ответ предоставляет шаблон, но не содержит полной детализации.  Для полной документации, необходимо проанализировать код каждого метода и описать его поведение с необходимой точностью.