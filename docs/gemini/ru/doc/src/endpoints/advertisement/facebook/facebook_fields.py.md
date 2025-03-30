# Модуль facebook_fields

## Обзор

Модуль `facebook_fields.py` предназначен для определения и загрузки полей, используемых в рекламных объявлениях и событиях Facebook. Он содержит класс `FacebookFields`, который инициализирует и загружает данные полей из JSON-файла.

## Подробней

Этот модуль играет важную роль в проекте, обеспечивая централизованное управление полями, необходимыми для работы с Facebook API. Он упрощает процесс настройки и обновления структуры данных, используемых в рекламных кампаниях и мероприятиях. Класс `FacebookFields` при инициализации загружает данные из файла `facebook_feilds.json` и устанавливает их как атрибуты экземпляра, что позволяет легко получать доступ к этим полям.

## Классы

### `FacebookFields`

**Описание**: Класс для хранения и управления полями, используемыми в рекламных объявлениях и событиях Facebook.

**Методы**:
- `__init__`: Инициализирует класс и вызывает метод `_payload` для загрузки данных.
- `_payload`: Загружает данные полей из JSON-файла и устанавливает их как атрибуты экземпляра.

**Параметры**:
- Нет явных параметров, но класс использует файл `facebook_feilds.json` для инициализации своих атрибутов.

**Примеры**

```python
from src.endpoints.advertisement.facebook.facebook_fields import FacebookFields

facebook_fields = FacebookFields()
# Теперь можно обращаться к полям как к атрибутам экземпляра, например:
# print(facebook_fields.some_field)
```

## Функции

### `_payload`

```python
def _payload(self):
    """
    Загружает данные полей из JSON-файла и устанавливает их как атрибуты экземпляра.

    Args:
        self (FacebookFields): Экземпляр класса `FacebookFields`.

    Returns:
        bool | None: Возвращает `True` в случае успешной загрузки и установки полей, `None` в случае ошибки.

    Raises:
        FileNotFoundError: Если файл `facebook_feilds.json` не найден.
        json.JSONDecodeError: Если файл `facebook_feilds.json` содержит невалидный JSON.

    Example:
        >>> facebook_fields = FacebookFields()
        >>> facebook_fields._payload()
        True
    """
```

**Описание**: Метод `_payload` загружает данные полей из JSON-файла (`facebook_feilds.json`) и устанавливает их как атрибуты экземпляра класса `FacebookFields`. Если файл не найден или содержит ошибки, регистрируется сообщение об ошибке.

**Параметры**:
- `self`: Ссылка на экземпляр класса.

**Возвращает**:
- `bool | None`: Возвращает `True` в случае успешной загрузки и установки полей, `None` в случае ошибки.

**Вызывает исключения**:
- `FileNotFoundError`: Если файл `facebook_feilds.json` не найден.
- `json.JSONDecodeError`: Если файл `facebook_feilds.json` содержит невалидный JSON.

**Примеры**:

```python
from src.endpoints.advertisement.facebook.facebook_fields import FacebookFields

facebook_fields = FacebookFields()
if facebook_fields._payload():
    print("Поля успешно загружены")
else:
    print("Ошибка при загрузке полей")