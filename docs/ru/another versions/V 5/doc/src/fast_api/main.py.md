# Модуль управления параметрами Fast API сервера

## Обзор

Модуль `main.py` предоставляет интерфейс командной строки для управления Fast API сервером. Он позволяет запускать, останавливать, просматривать статус и добавлять новые маршруты к серверу.

## Подробней

Этот модуль является точкой входа для управления Fast API сервером. Он предоставляет пользователю набор команд для взаимодействия с сервером через командную строку. Основная логика модуля заключается в обработке ввода пользователя и вызове соответствующих методов класса `CommandHandler` для выполнения операций с сервером. Модуль использует функции `display_menu` для отображения доступных команд и `main` для обработки ввода пользователя и выполнения команд.

## Функции

### `display_menu`

```python
def display_menu():
    """Выводит меню с доступными командами."""
```

**Как работает функция**:
Функция `display_menu` отвечает за вывод списка доступных команд, которые пользователь может ввести для управления сервером. Каждая команда сопровождается кратким описанием ее назначения.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Примеры**:

```
>>> display_menu()
Available commands:
  start <port>        - Start server on the specified port
  status              - Show all served ports status
  routes              - Show all registered routes
  stop <port>         - Stop server on the specified port
  stop_all            - Stop all servers
  add_route <path>    - Add a new route to the server
  shutdown            - Stop all servers and exit
  help                - Show this help menu
  exit                - Exit the program
```

### `main`

```python
def main():
    """Основная функция управления сервером."""
```

**Как работает функция**:
Функция `main` является основной точкой входа в программу. Она создает экземпляр класса `CommandHandler`, который используется для управления сервером. Функция входит в бесконечный цикл, в котором отображает меню доступных команд, принимает ввод пользователя, анализирует его и выполняет соответствующие действия. Обработка команд включает запуск и остановку серверов, отображение статуса и маршрутов, а также добавление новых маршрутов. Функция также обрабатывает исключения, которые могут возникнуть в процессе выполнения команд, и регистрирует ошибки с использованием модуля `logger`.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Вызывает исключения**:
- `ValueError`: Если введен некорректный номер порта.
- `Exception`: При возникновении других ошибок в процессе выполнения команд.

**Примеры**:

