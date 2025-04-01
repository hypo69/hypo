# Модуль `fast_api`

## Обзор

Модуль `fast_api` представляет собой FastAPI сервер с XML-RPC интерфейсом для удалённого управления.
Он позволяет запускать, останавливать и управлять серверами FastAPI через командную строку или XML-RPC.

## Подробней

Этот модуль предоставляет возможность динамического добавления новых маршрутов к уже работающему FastAPI приложению.
Он использует конфигурационный файл `fast_api.json` для настройки хоста и портов.
Для логирования используется модуль `logger` из `src.logger`.

## Классы

### `FastApiServer`

**Описание**: Класс `FastApiServer` реализует FastAPI сервер с применением паттерна Singleton.

**Как работает класс**:
- Класс использует паттерн Singleton, чтобы гарантировать существование только одного экземпляра сервера.
- При инициализации добавляет маршруты `/hello` и `/post` для тестирования.
- Позволяет добавлять новые маршруты с помощью метода `add_route`.
- Управляет серверами Uvicorn асинхронно, используя потоки.
- Предоставляет методы для запуска, остановки и получения статуса серверов.

**Методы**:
- `__new__(cls, *args, **kwargs)`: Создает новый экземпляр класса, если он еще не существует.
- `__init__(self, host: str = "127.0.0.1", title: str = "FastAPI RPC Server", **kwargs)`: Инициализирует экземпляр класса, добавляет маршруты `/hello` и `/post`.
- `add_route(self, path: str, func: Callable, methods: List[str] = ["GET"], **kwargs)`: Добавляет маршрут к FastAPI приложению.
- `_start_server(self, port: int)`: Запускает Uvicorn сервер асинхронно.
- `start(self, port: int, as_thread: bool = True)`: Запускает FastAPI сервер на указанном порту.
- `stop(self, port: int)`: Останавливает FastAPI сервер на указанном порту.
- `stop_all(self)`: Останавливает все запущенные сервера.
- `get_servers_status(self)`: Возвращает статус всех серверов.
- `get_routes(self)`: Возвращает список всех роутов.
- `get_app(self)`: Возвращает FastAPI приложение.
- `add_new_route(self, path: str, module_name: str, func_name: str, methods: List[str] = ["GET"], **kwargs)`: Добавляет новый маршрут к уже работающему приложению.

**Параметры**:
- `host` (str): Хост для запуска сервера. По умолчанию `"127.0.0.1"`.
- `title` (str): Заголовок FastAPI приложения. По умолчанию `"FastAPI RPC Server"`.
- `path` (str): Путь для нового маршрута.
- `func` (Callable): Функция, которая будет обрабатывать запросы к маршруту.
- `methods` (List[str]): Список HTTP методов, которые поддерживает маршрут. По умолчанию `["GET"]`.
- `module_name` (str): Имя модуля, содержащего функцию для нового маршрута.
- `func_name` (str): Имя функции, которая будет обрабатывать запросы к новому маршруту.

**Примеры**
```python
# Пример создания экземпляра FastApiServer
server = FastApiServer(host="0.0.0.0", title="My FastAPI Server")

# Пример добавления нового маршрута
def my_route_handler():
    return {"message": "Hello from my route!"}

server.add_route("/my_route", my_route_handler)

# Пример запуска сервера
server.start(port=8000)
```

### `CommandHandler`

**Описание**: Класс `CommandHandler` обрабатывает команды для FastAPI сервера через XML-RPC.

**Как работает класс**:
- Инициализирует XML-RPC сервер на указанном порту.
- Регистрирует методы для управления серверами FastAPI.
- Запускает XML-RPC сервер в отдельном потоке.
- Предоставляет методы для запуска, остановки и получения статуса серверов через XML-RPC.

**Методы**:
- `__init__(self, rpc_port=9000)`: Инициализирует XML-RPC сервер.
- `start_server(self, port: int, host: str)`: Запускает FastAPI сервер на указанном порту.
- `stop_server(self, port: int)`: Останавливает FastAPI сервер на указанном порту.
- `stop_all_servers(self)`: Останавливает все запущенные FastAPI сервера.
- `status_servers(self)`: Показывает статус серверов.
- `get_routes(self)`: Показывает все роуты.
- `add_new_route(self, path: str, module_name: str, func_name: str, methods: List[str] = ["GET"])`: Добавляет новый роут к серверу.
- `shutdown(self)`: Останавливает все сервера и завершает работу XML-RPC сервера.

