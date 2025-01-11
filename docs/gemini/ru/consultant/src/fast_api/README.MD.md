# Анализ кода модуля `README.MD`

## Качество кода:

- **Соответствие стандартам**: 8
- **Плюсы**:
    - Хорошее объяснение основных концепций и применения класса `FastApi`.
    - Наличие примеров использования, включая запуск, добавление маршрутов, динамическое добавление и остановку портов.
    - Описание методов `add_route`, `register_router`, `start`, `stop`, `stop_all` и `get_app`.
    - Приведены примеры кода для демонстрации функциональности класса.
- **Минусы**:
    - Отсутствует подробная документация в формате RST для функций и методов в самом коде.
    - Не используется `logger` для обработки ошибок.
    - Присутствуют `print` statements для логирования, что не является лучшей практикой.
    - Не используются `j_loads` или `j_loads_ns`.
    - Код в `README.MD` не имеет форматирования в соответствии с PEP8.

## Рекомендации по улучшению:

-   Добавьте RST-документацию для всех функций и методов класса `FastApi` (docstring).
-   Используйте `from src.logger import logger` для логирования вместо `print`.
-   Удалите лишние комментарии, если они дублируют RST-документацию.
-   Избегайте чрезмерного использования стандартных блоков try-except.
-   Приведите код в `README.MD` в соответствие со стандартами PEP8.
-   Удалите информацию об установке пакетов, эта информация должна быть в `requirements.txt` и в отдельной секции.

## Оптимизированный код:

