# Модуль `hypotez/src/endpoints/prestashop/language.py`

## Обзор

Модуль `language.py` предоставляет класс `PrestaLanguage`, предназначенный для работы с языками в магазине PrestaShop.  Класс наследуется от класса `PrestaShop` и предоставляет методы для добавления, удаления, обновления и получения деталей языковых настроек.

## Оглавление

- [Модуль `language.py`](#модуль-languagepy)
- [Класс `PrestaLanguage`](#класс-prestalanguage)
    - [Метод `__init__`](#метод-init)
    - [Метод `add_language_PrestaShop`](#метод-add_language_prestashop)
    - [Метод `delete_language_PrestaShop`](#метод-delete_language_prestashop)
    - [Метод `update_language_PrestaShop`](#метод-update_language_prestashop)
    - [Метод `get_language_details_PrestaShop`](#метод-get_language_details_prestashop)


## Классы

### `PrestaLanguage`

**Описание**: Класс `PrestaLanguage` расширяет функциональность класса `PrestaShop`, предоставляя методы для управления языками в системе PrestaShop.

**Методы**:

#### `__init__`

**Описание**: Инициализирует объект `PrestaLanguage`.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
- Не имеет возвращаемого значения.

**Вызывает исключения**:

- `ValueError`: Если не указаны значения для `api_domain` и `api_key`.


```python
def __init__(self,
                 credentials: Optional[dict | SimpleNamespace] = None,
                 api_domain: Optional[str] = None,
                 api_key: Optional[str] = None,
                 *args, **kwards):
    """Инициализация класса PrestaLanguage.

    Args:
        credentials (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. Defaults to None.
        api_domain (Optional[str], optional): Домен API. Defaults to None.
        api_key (Optional[str], optional): Ключ API. Defaults to None.
    """

    if credentials is not None:
        api_domain = credentials.get('api_domain', api_domain)
        api_key = credentials.get('api_key', api_key)

    if not api_domain or not api_key:
        raise ValueError('Необходимы оба параметра: api_domain и api_key.')

    super().__init__(api_domain, api_key, *args, **kwards)
```


#### (Другие методы `add_language_PrestaShop`, `delete_language_PrestaShop`, `update_language_PrestaShop`, `get_language_details_PrestaShop`)

*Эти методы предполагаются, но не реализованы в представленном коде.  Для полноценной документации необходимы их реализации с описаниями аргументов, возвращаемых значений и возможных исключений.*

```
```
```
```

**Примечание:**  Документация для методов `add_language_PrestaShop`, `delete_language_PrestaShop`, `update_language_PrestaShop`, `get_language_details_PrestaShop` не может быть сгенерирована без наличия кода этих методов.