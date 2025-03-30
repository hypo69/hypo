## Анализ кода модуля `fast_api.py`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
  - Использование FastAPI для создания API.
  - Реализация паттерна Singleton для класса `FastApiServer`.
  - Поддержка динамического добавления маршрутов.
  - Обработка ошибок с логированием через `logger`.
  - Использование `j_loads_ns` для загрузки конфигурации.
- **Минусы**:
  - Неполная документация функций и классов.
  - Смешанный стиль: где-то есть аннотации типов, где-то нет.
  - Местами отсутствует обработка исключений.
  - Дублирование кода (например, `status_servers`, `get_routes`, `add_new_route` в классе `CommandHandler` и вне его).
  - Использование глобальных переменных.
  - Отсутствие тестов.

**Рекомендации по улучшению:**

1.  **Документирование кода**:
    - Добавить подробные docstring к каждой функции, методу и классу.
    - Описать все параметры и возвращаемые значения.
    - Привести примеры использования.

2.  **Улучшение обработки ошибок**:
    - Обернуть потенциально проблемные участки кода в блоки `try-except` для более надежной обработки ошибок.
    - Использовать `logger.exception` для логирования полной трассировки исключений.

3.  **Рефакторинг**:
    - Избавиться от дублирования кода. Например, методы `status_servers`, `get_routes` и `add_new_route` в `CommandHandler` просто вызывают функции с тем же именем. Вместо этого можно передавать экземпляр `FastApiServer` в `CommandHandler` и вызывать методы напрямую.
    - Уменьшить использование глобальных переменных, таких как `_api_server_instance`.
    - Разбить большие функции на более мелкие и понятные.
    - Использовать внедрение зависимостей для улучшения тестируемости.

4.  **Типизация**:
    - Добавить аннотации типов ко всем функциям и переменным, чтобы улучшить читаемость и предотвратить ошибки.

5.  **Форматирование**:
    - Привести код в соответствие со стандартами PEP8.

6. **Безопасность**:
    - Рассмотреть возможность добавления валидации входных данных для защиты от уязвимостей, таких как SQL-инъекции или межсайтовый скриптинг (XSS).

**Оптимизированный код:**

