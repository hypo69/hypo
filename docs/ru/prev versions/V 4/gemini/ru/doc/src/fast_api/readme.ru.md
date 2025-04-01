# Документация для `fast_api_rpc.py` и `main.py`

## Обзор

Данная документация описывает взаимодействие между `fast_api_rpc.py` (серверная часть) и `main.py` (клиентская часть) в проекте `hypotez`. `fast_api_rpc.py` предоставляет функциональность для управления FastAPI сервером через XML-RPC, а `main.py` предоставляет пользовательский интерфейс для отправки команд на сервер.

## Подробней

### `fast_api_rpc.py` (серверная часть)

Содержит класс `FastApiServer` для запуска FastAPI-сервера и класс `CommandHandler`, который управляет вызовами функций управления сервером через XML-RPC. `CommandHandler` содержит методы для запуска, остановки и управления серверами, а также для добавления новых маршрутов.

### `main.py` (клиентская часть)

Предоставляет интерфейс командной строки для взаимодействия с сервером `fast_api_rpc.py`. Использует `ServerProxy` из библиотеки `xmlrpc.client` для отправки команд на сервер.

## Классы

### `FastApiServer`

**Описание**: Класс для управления FastAPI сервером.

**Методы**: 
- `start()`: Запускает FastAPI сервер.
- `stop()`: Останавливает FastAPI сервер.

**Параметры**: 
- `port` (int): Порт для запуска сервера.
- `host` (str): Хост для запуска сервера.

**Примеры**:
```python
# Пример использования класса FastApiServer
# from fast_api_rpc import FastApiServer
# server = FastApiServer(port=8000, host="0.0.0.0")
# server.start()
# server.stop()
```

### `CommandHandler`

**Описание**: Класс для управления сервером через XML-RPC.

**Методы**: 
- `start_server(port: int, host: str)`: Запускает FastAPI сервер.
- `stop_server(port: int)`: Останавливает FastAPI сервер.
- `stop_all_servers()`: Останавливает все запущенные серверы.
- `status_servers()`: Возвращает статус всех серверов.
- `add_new_route(path: str, response: str, methods: list[str], port: int)`: Добавляет новый маршрут на сервер.
- `shutdown()`: Завершает работу XML-RPC сервера.

**Параметры**: 
- `port` (int): Порт для запуска сервера.
- `host` (str): Хост для запуска сервера.
- `path` (str): Путь для нового маршрута.
- `response` (str): Ответ для нового маршрута.
- `methods` (list[str]): Список HTTP методов для нового маршрута.

**Примеры**:
```python
# from fast_api_rpc import CommandHandler
# handler = CommandHandler()
# handler.start_server(port=8000, host="0.0.0.0")
# handler.stop_server(port=8000)
# handler.add_new_route(path="/test", response="Hello, world!", methods=["GET"], port=8000)
```

## Функции

### `start_server`

```python
def start_server(port: int, host: str) -> None:
    """
    Args:
        port (int): Порт для запуска сервера.
        host (str): Хост для запуска сервера.

    Returns:
        None: Ничего не возвращает.

    Raises:
        Exception: В случае ошибки при запуске сервера.

    Example:
        >>> start_server(port=8000, host="0.0.0.0")
    """
    - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Запускает FastAPI сервер на указанном порту и хосте.

**Параметры**: 
- `port` (int): Порт для запуска сервера.
- `host` (str): Хост для запуска сервера.

**Возвращает**: 
- `None`: Ничего не возвращает.

**Вызывает исключения**: 
- `Exception`: В случае ошибки при запуске сервера.

**Примеры**:
```python
# Пример вызова функции start_server
# start_server(port=8000, host="0.0.0.0")
```

### `stop_server`

```python
def stop_server(port: int) -> None:
    """
    Args:
        port (int): Порт сервера, который нужно остановить.

    Returns:
        None: Ничего не возвращает.

    Raises:
        Exception: В случае ошибки при остановке сервера.

    Example:
        >>> stop_server(port=8000)
    """
    - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Останавливает FastAPI сервер на указанном порту.

**Параметры**: 
- `port` (int): Порт сервера, который нужно остановить.

**Возвращает**: 
- `None`: Ничего не возвращает.

**Вызывает исключения**: 
- `Exception`: В случае ошибки при остановке сервера.

**Примеры**:
```python
# Пример вызова функции stop_server
# stop_server(port=8000)
```

### `stop_all_servers`

```python
def stop_all_servers() -> None:
    """
    Args:
        Нет параметров.

    Returns:
        None: Ничего не возвращает.

    Raises:
        Exception: В случае ошибки при остановке серверов.

    Example:
        >>> stop_all_servers()
    """
    - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Останавливает все запущенные FastAPI серверы.

**Параметры**: 
- Нет параметров.

**Возвращает**: 
- `None`: Ничего не возвращает.

**Вызывает исключения**: 
- `Exception`: В случае ошибки при остановке серверов.

**Примеры**:
```python
# Пример вызова функции stop_all_servers
# stop_all_servers()
```

### `status_servers`

```python
def status_servers() -> dict:
    """
    Args:
        Нет параметров.

    Returns:
        dict: Словарь, содержащий статус всех серверов.

    Raises:
        Exception: В случае ошибки при получении статуса серверов.

    Example:
        >>> status_servers()
        {'8000': 'running', '8001': 'stopped'}
    """
    - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Возвращает словарь, содержащий статус всех FastAPI серверов.

**Параметры**: 
- Нет параметров.

**Возвращает**: 
- `dict`: Словарь, содержащий статус всех серверов.

**Вызывает исключения**: 
- `Exception`: В случае ошибки при получении статуса серверов.

**Примеры**:
```python
# Пример вызова функции status_servers
# status = status_servers()
# print(status)
```

### `add_new_route`

```python
def add_new_route(path: str, response: str, methods: list[str], port: int) -> None:
    """
    Args:
        path (str): Путь для нового маршрута.
        response (str): Ответ для нового маршрута.
        methods (list[str]): Список HTTP методов для нового маршрута.
        port (int): Порт сервера, на который нужно добавить маршрут.

    Returns:
        None: Ничего не возвращает.

    Raises:
        Exception: В случае ошибки при добавлении маршрута.

    Example:
        >>> add_new_route(path="/test", response="Hello, world!", methods=["GET"], port=8000)
    """
    - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Добавляет новый маршрут на FastAPI сервер.

**Параметры**: 
- `path` (str): Путь для нового маршрута.
- `response` (str): Ответ для нового маршрута.
- `methods` (list[str]): Список HTTP методов для нового маршрута.
- `port` (int): Порт сервера, на который нужно добавить маршрут.

**Возвращает**: 
- `None`: Ничего не возвращает.

**Вызывает исключения**: 
- `Exception`: В случае ошибки при добавлении маршрута.

**Примеры**:
```python
# Пример вызова функции add_new_route
# add_new_route(path="/test", response="Hello, world!", methods=["GET"], port=8000)
```

### `shutdown`

```python
def shutdown() -> None:
    """
    Args:
        Нет параметров.

    Returns:
        None: Ничего не возвращает.

    Raises:
        Exception: В случае ошибки при завершении работы сервера.

    Example:
        >>> shutdown()
    """
    - Не выводи тело функции. только документацию и примеры вызова функции;
```

**Описание**: Завершает работу XML-RPC сервера.

**Параметры**: 
- Нет параметров.

**Возвращает**: 
- `None`: Ничего не возвращает.

**Вызывает исключения**: 
- `Exception`: В случае ошибки при завершении работы сервера.

**Примеры**:
```python
# Пример вызова функции shutdown
# shutdown()
```