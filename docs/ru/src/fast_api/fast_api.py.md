# Модуль `fast_api`
## Обзор

Модуль `fast_api` предоставляет реализацию FastAPI сервера с интерфейсом XML-RPC для удаленного управления. Он позволяет запускать, останавливать и управлять серверами FastAPI через командную строку или XML-RPC.

## Подробней

Этот модуль предоставляет возможность удаленного управления FastAPI сервером через XML-RPC интерфейс. Он использует библиотеку `uvicorn` для запуска FastAPI приложения асинхронно. Основные компоненты модуля включают:

- Загрузка конфигурации из файла `fast_api.json`.
- Класс `FastApiServer`, реализующий Singleton для управления сервером FastAPI.
- Функции для запуска, остановки и получения статуса серверов FastAPI.
- Обработчик команд `CommandHandler` для управления сервером через XML-RPC.
- Функция `main` для обработки команд из командной строки.

## Классы

### `FastApiServer`

**Описание**: Класс `FastApiServer` реализует Singleton паттерн для управления FastAPI сервером.

**Наследует**:
- Не наследует никаких классов.

**Атрибуты**:
- `_instance`: Приватный атрибут, хранящий единственный экземпляр класса.
- `app` (FastAPI): Экземпляр FastAPI приложения.
- `host` (str): Хост для запуска сервера (по умолчанию "127.0.0.1").
- `port` (int): Порт для запуска сервера (по умолчанию 8000).
- `router` (APIRouter): Экземпляр APIRouter для добавления маршрутов.
- `server_tasks` (dict): Словарь для хранения задач серверов.
- `servers` (dict): Словарь для хранения запущенных серверов.

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

**Описание**: Обработчик команд для управления FastAPI сервером через XML-RPC.

**Наследует**:
- Не наследует никаких классов.

**Атрибуты**:
- `rpc_port` (int): Порт для запуска XML-RPC сервера (по умолчанию 9000).
- `rpc_server` (SimpleXMLRPCServer): Экземпляр XML-RPC сервера.

**Методы**:
- `__init__(self, rpc_port=9000)`: Инициализирует экземпляр класса, запускает XML-RPC сервер в отдельном потоке.
- `start_server(self, port: int, host: str)`: Запускает FastAPI сервер на указанном порту и хосте.
- `stop_server(self, port: int)`: Останавливает FastAPI сервер на указанном порту.
- `stop_all_servers(self)`: Останавливает все запущенные FastAPI сервера.
- `status_servers(self)`: Выводит статус всех серверов.
- `get_routes(self)`: Выводит список всех роутов.
- `add_new_route(self, path: str, module_name: str, func_name: str, methods: List[str] = ["GET"])`: Добавляет новый роут к серверу.
- `shutdown(self)`: Останавливает все сервера и завершает работу XML-RPC сервера.

## Функции

### `telegram_webhook`

```python
def telegram_webhook():
    """"""
    return 'Hello, World!'
```

**Назначение**: Возвращает строку "Hello, World!".

**Параметры**:
- Нет параметров.

**Возвращает**:
- `str`: Строка "Hello, World!".

**Как работает функция**:
1. Функция просто возвращает строку 'Hello, World!'.

**Примеры**:
```python
>>> telegram_webhook()
'Hello, World!'
```

### `test_function`

```python
def test_function():
    return "It is working!!!"
```

**Назначение**: Возвращает строку "It is working!!!".

**Параметры**:
- Нет параметров.

**Возвращает**:
- `str`: Строка "It is working!!!".

**Как работает функция**:
1. Функция просто возвращает строку 'It is working!!!'.

**Примеры**:
```python
>>> test_function()
'It is working!!!'
```

### `test_post`

```python
def test_post(data: Dict[str, str]):
    return {"result": "post ok", "data": data}
```

**Назначение**: Возвращает словарь с результатом "post ok" и переданными данными.

**Параметры**:
- `data` (Dict[str, str]): Словарь с данными для возврата.

**Возвращает**:
- `dict`: Словарь с ключами "result" и "data".

**Как работает функция**:
1. Функция принимает словарь `data` в качестве аргумента.
2. Функция возвращает новый словарь, содержащий ключ "result" со значением "post ok" и ключ "data" со значением переданного словаря `data`.

**Примеры**:
```python
>>> test_post({"key": "value"})
{'result': 'post ok', 'data': {'key': 'value'}}
```

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

**Назначение**: Запускает FastAPI сервер на указанном порту и хосте.

**Параметры**:
- `port` (int): Порт для запуска сервера.
- `host` (str): Хост для запуска сервера.

**Как работает функция**:

```
A: Проверка инициализации сервера
|
B: Создание экземпляра FastApiServer (если не создан)
|
C: Запуск сервера на указанном порту
|
D: Обработка исключений и логирование ошибок
```

1. Функция проверяет, инициализирован ли уже экземпляр `FastApiServer`.
2. Если экземпляр не инициализирован, создается новый экземпляр `FastApiServer` с указанным хостом.
3. Функция пытается запустить сервер на указанном порту.
4. Если во время запуска возникает исключение, оно логируется.

**Примеры**:
```python
start_server(port=8000, host="127.0.0.1")
```

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

**Назначение**: Останавливает FastAPI сервер на указанном порту.

**Параметры**:
- `port` (int): Порт сервера для остановки.

**Как работает функция**:

