# Модуль для создания парсера аргументов командной строки для GUI
## Обзор

Этот модуль предназначен для создания и настройки парсера аргументов командной строки, который используется для запуска графического интерфейса (GUI) проекта `hypotez`. Он определяет аргументы, такие как хост, порт, режим отладки, игнорирование файлов cookie и выбор провайдеров и браузеров для работы с cookie.

## Подробней

Модуль `gui_parser.py` предоставляет функцию `gui_parser`, которая создает экземпляр `ArgumentParser` и добавляет аргументы, необходимые для настройки и запуска GUI. Это позволяет пользователям настраивать различные параметры GUI через командную строку, такие как адрес хоста, порт, включение режима отладки, игнорирование cookie файлов, выбор игнорируемых провайдеров и браузеров для обработки cookie.

## Функции

### `gui_parser`

```python
def gui_parser() -> ArgumentParser:
    """Создает парсер аргументов командной строки для GUI.

    Returns:
        ArgumentParser: Объект парсера аргументов, настроенный для GUI.
    """
```

**Назначение**: Функция создает парсер аргументов командной строки, который используется для запуска графического интерфейса (GUI). Она добавляет аргументы, такие как хост, порт, режим отладки, игнорирование файлов cookie, а также выбор провайдеров и браузеров для работы с cookie.

**Возвращает**:
- `ArgumentParser`: Объект парсера аргументов, настроенный для GUI.

**Как работает функция**:

1. **Создание парсера**: Создается экземпляр класса `ArgumentParser` с описанием "Run the GUI".
2. **Добавление аргументов**: Добавляются следующие аргументы:
   - `--host`: Тип `str`, значение по умолчанию "0.0.0.0", помощь: "hostname".
   - `--port`, `-p`: Тип `int`, значение по умолчанию 8080, помощь: "port".
   - `--debug`, `-d`, `-debug`: `action="store_true"`, помощь: "debug mode".
   - `--ignore-cookie-files`: `action="store_true"`, помощь: "Don't read .har and cookie files.".
   - `--ignored-providers`: `nargs="+"`, `choices=[provider.__name__ for provider in Provider.__providers__ if provider.working]`, `default=[]`, помощь: "List of providers to ignore when processing request. (incompatible with --reload and --workers)".
   - `--cookie-browsers`: `nargs="+"`, `choices=[browser.__name__ for browser in browsers]`, `default=[]`, помощь: "List of browsers to access or retrieve cookies from.".
3. **Возврат парсера**: Возвращается настроенный объект `ArgumentParser`.

```ascii
Создание ArgumentParser
    ↓
Добавление аргументов (host, port, debug, ignore-cookie-files, ignored-providers, cookie-browsers)
    ↓
Возврат ArgumentParser
```

**Примеры**:

```python
# Пример использования функции gui_parser
from argparse import ArgumentParser

def gui_parser() -> ArgumentParser:
    """Создает парсер аргументов командной строки для GUI."""
    parser = ArgumentParser(description="Run the GUI")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="hostname")
    parser.add_argument("--port", "-p", type=int, default=8080, help="port")
    parser.add_argument("--debug", "-d", "-debug", action="store_true", help="debug mode")
    parser.add_argument("--ignore-cookie-files", action="store_true", help="Don't read .har and cookie files.")
    parser.add_argument("--ignored-providers", nargs="+", choices=[provider.__name__ for provider in Provider.__providers__ if provider.working],
                            default=[], help="List of providers to ignore when processing request. (incompatible with --reload and --workers)")
    parser.add_argument("--cookie-browsers", nargs="+", choices=[browser.__name__ for browser in browsers],\
                            default=[], help="List of browsers to access or retrieve cookies from.")
    return parser

parser = gui_parser()
args = parser.parse_args(["--port", "9000", "--debug"])
print(args.port)  # Вывод: 9000
print(args.debug) # Вывод: True

args = parser.parse_args([])
print(args.port)  # Вывод: 8080
print(args.debug) # Вывод: False