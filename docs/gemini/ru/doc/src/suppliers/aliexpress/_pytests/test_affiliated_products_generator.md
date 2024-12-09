# Модуль `hypotez/src/suppliers/aliexpress/_pytests/test_affiliated_products_generator.py`

## Обзор

Данный модуль содержит тесты для класса `AliAffiliatedProducts`, отвечающего за обработку аффилированных продуктов с AliExpress.  Тесты проверяют корректность работы методов `check_and_process_affiliate_products` и `process_affiliate_products`.

## Фикстуры

### `ali_affiliated_products`

**Описание**: Фикстура, возвращающая экземпляр класса `AliAffiliatedProducts` с заданными параметрами кампании, категории, языка и валюты.

**Возвращает**: Экземпляр класса `AliAffiliatedProducts`.

## Функции

### `test_check_and_process_affiliate_products`

**Описание**: Тестирует метод `check_and_process_affiliate_products`, проверяя, что он корректно вызывает метод `process_affiliate_products`.

**Аргументы**:
- `ali_affiliated_products`: экземпляр класса `AliAffiliatedProducts`, полученный через фикстуру.
- `prod_urls` (list): список URL-адресов продуктов.

**Вызывает**:
- `process_affiliate_products` (метод `AliAffiliatedProducts`).

**Проверяемые утверждения**:
- Метод `process_affiliate_products` вызывается ровно один раз с переданным списком `prod_urls`.


### `test_process_affiliate_products`

**Описание**: Тестирует метод `process_affiliate_products`, проверяя корректность обработки продуктов.

**Аргументы**:
- `ali_affiliated_products`: экземпляр класса `AliAffiliatedProducts`, полученный через фикстуру.
- `prod_urls` (list): список URL-адресов продуктов.

**Вызывает**:
- `retrieve_product_details`:  метод для получения деталей продукта.
- `ensure_https`: метод, который должен возвращать переданные ему данные.
- `save_png_from_url`: метод для сохранения изображения.
- `save_video_from_url`: метод для сохранения видео.
- `j_dumps`: метод для работы с JSON.


**Проверяемые утверждения**:
- `len(processed_products)` равно 1
- `processed_products[0].product_id` равно "123"
- Методы `retrieve_product_details`, `ensure_https`, `save_png_from_url`, `save_video_from_url` и `j_dumps` вызываются с ожидаемыми аргументами.


## Модульные тесты

**Описание**: Данный модуль содержит тесты для модуля.

**Выполняется**:
- При выполнении скрипта с параметром `__name__ == "__main__":`, запускаются тесты модуля `pytest`.