**Параметры**:
- `rpc_port` (int): Порт для запуска XML-RPC сервера. По умолчанию `9000`.
- `port` (int): Порт для запуска FastAPI сервера.
- `host` (str): Хост для запуска FastAPI сервера.
- `path` (str): Путь для нового маршрута.
- `module_name` (str): Имя модуля, содержащего функцию для нового маршрута.
- `func_name` (str): Имя функции, которая будет обрабатывать запросы к новому маршруту.
- `methods` (List[str]): Список HTTP методов, которые поддерживает маршрут. По умолчанию `["GET"]`.

## Функции

### `telegram_webhook`

```python
def telegram_webhook():
    """"""
    return 'Hello, World!'
```

**Описание**: Пустая функция-заглушка для telegram webhook.

**Как работает функция**:
- Просто возвращает строку "Hello, World!".

**Возвращает**:
- `str`: Строка "Hello, World!".

### `test_function`

```python
def test_function():
    return "It is working!!!"
```

**Описание**: Тестовая функция, возвращающая строку "It is working!!!".

**Как работает функция**:
- Просто возвращает строку "It is working!!!".

**Возвращает**:
- `str`: Строка "It is working!!!".

### `test_post`

```python
def test_post(data: Dict[str, str]):
    return {"result": "post ok", "data": data}
```

**Описание**: Тестовая функция для обработки POST запросов.

**Как работает функция**:
- Принимает словарь `data` в качестве параметра.
- Возвращает словарь с результатом "post ok" и переданными данными.

**Параметры**:
- `data` (Dict[str, str]): Словарь с данными, переданными в POST запросе.

**Возвращает**:
- `dict`: Словарь с результатом "post ok" и переданными данными.

### `start_server`

```python
def start_server(port: int, host: str):
    """Запускает FastAPI сервер на указанном порту."""
    global _api_server_instance
    if _api_server_instance is None:
        _api_server_instance = FastApiServer(host=host)
    try:
      _api_server_instance.start(port=port)
    except Exception as ex:
      logger.error(f"Ошибка запуска FastAPI сервера на порту {port}:",ex, exc_info=True)
```

**Описание**: Запускает FastAPI сервер на указанном порту.

**Как работает функция**:
- Использует глобальную переменную `_api_server_instance` для хранения экземпляра `FastApiServer`.
- Если экземпляр не существует, создает новый.
- Запускает сервер на указанном порту с использованием метода `start` экземпляра `FastApiServer`.
- Логирует ошибки, если возникают при запуске сервера.

**Параметры**:
- `port` (int): Порт для запуска сервера.
- `host` (str): Хост для запуска сервера.

### `stop_server`

```python
def stop_server(port: int):
    """Останавливает FastAPI сервер на указанном порту."""
    global _api_server_instance
    if _api_server_instance:
        try:
            _api_server_instance.stop(port=port)
        except Exception as ex:
            logger.error(f"Ошибка остановки FastAPI сервера на порту {port}:",ex, exc_info=True)
```

**Описание**: Останавливает FastAPI сервер на указанном порту.

**Как работает функция**:
- Использует глобальную переменную `_api_server_instance` для доступа к экземпляру `FastApiServer`.
- Если экземпляр существует, останавливает сервер на указанном порту с использованием метода `stop` экземпляра `FastApiServer`.
- Логирует ошибки, если возникают при остановке сервера.

**Параметры**:
- `port` (int): Порт сервера для остановки.

### `stop_all_servers`

```python
def stop_all_servers():
    """Останавливает все запущенные FastAPI сервера."""
    global _api_server_instance
    if _api_server_instance:
      try:
        _api_server_instance.stop_all()
      except Exception as ex:
        logger.error(f"Ошибка остановки всех FastAPI серверов:",ex, exc_info=True)
```

**Описание**: Останавливает все запущенные FastAPI сервера.

