# Документация модуля `test_affiliated_products_generator`

## Обзор

Этот модуль содержит тесты для класса `AliAffiliatedProducts`, проверяя корректность его методов `check_and_process_affiliate_products` и `process_affiliate_products`. Он использует `pytest` для запуска тестов и `unittest.mock` для мокирования внешних зависимостей.

## Содержание

- [Обзор](#обзор)
- [Фикстуры](#Фикстуры)
    - [ali_affiliated_products](#ali_affiliated_products)
- [Функции](#Функции)
    - [test_check_and_process_affiliate_products](#test_check_and_process_affiliate_products)
    - [test_process_affiliate_products](#test_process_affiliate_products)

## Фикстуры

### `ali_affiliated_products`

**Описание**:
Фикстура, которая возвращает экземпляр класса `AliAffiliatedProducts` с заданными параметрами.

**Возвращает**:
- `AliAffiliatedProducts`: Экземпляр класса `AliAffiliatedProducts`.

## Функции

### `test_check_and_process_affiliate_products`

**Описание**:
Тестирует метод `check_and_process_affiliate_products` класса `AliAffiliatedProducts`. Проверяет, что метод `process_affiliate_products` вызывается корректно с переданными `prod_urls`.

**Параметры**:
- `ali_affiliated_products` (AliAffiliatedProducts): Фикстура, представляющая экземпляр класса `AliAffiliatedProducts`.

### `test_process_affiliate_products`

**Описание**:
Тестирует метод `process_affiliate_products` класса `AliAffiliatedProducts`. Проверяет, что метод корректно обрабатывает URL товаров, получает их детали и возвращает обработанные данные. Использует моки для внешних зависимостей.

**Параметры**:
- `ali_affiliated_products` (AliAffiliatedProducts): Фикстура, представляющая экземпляр класса `AliAffiliatedProducts`.

**Возвращает**:
- `list`: Список обработанных продуктов, где каждый элемент является объектом с атрибутами `product_id`, `promotion_link`, `product_main_image_url` и `product_video_url`.