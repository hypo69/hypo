


""" Парсер таблицы xls, сгенегированной в личном кабинете portals.aliexpress.com"""
...
import header
from src.suppliers.aliexpress import DealsFromXLS 
from src.utils import pprint

deals_parser = DealsFromXLS(language='EN', currency= 'USD')

for deal in deals_parser.get_next_deal():
    pprint(deal)
    ...
...