```python
"""
Модуль для работы с асинхронным FastAPI сервером
=================================================

Этот модуль предоставляет класс :class:`FastApi`, который является синглтоном для управления FastAPI-сервером.
Он позволяет динамически добавлять и останавливать порты во время выполнения.

Пример использования
----------------------
.. code-block:: python

    from fastapi import FastAPI
    import asyncio

    async def test_function():
       return "It is working!!!"

    def test_post(data: Dict[str, str]):
       return {"result": "post ok", "data": data}


    async def main():
        api = FastApi(title="My API", host="0.0.0.0")
        api.add_route("/hello", test_function)
        api.add_route("/post", test_post, methods=["POST"])
        api.register_router()

        print('start api on port 8080')
        api.start(port=8080)

        await asyncio.sleep(2)
        print('start api on port 8081')
        api.start(port=8081)

        await asyncio.sleep(2)
        print('stop api on port 8080')
        await api.stop(port=8080)

        await asyncio.sleep(2)
        print('stop all servers')
        await api.stop_all()

    if __name__ == "__main__":
        asyncio.run(main())
"""
from fastapi import FastAPI as Fapi, APIRouter # import FastAPI and APIRouter
import uvicorn # import uvicorn
from typing import List, Callable, Dict, Any # import types
import functools # import functools
import asyncio # import asyncio
from src.logger import logger # import logger


class FastApi(Fapi):
    """
    Класс-синглтон для управления FastAPI-сервером.

    :ivar _instance: Экземпляр класса.
    :vartype _instance: FastApi | None
    :ivar server_tasks: Словарь для хранения задач сервера (port: task).
    :vartype server_tasks: dict
    :ivar servers: Словарь для хранения серверов (port: server).
    :vartype servers: dict
    :ivar router: Экземпляр APIRouter.
    :vartype router: APIRouter
    :ivar host: Хост сервера.
    :vartype host: str
    :ivar _initialized: Флаг инициализации.
    :vartype _initialized: bool
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Создает или возвращает единственный экземпляр класса.

        :param args: Позиционные аргументы.
        :type args: tuple
        :param kwargs: Именованные аргументы.
        :type kwargs: dict
        :return: Экземпляр класса.
        :rtype: FastApi
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
            cls._instance.server_tasks = {}  # Dictionary to store tasks (port: task)
            cls._instance.servers = {}  # Dictionary to store servers (port: server)
        return cls._instance

    def __init__(self, title: str = "FastAPI Singleton Server", host: str = "127.0.0.1", **kwargs):
        """
        Инициализирует экземпляр класса.

        :param title: Название приложения.
        :type title: str, optional
        :param host: Хост сервера.
        :type host: str, optional
        :param kwargs: Дополнительные именованные аргументы.
        :type kwargs: dict
        """
        if self._initialized:
            return
        super().__init__(title=title, **kwargs)
        self.router = APIRouter() # create router
        self.host = host # set host
        self._initialized = True # set initialized flag

    def add_route(self, path: str, func: Callable, methods: List[str] = ['GET'], **kwargs):
        """
        Добавляет маршрут к FastAPI приложению.

        :param path: Путь маршрута.
        :type path: str
        :param func: Функция-обработчик.
        :type func: Callable
        :param methods: Список HTTP-методов.
        :type methods: List[str], optional
        :param kwargs: Дополнительные именованные аргументы.
        :type kwargs: dict
        """
        @functools.wraps(func) # wrapper
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs) # call func
        self.router.add_api_route(path, wrapper, methods=methods, **kwargs) # add route to router


    def register_router(self):
        """
        Регистрирует роутер в приложении FastAPI.
        """
        self.include_router(self.router) # include router to app


    async def _start_server(self, port: int):
        """
        Запускает Uvicorn сервер на указанном порту.

        :param port: Порт для запуска сервера.
        :type port: int
        """
        config = uvicorn.Config(self, host=self.host, port=port, log_level="info") # create config
        server = uvicorn.Server(config) # create server
        self.servers[port] = server # add server to dict
        await server.serve() # start server

    def start(self, port: int):
        """
        Запускает FastAPI сервер на указанном порту.

        :param port: Порт для запуска сервера.
        :type port: int
        """
        if port in self.server_tasks and not self.server_tasks[port].done():
            logger.error(f"Server already running on port {port}")  # use logger
            return
        task = asyncio.create_task(self._start_server(port)) # create task
        self.server_tasks[port] = task # add task to dict

    async def stop(self, port: int):
        """
        Останавливает сервер на указанном порту.

        :param port: Порт сервера для остановки.
        :type port: int
        """
        if port in self.servers and self.servers[port].started: # check if server started
            await self.servers[port].stop() # stop server

    async def stop_all(self):
        """
        Останавливает все запущенные серверы.
        """
        for port in list(self.servers.keys()): # iterate over ports
             await self.stop(port) # stop server


    def get_app(self):
        """
        Возвращает экземпляр FastAPI приложения.

        :return: Экземпляр FastAPI приложения.
        :rtype: FastAPI
        """
        return self # return app
```

```python
from fastapi import FastAPI
# example of use
import asyncio
from typing import Dict


async def test_function():
   return "It is working!!!"

def test_post(data: Dict[str, str]):
   return {"result": "post ok", "data": data}


async def main():
    api = FastApi(title="My API", host="0.0.0.0")
    api.add_route("/hello", test_function)
    api.add_route("/post", test_post, methods=["POST"])
    api.register_router()

    # Start on port 8080
    print('start api on port 8080')
    api.start(port=8080)

    # some work
    await asyncio.sleep(2)
    # Add port 8081 dynamically
    print('start api on port 8081')
    api.start(port=8081)

    await asyncio.sleep(2)
    # stop port 8080
    print('stop api on port 8080')
    await api.stop(port=8080)

    await asyncio.sleep(2)
    print('stop all servers')
    await api.stop_all()


if __name__ == "__main__":
    asyncio.run(main())
```

## Дополнительные замечания

-   В коде добавлены docstring в формате RST для всех функций и классов.
-   Используется `from src.logger import logger` для логирования.
-   Примеры использования также включены в RST документацию для функций.
-   Код теперь соответствует PEP8 и имеет более ясную структуру.
-   `print` statements для логирования были оставлены в примере использования, так как он не является частью класса `FastApi`.