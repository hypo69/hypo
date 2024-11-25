# hypotez/src/endpoints/kazarinov/main.py

## Overview

This module provides the main logic for running the Kazarinov Telegram Bot. It handles command-line arguments, loads settings from a JSON file if specified, and starts the bot application using asyncio.

## Table of Contents

- [parse_args](#parse-args)
- [main](#main)


## Functions

### `parse_args`

**Description**: Parses command-line arguments for the Kazarinov Telegram Bot.

**Returns**:
- `dict`: A dictionary containing the parsed arguments.

**Raises**:
- `argparse.ArgumentError`: If there are errors in parsing the command-line arguments.


```python
def parse_args() -> dict:
    """Парсинг аргументов командной строки.

    Returns:
        dict: Словарь с параметрами запуска.
    """
    parser = argparse.ArgumentParser(description="Kazarinov's Telegram Bot CLI")

    parser.add_argument(
        "--settings",
        type=str,
        help="Путь к файлу настроек JSON.",
    )
    parser.add_argument(
        "--mode",
        type=str,
        choices=["test", "prod"],
        default="test",
        help="Режим работы бота (\'test\' или \'prod\').",
    )

    return vars(parser.parse_args())
```

### `main`

**Description**: The main function responsible for starting the Kazarinov Telegram Bot. It either loads settings from a file or uses command-line arguments, then runs the bot application.

**Raises**:
- `Exception`: If any error occurs during the bot's operation.


```python
def main():
    """Главная функция запуска KazarinovTelegramBot с параметрами из командной строки или файла настроек."""
    print("Starting Kazarinov's Telegram Bot...")

    args = parse_args()

    # Если указан файл настроек, загружаем параметры из него
    if args.get("settings"):
        settings_path = Path(args["settings"])
        if settings_path.exists():
            with open(settings_path, "r", encoding="utf-8") as file:
                settings = json.load(file)
            settings["mode"] = args.get("mode", "test")  # Дополнительно задаём режим
            bot = KazarinovTelegramBot(**settings)
        else:
            print(f"Файл настроек \'{settings_path}\' не найден.")
            return
    else:
        # Создаем экземпляр бота с параметрами из командной строки
        mode = args.get("mode", "test")
        bot = KazarinovTelegramBot(mode=mode)

    # Запуск бота
    try:
        asyncio.run(bot.application.run_polling())
    except Exception as ex:
        logger.error("Ошибка при запуске бота: %s", ex)
```