## Анализ кода модуля `main.py`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
  - Код достаточно структурирован и читаем.
  - Присутствуют базовые обработчики команд для управления сервером.
  - Используется логирование ошибок через `logger.error`.
- **Минусы**:
  - Отсутствует подробная документация функций и классов.
  - Не все переменные аннотированы типами.
  - Используется небезопасный `eval` при добавлении маршрутов.
  - Нет обработки возможных ошибок при вводе данных (например, пустой ввод).
  - `header` импортируется, но не используется.

**Рекомендации по улучшению:**

1.  **Документирование кода**:
    - Добавить docstring к каждой функции и классу, следуя указанному формату.

2.  **Обработка ошибок**:
    - Реализовать более надежную обработку ошибок, включая проверку ввода пользователя на корректность.
    - Добавить обработку исключений при конвертации типов и других операциях.

3.  **Аннотация типов**:
    - Добавить аннотации типов для всех переменных и аргументов функций.

4.  **Безопасность**:
    - Избегать использования `eval` или `exec` для динамического создания функций. Вместо этого рассмотреть возможность использования более безопасных методов, таких как `dict` с функциями или декораторы.

5.  **Удаление неиспользуемого импорта**:
    - Удалить импорт `header`, так как он не используется в коде.

6.  **Улучшение пользовательского интерфейса**:
    - Добавить больше информации в сообщения об ошибках, чтобы пользователю было понятнее, что пошло не так.

7.  **Соответствие PEP8**:
    - Проверить код на соответствие стандартам PEP8 и исправить возможные нарушения.

**Оптимизированный код:**

```python
## \file /src/fast_api/main.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
Модуль управления параметрами Fast API сервера.
=================================================

Модуль содержит функции для запуска, остановки и управления сервером Fast API.

Пример использования:
----------------------
>>> main()
"""

import sys
from src.fast_api.fast_api import CommandHandler, logger
from typing import List


def display_menu() -> None:
    """
    Выводит меню с доступными командами.
    """
    print('\nAvailable commands:')
    print('  start <port>        - Start server on the specified port')
    print('  status              - Show all served ports status')
    print('  routes              - Show all registered routes')
    print('  stop <port>         - Stop server on the specified port')
    print('  stop_all            - Stop all servers')
    print('  add_route <path>    - Add a new route to the server')
    print('  shutdown            - Stop all servers and exit')
    print('  help                - Show this help menu')
    print('  exit                - Exit the program')


def main() -> None:
    """
    Основная функция управления сервером.
    """
    command_handler = CommandHandler()
    while True:
        display_menu()
        try:
            command_line = input('Enter command: ').strip().lower()
            if not command_line:
                continue

            parts = command_line.split()
            command = parts[0]

            if command == 'start':
                if len(parts) != 2:
                    print('Usage: start <port>')
                    continue
                try:
                    port = int(parts[1])
                    host = input('Enter host address (default: 127.0.0.1): ').strip() or '127.0.0.1'
                    command_handler.start_server(port=port, host=host)
                except ValueError:
                    print('Invalid port number.')
                except Exception as ex:
                    logger.error('An error occurred:', ex, exc_info=True)

            elif command == 'status':
                command_handler.status_servers()

            elif command == 'routes':
                command_handler.get_routes()

            elif command == 'stop':
                if len(parts) != 2:
                    print('Usage: stop <port>')
                    continue
                try:
                    port = int(parts[1])
                    command_handler.stop_server(port=port)
                except ValueError:
                    print('Invalid port number.')
                except Exception as ex:
                    logger.error('An error occurred:', ex, exc_info=True)

            elif command == 'stop_all':
                command_handler.stop_all_servers()

            elif command == 'add_route':
                if len(parts) != 2:
                    print('Usage: add_route <path>')
                    continue
                path = parts[1]
                methods_input = input('Enter HTTP methods (comma-separated, default: GET): ').strip().upper() or 'GET'
                methods: List[str] = [method.strip() for method in methods_input.split(',')]
                # TODO:  Безопасная реализация add_new_route
                command_handler.add_new_route(path=path, func='lambda: {\"message\": \"Hello from the new route\"}', methods=methods) # TODO: заменить func на безопасный вызов

            elif command == 'shutdown':
                command_handler.stop_all_servers()
                print('Shutting down all servers.')
                sys.exit(0)

            elif command == 'help':
                display_menu()

            elif command == 'exit':
                print('Exiting the program.')
                sys.exit(0)

            else:
                print('Unknown command. Type \'help\' to see the list of available commands')

        except Exception as ex:
            logger.error('An error occurred:', ex, exc_info=True)


if __name__ == '__main__':
    main()