```
A: Проверка инициализации сервера
|
B: Остановка сервера на указанном порту
|
C: Обработка исключений и логирование ошибок
```

1. Функция проверяет, инициализирован ли экземпляр `FastApiServer`.
2. Если экземпляр инициализирован, функция пытается остановить сервер на указанном порту.
3. Если во время остановки возникает исключение, оно логируется.

**Примеры**:
```python
stop_server(port=8000)
```

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

**Назначение**: Останавливает все запущенные FastAPI сервера.

**Параметры**:
- Нет параметров.

**Как работает функция**:

```
A: Проверка инициализации сервера
|
B: Остановка всех серверов
|
C: Обработка исключений и логирование ошибок
```

1. Функция проверяет, инициализирован ли экземпляр `FastApiServer`.
2. Если экземпляр инициализирован, функция пытается остановить все запущенные сервера.
3. Если во время остановки возникает исключение, оно логируется.

**Примеры**:
```python
stop_all_servers()
```

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

**Назначение**: Выводит статус всех серверов.

**Параметры**:
- Нет параметров.

**Как работает функция**:

```
A: Проверка инициализации сервера
|
B: Получение статуса серверов
|
C: Вывод статуса серверов
```

1. Функция проверяет, инициализирован ли экземпляр `FastApiServer`.
2. Если экземпляр инициализирован, функция получает статус всех серверов.
3. Если есть работающие сервера, выводится их статус.
4. Если сервера не запущены, выводится соответствующее сообщение.

**Примеры**:
```python
status_servers()
```

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

**Назначение**: Выводит список всех доступных маршрутов FastAPI приложения.

**Параметры**:
- Нет параметров.

**Как работает функция**:

```
A: Проверка инициализации сервера
|
B: Получение списка роутов
|
C: Вывод списка роутов
```

1. Функция проверяет, инициализирован ли экземпляр `FastApiServer`.
2. Если экземпляр инициализирован, функция получает список всех маршрутов.
3. Если маршруты найдены, выводится их список.
4. Если маршруты не определены, выводится соответствующее сообщение.

**Примеры**:
```python
get_routes()
```

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

**Назначение**: Добавляет новый маршрут к FastAPI приложению.

**Параметры**:
- `path` (str): Путь для нового маршрута.
- `module_name` (str): Имя модуля, содержащего функцию для маршрута.
- `func_name` (str): Имя функции, которая будет обрабатывать запросы к маршруту.
- `methods` (List[str]): Список HTTP методов, поддерживаемых маршрутом (по умолчанию ["GET"]).

**Как работает функция**:

```
A: Проверка инициализации сервера
|
B: Добавление нового роута
|
C: Обработка исключений и логирование ошибок
```

1. Функция проверяет, инициализирован ли экземпляр `FastApiServer`.
2. Если экземпляр инициализирован, функция пытается добавить новый маршрут с указанными параметрами.
3. Если во время добавления возникает исключение, оно логируется.

**Примеры**:
```python
add_new_route(path="/test", module_name="my_module", func_name="my_function")
```

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

**Назначение**: Разбирает строку с диапазоном портов и возвращает список портов.

**Параметры**:
- `range_str` (str): Строка с диапазоном портов (например, "8000-8005" или "8000").

**Возвращает**:
- `list`: Список целых чисел, представляющих порты. Возвращает пустой список, если строка содержит недопустимый диапазон.

**Как работает функция**:

```
A: Проверка строки на соответствие шаблону диапазона портов
|
B: Разбор строки на начало и конец диапазона (если есть)
|
C: Преобразование диапазона в список портов
|
D: Обработка исключений и возврат списка портов
```

1. Функция проверяет, соответствует ли входная строка шаблону диапазона портов (только цифры и дефис).
2. Если строка содержит дефис, она разделяется на начало и конец диапазона, и генерируется список портов в этом диапазоне.
3. Если строка не содержит дефис, она преобразуется в целое число и возвращается список, содержащий только этот порт.
4. Если во время разбора возникает исключение, оно обрабатывается, и возвращается пустой список.

**Примеры**:
```python
>>> parse_port_range("8000-8005")
[8000, 8001, 8002, 8003, 8004, 8005]

>>> parse_port_range("8000")
[8000]

>>> parse_port_range("invalid")
[]
```

### `display_menu`

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

**Назначение**: Выводит меню с доступными командами для управления сервером.

**Параметры**:
- Нет параметров.

**Как работает функция**:
1. Функция выводит на экран список доступных команд и их описание.

**Примеры**:
```python
display_menu()
```

### `main`

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

**Назначение**: Основная функция управления сервером, обрабатывает команды из командной строки.

**Параметры**:
- Нет параметров.

**Как работает функция**:

```
A: Инициализация обработчика команд CommandHandler
|
B: Бесконечный цикл обработки команд
|
C: Вывод меню доступных команд
|
D: Получение команды от пользователя
|
E: Разбор команды и вызов соответствующих методов CommandHandler
|
F: Обработка исключений и логирование ошибок
```

1. Функция инициализирует обработчик команд `CommandHandler`.
2. Функция входит в бесконечный цикл, в котором:
   - Выводит меню доступных команд.
   - Получает команду от пользователя.
   - Разбирает команду и вызывает соответствующие методы `CommandHandler` для выполнения команды.
   - Обрабатывает возможные исключения и логирует ошибки.

**Примеры**:
```python
main()
```