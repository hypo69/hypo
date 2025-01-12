# Модуль `language.py`

## Обзор

Модуль `language.py` предоставляет класс `PrestaLanguage` для управления языковыми настройками в магазине PrestaShop. Класс позволяет добавлять, удалять, обновлять и получать информацию о языках.

## Оглавление

1.  [Классы](#классы)
    *   [PrestaLanguage](#PrestaLanguage)
2.  [Функции](#функции)
   

## Классы

### `PrestaLanguage`

**Описание**: Класс `PrestaLanguage` предназначен для управления языками в PrestaShop.

**Пример использования:**

```python
prestalanguage = PrestaLanguage(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
prestalanguage.add_language_PrestaShop('English', 'en')
prestalanguage.delete_language_PrestaShop(3)
prestalanguage.update_language_PrestaShop(4, 'Updated Language Name')
print(prestalanguage.get_language_details_PrestaShop(5))
```

**Методы**:

- `__init__`: Инициализация класса `PrestaLanguage`.

   **Описание**: Инициализирует экземпляр класса `PrestaLanguage` с параметрами подключения к API PrestaShop.

   **Параметры**:
      - `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
      - `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
      - `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.
      - `*args`: Произвольные позиционные аргументы.
      - `**kwards`: Произвольные именованные аргументы.

   **Возвращает**:
        - `None`

   **Вызывает исключения**:
        - `ValueError`: Если не переданы оба параметра `api_domain` и `api_key`.

## Функции

В данном файле функции отсутствуют.