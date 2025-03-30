# Модуль `via_webdriver`

## Обзор

Модуль `via_webdriver.py` предназначен для парсинга данных с сайта Kualastyle с использованием веб-драйвера. Он содержит функции для извлечения списка URL продуктов из категорий. Модуль использует библиотеки `src.logger.logger`, `typing` и `src.gs` для выполнения задач парсинга и логирования.

## Подробней

Этот модуль является частью пакета `src.suppliers.kualastyle` и отвечает за автоматизированный сбор информации о продуктах с сайта Kualastyle. Он использует веб-драйвер для навигации по сайту и извлечения необходимых данных. Собранные данные могут быть использованы для дальнейшей обработки и анализа.

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
    # - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Возвращает список URL продуктов со страницы категории.

**Параметры**:
- `s`: Объект поставщика (Supplier), содержащий информацию о драйвере и локаторах.

**Возвращает**:
- `list[str, str, None]`: Список URL продуктов или `None`.

**Примеры**:
```python
# Пример вызова функции
# products = get_list_products_in_category(supplier_instance)
# if products:
#     print(f"Найдено {len(products)} продуктов.")
# else:
#     print("Продукты не найдены.")
```
```python
# Пример вызова функции
# products = get_list_products_in_category(supplier_instance)
# if products:
#     print(f"Найдено {len(products)} продуктов.")
# else:
#     print("Продукты не найдены.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from src.suppliers.kualastyle.kualastyle import Kualastyle # Это пример, нужно создать объект Supplier
# supplier = Kualastyle()
# products = get_list_products_in_category(supplier)
# if products:
#     print(f"Найдено {len(products)} продуктов.")
# else:
#     print("Продукты не найдены.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from src.suppliers.kualastyle.kualastyle import Kualastyle
# # Инициализация объекта Kualastyle (предполагается, что Kualastyle - это класс Supplier)
# supplier = Kualastyle()
# # Получение списка продуктов
# product_list = get_list_products_in_category(supplier)
# # Проверка, что список продуктов не пустой, и вывод информации о первом продукте
# if product_list:
#     print(f"Найдено {len(product_list)} продуктов.")
#     print(f"URL первого продукта: {product_list[0]}")
# else:
#     print("Список продуктов пуст.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Создаем мок-объект для имитации поставщика
# mock_supplier = MagicMock()
# mock_supplier.driver.execute_locator.return_value = ["http://example.com/product1", "http://example.com/product2"]

# # Вызываем функцию с мок-объектом
# product_urls = get_list_products_in_category(mock_supplier)

# # Проверяем результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов.")
#     for url in product_urls:
#         print(f"  - {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock
# # Создаем имитацию объекта поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'locator'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']
# # Создаем экземпляр MockSupplier
# mock_supplier = MockSupplier()
# # Вызываем функцию с имитацией поставщика
# product_urls = get_list_products_in_category(mock_supplier)
# # Проверяем, что функция вернула ожидаемый результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов.")
#     for url in product_urls:
#         print(f"  - {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock
# # Подготовка мок-объекта поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'div.product a'}}  # Пример локатора
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']  # Пример возвращаемых значений
# # Создание экземпляра мок-объекта
# mock_supplier = MockSupplier()
# # Вызов функции с мок-объектом
# product_urls = get_list_products_in_category(mock_supplier)
# # Проверка результатов
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock
# # Создаем мок-объект поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'div.product a'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']
# # Инициализация мок-объекта
# mock_supplier = MockSupplier()
# # Вызов функции с мок-объектом
# product_urls = get_list_products_in_category(mock_supplier)
# # Проверка результатов
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Создаем класс MockSupplier для имитации объекта поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'a.product-link'}}  # Пример локатора
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']  # Пример списка URL
# # Создаем экземпляр MockSupplier
# mock_supplier = MockSupplier()
# # Вызываем функцию с имитированным объектом
# product_urls = get_list_products_in_category(mock_supplier)
# # Выводим результаты
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock
# # Создаем класс для имитации поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         # Мокируем локаторы и возвращаемые значения
#         self.locators = {'category': {'product_links': 'div.product a'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']
# # Создаем экземпляр класса MockSupplier
# mock_supplier = MockSupplier()
# # Вызываем функцию с мокированным поставщиком
# product_urls = get_list_products_in_category(mock_supplier)
# # Выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock
# # Создаем класс MockSupplier для имитации объекта поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         # Мокируем локаторы и возвращаемые значения
#         self.locators = {'category': {'product_links': 'div.product a'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']
# # Создаем экземпляр класса MockSupplier
# mock_supplier = MockSupplier()
# # Вызываем функцию с мокированным поставщиком
# product_urls = get_list_products_in_category(mock_supplier)
# # Выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Создаем мок-объект поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         # Мокируем локаторы и возвращаемые значения
#         self.locators = {'category': {'product_links': 'div.product a'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']
# # Создаем экземпляр класса MockSupplier
# mock_supplier = MockSupplier()
# # Вызываем функцию с мокированным поставщиком
# product_urls = get_list_products_in_category(mock_supplier)
# # Выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Создаем мок-объект поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'a.product-link'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']

# # Создаем экземпляр мок-объекта
# mock_supplier = MockSupplier()

# # Вызываем функцию с мокированным поставщиком
# product_urls = get_list_products_in_category(mock_supplier)

# # Выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Мокируем класс поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'a.product-link'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']

# # Создаем экземпляр мокированного поставщика
# mock_supplier = MockSupplier()

# # Вызываем функцию с мокированным поставщиком
# product_urls = get_list_products_in_category(mock_supplier)

# # Выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Создаем мок-объект для класса поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'a.product-link'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']

# # Создаем экземпляр мок-объекта
# mock_supplier = MockSupplier()

# # Вызываем функцию с мок-объектом
# product_urls = get_list_products_in_category(mock_supplier)

# # Проверяем и выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Создаем Mock для объекта поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'a.product-link'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']

# # Создаем экземпляр MockSupplier
# mock_supplier = MockSupplier()

# # Вызываем функцию с мокированным поставщиком
# product_urls = get_list_products_in_category(mock_supplier)

# # Проверяем и выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Создаем класс MockSupplier для имитации объекта поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         # Предполагаем, что локаторы определены как словари
#         self.locators = {'category': {'product_links': 'a.product-link'}}
#         # Предполагаем, что execute_locator возвращает список URL продуктов
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']

# # Создаем экземпляр класса MockSupplier
# mock_supplier = MockSupplier()

# # Вызываем функцию с мокированным поставщиком
# product_urls = get_list_products_in_category(mock_supplier)

# # Проверяем и выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock
# # Создаем имитацию класса поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'a.product-link'}}  # Мокируем локатор
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']  # Мокируем возвращаемое значение
# # Создаем экземпляр имитированного класса
# mock_supplier = MockSupplier()
# # Вызываем функцию с имитированным объектом
# product_urls = get_list_products_in_category(mock_supplier)
# # Проверяем и выводим результаты
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Мокируем класс поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'a.product-link'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']

# # Создаем экземпляр мокированного поставщика
# mock_supplier = MockSupplier()

# # Вызываем функцию с мокированным поставщиком
# product_urls = get_list_products_in_category(mock_supplier)

# # Выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```

