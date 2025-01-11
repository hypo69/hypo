### Анализ кода модуля `README.MD`

**Качество кода**:
- **Соответствие стандартам**: 6
- **Плюсы**:
  - Реализация паттерна Singleton для FastAPI.
  - Динамическое добавление и остановка портов.
  - Асинхронная работа с сервером.
- **Минусы**:
  - Отсутствует обработка исключений.
  - Не используются логирование ошибок.
  - Код недостаточно документирован (отсутствует RST-документация).
  - Используются `print` для вывода, вместо `logger`.

**Рекомендации по улучшению**:
  - Добавить логирование ошибок с помощью `logger.error`.
  - Использовать RST-документацию для всех функций и классов.
  - Избегать `print` для вывода сообщений, использовать `logger.info` и `logger.error`.
  - Обработать возможные исключения в методах `_start_server`, `start`, `stop` и `stop_all`.
  - Переименовать `Fapi` в `FastAPI` для соответствия PEP8.
  - Выравнивать импорты и переменные.
  - Добавить докстринги к классам и методам.
  - Удалить неиспользуемые импорты.

**Оптимизированный код**:
```python
"""
Модуль для работы с FastAPI сервером.
====================================

Этот модуль предоставляет класс :class:`FastApi`, который является синглтоном
для FastAPI приложений и позволяет динамически управлять портами.

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
from fastapi import FastAPI as FastAPI, APIRouter  # Исправлено название импорта
import uvicorn
from typing import List, Callable, Dict, Any
import functools
import asyncio
from src.logger import logger # импортируем logger


class FastApi(FastAPI): # Исправлено название класса
    """
    Класс-синглтон для управления FastAPI сервером.

    Предоставляет методы для запуска, остановки и динамического управления портами сервера.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Создает или возвращает существующий экземпляр класса.

        :return: Экземпляр класса FastApi.
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
        Инициализирует экземпляр класса FastApi.

        :param title: Заголовок FastAPI приложения.
        :type title: str, optional
        :param host: Хост для запуска сервера.
        :type host: str, optional
        :param kwargs: Дополнительные параметры для FastAPI.
        :type kwargs: dict, optional
        """
        if self._initialized:
            return
        super().__init__(title=title, **kwargs)
        self.router = APIRouter()
        self.host = host
        self._initialized = True

    def add_route(self, path: str, func: Callable, methods: List[str] = ["GET"], **kwargs):
        """
        Добавляет маршрут в FastAPI приложение.

        :param path: Путь маршрута.
        :type path: str
        :param func: Функция-обработчик маршрута.
        :type func: Callable
        :param methods: Список HTTP методов.
        :type methods: List[str], optional
        :param kwargs: Дополнительные параметры для маршрута.
        :type kwargs: dict, optional
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        self.router.add_api_route(path, wrapper, methods=methods, **kwargs)

    def register_router(self):
        """
        Регистрирует маршрутизатор в FastAPI приложении.
        """
        self.include_router(self.router)

    async def _start_server(self, port: int):
        """
        Запускает Uvicorn сервер на указанном порту.

        :param port: Порт для запуска сервера.
        :type port: int
        """
        try:
           config = uvicorn.Config(self, host=self.host, port=port, log_level="info")
           server = uvicorn.Server(config)
           self.servers[port] = server
           await server.serve()
        except Exception as e: # Обработка исключения
            logger.error(f"Error starting server on port {port}: {e}") # Логируем ошибку

    def start(self, port: int):
        """
        Запускает FastAPI сервер на указанном порту.

        :param port: Порт для запуска сервера.
        :type port: int
        """
        if port in self.server_tasks and not self.server_tasks[port].done():
            logger.info(f"Server already running on port {port}") # Заменили print на logger
            return
        task = asyncio.create_task(self._start_server(port))
        self.server_tasks[port] = task

    async def stop(self, port: int):
        """
        Останавливает FastAPI сервер на указанном порту.

        :param port: Порт для остановки сервера.
        :type port: int
        """
        try:
            if port in self.servers and self.servers[port].started:
               await self.servers[port].stop()
        except Exception as e: # Обработка исключения
            logger.error(f"Error stopping server on port {port}: {e}") # Логируем ошибку

    async def stop_all(self):
        """
        Останавливает все запущенные FastAPI серверы.
        """
        for port in list(self.servers.keys()):
            await self.stop(port)

    def get_app(self):
        """
        Возвращает экземпляр FastAPI приложения.

        :return: Экземпляр FastAPI.
        :rtype: FastAPI
        """
        return self
```
```python
from fastapi import FastAPI
# example of use
import asyncio
from typing import Dict
from src.fast_api.fast_api import FastApi


async def test_function():
   return 'It is working!!!'


def test_post(data: Dict[str, str]):
   return {'result': 'post ok', 'data': data}


async def main():
    api = FastApi(title='My API', host='0.0.0.0')
    api.add_route('/hello', test_function)
    api.add_route('/post', test_post, methods=['POST'])
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


if __name__ == '__main__':
    asyncio.run(main())
```
```
# FastApi: Singleton for FastAPI with Dynamic Port Management

This `FastApi` class provides a singleton implementation for FastAPI, allowing you to launch and manage a FastAPI server and dynamically add and stop ports during runtime.

## Key Features

*   **Singleton:** Ensures a single instance of the FastAPI application in your application.
*   **Dynamic Port Management:** Allows you to launch the server on multiple ports and add and stop ports during runtime.
*   **Explicit Start and Stop:** Provides `start()` and `stop()` methods to manage the server on each port.
*   **Asynchronous:** Uses `asyncio` for asynchronous server launching.

## Usage

### Installation

To use the `FastApi` class, you need to install FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

### Creating an Instance

Create an instance of the `FastApi` class:

```python
from fastapi import FastAPI as Fapi, APIRouter
import uvicorn
from typing import List, Callable, Dict, Any
import functools
import threading
import asyncio


