# `quickstart.py`

## Обзор

Модуль `quickstart.py` предназначен для демонстрации базового использования Apps Script API от Google. Он выполняет следующие действия: создает новый проект скрипта, загружает в него файлы и выводит URL скрипта для пользователя.

## Содержание

- [Обзор](#обзор)
- [Константы](#константы)
- [Функции](#функции)
    - [`main`](#main)

## Константы

### `MODE`

```python

```

Режим работы приложения, по умолчанию установлен в `dev`.

### `SCOPES`

```python
SCOPES = ['https://www.googleapis.com/auth/script.projects']
```

Список областей доступа, необходимых для работы с Apps Script API.

### `SAMPLE_CODE`

```python
SAMPLE_CODE = '''
function helloWorld() {
  console.log("Hello, world!");
}
'''.strip()
```

Пример кода JavaScript для скрипта.

### `SAMPLE_MANIFEST`

```python
SAMPLE_MANIFEST = '''
{
  "timeZone": "America/New_York",
  "exceptionLogging": "CLOUD"
}
'''.strip()
```

Пример манифеста проекта скрипта в формате JSON.

## Функции

### `main`

```python
def main():
    """Calls the Apps Script API."""
```

**Описание**:
Основная функция, вызывающая Apps Script API для создания нового проекта, загрузки файлов и вывода URL скрипта.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Вызывает исключения**:
- `googleapiclient.errors.HttpError`: Ошибка, возникающая при взаимодействии с API.
```