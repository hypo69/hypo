# Модуль hypotez/src/endpoints/prestashop/language.py

## Обзор

Модуль `language.py` предоставляет класс `PrestaLanguage`, предназначенный для управления языками в магазине PrestaShop.  Класс наследуется от `PrestaShop` и предоставляет методы для добавления, удаления, обновления и получения информации о языках.

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

**Описание**: Класс, отвечающий за управление языками магазина PrestaShop.

**Пример использования**:

```python
prestalanguage = PrestaLanguage(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
prestalanguage.add_language_PrestaShop('English', 'en')
prestalanguage.delete_language_PrestaShop(3)
prestalanguage.update_language_PrestaShop(4, 'Updated Language Name')
print(prestalanguage.get_language_details_PrestaShop(5))
```

**Методы**:

#### `__init__`

**Описание**: Инициализация класса `PrestaLanguage`.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:  Не имеет значения.

**Вызывает исключения**:

- `ValueError`: Если не заданы значения для `api_domain` и `api_key`.


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
(Другие методы `add_language_PrestaShop`, `delete_language_PrestaShop`, `update_language_PrestaShop`, `get_language_details_PrestaShop` требуют реализации.)


```
```