class FastApi(Fapi):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._initialized = False
            cls._instance.server_tasks = {}  # Dictionary to store tasks (port: task)
            cls._instance.servers = {}  # Dictionary to store servers (port: server)
        return cls._instance

    def __init__(self, title: str = "FastAPI Singleton Server", host: str = "127.0.0.1", **kwargs):
        if self._initialized:
            return
        super().__init__(title=title, **kwargs)
        self.router = APIRouter()
        self.host = host
        self._initialized = True


    def add_route(self, path: str, func: Callable, methods: List[str] = ["GET"], **kwargs):
        """Adds a route to the FastAPI application."""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        self.router.add_api_route(path, wrapper, methods=methods, **kwargs)


    def register_router(self):
        """Registers the router"""
        self.include_router(self.router)


    async def _start_server(self, port: int):
        config = uvicorn.Config(self, host=self.host, port=port, log_level="info")
        server = uvicorn.Server(config)
        self.servers[port] = server
        await server.serve()

    def start(self, port: int):
        """Launches the FastAPI server on the specified port."""
        if port in self.server_tasks and not self.server_tasks[port].done():
            print(f"Server already running on port {port}")
            return
        task = asyncio.create_task(self._start_server(port))
        self.server_tasks[port] = task


    async def stop(self, port: int):
        if port in self.servers and self.servers[port].started:
            await self.servers[port].stop()

    async def stop_all(self):
        for port in list(self.servers.keys()):
             await self.stop(port)

    def get_app(self):
      """Returns the FastAPI application"""
      return self
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

### Adding Routes

Use the `add_route()` method to add routes to your application:

```python
api.add_route("/hello", test_function)
api.add_route("/post", test_post, methods=["POST"])
```
`path`: The path of the route.
`func`: The handler function.
`methods`: A list of HTTP methods.
`kwargs`: Additional arguments.

### Registering the Router

Don't forget to register the router using the `register_router()` method:

```python
api.register_router()
```

### Launching the Server on a Port

Use the `start()` method to launch the server on a specific port:

```python
api.start(port=8080)
```
`port`: The port to launch.

### Adding Ports Dynamically

You can add new ports to listen on at any time by calling `start()` with a new port number:

```python
api.start(port=8081)
```

### Stopping the Server on a Port

Use the `stop()` method to stop the server on a specific port:

```python
await api.stop(port=8080)
```
`port`: The port to stop.

### Stopping All Servers

Use the `stop_all()` method to stop all running servers:

```python
await api.stop_all()
```

## Settings

*   **`title`**: The title of your FastAPI application. Set when creating an instance of the class.
     ```python
        api = FastApi(title="My API", host="0.0.0.0")
     ```
*   **`host`**: The host the server will run on. Set when creating an instance of the class.
    ```python
    api = FastApi(title="My API", host="0.0.0.0")
    ```
*  **`port`** The port the server will be launch on. Set in the start method.
     ```python
       api.start(port=8081)
     ```

## Examples

Examples of use can be found in the code above.

## Conclusion

The `FastApi` class provides a powerful and flexible tool for working with FastAPI, allowing you to dynamically manage ports and resources of your application.

This `readme.en.md` file should give users a good understanding of how to use your `FastApi` class. If you have any additional questions, I'm always ready to help!