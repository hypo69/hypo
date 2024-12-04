# Модуль hypotez/src/endpoints/prestashop/language.py

## Обзор

Данный модуль предоставляет класс `PrestaLanguage`, предназначенный для управления языками в магазине PrestaShop. Он использует базовый класс `PrestaShop` для взаимодействия с API PrestaShop и добавляет методы для работы с языками.

## Классы

### `PrestaLanguage`

**Описание**: Класс `PrestaLanguage` наследуется от класса `PrestaShop` и предоставляет методы для добавления, удаления, обновления и получения информации о языках в магазине PrestaShop.

**Методы**:

- `__init__`

#### `__init__`

**Описание**: Инициализирует объект `PrestaLanguage`.

**Параметры**:
- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект `SimpleNamespace` с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
-  (None): Не возвращает значение.

**Вызывает исключения**:
- `ValueError`: Если не указаны оба параметра `api_domain` и `api_key`.

**Пример использования**:

```python
prestalanguage = PrestaLanguage(credentials={'api_domain': 'your_api_domain', 'api_key': 'your_api_key'})
```


## Функции

(В данном файле нет функций, кроме методов класса)

```