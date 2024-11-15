```python
## \file hypotez/src/suppliers/grandadvance/graber.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.suppliers.grandadvance """


import asyncio
from pathlib import Path
from types import SimpleNamespace
from typing import Any, Callable, Optional
from dataclasses import dataclass, field
from functools import wraps

from __init__ import gs

from src.suppliers import Graber as Grbr, Locator
from src.product import ProductFields
from src.webdriver import Driver
from src.utils.jjson import j_loads_ns
from src.logger import logger
from src.logger.exceptions import ExecuteLocatorException

# Определение декоратора для закрытия всплывающих окон
def close_popup(value: Any = None) -> Callable:
    """Создаёт декоратор для закрытия всплывающих окон перед выполнением основной логики функции.

    Args:
        value (Any): Необязательное значение, передаваемое декоратору.

    Returns:
        Callable: Декоратор, обертывающий функцию.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                await d.execute_locator(l.close_popup)  # Ожидание асинхронного закрытия всплывающих окон
            except ExecuteLocatorException as e:
                logger.debug(f"Ошибка выполнения локетора: {e}")
            return await func(*args, **kwargs)  # Ожидание основной функции
        return wrapper
    return decorator


supplier_prefix = 'grandadvance'
@dataclass(frozen=True)
class Graber(Grbr):
    """Класс Graber для извлечения данных из Grand Advance."""
    supplier_prefix: str = field(default=supplier_prefix)
    d: Driver = None  # d будет назначен позже в `grab_page()`
    l: Locator = None  # l будет назначен позже в `__post_init__()`

    def __post_init__(self):
        """Инициализация локетора и глобальных переменных."""
        locator_path = Path(gs.path.src, 'suppliers', self.supplier_prefix, 'locators', 'product.json')
        self.l = Locator(self.supplier_prefix) # прямая привязка локетора к классу
        global l
        l = self.l
        super().__init__(self.supplier_prefix, self.l)  # передаем locator

    async def grab_page(self, driver: Driver) -> ProductFields:
        """Асинхронная функция для извлечения данных о продукте.

        Args:
            driver (Driver): Экземпляр драйвера для извлечения данных.

        Returns:
            ProductFields: Извлеченные данные о продукте.
        """
        global d
        d = self.d = driver
        
        try:
            # Важно! Обработка потенциальных ошибок, например, если страница не загрузилась.
            await self._fetch_data()
        except Exception as e:
            logger.error(f"Ошибка при извлечении данных: {e}")
            return None # Возвращаем None в случае ошибки

        return self.fields


    async def _fetch_data(self):
        """Функция для извлечения данных о продукте."""
        await self._fetch_all_data()

    async def _fetch_all_data(self):
        """Функция для извлечения всех данных. Используйте асинхронные методы класса."""
        # Лучше использовать await self.метод_из_класса(параметры), а не await fetch_specific_data()
        # Избегаем глобальных переменных внутри fetch_all_data.
        await self.id_product(self._get_id_product())
        # ... другие методы (см. ниже)

    def _get_id_product(self):
      #  Получение id_product из источников (например, из URL, из глобальных переменных)
      # Здесь должна быть логика получения id_product.
      return "example_id" #Пример, замените на ваш источник

    # Пример асинхронных методов:
    async def id_product(self, product_id: str):
        # ... ваша логика извлечения id_product
        self.fields.id_product = product_id

    # Другие методы: (id_category_default, name, price, etc)
    # ...


```

**Пояснения и улучшения:**

* **Обработка ошибок:** Добавил `try...except` блок в `grab_page`, чтобы ловить и обрабатывать любые исключения, возникающие при извлечении данных. Это предотвращает сбой всего процесса.  Возвращаем `None`, если произошла ошибка.
* **`_fetch_data` и `_fetch_all_data`:** Ввели вспомогательные функции, которые скрывают внутреннюю логику извлечения данных. Это улучшает структуру кода и делает его более читабельным.
* **`_get_id_product()`:** Создал функцию, которая отвечает за получение `id_product`. Это важный шаг для лучшей организации кода. Замените `return "example_id"` на ваш способ получения `id_product` из других источников (например, из URL или других глобальных переменных).
* **Асинхронные методы класса:** Все методы извлечения данных (например, `id_product`, `name`, `price`) должны быть асинхронными методами класса `Graber`.  Вызывайте их с помощью `await self.метод_из_класса(...)`.
* **Удаление глобальных переменных внутри `fetch_all_data`:** Вместо глобальных переменных `d` и `l` внутри `fetch_all_data` теперь используется `self.d` и `self.l`, что улучшает структуру кода и предотвращает ошибки.
* **Более корректное использование глобальных переменных:** Глобальные переменные `d` и `l` всё ещё используются, но теперь их инициализация происходит в `__post_init__` и `grab_page`, а не в самом верху файла. Это важно для корректного состояния.
* **Документация:** Добавлены docstrings к функциям, чтобы улучшить документацию и читабельность кода.
* **Проверка параметров:** Добавлены типы для параметров (например, `product_id: str` в `id_product`).


**Как использовать:**

```python
# ... (ваш код с созданием экземпляра Driver)

graber = Graber()
driver = Driver(...) # ... инициализация драйвера
result = await graber.grab_page(driver)

if result:
    print(result.fields)  # Доступ к данным
else:
    print("Ошибка при извлечении данных.")

```

**Важные замечания:**

* Замените `"example_id"` в методе `_get_id_product()` на ваш реальный способ получения `id_product`.
* Реализуйте все остальные асинхронные методы класса `Graber` (`id_product`, `name`, `price` и т.д.), которые необходимы для извлечения данных о продукте.  Используйте локеторы из `Locator` для поиска элементов на странице.
* Проверьте корректность работы всех локеторов (locators) в файле `product.json`.


Этот обновлённый код более структурирован, чист и устойчив к ошибкам, чем исходный. Он также лучше отвечает современным принципам разработки Python.  Теперь вы можете более чётко контролировать потоки данных и обращаться к ним из отдельных методов. Remember to fill in the missing parts for other data fields and data retrieval logic!