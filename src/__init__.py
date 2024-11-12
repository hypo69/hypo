## \file hypotez/src/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src """
"""  **Это корневая директория проекта** 
TODO: Расписать скрипты запуска
""" 


from packaging.version import Version
from .version import __version__, __doc__, __details__

import argparse
from .credentials import gs  # <- здесь все настроийки паролей, апи итп.

def script1():
    print("Запущен скрипт 1")

def script2():
    print("Запущен скрипт 2")

def show_help():
    print("\nДоступные команды:")
    print("1. Запустить скрипт 1 — Запускает скрипт 1.")
    print("2. Запустить скрипт 2 — Запускает скрипт 2.")
    print("3. --help — Показать это меню.")
    print("4. exit — Выход из программы.\n")

def interactive_menu():
    print("Добро пожаловать! Выберите одну из команд:\n")
    while True:
        # Отображаем интерактивное меню
        print("1. Запустить скрипт 1")
        print("2. Запустить скрипт 2")
        print("3. --help — Показать список команд.")
        print("4. exit — Выход из программы.")
        
        # Запрашиваем ввод команды
        choice = input("Введите номер команды: ").strip()

        if choice == "1":
            script1()
        elif choice == "2":
            script2()
        elif choice == "3" or choice.lower() == "--help":
            show_help()
        elif choice.lower() == "exit":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите одну из предложенных команд.")

def main():
    # Обработка аргументов командной строки (если программа запускается напрямую)
    parser = argparse.ArgumentParser(description="Интерактивное меню для запуска скриптов и команд.")
    parser.add_argument(
        "--help",
        action="store_true",
        help="Показать доступные опции и справочную информацию"
    )
    args = parser.parse_args()

    if args.help:
        show_help()
    else:
        interactive_menu()

if __name__ == "__main__":
    main()
