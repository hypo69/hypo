# Анализ кода модуля `fast_api`

**Качество кода**:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Реализация паттерна Singleton для FastAPI сервера.
    - Использование асинхронности для запуска и остановки серверов.
    - Удобная структура для добавления маршрутов и управления серверами.
- **Минусы**:
    - Не хватает документации в формате RST для классов и методов.
    - Используется `print` для логирования, вместо `logger`.
    - Нет обработки исключений при запуске и остановке серверов.
    - Есть несоответствия в использовании кавычек.
    - Не все импорты выровнены.

**Рекомендации по улучшению**:

- Добавить RST-документацию для всех классов и методов.
- Использовать `from src.logger.logger import logger` для логирования вместо `print`.
- Добавить обработку исключений с помощью `try-except` и логирование ошибок через `logger.error`.
- Использовать одинарные кавычки для строк в коде, двойные только для вывода.
- Выровнять импорты и использовать `j_dumps` из `src.utils.jjson`.
- Убрать неясные комментарии и добавить более точные.

**Оптимизированный код**:

```python
"""
Модуль для запуска FastAPI сервера с паттерном Singleton.
==========================================================

Модуль предоставляет класс :class:`FastApiServer` для создания и управления FastAPI серверами.
Он использует паттерн Singleton для обеспечения единственного экземпляра сервера в приложении.

Пример использования
----------------------
.. code-block:: python

    async def main():
        api = FastApiServer(title='My API', host='0.0.0.0')
        api.add_route('/hello', test_function)
        api.add_route('/post', test_post, methods=['POST'])
        api.register_router()

        print('start api on port 8080')
        await api.start(port=8080)

        await asyncio.sleep(2)
        print('start api on port 8081')
        await api.start(port=8081)

        await asyncio.sleep(2)
        print('stop api on port 8080')
        await api.stop(port=8080)

        await asyncio.sleep(2)
        print('stop all servers')
        await api.stop_all()
"""
from fastapi import FastAPI, APIRouter # выравнивание импорта
import uvicorn # выравнивание импорта
from typing import List, Callable, Dict, Any # выравнивание импорта
import functools # выравнивание импорта
import asyncio # выравнивание импорта
# import header # не используется, можно удалить
from src.utils.jjson import j_dumps # импорт j_dumps
from src.logger.logger import logger # импорт logger


class Singleton(type):
    """
    Метакласс для реализации паттерна Singleton.

    :ivar _instances: Словарь для хранения экземпляров классов.
    :vartype _instances: dict
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Создает или возвращает существующий экземпляр класса.

        :param args: Позиционные аргументы для конструктора класса.
        :type args: tuple
        :param kwargs: Именованные аргументы для конструктора класса.
        :type kwargs: dict
        :return: Экземпляр класса.
        :rtype: object
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class FastApiServer(FastAPI, metaclass=Singleton):
    """
    FastAPI сервер с реализацией Singleton.

    :ivar router: Роутер для добавления маршрутов.
    :vartype router: APIRouter
    :ivar host: Хост сервера.
    :vartype host: str
    :ivar server_tasks: Словарь для хранения задач (port: task).
    :vartype server_tasks: dict
    :ivar servers: Словарь для хранения серверов (port: server).
    :vartype servers: dict
    """

    def __init__(self, title: str = "FastAPI Singleton Server", host: str = "127.0.0.1", **kwargs):
        """
        Инициализирует FastAPI сервер.

        :param title: Заголовок сервера.
        :type title: str, optional
        :param host: Хост сервера.
        :type host: str, optional
        :param kwargs: Дополнительные именованные аргументы для FastAPI.
        :type kwargs: dict
        """
        super().__init__(title=title, **kwargs)
        self.router = APIRouter()
        self.host = host
        self.server_tasks = {}  # Словарь для хранения задач (port: task)
        self.servers = {}  # Словарь для хранения серверов (port: server)

    def add_route(self, path: str, func: Callable, methods: List[str] = ["GET"], **kwargs):
        """
        Добавляет маршрут к FastAPI приложению.

        :param path: Путь маршрута.
        :type path: str
        :param func: Функция обработчик маршрута.
        :type func: Callable
        :param methods: Список HTTP методов.
        :type methods: List[str], optional
        :param kwargs: Дополнительные именованные аргументы для add_api_route.
        :type kwargs: dict
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
        Запускает Uvicorn сервер на указанном порту.

        :param port: Порт для запуска сервера.
        :type port: int
        """
        config = uvicorn.Config(self, host=self.host, port=port, log_level="info")
        server = uvicorn.Server(config)
        self.servers[port] = server
        try: # обработка исключения
            await server.serve()
        except Exception as e: # обработка исключения
            logger.error(f"Error starting server on port {port}: {e}") # логируем ошибку

    async def start(self, port: int):
        """
        Запускает FastAPI сервер на указанном порту.

        :param port: Порт для запуска сервера.
        :type port: int
        """
        if port in self.server_tasks and not self.server_tasks[port].done():
            print(f"Server already running on port {port}") # сохраняем print, т.к. это часть вывода
            return
        task = asyncio.create_task(self._start_server(port))
        self.server_tasks[port] = task
        j_dumps(self.server_tasks, 'servers.json') # используем j_dumps

    async def stop(self, port: int):
        """
        Останавливает FastAPI сервер на указанном порту.

        :param port: Порт для остановки сервера.
        :type port: int
        """
        if port in self.servers and self.servers[port].started:
            try: # обработка исключения
                await self.servers[port].stop()
            except Exception as e: # обработка исключения
                logger.error(f"Error stopping server on port {port}: {e}") # логируем ошибку
            j_dumps(self.server_tasks, 'servers.json') # используем j_dumps

    async def stop_all(self):
        """Останавливает все запущенные серверы."""
        for port in list(self.servers.keys()):
             await self.stop(port)

    def get_app(self):
      """
      Возвращает FastAPI приложение.

      :return: FastAPI приложение.
      :rtype: FastAPI
      """
      return self


async def test_function():
   """
   Тестовая функция для GET запроса.

   :return: Строка "It is working!!!".
   :rtype: str
   """
   return "It is working!!!"


async def test_post(data: Dict[str, str]):
    """
    Тестовая функция для POST запроса.

    :param data: Данные из POST запроса.
    :type data: Dict[str, str]
    :return: Словарь с результатом и данными.
    :rtype: Dict[str, Any]
    """
    return {"result": "post ok", "data": data}


async def main():
    """
    Основная асинхронная функция для запуска и тестирования сервера.
    """
    api = FastApiServer(title='My API', host='0.0.0.0')
    api.add_route('/hello', test_function)
    api.add_route('/post', test_post, methods=['POST'])
    api.register_router()

    # Запускаем на порту 8080
    print('start api on port 8080') # сохраняем print, т.к. это часть вывода
    await api.start(port=8080)

    # some work
    await asyncio.sleep(2)
    # Добавляем порт 8081 на лету
    print('start api on port 8081') # сохраняем print, т.к. это часть вывода
    await api.start(port=8081)

    await asyncio.sleep(2)
    # stop port 8080
    print('stop api on port 8080') # сохраняем print, т.к. это часть вывода
    await api.stop(port=8080)

    await asyncio.sleep(2)
    print('stop all servers') # сохраняем print, т.к. это часть вывода
    await api.stop_all()


if __name__ == "__main__":
    asyncio.run(main())
```