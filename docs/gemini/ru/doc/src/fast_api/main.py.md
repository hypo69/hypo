# Модуль управления параметрами Fast API сервера

## Обзор

Модуль `src.fast_api.main` предоставляет интерфейс командной строки для управления Fast API серверами. Он позволяет запускать, останавливать, просматривать статус серверов, добавлять новые маршруты и завершать работу.

## Подробней

Этот модуль является точкой входа для управления Fast API серверами. Он предоставляет пользователю интерфейс командной строки для выполнения различных действий, таких как запуск и остановка серверов, просмотр их статуса, добавление новых маршрутов и завершение работы. Модуль использует класс `CommandHandler` из `src.fast_api.fast_api` для выполнения фактических действий с серверами.

## Функции

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

**Назначение**: Выводит в консоль список доступных команд для управления сервером.

**Параметры**:
- Нет

**Возвращает**:
- Ничего

**Вызывает исключения**:
- Нет

**Как работает функция**:

1.  Функция `display_menu` выводит список доступных команд и их описания в консоль.
2.  Этот список помогает пользователю узнать, какие действия он может выполнять с помощью интерфейса командной строки.

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
                if len(parts) != 2:
                    print("Usage: add_route <path>")
                    continue
                path = parts[1]
                methods = input("Enter HTTP methods (comma-separated, default: GET): ").strip().upper() or "GET"
                methods = [method.strip() for method in methods.split(",")]
                command_handler.add_new_route(path=path, func="lambda: {\\"message\\": \\"Hello from the new route\\"}", methods=methods)


            elif command == "shutdown":
                command_handler.stop_all_servers()
                print("Shutting down all servers.")
                sys.exit(0)

            elif command == "help":
                display_menu()

            elif command == "exit":
                print("Exiting the program.")
                sys.exit(0)
            
            else:
                print("Unknown command. Type \'help\' to see the list of available commands")

        except Exception as ex:
            logger.error(f"An error occurred:", ex, exc_info=True)


if __name__ == "__main__":
    main()
```

**Назначение**: Основная функция управления сервером, обрабатывает команды пользователя и вызывает соответствующие методы `CommandHandler`.

**Параметры**:
- Нет

**Возвращает**:
- Ничего

**Вызывает исключения**:
- `ValueError`: Если введен некорректный номер порта.
- `Exception`: При возникновении других ошибок во время выполнения команды.

**Как работает функция**:

1.  Создается экземпляр класса `CommandHandler`.
2.  В бесконечном цикле:
    *   Вызывается функция `display_menu` для отображения доступных команд.
    *   Запрашивается ввод команды от пользователя.
    *   Команда разбивается на части для определения действия и параметров.
    *   В зависимости от введенной команды вызываются соответствующие методы `CommandHandler`:
        *   `start`: Запускает сервер на указанном порту и хосте.
        *   `status`: Отображает статус всех обслуживаемых портов.
        *   `routes`: Отображает все зарегистрированные маршруты.
        *   `stop`: Останавливает сервер на указанном порту.
        *   `stop_all`: Останавливает все серверы.
        *   `add_route`: Добавляет новый маршрут к серверу.
        *   `shutdown`: Останавливает все серверы и завершает работу программы.
        *   `help`: Выводит меню с доступными командами.
        *   `exit`: Завершает работу программы.
    *   Обрабатываются исключения, которые могут возникнуть во время выполнения команд, и информация об ошибках записывается в лог с использованием `logger.error`.

**ASCII flowchart функции**:

```
Начало
  ↓
Создание CommandHandler
  ↓
Отображение меню команд
  ↓
Ввод команды от пользователя
  ↓
Разбор команды
  ↓
Выполнение команды (start, status, routes, stop, stop_all, add_route, shutdown, help, exit)
  ↓
Обработка исключений
  ↓
Повтор цикла или завершение программы
```

**Примеры**:

```python
# Запуск сервера на порту 8000
# Ввод пользователя: start 8000
# Ввод пользователя (host): 127.0.0.1

# Отображение статуса серверов
# Ввод пользователя: status

# Остановка сервера на порту 8000
# Ввод пользователя: stop 8000

# Остановка всех серверов и завершение работы программы
# Ввод пользователя: shutdown
```