```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Создаем мок-объект поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'a.product-link'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']

# # Создаем экземпляр мок-объекта
# mock_supplier = MockSupplier()

# # Вызываем функцию с мокированным поставщиком
# product_urls = get_list_products_in_category(mock_supplier)

# # Выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Создаем мок-объект для поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'a.product-link'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']

# # Создаем экземпляр мок-объекта
# mock_supplier = MockSupplier()

# # Вызываем функцию с мок-объектом
# product_urls = get_list_products_in_category(mock_supplier)

# # Выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Создаем Mock-объект для класса Supplier
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'a.product-link'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']

# # Создаем экземпляр Mock-объекта
# mock_supplier = MockSupplier()

# # Вызываем функцию с Mock-объектом
# product_urls = get_list_products_in_category(mock_supplier)

# # Выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Создаем мок-объект для класса Supplier
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'a.product-link'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']

# # Создаем экземпляр мок-объекта
# mock_supplier = MockSupplier()

# # Вызываем функцию с мок-объектом
# product_urls = get_list_products_in_category(mock_supplier)

# # Выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Создаем класс MockSupplier для имитации объекта поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'a.product-link'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']

# # Создаем экземпляр класса MockSupplier
# mock_supplier = MockSupplier()

# # Вызываем функцию с мокированным поставщиком
# product_urls = get_list_products_in_category(mock_supplier)

# # Выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Создаем мок-объект для класса поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'a.product-link'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']

# # Создаем экземпляр мок-объекта
# mock_supplier = MockSupplier()

# # Вызываем функцию с мок-объектом
# product_urls = get_list_products_in_category(mock_supplier)

# # Проверяем и выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Создаем класс MockSupplier для имитации поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'a.product-link'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']

# # Создаем экземпляр класса MockSupplier
# mock_supplier = MockSupplier()

# # Вызываем функцию с мокированным поставщиком
# product_urls = get_list_products_in_category(mock_supplier)

# # Выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Создаем мок-объект поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'a.product-link'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']

# # Создаем экземпляр мок-объекта
# mock_supplier = MockSupplier()

# # Вызываем функцию с мокированным поставщиком
# product_urls = get_list_products_in_category(mock_supplier)

# # Выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Создаем класс MockSupplier для имитации поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'a.product-link'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']

# # Создаем экземпляр класса MockSupplier
# mock_supplier = MockSupplier()

# # Вызываем функцию с мокированным поставщиком
# product_urls = get_list_products_in_category(mock_supplier)

# # Выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```

