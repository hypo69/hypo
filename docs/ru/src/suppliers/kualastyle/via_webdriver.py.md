# Модуль `via_webdriver.py`

## Обзор

Модуль `via_webdriver.py` предназначен для парсинга данных с сайта Kualastyle с использованием веб-драйвера. Он извлекает список URL-адресов продуктов из заданной категории.

## Подробней

Этот модуль является частью пакета `src.suppliers.kualastyle` и используется для автоматизированного сбора информации о продуктах с сайта Kualastyle. В модуле используется веб-драйвер для навигации по сайту и извлечения необходимых данных.

## Функции

### `get_list_products_in_category`

```python
def get_list_products_in_category(s) -> list[str,str,None]:
    """ Returns list of products urls from category page
    Attrs:
        s - Suplier
    @returns
        list of products urls or None
    """
    ...
```

**Назначение**: Возвращает список URL-адресов продуктов со страницы категории.

**Параметры**:
- `s`: Объект поставщика (Suplier), содержащий информацию о драйвере и локаторах.

**Возвращает**:
- `list[str,str,None]`: Список URL-адресов продуктов или `None`, если список получить не удалось.

**Как работает функция**:
1. **Инициализация**:
   - Получает драйвер (`d`) из объекта поставщика `s`.
   - Получает локаторы категории (`l`) из объекта поставщика `s`.
2. **Прокрутка страницы**:
   - Выполняет прокрутку страницы вниз `scroll_count = 10` раз для загрузки всех продуктов в категории.
3. **Извлечение ссылок на продукты**:
   - Использует метод `execute_locator` для извлечения списка URL-адресов продуктов с использованием локатора `product_links`.
4. **Возврат результата**:
   - Возвращает список URL-адресов продуктов.

```python
from src.logger.logger import logger
from typing import Union

from src import gs
from src.logger.logger import logger

def get_list_products_in_category(s) -> list[str,str,None]:    
    """ Returns list of products urls from category page
    Attrs:
        s - Suplier
    @returns
        list of products urls or None
    """
    d = s.driver
    l: dict = s.locators.get('category')
    d.scroll(scroll_count = 10, direction = "forward")

    _ = d.execute_locator
    list_products_in_category = _(l['product_links'])
    #pprint(list_products_in_category)
    return list_products_in_category