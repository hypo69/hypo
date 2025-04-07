# Модуль FastAPI сервера с XML-RPC интерфейсом для удалённого управления
====================================================================

Модуль предоставляет FastAPI сервер с интерфейсом XML-RPC для удалённого управления.

## Обзор

Этот модуль реализует FastAPI сервер, который позволяет удалённо управлять им через XML-RPC. Он включает в себя функциональность для запуска и остановки серверов на различных портах, добавления новых маршрутов и получения статуса серверов.

## Подробнее

Модуль использует библиотеку `FastAPI` для создания веб-сервера и `xmlrpc.server` для реализации XML-RPC интерфейса. Конфигурация сервера, такая как хост и порты, загружается из файла `fast_api.json`.

## Классы

### `FastApiServer`

**Описание**: Класс, реализующий FastAPI сервер с поддержкой Singleton.

**Принцип работы**:
Класс `FastApiServer` является Singleton, что означает, что существует только один экземпляр этого класса. Он инициализирует FastAPI приложение, добавляет маршруты и предоставляет методы для запуска и остановки сервера.

**Атрибуты**:
- `_instance`: Приватный атрибут, хранящий единственный экземпляр класса.
- `app` (FastAPI): FastAPI приложение.
- `host` (str): Хост для запуска сервера (по умолчанию "127.0.0.1").
- `port` (int): Порт для запуска сервера (по умолчанию 8000).
- `router` (APIRouter): FastAPI роутер для добавления маршрутов.
- `server_tasks` (dict): Словарь для хранения задач сервера.
- `servers` (dict): Словарь для хранения запущенных серверов.
- `_initialized` (bool): Флаг, указывающий, был ли класс уже инициализирован.

**Методы**:
- `__new__(cls, *args, **kwargs)`: Создает новый экземпляр класса, если он еще не существует.
- `__init__(self, host: str = "127.0.0.1", title: str = "FastAPI RPC Server", **kwargs)`: Инициализирует экземпляр класса, добавляет маршруты `/hello` и `/post`.
- `add_route(self, path: str, func: Callable, methods: List[str] = ["GET"], **kwargs)`: Добавляет маршрут к FastAPI приложению.
- `_start_server(self, port: int)`: Запускает uvicorn сервер асинхронно.
- `start(self, port: int, as_thread: bool = True)`: Запускает FastAPI сервер на указанном порту.
- `stop(self, port: int)`: Останавливает FastAPI сервер на указанном порту.
- `stop_all(self)`: Останавливает все запущенные сервера.
- `get_servers_status(self)`: Возвращает статус всех серверов.
- `get_routes(self)`: Возвращает список всех роутов.
- `get_app(self)`: Возвращает FastAPI приложение.
- `add_new_route(self, path: str, module_name: str, func_name: str, methods: List[str] = ["GET"], **kwargs)`: Добавляет новый маршрут к уже работающему приложению.

### `CommandHandler`

**Описание**: Обработчик команд для FastAPI сервера через XML-RPC.

**Принцип работы**:
Класс `CommandHandler` предоставляет интерфейс для управления FastAPI сервером через XML-RPC. Он регистрирует методы для запуска, остановки, получения статуса серверов, а также для добавления новых маршрутов.

**Атрибуты**:
- `rpc_port` (int): Порт для запуска XML-RPC сервера (по умолчанию 9000).
- `rpc_server` (SimpleXMLRPCServer): Экземпляр XML-RPC сервера.

**Методы**:
- `__init__(self, rpc_port=9000)`: Инициализирует XML-RPC сервер и регистрирует экземпляр класса.
- `start_server(self, port: int, host: str)`: Запускает FastAPI сервер.
- `stop_server(self, port: int)`: Останавливает FastAPI сервер.
- `stop_all_servers(self)`: Останавливает все запущенные FastAPI сервера.
- `status_servers(self)`: Возвращает статус всех серверов.
- `get_routes(self)`: Возвращает список всех роутов.
- `add_new_route(self, path: str, module_name: str, func_name: str, methods: List[str] = ["GET"])`: Добавляет новый роут к серверу.
- `shutdown(self)`: Останавливает все сервера и завершает работу XML-RPC сервера.

## Функции

### `telegram_webhook`

