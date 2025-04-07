# Модуль для парсинга аргументов командной строки для GUI
==========================================================

Модуль содержит функцию `gui_parser`, которая создает парсер аргументов командной строки, используемый для настройки и запуска графического интерфейса (GUI).

Пример использования
----------------------

```python
>>> parser = gui_parser()
>>> args = parser.parse_args(['--host', '127.0.0.1', '--port', '5000', '--debug'])
>>> print(args.host, args.port, args.debug)
127.0.0.1 5000 True
```

## Функции

### `gui_parser`

```python
def gui_parser() -> ArgumentParser:
    """Создает парсер аргументов командной строки для настройки и запуска GUI.

    Args:
        None

    Returns:
        ArgumentParser: Объект парсера аргументов.

    Raises:
        None
    """
```

**Назначение**: Создание парсера аргументов командной строки для настройки и запуска графического интерфейса (GUI).

**Как работает функция**:
1. Инициализируется объект `ArgumentParser` с описанием "Run the GUI".
2. Добавляются аргументы командной строки:
   - `--host`: hostname (тип str, значение по умолчанию "0.0.0.0", help - "hostname").
   - `--port`, `-p`: port (тип int, значение по умолчанию 8080, help - "port").
   - `--debug`, `-d`, `-debug`: debug mode (action="store_true", help - "debug mode").
   - `--ignore-cookie-files`: Don't read .har and cookie files. (action="store_true", help="Don\'t read .har and cookie files.").
   - `--ignored-providers`: List of providers to ignore when processing request. (incompatible with --reload and --workers") (nargs="+", choices=[provider.__name__ for provider in Provider.__providers__ if provider.working], default=[], help="List of providers to ignore when processing request. (incompatible with --reload and --workers)").
   - `--cookie-browsers`: List of browsers to access or retrieve cookies from. (nargs="+", choices=[browser.__name__ for browser in browsers], default=[], help="List of browsers to access or retrieve cookies from.").
3. Возвращается объект парсера `parser`.

```
Создание парсера argparse
│
├─ Добавление аргумента --host
│  │
│  (тип: str, значение по умолчанию: "0.0.0.0", описание: "hostname")
│
├─ Добавление аргумента --port (-p)
│  │
│  (тип: int, значение по умолчанию: 8080, описание: "port")
│
├─ Добавление аргумента --debug (-d, -debug)
│  │
│  (действие: store_true, описание: "debug mode")
│
├─ Добавление аргумента --ignore-cookie-files
│  │
│  (действие: store_true, описание: "Don't read .har and cookie files.")
│
├─ Добавление аргумента --ignored-providers
│  │
│  (список провайдеров для игнорирования, описание: "List of providers to ignore when processing request.")
│
└─ Добавление аргумента --cookie-browsers
   │
   (список браузеров для получения cookies, описание: "List of browsers to access or retrieve cookies from.")
   │
Возврат парсера
```

**Примеры**:

```python
import argparse
from ..cookies import browsers
from .. import Provider

# Создание парсера
parser = gui_parser()

# Пример 1: Парсинг аргументов по умолчанию
args1 = parser.parse_args([])
print(f"Host: {args1.host}, Port: {args1.port}, Debug: {args1.debug}, ignore_cookie_files: {args1.ignore_cookie_files}, ignored_providers: {args1.ignored_providers}, cookie_browsers: {args1.cookie_browsers}")
# Host: 0.0.0.0, Port: 8080, Debug: False, ignore_cookie_files: False, ignored_providers: [], cookie_browsers: []

# Пример 2: Парсинг аргументов с указанием хоста и порта
args2 = parser.parse_args(["--host", "127.0.0.1", "--port", "5000"])
print(f"Host: {args2.host}, Port: {args2.port}, Debug: {args2.debug}, ignore_cookie_files: {args2.ignore_cookie_files}, ignored_providers: {args2.ignored_providers}, cookie_browsers: {args2.cookie_browsers}")
# Host: 127.0.0.1, Port: 5000, Debug: False, ignore_cookie_files: False, ignored_providers: [], cookie_browsers: []

# Пример 3: Парсинг аргументов с включением режима отладки
args3 = parser.parse_args(["--debug"])
print(f"Host: {args3.host}, Port: {args3.port}, Debug: {args3.debug}, ignore_cookie_files: {args3.ignore_cookie_files}, ignored_providers: {args3.ignored_providers}, cookie_browsers: {args3.cookie_browsers}")
# Host: 0.0.0.0, Port: 8080, Debug: True, ignore_cookie_files: False, ignored_providers: [], cookie_browsers: []

# Пример 4: Парсинг аргументов с указанием игнорируемых провайдеров и браузеров
# Для этого необходимо определить список провайдеров и браузеров
providers = [provider.__name__ for provider in Provider.__providers__ if provider.working]
browsers_list = [browser.__name__ for browser in browsers]

# Предположим, что у нас есть провайдер "FakeProvider" и браузер "Chrome"
# providers = ["FakeProvider"]
# browsers_list = ["Chrome"]

# args4 = parser.parse_args(["--ignored-providers", providers[0], "--cookie-browsers", browsers_list[0]])
# print(f"Host: {args4.host}, Port: {args4.port}, Debug: {args4.debug}, ignore_cookie_files: {args4.ignore_cookie_files}, ignored_providers: {args4.ignored_providers}, cookie_browsers: {args4.cookie_browsers}")
# Host: 0.0.0.0, Port: 8080, Debug: False, ignore_cookie_files: False, ignored_providers: ['FakeProvider'], cookie_browsers: ['Chrome']