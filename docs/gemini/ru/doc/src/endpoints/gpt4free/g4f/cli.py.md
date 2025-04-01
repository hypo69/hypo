# Модуль для запуска gpt4free через CLI
## Обзор

Этот модуль предоставляет интерфейс командной строки (CLI) для запуска gpt4free с различными опциями, такими как запуск API, GUI, настройка провайдеров и моделей, а также управление cookies и прокси. Он позволяет настраивать параметры запуска gpt4free через аргументы командной строки.

## Подробней

Модуль предназначен для упрощения запуска и настройки gpt4free. Он включает в себя функции для парсинга аргументов командной строки, настройки приложения и запуска API или GUI. Модуль использует `argparse` для обработки аргументов командной строки и `g4f` для запуска API и GUI.

## Функции

### `get_api_parser`

```python
def get_api_parser() -> ArgumentParser:
    """Создает парсер аргументов для API.

    Args:
        Нет аргументов.

    Returns:
        ArgumentParser: Объект парсера аргументов.

    Как работает функция:
    1. Создает объект `ArgumentParser` с описанием "Run the API and GUI".
    2. Добавляет аргумент `--bind` для указания строки привязки (bind string).
    3. Добавляет аргумент `--port` или `-p` для изменения порта сервера.
    4. Добавляет аргумент `--debug` или `-d` для включения подробного логирования.
    5. Добавляет аргумент `--gui` или `-g` для запуска GUI.
    6. Добавляет аргумент `--model` для указания модели по умолчанию для завершения чата.
    7. Добавляет аргумент `--provider` для указания провайдера по умолчанию для завершения чата.
    8. Добавляет аргумент `--image-provider` для указания провайдера по умолчанию для генерации изображений.
    9. Добавляет аргумент `--proxy` для указания прокси по умолчанию.
    10. Добавляет аргумент `--workers` для указания количества рабочих процессов.
    11. Добавляет аргумент `--disable-colors` для отключения цветов.
    12. Добавляет аргумент `--ignore-cookie-files` для игнорирования файлов cookie.
    13. Добавляет аргумент `--g4f-api-key` для установки ключа аутентификации для API.
    14. Добавляет аргумент `--ignored-providers` для указания списка провайдеров, которые следует игнорировать.
    15. Добавляет аргумент `--cookie-browsers` для указания списка браузеров, из которых следует получать cookie.
    16. Добавляет аргумент `--reload` для включения перезагрузки.
    17. Добавляет аргумент `--demo` для включения демо-режима.
    18. Добавляет аргумент `--ssl-keyfile` для указания пути к файлу ключа SSL для HTTPS.
    19. Добавляет аргумент `--ssl-certfile` для указания пути к файлу сертификата SSL для HTTPS.
    20. Добавляет аргумент `--log-config` для указания пользовательской конфигурации логирования.
    21. Возвращает объект `ArgumentParser`.

    Примеры:
        >>> parser = get_api_parser()
        >>> print(parser)
        ArgumentParser(description='Run the API and GUI')
    """
    api_parser = ArgumentParser(description="Run the API and GUI")
    api_parser.add_argument("--bind", default=None, help="The bind string. (Default: 0.0.0.0:1337)")
    api_parser.add_argument("--port", "-p", default=None, help="Change the port of the server.")
    api_parser.add_argument("--debug", "-d", action="store_true", help="Enable verbose logging.")
    api_parser.add_argument("--gui", "-g", default=None, action="store_true", help="Start also the gui.")
    api_parser.add_argument("--model", default=None, help="Default model for chat completion. (incompatible with --reload and --workers)")
    api_parser.add_argument("--provider", choices=[provider.__name__ for provider in Provider.__providers__ if provider.working],
                            default=None, help="Default provider for chat completion. (incompatible with --reload and --workers)")
    api_parser.add_argument("--image-provider", choices=[provider.__name__ for provider in Provider.__providers__ if provider.working and hasattr(provider, "image_models")],
                            default=None, help="Default provider for image generation. (incompatible with --reload and --workers)"),
    api_parser.add_argument("--proxy", default=None, help="Default used proxy. (incompatible with --reload and --workers)")
    api_parser.add_argument("--workers", type=int, default=None, help="Number of workers.")
    api_parser.add_argument("--disable-colors", action="store_true", help="Don\'t use colors.")
    api_parser.add_argument("--ignore-cookie-files", action="store_true", help="Don\'t read .har and cookie files. (incompatible with --reload and --workers)")
    api_parser.add_argument("--g4f-api-key", type=str, default=None, help="Sets an authentication key for your API. (incompatible with --reload and --workers)")
    api_parser.add_argument("--ignored-providers", nargs="+", choices=[provider.__name__ for provider in Provider.__providers__ if provider.working],\
                            default=[], help="List of providers to ignore when processing request. (incompatible with --reload and --workers)")
    api_parser.add_argument("--cookie-browsers", nargs="+", choices=[browser.__name__ for browser in g4f.cookies.browsers],\
                            default=[], help="List of browsers to access or retrieve cookies from. (incompatible with --reload and --workers)")
    api_parser.add_argument("--reload", action="store_true", help="Enable reloading.")
    api_parser.add_argument("--demo", action="store_true", help="Enable demo mode.")
\t
    api_parser.add_argument("--ssl-keyfile", type=str, default=None, help="Path to SSL key file for HTTPS.")
    api_parser.add_argument("--ssl-certfile", type=str, default=None, help="Path to SSL certificate file for HTTPS.")
    api_parser.add_argument("--log-config", type=str, default=None, help="Custom log config.")
\t
    return api_parser
```

