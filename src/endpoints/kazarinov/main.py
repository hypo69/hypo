## \file hypotez/src/endpoints/kazarinov/main.py
# -*- coding: utf-8 -*-

""" module: src.endpoints.kazarinov 


Примеры запуска:
1. Запуск в тестовом режиме:
    python main.py --mode test

2. Запуск в продакшн режиме:
    python main.py --mode prod

3. Запуск с указанием пути к файлу настроек:
    python main.py --settings settings.json --mode prod
"""
MODE = 'debug'
import argparse
import asyncio
import json
from pathlib import Path
from pydantic import BaseModel
from src.logger import logger
from src.endpoints.kazarinov.bot import KazarinovTelegramBot


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
        help="Режим работы бота ('test' или 'prod').",
    )

    return vars(parser.parse_args())


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
            settings['mode'] = args.get("mode", "test")  # Дополнительно задаём режим
            bot = KazarinovTelegramBot(**settings)
        else:
            print(f"Файл настроек '{settings_path}' не найден.")
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


if __name__ == "__main__":
    main()