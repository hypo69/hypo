# Модуль hypotez/src/endpoints/prestashop/language.py

## Обзор

Этот модуль предоставляет класс `PrestaLanguage`, предназначенный для работы с языками в магазине PrestaShop через API. Класс наследуется от `PrestaShop` и предоставляет методы для добавления, удаления, обновления и получения информации о языках.

## Классы

### `PrestaLanguage`

**Описание**:  Класс, отвечающий за управление языками в магазине PrestaShop.  Позволяет добавлять, удалять, обновлять и получать информацию о языках.

**Методы**:

- `__init__`


**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Описание метода `__init__`**:

**Описание**: Инициализация класса `PrestaLanguage`.

**Параметры**:

- `credentials` (Optional[dict | SimpleNamespace], optional): Словарь или объект SimpleNamespace с параметрами `api_domain` и `api_key`. По умолчанию `None`.
- `api_domain` (Optional[str], optional): Домен API. По умолчанию `None`.
- `api_key` (Optional[str], optional): Ключ API. По умолчанию `None`.

**Возвращает**:
-  Не имеет возвращаемого значения.

**Вызывает исключения**:

- `ValueError`: Если не заданы `api_domain` и `api_key`.

**Примечания**: Если `credentials` предоставлен, значения `api_domain` и `api_key` берутся из него. Если ни `credentials`, ни `api_domain`, ни `api_key` не заданы, возникает `ValueError`.

**Примеры использования (см. документацию класса):**

```python
prestalanguage = PrestaLanguage(API_DOMAIN=API_DOMAIN, API_KEY=API_KEY)
```


```python
prestalanguage = PrestaLanguage(credentials={'api_domain': 'example.com', 'api_key': 'your_api_key'})
```


## Дополнительные заметки

Данный модуль предполагает существование модулей `src.endpoints.prestashop.api`, `src`, `src.utils.printer`,  `src.logger.logger`, `src.logger.exceptions`, и `header`.  Они должны быть импортированы и доступны для работы.


```
```
```
```