### `main`

```python
def main() -> None:
    """Основная функция для запуска gpt4free.

    Args:
        Нет аргументов.

    Returns:
        None

    Как работает функция:
    1. Создает главный парсер аргументов с описанием "Run gpt4free".
    2. Создает subparsers для режимов "api" и "gui".
    3. Добавляет парсеры аргументов API и GUI в subparsers.
    4. Разбирает аргументы командной строки.
    5. Если режим "api", запускает API с переданными аргументами.
    6. Если режим "gui", запускает GUI с переданными аргументами.
    7. Если режим не указан, выводит справку и завершает программу с кодом ошибки 1.

    Примеры:
        >>> # Запуск API с аргументами
        >>> # python cli.py api --port 8000 --debug
        >>> # Запуск GUI
        >>> # python cli.py gui
    """
    parser = argparse.ArgumentParser(description="Run gpt4free")
    subparsers = parser.add_subparsers(dest="mode", help="Mode to run the g4f in.")
    subparsers.add_parser("api", parents=[get_api_parser()], add_help=False)
    subparsers.add_parser("gui", parents=[gui_parser()], add_help=False)

    args = parser.parse_args()
    if args.mode == "api":
        run_api_args(args)
    elif args.mode == "gui":
        run_gui_args(args)
    else:
        parser.print_help()
        exit(1)
```

### `run_api_args`

```python
def run_api_args(args: argparse.Namespace) -> None:
    """Запускает API с заданными аргументами.

    Args:
        args (argparse.Namespace): Объект, содержащий аргументы командной строки.

    Returns:
        None

    Как работает функция:
    1. Импортирует `AppConfig` и `run_api` из модуля `g4f.api`.
    2. Устанавливает конфигурацию приложения с использованием переданных аргументов.
    3. Если указаны браузеры для cookie, обновляет список браузеров для cookie.
    4. Запускает API с переданными аргументами.

    Примеры:
        >>> # Запуск API с аргументами
        >>> # python cli.py api --port 8000 --debug
        >>> # args - объект, возвращаемый `parser.parse_args()`
        >>> run_api_args(args)
    """
    from g4f.api import AppConfig, run_api

    AppConfig.set_config(
        ignore_cookie_files=args.ignore_cookie_files,
        ignored_providers=args.ignored_providers,
        g4f_api_key=args.g4f_api_key,
        provider=args.provider,
        image_provider=args.image_provider,
        proxy=args.proxy,
        model=args.model,
        gui=args.gui,
        demo=args.demo,
    )
    if args.cookie_browsers:
        g4f.cookies.browsers = [g4f.cookies[browser] for browser in args.cookie_browsers]
    run_api(
        bind=args.bind,
        port=args.port,
        debug=args.debug,
        workers=args.workers,
        use_colors=not args.disable_colors,
        reload=args.reload,
        ssl_keyfile=args.ssl_keyfile,
        ssl_certfile=args.ssl_certfile,
        log_config=args.log_config,
    )