# Модуль `language.py`

## Обзор

Модуль `language.py` предоставляет класс `PrestaLanguage` для взаимодействия с языковыми настройками магазина PrestaShop через API. Этот класс позволяет добавлять, удалять, обновлять и получать информацию о языках.

## Содержание

- [Классы](#Классы)
  - [`PrestaLanguage`](#PrestaLanguage)
    - [`__init__`](#__init__)
    - [`add_language_PrestaShop`](#add_language_PrestaShop)
    - [`delete_language_PrestaShop`](#delete_language_PrestaShop)
    - [`update_language_PrestaShop`](#update_language_PrestaShop)
    - [`get_language_details_PrestaShop`](#get_language_details_PrestaShop)
    
## Классы

### `PrestaLanguage`

**Описание**: Класс для управления языками в PrestaShop через API.

**Пример использования**
```python
prestalanguage = PrestaLanguage(API_DOMAIN="your_api_domain", API_KEY="your_api_key")
prestalanguage.add_language_PrestaShop('English', 'en')
prestalanguage.delete_language_PrestaShop(3)
prestalanguage.update_language_PrestaShop(4, 'Updated Language Name')
print(prestalanguage.get_language_details_PrestaShop(5))
```

#### `__init__`

**Описание**: Инициализирует экземпляр класса `PrestaLanguage`.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `ValueError`: Если не предоставлены `api_domain` и `api_key`.

#### `add_language_PrestaShop`

**Описание**: Добавляет новый язык в PrestaShop.

**Параметры**:
- `name` (str): Название добавляемого языка.
- `iso_code` (str): ISO-код добавляемого языка.
- `active` (int, optional): Статус активности языка (1 - активен, 0 - неактивен). По умолчанию `1`.
- `format` (str, optional): Формат языка (например, 'en-US'). По умолчанию `None`.

**Возвращает**:
- `dict | None`: Словарь с данными о добавленном языке или `None`, если произошла ошибка.

**Вызывает исключения**:
- `PrestaShopException`: Если возникает ошибка при выполнении запроса к API.

#### `delete_language_PrestaShop`

**Описание**: Удаляет язык из PrestaShop по его ID.

**Параметры**:
- `language_id` (int): ID языка для удаления.

**Возвращает**:
- `dict | None`: Словарь с подтверждением удаления или `None`, если произошла ошибка.

**Вызывает исключения**:
- `PrestaShopException`: Если возникает ошибка при выполнении запроса к API.

#### `update_language_PrestaShop`

**Описание**: Обновляет данные языка в PrestaShop по его ID.

**Параметры**:
- `language_id` (int): ID языка для обновления.
- `name` (str, optional): Новое название языка. По умолчанию `None`.
- `iso_code` (str, optional): Новый ISO-код языка. По умолчанию `None`.
- `active` (int, optional): Новый статус активности языка (1 - активен, 0 - неактивен). По умолчанию `None`.
- `format` (str, optional): Новый формат языка. По умолчанию `None`.

**Возвращает**:
- `dict | None`: Словарь с данными об обновленном языке или `None`, если произошла ошибка.

**Вызывает исключения**:
- `PrestaShopException`: Если возникает ошибка при выполнении запроса к API.

#### `get_language_details_PrestaShop`

**Описание**: Получает подробную информацию о языке из PrestaShop по его ID.

**Параметры**:
- `language_id` (int): ID языка, информацию о котором нужно получить.

**Возвращает**:
- `dict | None`: Словарь с данными о языке или `None`, если произошла ошибка.

**Вызывает исключения**:
- `PrestaShopException`: Если возникает ошибка при выполнении запроса к API.