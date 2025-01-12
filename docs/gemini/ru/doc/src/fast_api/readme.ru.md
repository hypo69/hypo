# FastApi: Синглтон для FastAPI с динамическим управлением портами

## Обзор

Класс `FastApi` позволяет динамически управлять портами и ресурсами вашего приложения, позволяя запускать и управлять FastAPI-сервером, а также динамически добавлять и останавливать порты во время работы приложения.

## Содержание

- [Основные возможности](#основные-возможности)
- [Использование](#использование)
  - [Установка](#установка)
  - [Создание экземпляра](#создание-экземпляра)
  - [Добавление маршрутов](#добавление-маршрутов)
  - [Регистрация роутера](#регистрация-роутера)
  - [Запуск сервера на порту](#запуск-сервера-на-порту)
  - [Динамическое добавление портов](#динамическое-добавление-портов)
  - [Остановка сервера на порту](#остановка-сервера-на-порту)
  - [Остановка всех серверов](#остановка-всех-серверов)
- [Настройки](#настройки)
- [Примеры](#примеры)

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

### `FastApi`

**Описание**: Класс, реализующий синглтон для FastAPI с динамическим управлением портами.

**Методы**:

- `__new__`: Создает или возвращает существующий экземпляр класса.
- `__init__`: Инициализирует экземпляр класса.
- `add_route`: Добавляет маршрут к FastAPI приложению.
- `register_router`: Регистрирует роутер.
- `_start_server`: Запускает сервер на указанном порту.
- `start`: Запускает FastAPI сервер на указанном порту.
- `stop`: Останавливает сервер на указанном порту.
- `stop_all`: Останавливает все запущенные серверы.
- `get_app`: Возвращает FastAPI приложение.

#### `__new__`
**Описание**: Создает новый экземпляр класса, если он еще не существует, иначе возвращает существующий.

**Параметры**:
    - `cls` (`type`): Класс, для которого создается экземпляр.
    - `*args`: Позиционные аргументы, передаваемые конструктору.
    - `**kwargs`: Именованные аргументы, передаваемые конструктору.

**Возвращает**:
    - `FastApi`: Экземпляр класса `FastApi`.

#### `__init__`
**Описание**: Инициализирует экземпляр класса `FastApi`.

**Параметры**:
    - `title` (`str`, optional): Заголовок FastAPI-приложения. По умолчанию "FastAPI Singleton Server".
    - `host` (`str`, optional): Хост, на котором будет запущен сервер. По умолчанию "127.0.0.1".
    - `**kwargs`: Дополнительные именованные аргументы, передаваемые конструктору FastAPI.

#### `add_route`
**Описание**: Добавляет маршрут к FastAPI приложению.

**Параметры**:
    - `path` (`str`): Путь маршрута.
    - `func` (`Callable`): Функция-обработчик для данного маршрута.
    - `methods` (`List[str]`, optional): Список HTTP-методов, которые будут обрабатываться данным маршрутом. По умолчанию ["GET"].
    - `**kwargs`: Дополнительные именованные аргументы для `add_api_route`.

#### `register_router`
**Описание**: Регистрирует роутер в FastAPI приложении.

#### `_start_server`
**Описание**: Запускает сервер Uvicorn на указанном порту.

**Параметры**:
    - `port` (`int`): Порт для запуска сервера.

#### `start`
**Описание**: Запускает FastAPI сервер на указанном порту.

**Параметры**:
    - `port` (`int`): Порт, на котором необходимо запустить сервер.

#### `stop`
**Описание**: Останавливает сервер на указанном порту.

**Параметры**:
   - `port` (`int`): Порт, на котором нужно остановить сервер.

#### `stop_all`
**Описание**: Останавливает все запущенные серверы.

#### `get_app`
**Описание**: Возвращает FastAPI приложение.

**Возвращает**:
   - `FastApi`: Экземпляр класса FastApi.

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

## Примеры

Примеры использования можно найти в коде выше.

```python
from fastapi import FastAPI
# пример использования
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

**Как использовать этот файл:**

1.  Создайте файл с именем `readme.ru.md` в том же каталоге, где находится ваш код.
2.  Скопируйте и вставьте этот текст в файл `readme.ru.md`.

Теперь у вас есть подробный файл `README` на русском языке, который поможет пользователям разобраться с вашим классом `FastApi`.