Как использовать класс PrestaProduct
========================================================================================

Описание
-------------------------
Класс `PrestaProduct` предоставляет методы для взаимодействия с API PrestaShop, позволяя проверять наличие товара, выполнять расширенный поиск и получать информацию о товаре по ID.  Он наследуется от класса `PrestaShop`, обеспечивая базовые функции работы с API.  Класс инициализируется с параметрами `credentials`, `api_domain` и `api_key`, позволяющими указать информацию для доступа к API.  Если `credentials` является словарем или объектом `SimpleNamespace`, то `api_domain` и `api_key` берутся из него, в противном случае их нужно указать напрямую. Если не указаны оба параметра, то генерируется исключение `ValueError`.

Шаги выполнения
-------------------------
1. Импортировать необходимый модуль:
   ```python
   from hypotez.src.endpoints.prestashop.product import PrestaProduct
   ```

2. Создать экземпляр класса `PrestaProduct`, передав требуемые параметры инициализации:
   ```python
   credentials = {'api_domain': 'ваш_домен', 'api_key': 'ваш_ключ'}
   product = PrestaProduct(credentials=credentials)
   ```
   Или, если `credentials` - это объект `SimpleNamespace`:
   ```python
   credentials = SimpleNamespace(api_domain='ваш_домен', api_key='ваш_ключ')
   product = PrestaProduct(credentials=credentials)
   ```
   Или, если  `api_domain` и `api_key` задаются явно:
   ```python
   product = PrestaProduct(api_domain='ваш_домен', api_key='ваш_ключ')
   ```

3. Вызвать нужный метод для взаимодействия с API PrestaShop:
   - `check(product_reference: str)`: Проверяет наличие товара по указанному артикулу (SKU, MKT). Возвращает словарь с информацией о товаре, если он найден, иначе `False`.
     ```python
     result = product.check('ваш_артикул')
     if result:
         pprint(result)  # Распечатать информацию о товаре
     else:
         print('Товар не найден')
     ```
   - `search(filter: str, value: str)`: Выполняет расширенный поиск в базе данных по заданному фильтру и значению. Возвращает результат поиска (подробности зависят от API PrestaShop).
     ```python
     result = product.search('name', 'искомое_значение')
     pprint(result) # Распечатать результаты поиска
     ```
   - `get(id_product)`: Возвращает информацию о товаре по его идентификатору.
     ```python
     result = product.get(123)  # Получить информацию о товаре с id 123
     pprint(result)
     ```


Пример использования
-------------------------
.. code-block:: python

    from types import SimpleNamespace
    from hypotez.src.endpoints.prestashop.product import PrestaProduct
    from hypotez.src.utils.printer import pprint

    credentials = SimpleNamespace(api_domain='ваш_домен', api_key='ваш_ключ')

    try:
        product = PrestaProduct(credentials=credentials)
        result = product.check('ваш_артикул')
        if result:
            pprint(result)
        else:
            print('Товар не найден')
    except ValueError as e:
        print(f"Ошибка: {e}")