```python
def telegram_webhook() -> str:
    """ """
    return 'Hello, World!'
```

**Назначение**:
Возвращает строку "Hello, World!".

**Параметры**:
- Нет параметров.

**Возвращает**:
- `str`: Строка "Hello, World!".

**Как работает функция**:
Функция просто возвращает статическую строку "Hello, World!".

```
Начало
↓
Возврат "Hello, World!"
↓
Конец
```

**Примеры**:

```python
result = telegram_webhook()
print(result)  # Вывод: Hello, World!
```

### `test_function`

```python
def test_function() -> str:
    """ """
    return "It is working!!!"
```

**Назначение**:
Возвращает строку "It is working!!!".

**Параметры**:
- Нет параметров.

**Возвращает**:
- `str`: Строка "It is working!!!".

**Как работает функция**:
Функция просто возвращает статическую строку "It is working!!!".

```
Начало
↓
Возврат "It is working!!!"
↓
Конец
```

**Примеры**:

```python
result = test_function()
print(result)  # Вывод: It is working!!!
```

### `test_post`

```python
def test_post(data: Dict[str, str]) -> Dict[str, str]:
    """ """
    return {"result": "post ok", "data": data}
```

**Назначение**:
Возвращает словарь с результатом "post ok" и переданными данными.

**Параметры**:
- `data` (Dict[str, str]): Словарь с данными.

**Возвращает**:
- `Dict[str, str]`: Словарь вида `{"result": "post ok", "data": data}`.

**Как работает функция**:
Функция принимает словарь `data` и возвращает новый словарь, содержащий результат "post ok" и переданные данные.

```
Начало
↓
Создание словаря {"result": "post ok", "data": data}
↓
Возврат словаря
↓
Конец
```

**Примеры**:

```python
data = {"key": "value"}
result = test_post(data)
print(result)  # Вывод: {'result': 'post ok', 'data': {'key': 'value'}}
```

### `start_server`

```python
def start_server(port: int, host: str) -> None:
    """Запускает FastAPI сервер на указанном порту."""
    global _api_server_instance
    if _api_server_instance is None:
        _api_server_instance = FastApiServer(host=host)
    try:
      _api_server_instance.start(port=port)
    except Exception as ex:
      logger.error(f"Ошибка запуска FastAPI сервера на порту {port}:",ex, exc_info=True)
```

**Назначение**:
Запускает FastAPI сервер на указанном порту.

**Параметры**:
- `port` (int): Порт для запуска сервера.
- `host` (str): Хост для запуска сервера.

**Как работает функция**:
1. Проверяет, инициализирован ли экземпляр `FastApiServer`. Если нет, создает новый экземпляр.
2. Запускает сервер на указанном порту, используя метод `start` экземпляра `FastApiServer`.
3. Логирует ошибку, если происходит исключение.

```
Начало
↓
Проверка _api_server_instance == None
| Да ↓
| Создание FastApiServer
↓
Запуск _api_server_instance.start(port)
↓
Конец
```

**Примеры**:

```python
start_server(port=8000, host="127.0.0.1")
```

### `stop_server`

```python
def stop_server(port: int) -> None:
    """Останавливает FastAPI сервер на указанном порту."""
    global _api_server_instance
    if _api_server_instance:
        try:
            _api_server_instance.stop(port=port)
        except Exception as ex:
            logger.error(f"Ошибка остановки FastAPI сервера на порту {port}:",ex, exc_info=True)
```

**Назначение**:
Останавливает FastAPI сервер на указанном порту.

**Параметры**:
- `port` (int): Порт сервера для остановки.

**Как работает функция**:
1. Проверяет, инициализирован ли экземпляр `FastApiServer`.
2. Останавливает сервер на указанном порту, используя метод `stop` экземпляра `FastApiServer`.
3. Логирует ошибку, если происходит исключение.

```
Начало
↓
Проверка _api_server_instance != None
| Да ↓
| Остановка _api_server_instance.stop(port)
↓
Конец
```

**Примеры**:

```python
stop_server(port=8000)
```

### `stop_all_servers`

```python
def stop_all_servers() -> None:
    """Останавливает все запущенные FastAPI сервера."""
    global _api_server_instance
    if _api_server_instance:
      try:
        _api_server_instance.stop_all()
      except Exception as ex:
        logger.error(f"Ошибка остановки всех FastAPI серверов:",ex, exc_info=True)
```

