# Модуль `hypotez/src/suppliers/aliexpress/_pytests/test_affiliated_products_generator.py`

## Обзор

Этот модуль содержит тесты для класса `AliAffiliatedProducts`, отвечающего за генерацию и обработку аффилированных продуктов с AliExpress.  Модуль использует `pytest` для написания тестов и `unittest.mock` для имитации внешних зависимостей.

## Фикстуры

### `ali_affiliated_products`

**Описание**: Фикстура, возвращающая экземпляр класса `AliAffiliatedProducts` с заданными параметрами кампании, категории, языка и валюты.

**Аргументы**:
* Нет

**Возвращает**:
* `AliAffiliatedProducts`: Экземпляр класса `AliAffiliatedProducts`.


## Функции

### `test_check_and_process_affiliate_products`

**Описание**: Тестирует метод `check_and_process_affiliate_products`, проверяя корректное вызов метода `process_affiliate_products`.

**Аргументы**:
* `ali_affiliated_products` (`AliAffiliatedProducts`): Экземпляр класса `AliAffiliatedProducts`.

**Возвращает**:
* Нет

**Использует патчи**:
* `patch.object(ali_affiliated_products, 'process_affiliate_products')`: Патч метода `process_affiliate_products` для проверки его вызова.

**Проверяемые действия**:
* Проверяет, что метод `process_affiliate_products` был вызван один раз с предоставленным списком `prod_urls`.


### `test_process_affiliate_products`

**Описание**: Тестирует метод `process_affiliate_products`, проверяя корректную обработку продуктов.

**Аргументы**:
* `ali_affiliated_products` (`AliAffiliatedProducts`): Экземпляр класса `AliAffiliatedProducts`.


**Возвращает**:
* Нет

**Использует патчи**:
* `patch.object(ali_affiliated_products, 'retrieve_product_details')`: Патч метода `retrieve_product_details` для возвращения данных продукта.
* `patch("src.suppliers.aliexpress.affiliated_products_generator.ensure_https")`: Патч функции `ensure_https`, чтобы проверить её поведение (возвращает prod_urls).
* `patch("src.suppliers.aliexpress.affiliated_products_generator.save_png_from_url")`: Патч функции сохранения изображений.
* `patch("src.suppliers.aliexpress.affiliated_products_generator.save_video_from_url")`: Патч функции сохранения видео.
* `patch("src.suppliers.aliexpress.affiliated_products_generator.j_dumps")`: Патч функции сериализации JSON (возвращает True).

**Проверяемые действия**:
* Проверяет, что метод `retrieve_product_details` был вызван.
* Проверяет, что длина списка обработанных продуктов `processed_products` равна 1.
* Проверяет, что `product_id` первого обработанного продукта равен "123".
* Проверяет правильность возвращаемого значения.


## Константы

### `MODE`

**Описание**: Константа, определяющая режим работы.

**Значение**: `'dev'`