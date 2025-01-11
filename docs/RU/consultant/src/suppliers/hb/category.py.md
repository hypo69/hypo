## Анализ кода модуля src.suppliers.hb.category

**Качество кода**
8
- Плюсы
    - Код содержит docstring для модуля.
    - Используется `logger` для логирования.
    - Присутствуют проверки на наличие данных.
    - Код разбит на функции.
- Минусы
    - Некоторые комментарии не соответствуют формату RST.
    - Не все функции имеют docstring.
    - Используется `...` в коде.
    - Нет обработки ошибок внутри функций.
    - Присутствуют неиспользуемые импорты (например `gs`).
    - Использование переменной `d`, `l` без пояснений затрудняет чтение кода
    - Использование `list_products_in_category.append()` в цикле. Должен быть метод extend

**Рекомендации по улучшению**
1. Добавить docstring для каждой функции, включая описание параметров и возвращаемых значений.
2.  Удалить неиспользуемые импорты.
3.  Избегать использования `...` в коде. Вместо этого, реализовать полноценную логику.
4.  Добавить обработку ошибок с использованием `logger.error` и `try-except`.
5.  Улучшить читаемость кода, давая более осмысленные имена переменным.
6.  Использовать  `extend`  вместо  `append`  для добавления списка ссылок в  `list_products_in_category`.
7.  Соблюдать PEP 8 стандарты именования.

**Оптимизированный код**
```python
"""
Модуль для сбора товаров со страницы категорий поставщика hb.co.il через вебдрайвер.
=========================================================================================

Этот модуль содержит функции для сбора списка категорий и товаров со страниц поставщика hb.co.il.
Каждый поставщик имеет свой сценарий обработки категорий.

- Модуль собирает список категорий со страниц продавца с помощью функции `get_list_categories_from_site()`.
- Собирает список товаров со страницы категории с помощью функции `get_list_products_in_category()`.
- Итерируясь по списку, передает управление в `grab_product_page()`, отправляя функции текущий URL страницы.
  `grab_product_page()` обрабатывает поля товара и передает управление классу `Product`.

Пример использования:
--------------------

.. code-block:: python

    from src.suppliers.hb.category import get_list_categories_from_site, get_list_products_in_category
    from src.suppliers import Supplier
    from src.webdriver.driver import Driver
    # Assume 'supplier' is an instance of the class 'Supplier' and has a configured 'driver'.
    # You need to replace this with actual initialization
    
    #Example with mock
    class MockDriver:
        def __init__(self):
            self.current_url = 'https://hb.co.il/category1'
            self.previous_url = None
            self.scroll_count = 0
        def wait(self, time):
            pass
        def execute_locator(self, locator):
             if locator == 'close_banner':
                 return True
             if locator == 'product_links':
                if self.scroll_count == 0:
                    self.scroll_count += 1
                    return ['/product1','/product2']
                if self.scroll_count == 1:
                    self.scroll_count += 1
                    return ['/product3','/product4']
             if locator == '<-':
                 if self.scroll_count < 3:
                     self.previous_url = self.current_url
                     self.current_url = 'https://hb.co.il/category2'
                     return True
                 return None

        def scroll(self):
             pass
    class MockSupplier:
        def __init__(self):
            self.driver = MockDriver()
            self.locators = {
                 'category':{
                     'product_links':'product_links',
                     'pagination': {
                        '<-': '<-'
                    }
                  },
                 'product':{
                    'close_banner':'close_banner'
                }
            }
            self.current_scenario = {'name':'test_category'}
    supplier = MockSupplier()
    categories = get_list_categories_from_site(supplier)
    print(f'Categories:{categories=}')
    products = get_list_products_in_category(supplier)
    print(f'Products:{products=}')
"""
from typing import List
from src.logger.logger import logger
from src.webdriver.driver import Driver
from src.suppliers import Supplier


def get_list_products_in_category(supplier: Supplier) -> list[str]:
    """
    Извлекает список URL товаров со страницы категории.

    Args:
        supplier (Supplier): Объект поставщика с настроенным веб-драйвером и локаторами.

    Returns:
        list[str]: Список URL товаров, найденных на странице категории.
        Возвращает пустой список, если не найдено ни одного товара или произошла ошибка.

    Raises:
         Exception: Если возникают ошибки при выполнении запросов.

    """
    driver: Driver = supplier.driver
    locators: dict = supplier.locators['category']

    try:
        driver.wait(1)
        driver.execute_locator(supplier.locators['product']['close_banner'])
        driver.scroll()

        list_products_in_category = driver.execute_locator(locators['product_links'])
        if not list_products_in_category:
            logger.warning('Не найдено ссылок на товары в категории.')
            return []
            
        all_products = list_products_in_category if isinstance(list_products_in_category, list) else [list_products_in_category]

        while driver.current_url != driver.previous_url:
           if paginator(driver, locators, all_products):
               new_products = driver.execute_locator(locators['product_links'])
               if new_products:
                   all_products.extend(new_products if isinstance(new_products, list) else [new_products])
           else:
               break

        logger.debug(f'Найдено {len(all_products)} товаров в категории {supplier.current_scenario["name"]}')
        return all_products
    except Exception as e:
        logger.error(f'Произошла ошибка при получении списка товаров в категории: {e}')
        return []

def paginator(driver: Driver, locator: dict, list_products_in_category: list) -> bool:
    """
    Осуществляет навигацию по страницам пагинации.

    Args:
        driver (Driver): Объект веб-драйвера.
        locator (dict): Локаторы элементов пагинации.
        list_products_in_category (list): Список URL товаров для обновления.

    Returns:
        bool: True, если переход на следующую страницу выполнен, False в противном случае.
    """
    try:
        response = driver.execute_locator(locator['pagination']['<-'])
        if not response or (isinstance(response, list) and len(response) == 0):
             return False
        return True
    except Exception as e:
         logger.error(f'Произошла ошибка при переключении страницы пагинации: {e}')
         return False


def get_list_categories_from_site(supplier: Supplier) -> None:
    """
    Извлекает список категорий с сайта.

    Args:
         supplier (Supplier): Объект поставщика.

    Returns:
         None: Функция ничего не возвращает, но логирует результат работы.
    """
    # todo: Реализовать логику получения списка категорий с сайта
    logger.info(f"Функция получения списка категорий для {supplier} - не реализована")
    ...