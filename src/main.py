## \file /src/main.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3




                    #################################################################################################
                    #                                                                                               #
                    #           THIS IS ONLY TEMPLATE FOR FUTURE REALISATION                                        #
                    #                                                                                               #
                    #################################################################################################





"""
Module for interactive script execution.
=========================================================================================

This module provides an interactive menu for running predefined scripts.
It takes user input to select and execute scripts 1 or 2.

Usage Example
--------------------
.. module:: src 
	:platform: Windows, Unix
	:synopsis:

.. code-block:: python

    python main.py  # Starts interactive menu
    python main.py --help # Displays help

"""



import argparse
from src.utils.jjson import j_loads, j_loads_ns
from src.logger.logger import logger

def script1():
    """Executes script 1."""
    print("Script 1 started")
    # ... (Add script 1 code here)

def script2():
    """Executes script 2."""
    print("Script 2 started")
    # ... (Add script 2 code here)

def show_help():
    """Displays help information for available commands."""
    print("\nAvailable commands:")
    print("1. Run script 1 - Executes script 1.")
    print("2. Run script 2 - Executes script 2.")
    print("3. --help - Displays this help menu.")
    print("4. exit - Exits the program.\n")


def interactive_menu():
    """Interactive menu for selecting and running scripts."""
    print("Welcome! Choose one of the commands:\n")
    while True:
        print("1. Run script 1")
        print("2. Run script 2")
        print("3. --help - Show command list.")
        print("4. exit - Exit the program.")

        choice = input("Enter command number: ").strip()

        if choice == "1":
            script1()
        elif choice == "2":
            script2()
        elif choice == "3" or choice.lower() == "--help":
            show_help()
        elif choice.lower() == "exit":
            print("Exiting the program.")
            break
        else:
            logger.error("Invalid input. Please choose a valid command.")


def main():
    """Main function for handling command-line arguments and starting the menu."""
    parser = argparse.ArgumentParser(description="Interactive menu for running scripts.")
    parser.add_argument(
        "--help",
        action="store_true",
        help="Show available options and help information",
    )
    args = parser.parse_args()

    if args.help:
        show_help()
    else:
        interactive_menu()


if __name__ == "__main__":
    main()







# import argparse

# def script1():
#     """Запускает скрипт 1."""
#     print("Запущен скрипт 1")
#     # Добавьте здесь код скрипта 1


# def script2():
#     """Запускает скрипт 2."""
#     print("Запущен скрипт 2")
#     # Добавьте здесь код скрипта 2


# def show_help():
#     """Выводит справку по доступным командам."""
#     print("\nДоступные команды:")
#     print("1. Запустить скрипт 1 — Запускает скрипт 1.")
#     print("2. Запустить скрипт 2 — Запускает скрипт 2.")
#     print("3. --help — Показать это меню.")
#     print("4. exit — Выход из программы.\n")


# def interactive_menu():
#     """Интерактивное меню для выбора и запуска скриптов."""
#     print("Добро пожаловать! Выберите одну из команд:\n")
#     while True:
#         print("1. Запустить скрипт 1")
#         print("2. Запустить скрипт 2")
#         print("3. --help — Показать список команд.")
#         print("4. exit — Выход из программы.")

#         choice = input("Введите номер команды: ").strip()

#         if choice == "1":
#             script1()
#         elif choice == "2":
#             script2()
#         elif choice == "3" or choice.lower() == "--help":
#             show_help()
#         elif choice.lower() == "exit":
#             print("Выход из программы.")
#             break
#         else:
#             print("Некорректный ввод. Пожалуйста, выберите одну из предложенных команд.")


# def main():
#     """Основная функция для обработки аргументов командной строки и запуска меню."""
#     parser = argparse.ArgumentParser(description="Интерактивное меню для запуска скриптов.")
#     parser.add_argument(
#         "--help",
#         action="store_true",
#         help="Показать доступные опции и справочную информацию",
#     )
#     args = parser.parse_args()

#     if args.help:
#         show_help()
#     else:
#         interactive_menu()


# if __name__ == "__main__":
#     main()