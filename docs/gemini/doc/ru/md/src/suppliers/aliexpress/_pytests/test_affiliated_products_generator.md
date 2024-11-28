# Модуль `hypotez/src/suppliers/aliexpress/_pytests/test_affiliated_products_generator.py`

## Обзор

Этот модуль содержит тесты для класса `AliAffiliatedProducts`, предназначенного для обработки данных аффилированных продуктов с AliExpress.  Тесты проверяют корректность работы методов `check_and_process_affiliate_products` и `process_affiliate_products`, используя мокирование внешних зависимостей.

## Фикстуры

### `ali_affiliated_products`

**Описание**: Фикстура, возвращающая экземпляр класса `AliAffiliatedProducts`.

**Параметры**:  
Нет.

**Возвращает**:
- `AliAffiliatedProducts`: Экземпляр класса `AliAffiliatedProducts` с заданными параметрами.


## Функции

### `test_check_and_process_affiliate_products`

**Описание**: Тестирует метод `check_and_process_affiliate_products`, проверяя, что он корректно вызывает метод `process_affiliate_products`.

**Параметры**:
- `ali_affiliated_products`: Экземпляр класса `AliAffiliatedProducts`.

**Возвращает**:
- Нет.

**Вызывает исключения**:
- Нет.


### `test_process_affiliate_products`

**Описание**: Тестирует метод `process_affiliate_products`, проверяя, что он корректно обрабатывает список продуктов.

**Параметры**:
- `ali_affiliated_products`: Экземпляр класса `AliAffiliatedProducts`.

**Возвращает**:
- `list`: Список обработанных продуктов.

**Вызывает исключения**:
- Нет.


**Примечания:**
Тест использует мокирование методов `retrieve_product_details`, `ensure_https`, `save_png_from_url`, `save_video_from_url` и `j_dumps` для имитации поведения внешних сервисов.  Ожидается, что метод вернет список продуктов, длина которого равна количеству элементов в `prod_urls`.