**Назначение**:
Останавливает все запущенные FastAPI сервера.

**Параметры**:
- Нет параметров.

**Как работает функция**:
1. Проверяет, инициализирован ли экземпляр `FastApiServer`.
2. Останавливает все сервера, используя метод `stop_all` экземпляра `FastApiServer`.
3. Логирует ошибку, если происходит исключение.

```
Начало
↓
Проверка _api_server_instance != None
| Да ↓
| Остановка _api_server_instance.stop_all()
↓
Конец
```

**Примеры**:

```python
stop_all_servers()
```

### `status_servers`

```python
def status_servers() -> None:
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

**Назначение**:
Выводит статус всех запущенных серверов.

**Параметры**:
- Нет параметров.

**Как работает функция**:
1. Проверяет, инициализирован ли экземпляр `FastApiServer`.
2. Получает статус серверов, используя метод `get_servers_status` экземпляра `FastApiServer`.
3. Выводит информацию о статусе каждого сервера.

```
Начало
↓
Проверка _api_server_instance != None
| Да ↓
| Получение статуса servers = _api_server_instance.get_servers_status()
↓
Вывод статуса серверов
↓
Конец
```

**Примеры**:

```python
status_servers()
```

### `get_routes`

```python
def get_routes() -> None:
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

**Назначение**:
Выводит список всех зарегистрированных маршрутов.

**Параметры**:
- Нет параметров.

**Как работает функция**:
1. Проверяет, инициализирован ли экземпляр `FastApiServer`.
2. Получает список маршрутов, используя метод `get_routes` экземпляра `FastApiServer`.
3. Выводит информацию о каждом маршруте.

```
Начало
↓
Проверка _api_server_instance != None
| Да ↓
| Получение маршрутов routes = _api_server_instance.get_routes()
↓
Вывод маршрутов
↓
Конец
```

**Примеры**:

```python
get_routes()
```

### `add_new_route`

```python
def add_new_route(path: str, module_name: str, func_name: str, methods: List[str] = ["GET"]) -> None:
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

**Назначение**:
Добавляет новый маршрут к серверу.

**Параметры**:
- `path` (str): Путь для нового маршрута.
- `module_name` (str): Имя модуля, содержащего функцию обработчика.
- `func_name` (str): Имя функции обработчика.
- `methods` (List[str]): Список HTTP методов для маршрута (по умолчанию `["GET"]`).

**Как работает функция**:
1. Проверяет, инициализирован ли экземпляр `FastApiServer`.
2. Добавляет новый маршрут, используя метод `add_new_route` экземпляра `FastApiServer`.
3. Логирует ошибку, если происходит исключение.

```
Начало
↓
Проверка _api_server_instance != None
| Да ↓
| Добавление маршрута _api_server_instance.add_new_route(path, module_name, func_name, methods)
↓
Конец
```

**Примеры**:

```python
add_new_route(path="/test", module_name="my_module", func_name="my_function")
```

### `parse_port_range`

```python
def parse_port_range(range_str: str) -> List[int]:
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

**Назначение**:
Разбирает строку с диапазоном портов.

**Параметры**:
- `range_str` (str): Строка, представляющая диапазон портов.

**Возвращает**:
- `List[int]`: Список портов в диапазоне.

**Как работает функция**:
1. Проверяет, соответствует ли строка диапазону портов.
2. Если строка содержит дефис, разбивает строку на начало и конец диапазона и возвращает список портов в этом диапазоне.
3. Если строка не содержит дефис, пытается преобразовать строку в целое число и возвращает список, содержащий только это число.
4. Возвращает пустой список, если строка не соответствует формату диапазона портов.

```
Начало
↓
Проверка формата range_str
| Не соответствует ↓
| Вывод ошибки и возврат []
↓
Проверка наличия '-' в range_str
| Да ↓          | Нет ↓
| Разбиение на start и end  | Попытка преобразования в int
| Проверка start > end   | Вывод ошибки и возврат [] при неудаче
| Возврат списка портов в диапазоне | Возврат списка с одним портом
↓
Конец
```

**Примеры**:

```python
print(parse_port_range("8000-8005"))  # Вывод: [8000, 8001, 8002, 8003, 8004, 8005]
print(parse_port_range("8000"))  # Вывод: [8000]
print(parse_port_range("invalid"))  # Вывод: []
```

### `display_menu`

```python
def display_menu() -> None:
    """Выводит меню с доступными командами."""
    print("\nAvailable commands:")
    print("  start <port>        - Start server on the specified port")
    print("  status              - Show all served ports status")
    print("  routes              - Show all registered routes")
    print("  stop <port>         - Stop server on the specified port")
    print("  stop_all            - Stop all servers")
    print("  add_route <path>    - Add a new route to the server")
    print("  shutdown            - Stop all servers and exit")
    print("  help                - Show this help menu")
    print("  exit                - Exit the program")
```

**Назначение**:
Выводит меню с доступными командами.

**Параметры**:
- Нет параметров.

**Как работает функция**:
Функция просто выводит список доступных команд в консоль.

```
Начало
↓
Вывод списка команд
↓
Конец
```

**Примеры**:

```python
display_menu()
```

### `main`

```python
def main() -> None:
    """Основная функция управления сервером."""
    command_handler = CommandHandler()
    while True:
        display_menu()
        try:
            command_line = input("Enter command: ").strip().lower()
            if not command_line:
                continue

            parts = command_line.split()
            command = parts[0]

            if command == "start":
                if len(parts) != 2:
                    print("Usage: start <port>")
                    continue
                try:
                    port = int(parts[1])
                    host = input("Enter host address (default: 127.0.0.1): ").strip() or "127.0.0.1"
                    command_handler.start_server(port=port, host=host)
                except ValueError:
                    print("Invalid port number.")
                except Exception as ex:
                    logger.error(f"An error occurred:", ex, exc_info=True)

            elif command == "status":
                command_handler.status_servers()

            elif command == "routes":
                command_handler.get_routes()
            
            elif command == "stop":
               if len(parts) != 2:
                   print("Usage: stop <port>")
                   continue
               try:
                    port = int(parts[1])
                    command_handler.stop_server(port=port)
               except ValueError:
                   print("Invalid port number.")
               except Exception as ex:
                  logger.error(f"An error occurred:", ex, exc_info=True)
            
            elif command == "stop_all":
               command_handler.stop_all_servers()
            
            elif command == "add_route":
                if len(parts) < 2:
                    print("Usage: add_route <path> <module_name> <func_name>")
                    continue
                path = parts[1]
                module_name = input("Enter module name: ").strip()
                func_name = input("Enter function name: ").strip()
                methods = input("Enter HTTP methods (comma-separated, default: GET): ").strip().upper() or "GET"
                methods = [method.strip() for method in methods.split(",")]
                command_handler.add_new_route(path=path, module_name=module_name, func_name=func_name, methods=methods)


            elif command == "shutdown":
                command_handler.shutdown()  # call shutdown method on command_handler

            elif command == "help":
                display_menu()

            elif command == "exit":
                print("Exiting the program.")
                sys.exit(0)
            
            else:
                print("Unknown command. Type \'help\' to see the list of available commands")

        except Exception as ex:
            logger.error(f"An error occurred:", ex, exc_info=True)
```

**Назначение**:
Основная функция управления сервером.

**Как работает функция**:
1. Создает экземпляр `CommandHandler`.
2. В бесконечном цикле:
    - Выводит меню доступных команд.
    - Считывает команду пользователя.
    - Выполняет соответствующую команду, используя методы `CommandHandler`.
    - Обрабатывает возможные исключения.

```
Начало
↓
Создание CommandHandler
↓
Цикл:
    ↓
    Вывод меню
    ↓
    Считывание команды
    ↓
    Разбор команды
    ↓
    Выполнение команды через CommandHandler
    ↓
Конец (при команде "exit")
```

**Внутренние функции**:
В данной функции не используются внутренние функции.

**Примеры**:
Запуск сервера:

```
Enter command: start 8000
Enter host address (default: 127.0.0.1): 
```

Остановка сервера:

```
Enter command: stop 8000
```

## Переменные

- `config` (SimpleNamespace): Конфигурация, загруженная из `fast_api.json`.
- `_api_server_instance`: Глобальная переменная, хранящая экземпляр `FastApiServer`.