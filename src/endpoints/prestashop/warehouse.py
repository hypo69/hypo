


""" Класс склада (warwehouse) `PrestaShop`"""


import os,sys
from attr import attr, attrs
from pathlib import Path
import header
from src import gs
from src.utils import  pprint
from .api import PrestaShop
from src.logger import logger


class PrestaWarehouse(PrestaShop): 
    ...