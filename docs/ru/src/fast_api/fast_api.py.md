# Модуль FastAPI сервера с XML-RPC интерфейсом для удалённого управления

## Обзор

Модуль предоставляет FastAPI сервер с интерфейсом XML-RPC для удалённого управления. Он позволяет запускать и останавливать серверы на указанных портах, добавлять новые маршруты, просматривать статус серверов и зарегистрированные маршруты.

## Подробнее

Этот модуль реализует FastAPI сервер, который может управляться удаленно через XML-RPC. Он использует библиотеку `uvicorn` для запуска асинхронного сервера и предоставляет API для управления сервером через командную строку или XML-RPC.

## Классы

### `FastApiServer`

**Описание**:
Класс `FastApiServer` реализует FastAPI сервер с поддержкой Singleton.

**Как работает класс**:
Класс `FastApiServer` является Singleton, что означает, что существует только один экземпляр этого класса. Он инициализирует FastAPI приложение, добавляет маршруты и предоставляет методы для запуска и остановки сервера.

- `_instance`: Приватный атрибут класса, хранящий единственный экземпляр класса.
- `app`: Экземпляр FastAPI приложения.
- `host`: Хост, на котором будет запущен сервер. По умолчанию берется из конфигурационного файла.
- `port`: Порт, на котором будет запущен сервер. По умолчанию 8000.
- `router`: APIRouter для добавления маршрутов.

**Методы**:

- `__new__(cls, *args, **kwargs)`:
    - Проверяет, существует ли уже экземпляр класса. Если нет, создает новый экземпляр и сохраняет его в `_instance`.
    - Возвращает существующий экземпляр класса, если он уже создан.

- `__init__(self, host: str = "127.0.0.1", title: str = "FastAPI RPC Server", **kwargs)`:
    - Инициализирует экземпляр класса `FastApiServer`.
    - Проверяет, был ли уже инициализирован экземпляр, чтобы избежать повторной инициализации.
    - Добавляет маршруты `/hello` и `/post` к FastAPI приложению.
    - Инициализирует FastAPI приложение, хост, словарь задач сервера и словарь серверов.
    - Включает маршрутизатор в FastAPI приложение.

- `add_route(self, path: str, func: Callable, methods: List[str] = ["GET"], **kwargs)`:
    - Добавляет маршрут к FastAPI приложению.
    - `path` (str): Путь маршрута.
    - `func` (Callable): Функция, которая будет выполняться при запросе к маршруту.
    - `methods` (List[str]): Список HTTP методов, которые поддерживает маршрут. По умолчанию `["GET"]`.
    - `**kwargs`: Дополнительные аргументы, которые будут переданы в `router.add_api_route`.

- `_start_server(self, port: int)`:
    - Запускает uvicorn сервер асинхронно.
    - `port` (int): Порт, на котором будет запущен сервер.
    - Создает конфигурацию uvicorn сервера с указанным хостом, портом и уровнем логирования.
    - Запускает uvicorn сервер.
    - В случае ошибки логирует ее и удаляет сервер из словаря серверов.

- `start(self, port: int, as_thread: bool = True)`:
    - Запускает FastAPI сервер на указанном порту.
    - `port` (int): Порт, на котором будет запущен сервер.
    - `as_thread` (bool): Флаг, указывающий, запускать ли сервер в отдельном потоке. По умолчанию `True`.
    - Проверяет, запущен ли уже сервер на указанном порту.
    - Создает и запускает поток для запуска асинхронного сервера.

- `stop(self, port: int)`:
    - Останавливает FastAPI сервер на указанном порту.
    - `port` (int): Порт, на котором нужно остановить сервер.
    - Проверяет, запущен ли сервер на указанном порту.
    - Останавливает поток сервера и удаляет сервер из словаря серверов.
    - В случае ошибки логирует ее.

- `stop_all(self)`:
    - Останавливает все запущенные сервера.
    - Перебирает все порты в словаре серверов и останавливает каждый сервер.

- `get_servers_status(self)`:
    - Возвращает статус всех серверов.
    - Возвращает словарь, где ключ - порт, а значение - статус сервера ("Running" или "Stopped").

- `get_routes(self)`:
    - Возвращает список всех роутов.
    - Проходит по всем маршрутам в приложении и возвращает список словарей с информацией о каждом маршруте (путь и методы).

- `get_app(self)`:
    - Возвращает FastAPI приложение.
    - Позволяет получить доступ к FastAPI приложению для дальнейшей настройки или использования.

