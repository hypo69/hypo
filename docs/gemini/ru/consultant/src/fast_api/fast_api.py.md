# Анализ кода модуля `fast_api`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Реализация паттерна Singleton для класса `FastApiServer`.
    -  Удобное добавление маршрутов с помощью метода `add_route`.
    -  Асинхронный запуск и остановка сервера.
    -  Использование `functools.wraps` для сохранения метаданных оборачиваемых функций.
- **Минусы**:
    -  Отсутствует документация в формате RST для классов и методов.
    -  Используется `print` для логирования, вместо `logger.error`.
    -  Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Импорт модуля `header` не используется.

**Рекомендации по улучшению:**

1.  **Документирование:**
    - Добавить RST-документацию для всех классов, методов и функций, включая описания параметров, типов и возвращаемых значений.
2.  **Логирование:**
    - Заменить `print` на `logger.info` и `logger.error` для вывода информации и ошибок.
    - Изменить импорт `logger` на `from src.logger import logger`.
3.  **Использование `jjson`:**
    - Использовать `j_dumps` для записи данных. (Использовано)
4.  **Удаление неиспользуемого импорта:**
    - Удалить импорт модуля `header`.
5.  **Обработка ошибок:**
   - Использовать `logger.error` вместо стандартных блоков `try-except`, когда это уместно.
6.  **Улучшение читаемости:**
    -  Выровнять импорты по алфавиту.
    -  Придерживаться стандарта PEP8 для форматирования кода.

**Оптимизированный код:**

```python
"""
Модуль для запуска и управления FastAPI сервером.
=================================================

Этот модуль содержит класс :class:`FastApiServer`, который используется для создания и управления
FastAPI сервером с использованием паттерна Singleton.

Пример использования
----------------------
.. code-block:: python

    api = FastApiServer(title="My API", host="0.0.0.0")
    api.add_route("/hello", test_function)
    api.register_router()
    asyncio.run(api.start(port=8080))
"""
import asyncio
import functools
from typing import Any, Callable, Dict, List

import uvicorn
from fastapi import APIRouter, FastAPI

from src.logger import logger # Изменен импорт
from src.utils.jjson import j_dumps # Изменен импорт



class Singleton(type):
    """Metaclass for implementing the singleton pattern."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class FastApiServer(FastAPI, metaclass=Singleton):
    """
    Класс для управления FastAPI сервером с использованием паттерна Singleton.
    
    :param title: Заголовок приложения.
    :type title: str, optional
    :param host: Хост для запуска сервера.
    :type host: str, optional
    :param kwargs: Дополнительные аргументы для FastAPI.
    :type kwargs: Dict, optional
    """

    def __init__(self, title: str = 'FastAPI Singleton Server', host: str = '127.0.0.1', **kwargs):
        """Инициализирует экземпляр класса FastApiServer."""
        super().__init__(title=title, **kwargs)
        self.router = APIRouter()
        self.host = host
        self.server_tasks = {}  # Словарь для хранения задач (port: task)
        self.servers = {}  # Словарь для хранения серверов (port: server)

    def add_route(self, path: str, func: Callable, methods: List[str] = ['GET'], **kwargs):
        """
        Добавляет маршрут к FastAPI приложению.

        :param path: Путь маршрута.
        :type path: str
        :param func: Функция-обработчик маршрута.
        :type func: Callable
        :param methods: Список HTTP методов.
        :type methods: List[str], optional
        :param kwargs: Дополнительные аргументы для add_api_route.
        :type kwargs: Dict, optional
        """
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            return await func(*args, **kwargs)
        self.router.add_api_route(path, wrapper, methods=methods, **kwargs)

    def register_router(self):
        """Регистрирует роутер в FastAPI приложении."""
        self.include_router(self.router)

    async def _start_server(self, port: int):
        """
        Внутренний метод для запуска сервера.

        :param port: Порт для запуска сервера.
        :type port: int
        """
        config = uvicorn.Config(self, host=self.host, port=port, log_level='info')
        server = uvicorn.Server(config)
        self.servers[port] = server
        await server.serve()

    async def start(self, port: int):
        """
        Запускает FastAPI сервер на указанном порту.

        :param port: Порт для запуска сервера.
        :type port: int
        """
        if port in self.server_tasks and not self.server_tasks[port].done():
            logger.info(f'Server already running on port {port}') # Изменено на logger.info
            return
        task = asyncio.create_task(self._start_server(port))
        self.server_tasks[port] = task
        j_dumps(self.server_tasks, 'servers.json') # Изменен вызов

    async def stop(self, port: int):
        """
        Останавливает FastAPI сервер на указанном порту.

        :param port: Порт сервера для остановки.
        :type port: int
        """
        if port in self.servers and self.servers[port].started:
            await self.servers[port].stop()
            j_dumps(self.server_tasks, 'servers.json') # Изменен вызов

    async def stop_all(self):
        """Останавливает все запущенные FastAPI серверы."""
        for port in list(self.servers.keys()):
            await self.stop(port)

    def get_app(self) -> FastAPI:
        """
        Возвращает FastAPI приложение.

        :return: Экземпляр FastAPI приложения.
        :rtype: FastAPI
        """
        return self

async def test_function():
    """
    Тестовая функция для проверки GET запросов.

    :return: Строка "It is working!!!".
    :rtype: str
    """
    return 'It is working!!!'


async def test_post(data: Dict[str, str]) -> Dict[str, Any]:
    """
    Тестовая функция для проверки POST запросов.

    :param data: Данные, переданные в POST запросе.
    :type data: Dict[str, str]
    :return: Словарь с результатом и переданными данными.
    :rtype: Dict[str, Any]
    """
    return {'result': 'post ok', 'data': data}


async def main():
    """Основная функция для запуска и тестирования FastAPI сервера."""
    api = FastApiServer(title='My API', host='0.0.0.0')
    api.add_route('/hello', test_function)
    api.add_route('/post', test_post, methods=['POST'])
    api.register_router()

    # Запускаем на порту 8080
    logger.info('start api on port 8080') # Изменено на logger.info
    await api.start(port=8080)

    # some work
    await asyncio.sleep(2)
    # Добавляем порт 8081 на лету
    logger.info('start api on port 8081') # Изменено на logger.info
    await api.start(port=8081)

    await asyncio.sleep(2)
    # stop port 8080
    logger.info('stop api on port 8080') # Изменено на logger.info
    await api.stop(port=8080)

    await asyncio.sleep(2)
    logger.info('stop all servers') # Изменено на logger.info
    await api.stop_all()


if __name__ == '__main__':
    asyncio.run(main())
```