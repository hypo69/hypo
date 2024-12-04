# Модуль `hypotez/src/endpoints/advertisement/facebook/facebook_fields.py`

## Обзор

Данный модуль содержит класс `FacebookFields`, предназначенный для работы с полями объявлений и событий Facebook.  Класс загружает данные о полях из файла `facebook_feilds.json`, находящегося в папке `advertisement/facebok` проекта.

## Классы

### `FacebookFields`

**Описание**: Класс `FacebookFields` предназначен для хранения и доступа к полям объявлений и событий Facebook, загруженным из файла JSON.

**Методы**:

- `__init__`
  - **Описание**: Инициализирует экземпляр класса. Загружает данные из файла.
  - **Возвращает**:  Экземпляр класса.
  - **Внутренние методы**:
    - `_payload`
      - **Описание**: Загружает данные о полях из файла `facebook_feilds.json` и устанавливает их в атрибуты класса.
      - **Возвращает**:
        - `True`: Если загрузка прошла успешно.
        - `None`: Если файл не загружен или содержит ошибки.
      - **Обрабатываемые исключения**:
        - Возможны исключения при работе с файловой системой (например, `FileNotFoundError`).
        - Возможны исключения при работе с JSON (например, `json.JSONDecodeError`).


## Функции

(В данном файле нет независимых функций, только метод класса)


## Использование

```python
from hypotez.src.endpoints.advertisement.facebook.facebook_fields import FacebookFields

# Создание экземпляра класса
facebook_fields = FacebookFields()

# Доступ к загруженным полям (например):
try:
    ad_title_field = facebook_fields.ad_title
    print(f"Поле 'ad_title': {ad_title_field}")
except AttributeError as ex:
  print(f"Ошибка доступа к полю: {ex}")

```

**Примечание**:  Обратите внимание, что для корректной работы необходимо наличие файла `facebook_feilds.json` по указанному пути.  Необходима корректная настройка переменной `gs.path.src`. Код обработки ошибок в `_payload` требует доработки (обработка конкретных исключений `json.JSONDecodeError`, `FileNotFoundError` и др.).