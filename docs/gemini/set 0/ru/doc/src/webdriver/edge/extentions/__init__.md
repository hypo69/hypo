# Модуль hypotez/src/webdriver/edge/extentions/__init__.py

## Обзор

Этот модуль содержит инициализационные константы и импорты для расширений WebDriver для браузера Edge.

## Переменные

### `MODE`

**Описание**: Строковая константа, определяющая режим работы.

**Значение**: 'dev' (в текущей реализации).

## Импорты

### `from packaging.version import Version`

**Описание**: Импортирует класс `Version` из модуля `packaging.version` для работы с версиями.

### `from .version import __version__, __doc__, __details__`

**Описание**: Импортирует переменные `__version__`, `__doc__`, и `__details__` из модуля `version.py` (предполагается, что он находится в той же директории).  Вероятно, эти переменные содержат информацию о версии, документацию и другие детали расширения.