**Как работает функция**:
- Использует глобальную переменную `_api_server_instance` для доступа к экземпляру `FastApiServer`.
- Если экземпляр существует, останавливает все сервера с использованием метода `stop_all` экземпляра `FastApiServer`.
- Логирует ошибки, если возникают при остановке серверов.

### `status_servers`

```python
def status_servers():
    """Показывает статус серверов."""
    global _api_server_instance
    if _api_server_instance:
        servers = _api_server_instance.get_servers_status()
        if servers:
            print(f"Server initialized on host {_api_server_instance.host}")
            for port, status in servers.items():
                print(f"  - Port {port}: {status}")
        else:
            print("No servers running")
    else:
        print("Server not initialized.")
```

**Описание**: Показывает статус всех запущенных FastAPI серверов.

**Как работает функция**:
- Использует глобальную переменную `_api_server_instance` для доступа к экземпляру `FastApiServer`.
- Если экземпляр существует, получает статус всех серверов с использованием метода `get_servers_status` экземпляра `FastApiServer`.
- Выводит информацию о статусе каждого сервера.

### `get_routes`

```python
def get_routes():
    """Показывает все роуты."""
    global _api_server_instance
    if _api_server_instance:
      routes = _api_server_instance.get_routes()
      if routes:
        print("Available routes:")
        for route in routes:
          print(f"  - Path: {route['path']}, Methods: {route['methods']}")
      else:
        print("No routes defined")
    else:
        print("Server not initialized.")
```

**Описание**: Показывает все зарегистрированные маршруты FastAPI сервера.

**Как работает функция**:
- Использует глобальную переменную `_api_server_instance` для доступа к экземпляру `FastApiServer`.
- Если экземпляр существует, получает список маршрутов с использованием метода `get_routes` экземпляра `FastApiServer`.
- Выводит информацию о каждом маршруте.

### `add_new_route`

```python
def add_new_route(path: str, module_name: str, func_name: str, methods: List[str] = ["GET"]):
    """Добавляет новый роут к серверу."""
    global _api_server_instance
    if _api_server_instance:
      try:
          _api_server_instance.add_new_route(path=path, module_name=module_name, func_name=func_name, methods=methods)
          print(f"Route added: {path}, {methods=}")
      except Exception as ex:
        logger.error(f"Ошибка добавления нового роута {path}:",ex, exc_info=True)
    else:
        print("Server not initialized. Start server first")
```

**Описание**: Добавляет новый маршрут к FastAPI серверу.

**Как работает функция**:
- Использует глобальную переменную `_api_server_instance` для доступа к экземпляру `FastApiServer`.
- Если экземпляр существует, добавляет новый маршрут с использованием метода `add_new_route` экземпляра `FastApiServer`.
- Логирует ошибки, если возникают при добавлении маршрута.

**Параметры**:
- `path` (str): Путь для нового маршрута.
- `module_name` (str): Имя модуля, содержащего функцию для нового маршрута.
- `func_name` (str): Имя функции, которая будет обрабатывать запросы к новому маршруту.
- `methods` (List[str]): Список HTTP методов, которые поддерживает маршрут. По умолчанию `["GET"]`.

### `parse_port_range`

```python
def parse_port_range(range_str):
    """Разбирает строку с диапазоном портов."""
    if not re.match(r'^[\d-]+$', range_str):
        print(f"Invalid port range: {range_str}")
        return []
    if '-' in range_str:
        try:
            start, end = map(int, range_str.split('-'))
            if start > end:
                raise ValueError("Invalid port range")
            return list(range(start, end + 1))
        except ValueError:
            print(f"Invalid port range: {range_str}")
            return []
    else:
        try:
            return [int(range_str)]
        except ValueError:
            print(f"Invalid port: {range_str}")
            return []
```

**Описание**: Разбирает строку с диапазоном портов.

**Как работает функция**:
- Проверяет, соответствует ли строка диапазону портов.
- Если строка содержит дефис, разделяет строку на начало и конец диапазона и возвращает список портов в этом диапазоне.
- Если строка не содержит дефис, пытается преобразовать строку в целое число и возвращает список, содержащий это число.
- Возвращает пустой список, если строка не соответствует диапазону портов или не может быть преобразована в целое число.

**Параметры**:
- `range_str` (str): Строка с диапазоном портов.

**Возвращает**:
- `list[int]`: Список портов.