- `add_new_route(self, path: str, module_name: str, func_name: str, methods: List[str] = ["GET"], **kwargs)`:
    - Добавляет новый маршрут к уже работающему приложению.
    - `path` (str): Путь маршрута.
    - `module_name` (str): Имя модуля, содержащего функцию для маршрута.
    - `func_name` (str): Имя функции, которая будет обрабатывать запросы к маршруту.
    - `methods` (List[str]): Список HTTP методов, которые поддерживает маршрут. По умолчанию `["GET"]`.
    - `**kwargs`: Дополнительные аргументы, которые будут переданы в функцию маршрута.
    - Динамически импортирует модуль и получает функцию из модуля.
    - Добавляет маршрут к FastAPI приложению.

### `CommandHandler`

**Описание**:
Класс `CommandHandler` обрабатывает команды для FastAPI сервера через XML-RPC.

**Как работает класс**:
Класс `CommandHandler` предоставляет интерфейс XML-RPC для управления FastAPI сервером. Он позволяет запускать и останавливать серверы, просматривать статус серверов и зарегистрированные маршруты.

**Методы**:

- `__init__(self, rpc_port=9000)`:
    - Инициализирует обработчик команд.
    - `rpc_port` (int): Порт, на котором будет запущен XML-RPC сервер. По умолчанию 9000.
    - Создает XML-RPC сервер и регистрирует экземпляр класса `CommandHandler` для обработки запросов.
    - Запускает XML-RPC сервер в отдельном потоке.

- `start_server(self, port: int, host: str)`:
    - Запускает FastAPI сервер на указанном порту и хосте.
    - `port` (int): Порт, на котором будет запущен сервер.
    - `host` (str): Хост, на котором будет запущен сервер.
    - Вызывает функцию `start_server` для запуска сервера.

- `stop_server(self, port: int)`:
    - Останавливает FastAPI сервер на указанном порту.
    - `port` (int): Порт, на котором нужно остановить сервер.
    - Вызывает функцию `stop_server` для остановки сервера.

- `stop_all_servers(self)`:
    - Останавливает все запущенные FastAPI сервера.
    - Вызывает функцию `stop_all_servers` для остановки всех серверов.

- `status_servers(self)`:
    - Показывает статус серверов.
    - Вызывает функцию `status_servers` для получения и отображения статуса серверов.

- `get_routes(self)`:
    - Показывает все роуты.
    - Вызывает функцию `get_routes` для получения и отображения всех роутов.

- `add_new_route(self, path: str, module_name: str, func_name: str, methods: List[str] = ["GET"])`:
    - Добавляет новый роут к серверу.
    - `path` (str): Путь для нового роута.
    - `module_name` (str): Имя модуля, содержащего функцию для обработки роута.
    - `func_name` (str): Имя функции, которая будет обрабатывать роут.
    - `methods` (List[str]): Список HTTP методов, поддерживаемых роутом.
    - Вызывает функцию `add_new_route` для добавления нового роута.

- `shutdown(self)`:
    - Останавливает все серверы и выключает RPC сервер.
    - Вызывает `stop_all_servers` для остановки всех FastAPI серверов.
    - Вызывает `rpc_server.shutdown()` для остановки XML-RPC сервера.
    - Завершает работу программы.

## Функции

### `telegram_webhook()`

```python
def telegram_webhook():
    """"""
    return 'Hello, World!'
```

**Назначение**:
Функция `telegram_webhook` предназначена для обработки webhook запросов от Telegram. В текущей реализации она возвращает строку 'Hello, World!'.

**Как работает функция**:
Функция просто возвращает строку 'Hello, World!'. Она не выполняет никаких других действий.

**Возвращает**:
- `str`: Возвращает строку 'Hello, World!'.

### `test_function()`

```python
def test_function():
    return "It is working!!!"
```

**Назначение**:
Функция `test_function` предназначена для тестирования доступности сервера.

**Как работает функция**:
Функция просто возвращает строку "It is working!!!".

**Возвращает**:
- `str`: Возвращает строку "It is working!!!".

### `test_post(data: Dict[str, str])`

```python
def test_post(data: Dict[str, str]):
    return {"result": "post ok", "data": data}
```

**Назначение**:
Функция `test_post` предназначена для обработки POST запросов и возврата результата.

**Как работает функция**:
Функция принимает словарь `data` в качестве аргумента и возвращает словарь, содержащий результат "post ok" и переданные данные.

**Параметры**:
- `data` (Dict[str, str]): Словарь с данными, переданными в POST запросе.

**Возвращает**:
- `dict`: Возвращает словарь с результатом "post ok" и переданными данными.

### `start_server(port: int, host: str)`

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

**Назначение**:
Функция `start_server` запускает FastAPI сервер на указанном порту.

**Как работает функция**:
Функция сначала проверяет, инициализирован ли уже экземпляр `FastApiServer`. Если нет, она создает новый экземпляр. Затем она вызывает метод `start` экземпляра `FastApiServer` для запуска сервера на указанном порту.

