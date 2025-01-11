# Модуль `hypotez/src/suppliers/aliexpress/_pytests/test_affiliated_products_generator.py`

## Обзор

Этот модуль содержит тесты для класса `AliAffiliatedProducts`, отвечающего за генерацию и обработку аффилированных продуктов с AliExpress.  Модуль использует фреймворк `pytest` для тестирования функций проверки и обработки аффилированных ссылок.  Тесты проверяют корректное вызов методов и обработку возвращаемых значений.

## Фикстуры

### `ali_affiliated_products`

**Описание**: Фикстура, возвращающая экземпляр класса `AliAffiliatedProducts` с заданными параметрами кампании, категории, языка и валюты.

**Возвращает**: `AliAffiliatedProducts` - Экземпляр класса, используемый для тестирования.

## Функции

### `test_check_and_process_affiliate_products`

**Описание**: Тестирует метод `check_and_process_affiliate_products` для проверки корректного вызова метода `process_affiliate_products`.

**Параметры**:
- `ali_affiliated_products`: Экземпляр класса `AliAffiliatedProducts`.
- `prod_urls`: Список ссылок на продукты.

**Возвращает**: Не применимо (тест).

**Вызывает исключения**: Нет.

### `test_process_affiliate_products`

**Описание**: Тестирует метод `process_affiliate_products` для проверки корректной обработки продуктов.

**Параметры**:
- `ali_affiliated_products`: Экземпляр класса `AliAffiliatedProducts`.
- `prod_urls`: Список ссылок на продукты.

**Возвращает**: Список обработанных продуктов.

**Вызывает исключения**:  Нет.

**Детали**:
- Использует `patch` для мокирования методов `retrieve_product_details`, `ensure_https`, `save_png_from_url`, `save_video_from_url`, `j_dumps` для изоляции тестируемого кода от внешних зависимостей.
- Проверяет, что количество обработанных продуктов соответствует ожидаемому (в данном случае 1).
- Проверяет, что полученные данные содержат ожидаемые поля ( `product_id`, `promotion_link`, `product_main_image_url`, `product_video_url`).


##  Используемые модули

- `pytest`
- `unittest.mock`
- `src.suppliers.aliexpress.affiliated_products_generator`
- `types`