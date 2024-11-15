```python
# -*- coding: utf-8 -*-
 # <- venv win
## ~~~~~~~~~~~~~
""" module: src.db.manager_coupons_and_sales """
""" Менеджер скидок, купонов и т.п. в Prestashop  """
from packaging.version import Version
from .version import __version__, __doc__, __details__  

from .product_group_reduction_cache_manager import ProductGroupReductionCacheManager
from .product_campaigns import ProductCampaignsManager


# Добавьте сюда описание, что делает модуль,
# какие классы и функции он экспортирует и для чего они.
# Также можно добавить примеры использования,
# если они помогут понять назначение.


# Пример документации:
"""
Этот модуль предоставляет инструменты для работы со скидками, купонами и акциями в системе Prestashop.
Он содержит классы для управления группами продуктов со скидками,
а также менеджер для управления рекламными кампаниями.

Экспортируемые классы:

* ProductGroupReductionCacheManager: Менеджер кеша скидок для групп продуктов.  Обеспечивает кэширование и быстрый доступ к данным.
* ProductCampaignsManager: Менеджер для работы с рекламными кампаниями.  Предоставляет функции для создания, редактирования и получения данных о кампаниях.


Пример использования (в другом модуле):

```python
from hypotez.src.db.manager_coupons_and_sales import ProductGroupReductionCacheManager

# Создание менеджера для работы с кешем скидок.
cache_manager = ProductGroupReductionCacheManager()

# Получение данных о скидках для определённой группы продуктов.
data = cache_manager.get_data_for_group(group_id)

# Обработка данных...
```

"""
```