**Параметры**:
- `port` (int): Порт, на котором будет запущен сервер.
- `host` (str): Хост, на котором будет запущен сервер.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при запуске FastAPI сервера.

### `stop_server(port: int)`

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

**Назначение**:
Функция `stop_server` останавливает FastAPI сервер на указанном порту.

**Как работает функция**:
Функция проверяет, инициализирован ли экземпляр `FastApiServer`. Если да, она вызывает метод `stop` экземпляра `FastApiServer` для остановки сервера на указанном порту.

**Параметры**:
- `port` (int): Порт, на котором нужно остановить сервер.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при остановке FastAPI сервера.

### `stop_all_servers()`

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

**Назначение**:
Функция `stop_all_servers` останавливает все запущенные FastAPI сервера.

**Как работает функция**:
Функция проверяет, инициализирован ли экземпляр `FastApiServer`. Если да, она вызывает метод `stop_all` экземпляра `FastApiServer` для остановки всех серверов.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при остановке всех FastAPI серверов.

### `status_servers()`

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

**Назначение**:
Функция `status_servers` показывает статус серверов.

**Как работает функция**:
Функция проверяет, инициализирован ли экземпляр `FastApiServer`. Если да, она вызывает метод `get_servers_status` экземпляра `FastApiServer` для получения статуса серверов и выводит информацию о статусе каждого сервера.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при получении статуса серверов.

### `get_routes()`

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

**Назначение**:
Функция `get_routes` показывает все роуты.

**Как работает функция**:
Функция проверяет, инициализирован ли экземпляр `FastApiServer`. Если да, она вызывает метод `get_routes` экземпляра `FastApiServer` для получения списка роутов и выводит информацию о каждом роуте.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при получении списка роутов.

### `add_new_route(path: str, module_name: str, func_name: str, methods: List[str] = ["GET"])`

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

**Назначение**:
Функция `add_new_route` добавляет новый роут к серверу.

**Как работает функция**:
Функция проверяет, инициализирован ли экземпляр `FastApiServer`. Если да, она вызывает метод `add_new_route` экземпляра `FastApiServer` для добавления нового роута с указанными параметрами.

**Параметры**:
- `path` (str): Путь для нового роута.
- `module_name` (str): Имя модуля, содержащего функцию для обработки роута.
- `func_name` (str): Имя функции, которая будет обрабатывать роут.
- `methods` (List[str]): Список HTTP методов, поддерживаемых роутом.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при добавлении нового роута.

### `parse_port_range(range_str)`

```python
def parse_port_range(range_str):
    """Разбирает строку с диапазоном портов."""
    if not re.match(r'^[\\d-]+$', range_str):
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
Функция `parse_port_range` разбирает строку с диапазоном портов.

**Как работает функция**:
Функция принимает строку `range_str` в качестве аргумента и пытается разобрать ее как диапазон портов. Если строка содержит дефис (`-`), она разделяет строку на начало и конец диапазона и возвращает список всех портов в диапазоне. Если строка не содержит дефис, она пытается преобразовать строку в целое число и возвращает список, содержащий только это число.

**Параметры**:
- `range_str` (str): Строка с диапазоном портов.

**Возвращает**:
- `List[int]`: Возвращает список портов.

### `display_menu()`

```python
def display_menu():
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
Функция `display_menu` выводит меню с доступными командами.

**Как работает функция**:
Функция просто выводит список доступных команд в консоль.

### `main()`

```python
def main():
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
                print("Unknown command. Type 'help' to see the list of available commands")

        except Exception as ex:
            logger.error(f"An error occurred:", ex, exc_info=True)
```

**Назначение**:
Функция `main` является основной функцией управления сервером.

**Как работает функция**:
Функция создает экземпляр `CommandHandler`, который используется для обработки команд. Она входит в бесконечный цикл, в котором выводит меню доступных команд, принимает команду от пользователя и выполняет соответствующее действие.

**Логика работы цикла**:
1. **Отображение меню**: Вызывается функция `display_menu()` для отображения доступных команд.
2. **Ввод команды**: Пользователь вводит команду, которая затем обрабатывается.
3. **Обработка команды**:
   - Команда разбивается на части, и определяется основная команда.
   - В зависимости от команды выполняются различные действия:
     - `start`: Запускает сервер на указанном порту.
     - `status`: Отображает статус всех серверов.
     - `routes`: Отображает все зарегистрированные маршруты.
     - `stop`: Останавливает сервер на указанном порту.
     - `stop_all`: Останавливает все запущенные серверы.
     - `add_route`: Добавляет новый маршрут к серверу.
     - `shutdown`: Останавливает все серверы и завершает работу программы.
     - `help`: Отображает меню с доступными командами.
     - `exit`: Завершает работу программы.
   - В случае возникновения ошибки выводится сообщение об ошибке.