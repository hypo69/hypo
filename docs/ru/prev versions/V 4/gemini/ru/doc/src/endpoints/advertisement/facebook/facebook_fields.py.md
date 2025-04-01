# Модуль facebook_fields

## Обзор

Модуль `facebook_fields.py` предназначен для работы с полями, используемыми в рекламных объявлениях и событиях Facebook. Он содержит класс `FacebookFields`, который загружает необходимые данные из JSON-файла и делает их доступными для использования.

## Подробней

Этот модуль используется для централизованного хранения и управления полями, необходимыми для взаимодействия с API Facebook в контексте рекламных кампаний и событий. Использование класса `FacebookFields` позволяет избежать дублирования кода и упрощает обновление и поддержку структуры данных, используемых для работы с Facebook. Расположение файла в структуре проекта указывает на его роль в обработке данных, связанных с рекламными объявлениями Facebook.

## Классы

### `FacebookFields`

**Описание**: Класс `FacebookFields` предназначен для хранения и предоставления полей, используемых в рекламных объявлениях и событиях Facebook.

**Методы**:
- `__init__`: Инициализирует экземпляр класса и вызывает метод `_payload` для загрузки данных.
- `_payload`: Загружает данные из JSON-файла и устанавливает их как атрибуты экземпляра класса.

**Параметры**:
- Отсутствуют параметры, класс инициализируется без параметров.

**Примеры**

```python
from src.endpoints.advertisement.facebook.facebook_fields import FacebookFields

facebook_fields = FacebookFields()
# Теперь можно получить доступ к полям, определенным в JSON, как к атрибутам объекта
# Например: facebook_fields.ad_name
```

## Функции

### `_payload`

```python
def _payload(self):
    """ """
    ...
```

**Описание**: Метод `_payload` загружает данные из JSON-файла, содержащего поля для Facebook, и устанавливает их как атрибуты экземпляра класса `FacebookFields`.

**Параметры**:
- Отсутствуют параметры.

**Возвращает**:
- `True` в случае успешной загрузки и установки данных, `None` в случае ошибки.

**Вызывает исключения**:
- Не вызывает исключений напрямую, но может возникнуть исключение при попытке чтения или разбора JSON-файла.

**Примеры**:
```python
from src.endpoints.advertisement.facebook.facebook_fields import FacebookFields

facebook_fields = FacebookFields()
# После инициализации класса, метод _payload вызывается автоматически
# и поля из JSON-файла становятся доступны как атрибуты экземпляра класса.
# Пример доступа к полю:
# ad_name = facebook_fields.ad_name
```
```python
from pathlib import Path
from src.utils.jjson import j_loads

def _payload(self):
    """ """
    ...
    data = j_loads (Path (gs.path.src, 'advertisement', 'facebok', 'facebook_feilds.json'))
    if not data:
        logger.debug(f"Ошибка загрузки полей из файла {gs.path.src}/advertisement/facebok/facebook_feilds.json")
        return 
    for name, value in data.items():
        setattr(self, f'{name}', value)
    return True