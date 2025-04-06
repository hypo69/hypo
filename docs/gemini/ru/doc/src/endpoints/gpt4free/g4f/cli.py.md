# Модуль командной строки (CLI) для g4f

## Обзор

Этот модуль предоставляет интерфейс командной строки (CLI) для запуска `gpt4free` в различных режимах, таких как API и GUI. Он позволяет настраивать параметры запуска, такие как привязка, порт, модель, провайдер и другие.

## Подробней

Модуль `cli.py` является отправной точкой для запуска приложения `gpt4free` из командной строки. Он определяет аргументы командной строки для настройки API и GUI, а также запускает выбранный режим с указанными параметрами.

## Функции

### `get_api_parser`

```python
def get_api_parser() -> ArgumentParser:
    """
    Создает парсер аргументов командной строки для API.

    Args:
        None

    Returns:
        ArgumentParser: Парсер аргументов командной строки.

    Raises:
        None

    Как работает функция:
    1. Создает экземпляр `ArgumentParser` с описанием "Run the API and GUI".
    2. Добавляет аргументы, такие как `--bind`, `--port`, `--debug`, `--gui`, `--model`, `--provider`, `--image-provider`, `--proxy`, `--workers`, `--disable-colors`, `--ignore-cookie-files`, `--g4f-api-key`, `--ignored-providers`, `--cookie-browsers`, `--reload`, `--demo`, `--ssl-keyfile`, `--ssl-certfile`, `--log-config`.
    3. Возвращает настроенный парсер аргументов.

    ASCII flowchart:
    Создание парсера -> Добавление аргументов -> Возврат парсера

    Примеры:
    >>> parser = get_api_parser()
    >>> args = parser.parse_args(['--debug', '--gui'])
    >>> args.debug
    True
    >>> args.gui
    True
    """
```

### `main`

```python
def main() -> None:
    """
    Главная функция для запуска приложения gpt4free.

    Args:
        None

    Returns:
        None

    Raises:
        SystemExit: Если не указан режим запуска.

    Как работает функция:
    1. Создает основной парсер аргументов с описанием "Run gpt4free".
    2. Создает субпарсеры для режимов "api" и "gui", используя `get_api_parser` и `gui_parser` соответственно.
    3. Разбирает аргументы командной строки.
    4. В зависимости от выбранного режима запускает соответствующую функцию (`run_api_args` или `run_gui_args`).
    5. Если режим не указан, выводит справку и завершает программу с кодом ошибки 1.

    ASCII flowchart:
    Создание парсера -> Создание субпарсеров -> Разбор аргументов -> Выбор режима -> Запуск функции или вывод справки -> Завершение

    Примеры:
    Запуск API:
    >>> main(['api', '--debug'])

    Запуск GUI:
    >>> main(['gui'])
    """
```

### `run_api_args`

```python
def run_api_args(args: argparse.Namespace) -> None:
    """
    Запускает API с указанными аргументами.

    Args:
        args (argparse.Namespace): Аргументы командной строки.

    Returns:
        None

    Raises:
        None

    Как работает функция:
    1. Импортирует `AppConfig` и `run_api` из модуля `g4f.api`.
    2. Настраивает `AppConfig` с использованием аргументов командной строки, таких как `ignore_cookie_files`, `ignored_providers`, `g4f_api_key`, `provider`, `image_provider`, `proxy`, `model`, `gui`, `demo`.
    3. Если указаны браузеры для cookie, обновляет список `g4f.cookies.browsers`.
    4. Запускает API с использованием аргументов командной строки, таких как `bind`, `port`, `debug`, `workers`, `use_colors`, `reload`, `ssl_keyfile`, `ssl_certfile`, `log_config`.

    ASCII flowchart:
    Импорт -> Настройка AppConfig -> Обновление браузеров для cookie -> Запуск API

    Примеры:
    >>> args = argparse.Namespace(ignore_cookie_files=True, ignored_providers=[], g4f_api_key=None, provider=None, image_provider=None, proxy=None, model=None, gui=False, demo=False, cookie_browsers=[], bind=None, port=None, debug=True, workers=None, disable_colors=False, reload=False, ssl_keyfile=None, ssl_certfile=None, log_config=None)
    >>> run_api_args(args)
    """