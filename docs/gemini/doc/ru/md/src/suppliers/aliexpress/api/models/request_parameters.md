# Модуль hypotez/src/suppliers/aliexpress/api/models/request_parameters.py

## Обзор

Этот модуль определяет перечисления для параметров запроса API AliExpress.  Он содержит классы `ProductType`, `SortBy`, и `LinkType`,  предоставляющие константы для различных типов продуктов, способов сортировки и типов ссылок.

## Перечисления

### `ProductType`

**Описание**:  Класс `ProductType` определяет типы продуктов, которые могут быть запрошены у AliExpress API.

**Константы**:

- `ALL`:  Представляет все типы продуктов.
- `PLAZA`: Представляет тип продуктов PLAZA.
- `TMALL`: Представляет тип продуктов TMALL.


### `SortBy`

**Описание**: Класс `SortBy` определяет способы сортировки результатов запроса.

**Константы**:

- `SALE_PRICE_ASC`: Сортировка по цене (по возрастанию).
- `SALE_PRICE_DESC`: Сортировка по цене (по убыванию).
- `LAST_VOLUME_ASC`: Сортировка по последнему объему (по возрастанию).
- `LAST_VOLUME_DESC`: Сортировка по последнему объему (по убыванию).


### `LinkType`

**Описание**: Класс `LinkType` определяет типы ссылок на продукты.

**Константы**:

- `NORMAL`:  Обычный тип ссылки.
- `HOTLINK`: Тип ссылки "горячая ссылка".