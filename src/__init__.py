## \file hypotez/src/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src """
MODE = 'debug'
""" module: src """
MODE = 'debug'
"""
**Это корневой модуль проекта hypotez.**

Этот модуль предоставляет интерактивное меню для запуска скриптов проекта.
Он содержит функции для запуска скрипта 1 и 2, а также для вывода справки.
Также обрабатывает аргументы командной строки, позволяя запускать программу с параметром --help для вывода справки.
"""
from packaging.version import Version
from .version import __version__, __doc__, __details__
import argparse
from .credentials import gs  # Импортируем настройки


def script1():
    """Запускает скрипт 1."""
    print("Запущен скрипт 1")
    # Добавьте здесь код скрипта 1


def script2():
    """Запускает скрипт 2."""
    print("Запущен скрипт 2")
    # Добавьте здесь код скрипта 2


def show_help():
    """Выводит справку по доступным командам."""
    print("\nДоступные команды:")
    print("1. Запустить скрипт 1 — Запускает скрипт 1.")
    print("2. Запустить скрипт 2 — Запускает скрипт 2.")
    print("3. --help — Показать это меню.")
    print("4. exit — Выход из программы.\n")


def interactive_menu():
    """Интерактивное меню для выбора и запуска скриптов."""
    print("Добро пожаловать! Выберите одну из команд:\n")
    while True:
        print("1. Запустить скрипт 1")
        print("2. Запустить скрипт 2")
        print("3. --help — Показать список команд.")
        print("4. exit — Выход из программы.")

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
    """Основная функция для обработки аргументов командной строки и запуска меню."""
    parser = argparse.ArgumentParser(description="Интерактивное меню для запуска скриптов.")
    parser.add_argument(
        "--help",
        action="store_true",
        help="Показать доступные опции и справочную информацию",
    )
    args = parser.parse_args()

    if args.help:
        show_help()
    else:
        interactive_menu()


if __name__ == "__main__":
    main()