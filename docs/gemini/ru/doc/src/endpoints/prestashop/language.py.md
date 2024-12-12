# Модуль `language.py`

## Обзор

Модуль `language.py` предоставляет класс `PrestaLanguage`, который используется для управления языками в магазине PrestaShop через API. Он включает в себя методы для добавления, удаления, обновления и получения информации о языках.

## Содержание

- [Классы](#классы)
    - [`PrestaLanguage`](#prestalanguage)
        - [`__init__`](#__init__)
- [Функции](#функции)

## Классы

### `PrestaLanguage`

**Описание**: Класс `PrestaLanguage` предназначен для взаимодействия с API PrestaShop для управления языками магазина. Он предоставляет методы для добавления, удаления, обновления и получения информации о языках.

**Пример использования:**

```python
prestalanguage = PrestaLanguage(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
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
- `ValueError`: Если не предоставлены `api_domain` и `api_key` или они отсутствуют в `credentials`.

## Функции