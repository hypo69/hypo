# Модуль `main.py`

## Обзор

Модуль `main.py` предоставляет функциональность для управления FastAPI сервером через командную строку. Он позволяет запускать, останавливать, просматривать статус серверов, добавлять новые маршруты и завершать работу.

## Подробней

Этот модуль является точкой входа для управления FastAPI сервером. Он использует класс `CommandHandler` из модуля `src.fast_api.fast_api` для обработки команд. Модуль предоставляет интерфейс командной строки, который позволяет пользователю взаимодействовать с сервером, управляя его состоянием и маршрутами.

## Функции

### `display_menu`

```python
def display_menu():
    """Выводит меню с доступными командами."""
    ...
```

**Описание**: Выводит список доступных команд с их описанием.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Вызывает исключения**:
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
    ...
```

**Описание**: Основная функция для управления сервером FastAPI. Она обрабатывает команды, вводимые пользователем, и вызывает соответствующие методы `CommandHandler`.

**Параметры**:
- Нет

**Возвращает**:
- Нет

**Вызывает исключения**:
- `Exception`: В случае возникновения непредвиденной ошибки при выполнении команды.

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
Starting server on port 8000...
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
  exit                - Exit the program
Enter command: help
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
  exit                - Exit the program
Enter command: stop_all
Stopping all servers.
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
  exit                - Exit the program
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
  exit                - Exit the program
Enter command: add_route /test
Enter HTTP methods (comma-separated, default: GET): POST
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
  exit                - Exit the program
Enter command: status