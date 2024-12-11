# Модуль `hypotez/src/suppliers/aliexpress/_pytests/test_affiliated_products_generator.py`

## Обзор

Данный модуль содержит тесты для класса `AliAffiliatedProducts`, отвечающего за обработку и генерацию информации об аффилированных продуктах с AliExpress. Тесты проверяют корректность вызова методов, а также обработку данных.

## Фикстуры

### `ali_affiliated_products`

**Описание**: Фикстура, возвращающая экземпляр класса `AliAffiliatedProducts` с заданными параметрами кампании, категории, языка и валюты.

**Параметры**:
- Не имеет параметров.

**Возвращает**:
- `AliAffiliatedProducts`: Экземпляр класса `AliAffiliatedProducts`.


## Функции

### `test_check_and_process_affiliate_products`

**Описание**: Тестирует метод `check_and_process_affiliate_products`, проверяя, что он вызывает метод `process_affiliate_products` с корректными аргументами.

**Параметры**:
- `ali_affiliated_products` (`AliAffiliatedProducts`): Экземпляр класса `AliAffiliatedProducts`, полученный с помощью фикстуры.
- `prod_urls` (list): Список ссылок на продукты.

**Возвращает**:
- Не имеет возвращаемого значения.

**Используемые моки**:
- `patch.object(ali_affiliated_products, 'process_affiliate_products')`: Мок для метода `process_affiliate_products`, позволяющий проверить его вызов.

### `test_process_affiliate_products`

**Описание**: Тестирует метод `process_affiliate_products`, проверяя обработку продуктов и корректность возвращаемых данных.

**Параметры**:
- `ali_affiliated_products` (`AliAffiliatedProducts`): Экземпляр класса `AliAffiliatedProducts`, полученный с помощью фикстуры.
- `prod_urls` (list): Список ссылок на продукты.

**Возвращает**:
- `list`: Список обработанных продуктов.

**Используемые моки**:
- `patch.object(ali_affiliated_products, 'retrieve_product_details', return_value=mock_product_details)`: Мок для метода `retrieve_product_details`, возвращающий заданный список продуктов.
- `patch("src.suppliers.aliexpress.affiliated_products_generator.ensure_https", return_value=prod_urls)`: Мок для функции `ensure_https`.
- `patch("src.suppliers.aliexpress.affiliated_products_generator.save_png_from_url")`: Мок для функции `save_png_from_url`.
- `patch("src.suppliers.aliexpress.affiliated_products_generator.save_video_from_url")`: Мок для функции `save_video_from_url`.
- `patch("src.suppliers.aliexpress.affiliated_products_generator.j_dumps", return_value=True)`: Мок для функции `j_dumps`.

**Ассерты**:
- Проверяет длину списка обработанных продуктов.
- Проверяет значение `product_id` первого обработанного продукта.


##  Зависимости

Модуль использует следующие библиотеки:
- `pytest`
- `unittest.mock`
- `src.suppliers.aliexpress.affiliated_products_generator`
- `types`