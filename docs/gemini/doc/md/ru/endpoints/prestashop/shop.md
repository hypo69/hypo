```markdown
# Модуль `hypotez/src/endpoints/prestashop/shop.py`

## Обзор

Модуль `shop.py` содержит класс `PrestaShopShop`, предназначенный для взаимодействия с магазинами PrestaShop. Он наследуется от класса `PrestaShop` и предоставляет методы для работы с магазинами, используя предоставленные API-ключ и домен.

## Оглавление

* [Функции](#функции)
* [Класс `PrestaShopShop`](#класс-prestashopshop)


## Класс `PrestaShopShop`

### Описание

Класс `PrestaShopShop` наследует функциональность от класса `PrestaShop` и предоставляет расширенный функционал для работы с магазинами PrestaShop.

### Методы

* `__init__`: Инициализирует объект `PrestaShopShop`.


#### `__init__`

**Описание**: Инициализирует экземпляр класса `PrestaShopShop`.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
- Не имеет возвращаемого значения.

**Вызывает исключения**:
- `ValueError`: Если не предоставлены значения `api_domain` и `api_key`.  Подразумевается, что эти значения либо содержатся в объекте `credentials`, либо передаются явно.



```
```