```
>>> main()
Available commands:
  start <port>        - Start server on the specified port
  status              - Show all served ports status
  routes              - Show all registered routes
  stop <port>         - Stop server on the specified port
  stop_all            - Stop all servers
  add_route <path>    - Add a new route to the server
  shutdown            - Stop all servers and exit
  help                - Show this help menu
  exit                - Exit the program
Enter command: start 8000
Enter host address (default: 127.0.0.1): 
Starting server on port 8000 and host 127.0.0.1...
```
```
>>> main()
Available commands:
  start <port>        - Start server on the specified port
  status              - Show all served ports status
  routes              - Show all registered routes
  stop <port>         - Stop server on the specified port
  stop_all            - Stop all servers
  add_route <path>    - Add a new route to the server
  shutdown            - Stop all servers and exit
  help                - Show this help menu
Enter command: add_route /test
Enter HTTP methods (comma-separated, default: GET): POST,PUT
Adding route /test with methods ['POST', 'PUT']...
```
```
>>> main()
Available commands:
  start <port>        - Start server on the specified port
  status              - Show all served ports status
  routes              - Show all registered routes
  stop <port>         - Stop server on the specified port
  stop_all            - Stop all servers
  add_route <path>    - Add a new route to the server
  shutdown            - Stop all servers and exit
  help                - Show this help menu
Enter command: stop_all
Stopping all servers...
```
```
>>> main()
Available commands:
  start <port>        - Start server on the specified port
  status              - Show all served ports status
  routes              - Show all registered routes
  stop <port>         - Stop server on the specified port
  stop_all            - Stop all servers
  add_route <path>    - Add a new route to the server
  shutdown            - Stop all servers and exit
  help                - Show this help menu
Enter command: shutdown
Stopping all servers...
Shutting down all servers.
```
```
>>> main()
Available commands:
  start <port>        - Start server on the specified port
  status              - Show all served ports status
  routes              - Show all registered routes
  stop <port>         - Stop server on the specified port
  stop_all            - Stop all servers
  add_route <path>    - Add a new route to the server
  shutdown            - Stop all servers and exit
  help                - Show this help menu
Enter command: exit
Exiting the program.
```
```
>>> main()
Available commands:
  start <port>        - Start server on the specified port
  status              - Show all served ports status
  routes              - Show all registered routes
  stop <port>         - Stop server on the specified port
  stop_all            - Stop all servers
  add_route <path>    - Add a new route to the server
  shutdown            - Stop all servers and exit
  help                - Show this help menu
Enter command: status
All served ports status:
```
```
>>> main()
Available commands:
  start <port>        - Start server on the specified port
  status              - Show all served ports status
  routes              - Show all registered routes
  stop <port>         - Stop server on the specified port
  stop_all            - Stop all servers
  add_route <path>    - Add a new route to the server
  shutdown            - Stop all servers and exit
  help                - Show this help menu
Enter command: routes
All registered routes:
```
```
>>> main()
Available commands:
  start <port>        - Start server on the specified port
  status              - Show all served ports status
  routes              - Show all registered routes
  stop <port>         - Stop server on the specified port
  stop_all            - Stop all servers
  add_route <path>    - Add a new route to the server
  shutdown            - Stop all servers and exit
  help                - Show this help menu
Enter command: help
Available commands:
  start <port>        - Start server on the specified port
  status              - Show all served ports status
  routes              - Show all registered routes
  stop <port>         - Stop server on the specified port
  stop_all            - Stop all servers
  add_route <path>    - Add a new route to the server
  shutdown            - Stop all servers and exit
  help                - Show this help menu
  exit                - Exit the program
```
```
>>> main()
Available commands:
  start <port>        - Start server on the specified port
  status              - Show all served ports status
  routes              - Show all registered routes
  stop <port>         - Stop server on the specified port
  stop_all            - Stop all servers
  add_route <path>    - Add a new route to the server
  shutdown            - Stop all servers and exit
  help                - Show this help menu
Enter command: stop 8000
Stopping server on port 8000...
```
```
>>> main()
Available commands:
  start <port>        - Start server on the specified port
  status              - Show all served ports status
  routes              - Show all registered routes
  stop <port>         - Stop server on the specified port
  stop_all            - Stop all servers
  add_route <path>    - Add a new route to the server
  shutdown            - Stop all servers and exit
  help                - Show this help menu
Enter command: somecommand
Unknown command. Type 'help' to see the list of available commands
```
```
>>> main()
Available commands:
  start <port>        - Start server on the specified port
  status              - Show all served ports status
  routes              - Show all registered routes
  stop <port>         - Stop server on the specified port
  stop_all            - Stop all servers
  add_route <path>    - Add a new route to the server
  shutdown            - Stop all servers and exit
  help                - Show this help menu
Enter command: start test
Invalid port number.
```
```
>>> main()
Available commands:
  start <port>        - Start server on the specified port
  status              - Show all served ports status
  routes              - Show all registered routes
  stop <port>         - Stop server on the specified port
  stop_all            - Stop all servers
  add_route <path>    - Add a new route to the server
  shutdown            - Stop all servers and exit
  help                - Show this help menu
Enter command: stop test
Invalid port number.
```
```
>>> main()
Available commands:
  start <port>        - Start server on the specified port
  status              - Show all served ports status
  routes              - Show all registered routes
  stop <port>         - Stop server on the specified port
  stop_all            - Stop all servers
  add_route <path>    - Add a new route to the server
  shutdown            - Stop all servers and exit
  help                - Show this help menu
Enter command: add_route
Usage: add_route <path>
```
```
>>> main()
Available commands:
  start <port>        - Start server on the specified port
  status              - Show all served ports status
  routes              - Show all registered routes
  stop <port>         - Stop server on the specified port
  stop_all            - Stop all servers
  add_route <path>    - Add a new route to the server
  shutdown            - Stop all servers and exit
  help                - Show this help menu
Enter command: start
Usage: start <port>
```
```
>>> main()
Available commands:
  start <port>        - Start server on the specified port
  status              - Show all served ports status
  routes              - Show all registered routes
  stop <port>         - Stop server on the specified port
  stop_all            - Stop all servers
  add_route <path>    - Add a new route to the server
  shutdown            - Stop all servers and exit
  help                - Show this help menu
Enter command: stop
Usage: stop <port>
```
```
>>> main()
Available commands:
  start <port>        - Start server on the specified port
  status              - Show all served ports status
  routes              - Show all registered routes
  stop <port>         - Stop server on the specified port
  stop_all            - Stop all servers
  add_route <path>    - Add a new route to the server
  shutdown            - Stop all servers and exit
  help                - Show this help menu
Enter command:
Available commands:
  start <port>        - Start server on the specified port
  status              - Show all served ports status
  routes              - Show all registered routes
  stop <port>         - Stop server on the specified port
  stop_all            - Stop all servers
  add_route <path>    - Add a new route to the server
  shutdown            - Stop all servers and exit
  help                - Show this help menu
  exit                - Exit the program
Enter command: