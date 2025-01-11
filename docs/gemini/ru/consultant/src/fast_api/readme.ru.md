## Анализ кода модуля `FastApi`

### Качество кода:
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Реализация паттерна "Синглтон" для FastAPI приложения.
    - Динамическое управление портами.
    - Асинхронный запуск и остановка серверов.
    - Четкое разделение ответственности методов.
- **Минусы**:
    - Использование `print` для логирования.
    - Отсутствует обработка исключений в `_start_server`, `stop` и `stop_all`.
    - Недостаточно комментариев в коде, в том числе для функций и классов.
    - Нет проверки на корректность входящих параметров.
    - Не используется `from src.logger import logger`.

### Рекомендации по улучшению:
- Заменить `print` на `logger.info` для логирования.
- Добавить обработку исключений с использованием `logger.error` в методах `_start_server`, `stop` и `stop_all`.
- Добавить docstring для класса и методов в формате RST.
- Проверить входные параметры на корректность.
- Использовать `from src.logger import logger` для логирования.
- Добавить пример использования в docstring для функций.

### Оптимизированный код:
```python
"""
Модуль для работы с FastAPI с динамическим управлением портами
=============================================================

Этот модуль предоставляет класс :class:`FastApi`, который позволяет
динамически управлять портами и ресурсами FastAPI-приложения.

Основные возможности:
---------------------
- Синглтон: обеспечивает единственный экземпляр FastAPI-приложения.
- Динамическое управление портами: позволяет запускать сервер на нескольких портах,
  добавлять и останавливать порты во время работы приложения.
- Явный старт и остановка: методы `start()` и `stop()` для управления сервером.
- Многопоточность: использует `asyncio` для асинхронного запуска серверов.

Пример использования:
---------------------
.. code-block:: python

    from fastapi import FastAPI
    import asyncio
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

    if __name__ == '__main__':
        asyncio.run(main())
"""
from fastapi import FastAPI as Fapi, APIRouter # from fastapi import FastAPI as Fapi, APIRouter
import uvicorn # import uvicorn
from typing import List, Callable, Dict, Any # from typing import List, Callable, Dict, Any
import functools # import functools
import asyncio # import asyncio
from src.logger.logger import logger # from src.logger import logger


class FastApi(Fapi):
    """
    Класс для управления FastAPI приложением с динамическим управлением портами.

    :param title: Заголовок FastAPI-приложения.
    :type title: str, optional
    :param host: Хост, на котором будет запущен сервер.
    :type host: str, optional
    :param kwargs: Дополнительные аргументы для FastAPI.
    :type kwargs: dict
    """
    _instance = None # _instance = None

    def __new__(cls, *args, **kwargs):
        """
        Создает или возвращает существующий экземпляр класса FastApi (Singleton).

        :param args: Позиционные аргументы.
        :type args: tuple
        :param kwargs: Именованные аргументы.
        :type kwargs: dict
        :return: Экземпляр класса FastApi.
        :rtype: FastApi
        """
        if cls._instance is None: # if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs) # cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance._initialized = False # cls._instance._initialized = False
            cls._instance.server_tasks = {}  # Словарь для хранения задач (port: task) # cls._instance.server_tasks = {}  # Словарь для хранения задач (port: task)
            cls._instance.servers = {}  # Словарь для хранения серверов (port: server) # cls._instance.servers = {}  # Словарь для хранения серверов (port: server)
        return cls._instance # return cls._instance

    def __init__(self, title: str = 'FastAPI Singleton Server', host: str = '127.0.0.1', **kwargs):
        """
        Инициализирует экземпляр класса FastApi.

        :param title: Заголовок FastAPI-приложения.
        :type title: str, optional
        :param host: Хост, на котором будет запущен сервер.
        :type host: str, optional
        :param kwargs: Дополнительные аргументы для FastAPI.
        :type kwargs: dict
        """
        if self._initialized: # if self._initialized:
            return # return
        super().__init__(title=title, **kwargs) # super().__init__(title=title, **kwargs)
        self.router = APIRouter() # self.router = APIRouter()
        self.host = host # self.host = host
        self._initialized = True # self._initialized = True

    def add_route(self, path: str, func: Callable, methods: List[str] = ['GET'], **kwargs):
        """
        Добавляет маршрут к FastAPI приложению.

        :param path: Путь маршрута.
        :type path: str
        :param func: Функция-обработчик маршрута.
        :type func: Callable
        :param methods: Список HTTP-методов для маршрута.
        :type methods: List[str], optional
        :param kwargs: Дополнительные аргументы для `add_api_route`.
        :type kwargs: dict
        
        Пример:
           >>> async def test_function():
           ...     return 'It is working!!!'
           >>> api = FastApi()
           >>> api.add_route('/hello', test_function)
        """
        @functools.wraps(func) # @functools.wraps(func)
        def wrapper(*args, **kwargs): # def wrapper(*args, **kwargs):
            return func(*args, **kwargs) # return func(*args, **kwargs)
        self.router.add_api_route(path, wrapper, methods=methods, **kwargs) # self.router.add_api_route(path, wrapper, methods=methods, **kwargs)

    def register_router(self):
        """
        Регистрирует роутер в FastAPI приложении.
        
        Пример:
           >>> api = FastApi()
           >>> api.register_router()
        """
        self.include_router(self.router) # self.include_router(self.router)

    async def _start_server(self, port: int):
        """
        Асинхронно запускает Uvicorn сервер на указанном порту.

        :param port: Порт для запуска сервера.
        :type port: int
        :raises Exception: В случае ошибки при запуске сервера.
        """
        try: # try:
            config = uvicorn.Config(self, host=self.host, port=port, log_level='info') # config = uvicorn.Config(self, host=self.host, port=port, log_level='info')
            server = uvicorn.Server(config) # server = uvicorn.Server(config)
            self.servers[port] = server # self.servers[port] = server
            await server.serve() # await server.serve()
        except Exception as e: # except Exception as e:
           logger.error(f'Error starting server on port {port}: {e}') # logger.error(f'Error starting server on port {port}: {e}')


    def start(self, port: int):
        """
        Запускает FastAPI сервер на указанном порту.

        :param port: Порт для запуска сервера.
        :type port: int
        
        Пример:
           >>> api = FastApi()
           >>> api.start(port=8080)
        """
        if not isinstance(port, int): # if not isinstance(port, int):
            logger.error(f'Port must be an integer, got {type(port)}') # logger.error(f'Port must be an integer, got {type(port)}')
            return # return
        if port in self.server_tasks and not self.server_tasks[port].done(): # if port in self.server_tasks and not self.server_tasks[port].done():
            logger.info(f'Server already running on port {port}') # logger.info(f'Server already running on port {port}')
            return # return
        task = asyncio.create_task(self._start_server(port)) # task = asyncio.create_task(self._start_server(port))
        self.server_tasks[port] = task # self.server_tasks[port] = task


    async def stop(self, port: int):
        """
        Останавливает FastAPI сервер на указанном порту.

        :param port: Порт сервера для остановки.
        :type port: int
        
        Пример:
           >>> api = FastApi()
           >>> api.start(port=8080)
           >>> await api.stop(port=8080)
        """
        try: # try:
            if port in self.servers and self.servers[port].started: # if port in self.servers and self.servers[port].started:
                await self.servers[port].stop() # await self.servers[port].stop()
        except Exception as e: # except Exception as e:
            logger.error(f'Error stopping server on port {port}: {e}') # logger.error(f'Error stopping server on port {port}: {e}')


    async def stop_all(self):
        """
        Останавливает все запущенные FastAPI серверы.

        Пример:
           >>> api = FastApi()
           >>> api.start(port=8080)
           >>> api.start(port=8081)
           >>> await api.stop_all()
        """
        for port in list(self.servers.keys()): # for port in list(self.servers.keys()):
            await self.stop(port) # await self.stop(port)

    def get_app(self):
        """
        Возвращает FastAPI приложение.
        
        :return: FastAPI приложение
        :rtype: Fapi
        
        Пример:
           >>> api = FastApi()
           >>> app = api.get_app()
           >>> assert isinstance(app, Fapi)
        """
        return self # return self
```
```python
from fastapi import FastAPI # from fastapi import FastAPI
# пример использования # пример использования
import asyncio # import asyncio
from src.fast_api.fast_api import FastApi # from src.fast_api.fast_api import FastApi

async def test_function():
   return 'It is working!!!'

def test_post(data: Dict[str, str]):
   return {'result': 'post ok', 'data': data}


async def main():
    api = FastApi(title='My API', host='0.0.0.0')
    api.add_route('/hello', test_function)
    api.add_route('/post', test_post, methods=['POST'])
    api.register_router()

    # Запускаем на порту 8080
    print('start api on port 8080')
    api.start(port=8080)

    # some work
    await asyncio.sleep(2)
    # Добавляем порт 8081 на лету
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
# FastApi: Синглтон для FastAPI с динамическим управлением портами
Класс `FastApi` позволяет динамически управлять портами и ресурсами вашего приложения.
позволяя запускать и управлять FastAPI-сервером, а также динамически добавлять и останавливать порты
во время работы приложения.

## Основные возможности

*   **Синглтон:** Обеспечивает единственный экземпляр FastAPI-приложения в вашем приложении.
*   **Динамическое управление портами:** Позволяет запускать сервер на нескольких портах, а также добавлять и останавливать порты во время выполнения программы.
*   **Явный старт и остановка:**  Предоставляет методы `start()` и `stop()` для управления сервером на каждом порту.
*   **Многопоточность:** Использует `asyncio` для асинхронного запуска серверов.

## Использование

### Установка

Для использования класса `FastApi` вам необходимо установить FastAPI и Uvicorn:

```bash
pip install fastapi uvicorn
```

### Создание экземпляра

Создайте экземпляр класса `FastApi`:

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
            cls._instance.server_tasks = {}  # Словарь для хранения задач (port: task)
            cls._instance.servers = {}  # Словарь для хранения серверов (port: server)
        return cls._instance

    def __init__(self, title: str = "FastAPI Singleton Server", host: str = "127.0.0.1", **kwargs):
        if self._initialized:
            return
        super().__init__(title=title, **kwargs)
        self.router = APIRouter()
        self.host = host
        self._initialized = True


    def add_route(self, path: str, func: Callable, methods: List[str] = ["GET"], **kwargs):
        """Добавляет маршрут к FastAPI приложению."""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        self.router.add_api_route(path, wrapper, methods=methods, **kwargs)


    def register_router(self):
        """Регистрирует роутер"""
        self.include_router(self.router)


    async def _start_server(self, port: int):
        config = uvicorn.Config(self, host=self.host, port=port, log_level="info")
        server = uvicorn.Server(config)
        self.servers[port] = server
        await server.serve()

    def start(self, port: int):
        """Запускает FastAPI сервер на указанном порту."""
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
      """Возвращает FastAPI приложение"""
      return self
```

```python
from fastapi import FastAPI
# пример использования
import asyncio
from src.fast_api.fast_api import FastApi

async def test_function():
   return "It is working!!!"

def test_post(data: Dict[str, str]):
   return {"result": "post ok", "data": data}


async def main():
    api = FastApi(title="My API", host="0.0.0.0")
    api.add_route("/hello", test_function)
    api.add_route("/post", test_post, methods=["POST"])
    api.register_router()

    # Запускаем на порту 8080
    print('start api on port 8080')
    api.start(port=8080)

    # some work
    await asyncio.sleep(2)
    # Добавляем порт 8081 на лету
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

### Добавление маршрутов

Используйте метод `add_route()` для добавления маршрутов к вашему приложению:

```python
api.add_route("/hello", test_function)
api.add_route("/post", test_post, methods=["POST"])
```
`path`: путь маршрута
`func`: функция обработчик
`methods`: список методов
`kwargs`: дополнительные аргументы

### Регистрация роутера

Не забудьте зарегистрировать роутер с помощью метода `register_router()`:

```python
api.register_router()
```

### Запуск сервера на порту

Используйте метод `start()` для запуска сервера на определенном порту:

```python
api.start(port=8080)
```
`port`: порт для запуска

### Динамическое добавление портов

Вы можете добавить новые порты для прослушивания в любое время, вызвав `start()` с новым портом:

```python
api.start(port=8081)
```

### Остановка сервера на порту

Используйте метод `stop()` для остановки сервера на определенном порту:

```python
await api.stop(port=8080)
```
`port`: порт, который надо остановить

### Остановка всех серверов

Используйте метод `stop_all()` для остановки всех запущенных серверов:

```python
await api.stop_all()
```

## Настройки

*   **`title`**: Заголовок вашего FastAPI-приложения. Устанавливается при создании экземпляра класса.
    ```python
        api = FastApi(title="My API", host="0.0.0.0")
    ```
*   **`host`**: Хост, на котором будет запущен сервер. Устанавливается при создании экземпляра класса.
   ```python
    api = FastApi(title="My API", host="0.0.0.0")
    ```
* **`port`** Порт, на котором будет запущен сервер. Устанавливается в методе start
    ```python
       api.start(port=8081)
    ```
```
## Примеры

Примеры использования можно найти в коде выше.

**Как использовать этот файл:**

1.  Создайте файл с именем `readme.ru.md` в том же каталоге, где находится ваш код.
2.  Скопируйте и вставьте этот текст в файл `readme.ru.md`.

Теперь у вас есть подробный файл `README` на русском языке, который поможет пользователям разобраться с вашим классом `FastApi`.