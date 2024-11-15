## \file hypotez/src/suppliers/__init__.py
# -*- coding: utf-8 -*-

""" module: src.suppliers """
MODE = 'debug'
""" module: src.suppliers """
MODE = 'debug'

"""
Модуль поставщика. Класс `Supplier`

Для каждого конкретного поставщика есть свои специфичные методы (функции) извлечения информации. 
Эти функции дополняют базовый класс `Supplier` и подключаются через интерфейс `supplier.related_functions`.

Методы каждого конкретного поставщика находятся в директориях с именем <supplier_prefix>, 
например: `amazon`, `aliexpress`, `morlevi`,...  
- `supplier_prefix` задается во время создания в системе нового поставщика и обычно основывается на сокращении имени или сайта поставщика.

## Взаимосвязь сущностей Supplier, Driver, Product
@image html supplier-warehouse-client.png
"""

import header
# Импорт версий и основных модулей
from .version import __version__, __doc__, __details__
from .supplier import Supplier
from .graber import Graber
from .locator import Locator

