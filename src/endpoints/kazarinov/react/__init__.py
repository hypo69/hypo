## \file ./src/endpoints/kazarinov/react/__init__.py
# -*- coding: utf-8 -*-
#! /venv/Scripts/python.exe
#! /usr/bin/python
# /path/to/interpreter/python
"""  Модуль поставщика. Class `Supplier`
- для каждого конкретного поставщика есть свои специфичные методы (функции) извлечения информации. 
Эти функции дополняют базовый класс `Supplier` и подключаются через интерфейс  `supplier.related_functions`
Методы каждого конкретного поставщика находятся в директориях с именем <supplier_prefix>, 
например: 
`amazon`,`aliexpress`,`morlevi`,...  
- `supplier_prefix` задается во время создания в системе нового поставщика и обычно основывается на сокращении имени или сайта поставщика  


---

## Взаимосвязь сущностей Supplier, Driver, Product
@image html supplier-warehouse-client.png

"""

...
from packaging.version import Version
from .version import __version__, __doc__, __details__  

from .pricelist_generator import ReportGenerator

