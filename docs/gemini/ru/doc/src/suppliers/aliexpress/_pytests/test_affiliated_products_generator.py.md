# Документация для `test_affiliated_products_generator.py`

## Оглавление

- [Обзор](#обзор)
- [Фикстуры](#фикстуры)
    - [`ali_affiliated_products`](#ali_affiliated_products)
- [Тесты](#тесты)
    - [`test_check_and_process_affiliate_products`](#test_check_and_process_affiliate_products)
    - [`test_process_affiliate_products`](#test_process_affiliate_products)

## Обзор

Этот файл содержит тесты для модуля `affiliated_products_generator` в рамках поставщика AliExpress. Он использует `pytest` для проверки корректности работы методов `check_and_process_affiliate_products` и `process_affiliate_products` класса `AliAffiliatedProducts`.

## Фикстуры

### `ali_affiliated_products`

**Описание**:
Фикстура, возвращающая экземпляр класса `AliAffiliatedProducts`.

**Возвращает**:
- `AliAffiliatedProducts`: Экземпляр класса `AliAffiliatedProducts`.

## Тесты

### `test_check_and_process_affiliate_products`

**Описание**:
Тестирует метод `check_and_process_affiliate_products`, проверяя, что он вызывает метод `process_affiliate_products` с правильными аргументами.

**Параметры**:
- `ali_affiliated_products` (AliAffiliatedProducts): Экземпляр класса `AliAffiliatedProducts`, предоставляемый фикстурой.

**Проверяет**:
- Вызов метода `process_affiliate_products` с переданными `prod_urls`.

### `test_process_affiliate_products`

**Описание**:
Тестирует метод `process_affiliate_products` класса `AliAffiliatedProducts`, проверяя, что он правильно обрабатывает продукты и возвращает ожидаемые результаты.

**Параметры**:
- `ali_affiliated_products` (AliAffiliatedProducts): Экземпляр класса `AliAffiliatedProducts`, предоставляемый фикстурой.

**Проверяет**:
- Правильность обработки продуктов, включая извлечение деталей продукта, генерацию партнерских ссылок и сохранение медиа-контента.
- Возвращаемый список обработанных продуктов и их атрибуты.
- Вызовы моков.

**Моки**:
- `retrieve_product_details`: мок метода для возвращения данных о продукте.
- `ensure_https`: мок функции, гарантирующей, что URL начинается с `https`.
- `save_png_from_url`: мок функции для сохранения изображений.
- `save_video_from_url`: мок функции для сохранения видео.
- `j_dumps`: мок функции для преобразования объекта в строку JSON.