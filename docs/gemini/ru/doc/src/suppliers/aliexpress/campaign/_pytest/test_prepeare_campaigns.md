# Модуль `hypotez/src/suppliers/aliexpress/campaign/_pytest/test_prepeare_campaigns.py`

## Обзор

Этот модуль содержит тесты для функций, связанных с подготовкой рекламных кампаний на AliExpress.  Тесты покрывают обработку категорий, отдельных кампаний и основной функции `main`.  Используются фикстуры для подмены внешних зависимостей, таких как `jjson`, `logger` и `AliPromoCampaign`, для изолированного тестирования.

## Оглавление

* [Функции](#функции)
    * [`test_update_category_success`](#test_update_category_success)
    * [`test_update_category_failure`](#test_update_category_failure)
    * [`test_process_campaign_category_success`](#test_process_campaign_category_success)
    * [`test_process_campaign_category_failure`](#test_process_campaign_category_failure)
    * [`test_process_campaign`](#test_process_campaign)
    * [`test_main`](#test_main)
* [Фикстуры](#фикстуры)
    * [`mock_j_loads`](#mock_j_loads)
    * [`mock_j_dumps`](#mock_j_dumps)
    * [`mock_logger`](#mock_logger)
    * [`mock_get_directory_names`](#mock_get_directory_names)
    * [`mock_ali_promo_campaign`](#mock_ali_promo_campaign)


## Функции

### `test_update_category_success`

**Описание**: Тестирует успешную работу функции `update_category`.

**Параметры**:
* `mock_j_loads`:  Заглушка для `src.utils.jjson.j_loads`, возвращающая словарь.
* `mock_j_dumps`: Заглушка для `src.utils.jjson.j_dumps`,  используемая для проверки вызова.
* `mock_logger`: Заглушка для логгера.

**Возвращает**:
* `True`: Функция возвращает `True` при успешном выполнении.

**Вызывает исключения**:
* Никаких исключений не должно возникать при успешном выполнении.


### `test_update_category_failure`

**Описание**: Тестирует обработку исключения в функции `update_category`.

**Параметры**:
* `mock_j_loads`: Заглушка для `src.utils.jjson.j_loads`, которая генерирует исключение.
* `mock_j_dumps`: Заглушка для `src.utils.jjson.j_dumps`.
* `mock_logger`: Заглушка для логгера.


**Возвращает**:
* `False`: Функция возвращает `False` при возникновении исключения.


**Вызывает исключения**:
* `Exception`: Мок  `mock_j_loads` генерирует исключение, которое обрабатывается.


### `test_process_campaign_category_success`

**Описание**:  Тест успешного выполнения `process_campaign_category`.

**Параметры**:
* `mock_ali_promo_campaign`: Заглушка для класса `AliPromoCampaign`.
* `mock_logger`: Заглушка для логгера.


**Возвращает**:
* `result is not None`:  Функция возвращает не `None` при успешном выполнении.

**Вызывает исключения**:
* Никаких исключений не должно возникать при успешном выполнении.


### `test_process_campaign_category_failure`

**Описание**: Тест обработки исключения в `process_campaign_category`.

**Параметры**:
* `mock_ali_promo_campaign`: Заглушка для `AliPromoCampaign`.
* `mock_logger`: Заглушка для логгера.


**Возвращает**:
* `result is None`:  Функция возвращает `None` при возникновении исключения.

**Вызывает исключения**:
* `Exception`: Мок `mock_ali_promo_campaign` генерирует исключение, которое обрабатывается.



### `test_process_campaign`

**Описание**: Тест функции `process_campaign`.

**Параметры**:
* `mock_get_directory_names`: Заглушка для функции, возвращающей список категорий.
* `mock_logger`: Заглушка для логгера.

**Возвращает**:
* `len(results) == 2`:  Функция возвращает список результатов, длина которого равна количеству категорий.

**Вызывает исключения**:
* Никаких исключений не должно возникать при успешном выполнении.

### `test_main`

**Описание**: Тест основной функции `main`.

**Параметры**:
* `mock_get_directory_names`: Заглушка для функции, возвращающей список категорий.

**Возвращает**:
* Ничего, функция `main` является асинхронной и не возвращает значения напрямую.

**Вызывает исключения**:
* Никаких исключений не должно возникать при успешном выполнении.

## Фикстуры

### `mock_j_loads`

**Описание**: Фикстура для подмены `src.utils.jjson.j_loads`.


### `mock_j_dumps`

**Описание**: Фикстура для подмены `src.utils.jjson.j_dumps`.

### `mock_logger`

**Описание**: Фикстура для подмены логгера.


### `mock_get_directory_names`

**Описание**: Фикстура для подмены функции `src.utils.get_directory_names`.

### `mock_ali_promo_campaign`

**Описание**: Фикстура для подмены класса `src.suppliers.aliexpress.campaign.AliPromoCampaign`.