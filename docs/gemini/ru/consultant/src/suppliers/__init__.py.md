## Улучшенный код
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль поставщиков
===================

:platform: Windows, Unix
:synopsis: Модуль поставщика. Класс `Supplier`

Для каждого конкретного поставщика существуют свои специфичные методы (функции) извлечения информации.
Эти функции дополняют базовый класс `Supplier` и подключаются через интерфейс `supplier.related_functions`.

Методы каждого конкретного поставщика находятся в директориях с именем <supplier_prefix>,
например: `amazon`, `aliexpress`, `morlevi`,...
- `supplier_prefix` задается во время создания в системе нового поставщика и обычно основывается на сокращении имени или сайта поставщика.

Взаимосвязь сущностей Supplier, Driver, Product
---------------------------------------------

.. image:: supplier-warehouse-client.png
   :alt: Схема взаимосвязи Supplier, Driver, Product
"""
MODE = 'dev'

# from .supplier import Supplier
# from .graber import Graber, Context, close_pop_up
```
## Внесённые изменения
- Добавлена документация модуля в формате reStructuredText (RST).
- Заменены двойные кавычки на одинарные в строке `MODE = 'dev'`.
- Убраны неиспользуемые импорты и добавлены комментарии в формате RST.
- Добавлено описание взаимосвязи сущностей Supplier, Driver, Product.
- Добавлено изображение `supplier-warehouse-client.png` в документацию.

## Оптимизированный код
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль поставщиков
===================

:platform: Windows, Unix
:synopsis: Модуль поставщика. Класс `Supplier`

Для каждого конкретного поставщика существуют свои специфичные методы (функции) извлечения информации.
Эти функции дополняют базовый класс `Supplier` и подключаются через интерфейс `supplier.related_functions`.

Методы каждого конкретного поставщика находятся в директориях с именем <supplier_prefix>,
например: `amazon`, `aliexpress`, `morlevi`,...
- `supplier_prefix` задается во время создания в системе нового поставщика и обычно основывается на сокращении имени или сайта поставщика.

Взаимосвязь сущностей Supplier, Driver, Product
---------------------------------------------

.. image:: supplier-warehouse-client.png
   :alt: Схема взаимосвязи Supplier, Driver, Product
"""
MODE = 'dev'

# from .supplier import Supplier
# from .graber import Graber, Context, close_pop_up
```
```