```python
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
FastAPI сервер с XML-RPC интерфейсом для удалённого управления
====================================================

Модуль содержит класс :class:`FastApiServer`, который предоставляет FastAPI сервер
с интерфейсом XML-RPC для удалённого управления.

Пример использования
----------------------

>>> server = FastApiServer(host='127.0.0.1')
>>> server.start(port=8000)
"""
import asyncio
import functools
import importlib
import os
import re
import sys
import threading
from contextlib import asynccontextmanager
from pathlib import Path
from types import SimpleNamespace
from typing import List, Callable, Dict, Optional

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, APIRouter
from xmlrpc.server import SimpleXMLRPCServer

# Импорт header должен быть обязательным
import header
from header import __root__
from src import gs
from src.fast_api.routes import Routes
from src.logger import logger
from src.utils.jjson import j_loads, j_loads_ns
from src.utils.printer import pprint as print

load_dotenv()

try:
    config: SimpleNamespace = j_loads_ns(__root__ / 'src' / 'fast_api' / 'fast_api.json')
    config.ports: list = config.ports if isinstance(config.ports, list) else [config.ports]
except Exception as ex:
    logger.critical('Config file not found!')
    sys.exit()

class FastApiServer:
    """
    FastAPI сервер с реализацией Singleton.

    Args:
        host (str): Хост для запуска сервера. По умолчанию "127.0.0.1".
        title (str): Заголовок приложения FastAPI. По умолчанию "FastAPI RPC Server".

    Attributes:
        app (FastAPI): Экземпляр FastAPI приложения.
        host (str): Хост для запуска сервера.
        port (int): Порт для запуска сервера.
        router (APIRouter): Экземпляр APIRouter для добавления маршрутов.
        server_tasks (dict): Словарь задач серверов.
        servers (dict): Словарь запущенных серверов.
    """

    _instance = None
    app: FastAPI = FastAPI()
    host: str = '127.0.0.1'
    port: int = 8000
    router: APIRouter = APIRouter()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, host: str = '127.0.0.1', title: str = 'FastAPI RPC Server', **kwargs):
        if hasattr(self, '_initialized'):
            return
        self._initialized = True

        self.app = FastAPI(title=title)
        self.host = host or config.host
        self.server_tasks = {}
        self.servers = {}
        self.app.include_router(self.router)

        self.add_route('/hello', test_function) # Добавление тестового маршрута
        self.add_route('/post', test_post, methods=['POST']) # Добавление тестового post-маршрута
        #self.add_route("/telegram_webhook", telegram_webhook, methods=["POST"])

    def add_route(self, path: str, func: Callable, methods: List[str] = ['GET'], **kwargs):
        """
        Добавляет маршрут к FastAPI приложению.

        Args:
            path (str): Путь маршрута.
            func (Callable): Функция обработчик маршрута.
            methods (List[str], optional): Список HTTP методов. По умолчанию ['GET'].
            **kwargs: Дополнительные аргументы для `router.add_api_route`.

        Example:
            >>> app_server = FastApiServer()
            >>> app_server.add_route('/test', lambda: {'message': 'Test route'})
        """
        try:
            self.router.add_api_route(path, func, methods=methods, **kwargs)
            logger.info(f'Маршрут {path} зарегистрирован')
        except Exception as ex:
            logger.error(f'Ошибка добавления маршрута {path}: {ex}', exc_info=True)

    async def _start_server(self, port: int):
        """
        Запускает uvicorn сервер асинхронно.

        Args:
            port (int): Порт для запуска сервера.
        """
        config = uvicorn.Config(self.app, host=self.host, port=port, log_level='debug')
        server = uvicorn.Server(config)
        try:
            await server.serve()
            logger.success(f'Server started on: {self.host}:{port}')
        except Exception as e:
            logger.error(f'Error running server on port {port}: {e}', exc_info=True)
        finally:
            self.servers.pop(port, None)

    def start(self, port: int, as_thread: bool = True):
        """
        Запускает FastAPI сервер на указанном порту.

        Args:
            port (int): Порт для запуска сервера.
            as_thread (bool): Запускать сервер в отдельном потоке.
        """
        if port in self.servers:
            print(f'Server already running on port {port}')
            return

        task = threading.Thread(target=asyncio.run, args=(self._start_server(port),), daemon=True)
        self.server_tasks[port] = task
        self.servers[port] = task
        task.start()

    def stop(self, port: int):
        """
        Останавливает FastAPI сервер на указанном порту.

        Args:
            port (int): Порт для остановки сервера.
        """
        if port in self.servers:
            try:
                self.servers[port].join(1) # Ожидание завершения потока
                self.servers.pop(port)
                print(f'Server on port {port} stopped.')
            except Exception as e:
                logger.error(f'Error stopping server on port {port}: {e}', exc_info=True)
        else:
            print(f'Server on port {port} is not running or already stopped.')

    def stop_all(self):
        """Останавливает все запущенные сервера."""
        for port in list(self.servers):
            self.stop(port)

    def get_servers_status(self) -> Dict[int, str]:
        """
        Возвращает статус всех серверов.

        Returns:
            Dict[int, str]: Словарь, где ключ - порт, значение - статус сервера.
        """
        return {port: 'Running' if task.is_alive() else 'Stopped' for port, task in self.servers.items()}

    def get_routes(self) -> List[Dict[str, str]]:
        """
        Возвращает список всех роутов.

        Returns:
            List[Dict[str, str]]: Список словарей с информацией о маршрутах.
        """
        routes = []
        for route in self.app.routes:
            if hasattr(route, 'path'):
                methods = getattr(route, 'methods', ['GET'])
                routes.append({'path': route.path, 'methods': list(methods)})
        return routes

    def get_app(self) -> FastAPI:
        """
        Возвращает FastAPI приложение.

        Returns:
            FastAPI: FastAPI приложение.
        """
        return self.app

    def add_new_route(self, path: str, module_name: str, func_name: str, methods: List[str] = ['GET'], **kwargs):
        """
        Добавляет новый маршрут к уже работающему приложению.

        Args:
            path (str): Путь маршрута.
            module_name (str): Имя модуля, содержащего функцию обработчик.
            func_name (str): Имя функции обработчика.
            methods (List[str], optional): Список HTTP методов. По умолчанию ['GET'].
            **kwargs: Дополнительные аргументы для `add_route`.
        """
        try:
            # Динамически импортируем модуль
            module = importlib.import_module(module_name)
            # Получаем функцию из модуля
            func = getattr(module, func_name, None)
            if func is None:
                raise AttributeError(f'Function \'{func_name}\' not found in module \'{module_name}\'')

            self.add_route(path, func, methods=methods, **kwargs)
            logger.info(f'Маршрут {path} зарегистрирован из модуля {module_name}')
        except Exception as ex:
            logger.error(f'Ошибка добавления маршрута {path} из модуля {module_name}: {ex}', exc_info=True)


def telegram_webhook():
    """фикстура"""
    return 'Hello, World!'


def test_function():
    """фикстура"""
    return 'It is working!!!'


def test_post(data: Dict[str, str]):
    """фикстура"""
    return {'result': 'post ok', 'data': data}


_api_server_instance = None # Объявление глобальной переменной

def start_server(port: int, host: str):
    """
    Запускает FastAPI сервер на указанном порту.

    Args:
        port (int): Порт для запуска сервера.
        host (str): Хост для запуска сервера.
    """
    global _api_server_instance
    if _api_server_instance is None:
        _api_server_instance = FastApiServer(host=host)
    try:
        _api_server_instance.start(port=port)
    except Exception as ex:
        logger.error(f'Ошибка запуска FastAPI сервера на порту {port}:', ex, exc_info=True)


def stop_server(port: int):
    """
    Останавливает FastAPI сервер на указанном порту.

    Args:
        port (int): Порт для остановки сервера.
    """
    global _api_server_instance
    if _api_server_instance:
        try:
            _api_server_instance.stop(port=port)
        except Exception as ex:
            logger.error(f'Ошибка остановки FastAPI сервера на порту {port}:', ex, exc_info=True)


def stop_all_servers():
    """Останавливает все запущенные FastAPI сервера."""
    global _api_server_instance
    if _api_server_instance:
        try:
            _api_server_instance.stop_all()
        except Exception as ex:
            logger.error(f'Ошибка остановки всех FastAPI серверов:', ex, exc_info=True)


def status_servers():
    """Показывает статус серверов."""
    global _api_server_instance
    if _api_server_instance:
        servers = _api_server_instance.get_servers_status()
        if servers:
            print(f'Server initialized on host {_api_server_instance.host}')
            for port, status in servers.items():
                print(f'  - Port {port}: {status}')
        else:
            print('No servers running')
    else:
        print('Server not initialized.')


def get_routes():
    """Показывает все роуты."""
    global _api_server_instance
    if _api_server_instance:
        routes = _api_server_instance.get_routes()
        if routes:
            print('Available routes:')
            for route in routes:
                print(f'  - Path: {route['path']}, Methods: {route['methods']}')
        else:
            print('No routes defined')
    else:
        print('Server not initialized.')


def add_new_route(path: str, module_name: str, func_name: str, methods: List[str] = ['GET']):
    """Добавляет новый роут к серверу."""
    global _api_server_instance
    if _api_server_instance:
        try:
            _api_server_instance.add_new_route(path=path, module_name=module_name, func_name=func_name, methods=methods)
            print(f'Route added: {path}, {methods=}')
        except Exception as ex:
            logger.error(f'Ошибка добавления нового роута {path}:', ex, exc_info=True)
    else:
        print('Server not initialized. Start server first')


def parse_port_range(range_str: str) -> List[int]:
    """
    Разбирает строку с диапазоном портов.

    Args:
        range_str (str): Строка с диапазоном портов.

    Returns:
        List[int]: Список портов.
    """
    if not re.match(r'^[\d-]+$', range_str):
        print(f'Invalid port range: {range_str}')
        return []
    if '-' in range_str:
        try:
            start, end = map(int, range_str.split('-'))
            if start > end:
                raise ValueError('Invalid port range')
            return list(range(start, end + 1))
        except ValueError:
            print(f'Invalid port range: {range_str}')
            return []
    else:
        try:
            return [int(range_str)]
        except ValueError:
            print(f'Invalid port: {range_str}')
            return []


class CommandHandler:
    """Обработчик команд для FastAPI сервера через XML-RPC."""

    def __init__(self, rpc_port: int = 9000, api_server: Optional[FastApiServer] = None):
        """
        Args:
            rpc_port (int): Порт для XML-RPC сервера.
        """
        self.rpc_port = rpc_port
        self.api_server = api_server or FastApiServer() # Внедрение зависимости
        self.rpc_server = SimpleXMLRPCServer(('localhost', self.rpc_port), allow_none=True)
        self.rpc_server.register_instance(self)
        threading.Thread(target=self.rpc_server.serve_forever, daemon=True).start()
        print(f'RPC server started on port: {self.rpc_port}')

    def start_server(self, port: int, host: str):
        """Запускает сервер."""
        start_server(port=port, host=host)

    def stop_server(self, port: int):
        """Останавливает сервер."""
        stop_server(port=port)

    def stop_all_servers(self):
        """Останавливает все сервера."""
        stop_all_servers()

    def status_servers(self):
        """Возвращает статус серверов."""
        status_servers()

    def get_routes(self):
        """Возвращает все роуты."""
        get_routes()

    def add_new_route(self, path: str, module_name: str, func_name: str, methods: List[str] = ['GET']):
        """Добавляет новый роут."""
        add_new_route(path=path, module_name=module_name, func_name=func_name, methods=methods)

    def shutdown(self):
        """Останавливает все сервера и завершает работу."""
        self.stop_all_servers()
        self.rpc_server.shutdown()
        print('RPC server shutdown')
        sys.exit(0)


def display_menu():
    """Выводит меню с доступными командами."""
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


def main():
    """Основная функция управления сервером."""
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
                    logger.error(f'An error occurred:', ex, exc_info=True)

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
                    logger.error(f'An error occurred:', ex, exc_info=True)

            elif command == 'stop_all':
                command_handler.stop_all_servers()

            elif command == 'add_route':
                if len(parts) < 2:
                    print('Usage: add_route <path> <module_name> <func_name>')
                    continue
                path = parts[1]
                module_name = input('Enter module name: ').strip()
                func_name = input('Enter function name: ').strip()
                methods = input('Enter HTTP methods (comma-separated, default: GET): ').strip().upper() or 'GET'
                methods = [method.strip() for method in methods.split(',')]
                command_handler.add_new_route(path=path, module_name=module_name, func_name=func_name, methods=methods)

            elif command == 'shutdown':
                command_handler.shutdown()  # call shutdown method on command_handler

            elif command == 'help':
                display_menu()

            elif command == 'exit':
                print('Exiting the program.')
                sys.exit(0)

            else:
                print('Unknown command. Type \'help\' to see the list of available commands')

        except Exception as ex:
            logger.error(f'An error occurred:', ex, exc_info=True)


if __name__ == '__main__':
    main()