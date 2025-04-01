# Модуль командной строки (CLI) для g4f

## Обзор

Модуль `cli.py` предоставляет интерфейс командной строки для запуска `gpt4free`. Он позволяет запускать API и графический интерфейс (GUI) с различными опциями конфигурации, такими как выбор модели, провайдера, настройка прокси и т.д.

## Функции

### `get_api_parser`

```python
def get_api_parser() -> ArgumentParser:
    """
    Создает и возвращает парсер аргументов командной строки для API.

    Args:
        None

    Returns:
        ArgumentParser: Парсер аргументов командной строки.

    Как работает функция:
    1. Создает экземпляр `ArgumentParser` с описанием "Run the API and GUI".
    2. Добавляет аргументы, такие как `--bind`, `--port`, `--debug`, `--gui`, `--model`, `--provider`, `--image-provider`, `--proxy`, `--workers`, `--disable-colors`, `--ignore-cookie-files`, `--g4f-api-key`, `--ignored-providers`, `--cookie-browsers`, `--reload`, `--demo`, `--ssl-keyfile`, `--ssl-certfile`, `--log-config`.
    3. Настраивает аргументы с помощью `add_argument`, устанавливая значения по умолчанию, типы, подсказки и допустимые значения (например, для выбора провайдера).

    Примеры:
    >>> parser = get_api_parser()
    >>> args = parser.parse_args(['--port', '8080', '--debug'])
    >>> print(args.port)
    8080
    >>> print(args.debug)
    True
    """
```

### `main`

```python
def main() -> None:
    """
    Главная функция для запуска gpt4free через командную строку.

    Args:
        None

    Returns:
        None

    Как работает функция:
    1. Создает основной парсер аргументов с описанием "Run gpt4free".
    2. Добавляет подпарсеры для режимов "api" и "gui", используя `get_api_parser` и `gui_parser` соответственно.
    3. Обрабатывает аргументы командной строки с помощью `parser.parse_args()`.
    4. В зависимости от выбранного режима ("api" или "gui") вызывает соответствующие функции `run_api_args` или `run_gui_args`.
    5. Если режим не указан, выводит справку и завершает программу с кодом ошибки 1.

    Примеры:
    Для запуска API:
    >>> # в командной строке: python cli.py api --port 8080 --debug
    Для запуска GUI:
    >>> # в командной строке: python cli.py gui
    """
```

### `run_api_args`

```python
def run_api_args(args: argparse.Namespace) -> None:
    """
    Запускает API с заданными аргументами командной строки.

    Args:
        args (argparse.Namespace): Аргументы командной строки, полученные парсером.

    Returns:
        None

    Как работает функция:
    1. Импортирует `AppConfig` и `run_api` из модуля `g4f.api`.
    2. Устанавливает конфигурацию приложения `AppConfig` на основе аргументов командной строки, таких как `ignore_cookie_files`, `ignored_providers`, `g4f_api_key`, `provider`, `image_provider`, `proxy`, `model`, `gui`, `demo`.
    3. Если указаны браузеры для cookie (`cookie_browsers`), обновляет список браузеров в `g4f.cookies`.
    4. Запускает API с помощью `run_api`, передавая аргументы, такие как `bind`, `port`, `debug`, `workers`, `use_colors`, `reload`, `ssl_keyfile`, `ssl_certfile`, `log_config`.

    Примеры:
    >>> # Предположим, что args - это объект argparse.Namespace, полученный из командной строки
    >>> # python cli.py api --port 8080 --debug
    >>> # run_api_args(args)
    """