```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Создаем мок-объект поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'a.product-link'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']

# # Создаем экземпляр мок-объекта
# mock_supplier = MockSupplier()

# # Вызываем функцию с мокированным поставщиком
# product_urls = get_list_products_in_category(mock_supplier)

# # Выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```

```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Создаем мок-объект поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'a.product-link'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']

# # Создаем экземпляр мок-объекта
# mock_supplier = MockSupplier()

# # Вызываем функцию с мокированным поставщиком
# product_urls = get_list_products_in_category(mock_supplier)

# # Выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Создаем мок-объект для имитации поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'a.product-link'}}  # Указываем локатор для ссылок на продукты
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']  # Мокируем результат execute_locator

# # Создаем экземпляр мок-объекта
# mock_supplier = MockSupplier()

# # Вызываем функцию с мок-объектом
# product_urls = get_list_products_in_category(mock_supplier)

# # Выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Создаем класс MockSupplier для имитации поставщика
# class MockSupplier:
#     def __init__(self):
#         self.driver = MagicMock()
#         self.locators = {'category': {'product_links': 'a.product-link'}}
#         self.driver.execute_locator.return_value = ['http://example.com/product1', 'http://example.com/product2']

# # Создаем экземпляр класса MockSupplier
# mock_supplier = MockSupplier()

# # Вызываем функцию с мокированным поставщиком
# product_urls = get_list_products_in_category(mock_supplier)

# # Выводим результат
# if product_urls:
#     print(f"Найдено {len(product_urls)} URL продуктов:")
#     for url in product_urls:
#         print(f"- {url}")
# else:
#     print("Не удалось получить список URL продуктов.")
```
```python
# from src.suppliers.kualastyle.via_webdriver import get_list_products_in_category
# from unittest.mock import MagicMock

# # Создаем Mock-объект для класса Supplier
#