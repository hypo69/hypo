# Модуль `hypotez/src/endpoints/prestashop/shop.py`

## Обзор

Этот модуль предоставляет класс `PrestaShopShop`, который расширяет класс `PrestaShop` для работы с магазинами PrestaShop. Класс содержит методы для взаимодействия с API PrestaShop и обработки различных запросов.

## Классы

### `PrestaShopShop`

**Описание**: Класс для работы с магазинами PrestaShop, наследуется от `PrestaShop`.

**Методы**:

- `__init__`: Инициализирует объект `PrestaShopShop`.


**Методы с детальным описанием:**


#### `__init__`

**Описание**: Инициализирует объект магазина PrestaShop.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.


**Возвращает**:
-  Не имеет возвращаемого значения.


**Вызывает исключения**:

- `ValueError`: Если не заданы оба параметра `api_domain` и `api_key`.


## Функции

(В этом файле нет функций, только класс)


## Модули

(Список импортированных модулей)

- `header`
- `gs`
- `src.logger.logger`
- `src.utils.jjson`
- `.api` (из текущего пакета)
- `src.logger.exceptions`
- `pathlib`
- `attr`
- `sys`
- `os`
- `types`


## Константы

(Если есть константы, то здесь их описание)


- `MODE`: 'dev'


## Замечания

(Любые дополнительные замечания)

```
```