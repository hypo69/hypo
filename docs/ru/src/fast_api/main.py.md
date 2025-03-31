# Модуль управления Fast API сервером

## Обзор

Модуль `main.py` предоставляет интерфейс командной строки для управления сервером Fast API. Он позволяет запускать, останавливать, просматривать статус и добавлять новые маршруты к серверу.

## Подробней

Этот файл является точкой входа для управления сервером Fast API. Он включает в себя функции для отображения меню доступных команд и обработки пользовательского ввода для выполнения различных операций с сервером. Модуль использует `CommandHandler` из `src.fast_api.fast_api` для выполнения фактических операций управления сервером.

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

**Назначение**: Выводит на экран меню с перечнем доступных команд для управления сервером Fast API.

**Как работает функция**:
Функция `display_menu` просто печатает в консоль список доступных команд с их кратким описанием.

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
                command_handler.add_new_route(path=path, func="lambda: {\"message\": \"Hello from the new route\"}", methods=methods)


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
                print("Unknown command. Type 'help' to see the list of available commands")

        except Exception as ex:
            logger.error(f"An error occurred:", ex, exc_info=True)


if __name__ == "__main__":
    main()
```

**Назначение**: Основная функция управления сервером, которая обрабатывает команды пользователя и вызывает соответствующие методы `CommandHandler` для выполнения операций с сервером.

**Как работает функция**:

Функция `main` выполняет следующие действия:

1.  Создает экземпляр класса `CommandHandler`.
2.  Входит в бесконечный цикл, в котором:

    *   Отображает меню доступных команд с помощью `display_menu()`.
    *   Считывает команду, введенную пользователем, приводит ее к нижнему регистру и удаляет лишние пробелы.
    *   Разбивает введенную строку на части, разделенные пробелами, чтобы выделить команду и ее аргументы.
    *   Выполняет различные действия в зависимости от введенной команды:
        *   `start`: Запускает сервер на указанном порту. Запрашивает у пользователя адрес хоста (по умолчанию `127.0.0.1`).
        *   `status`: Отображает статус всех обслуживаемых портов.
        *   `routes`: Отображает все зарегистрированные маршруты.
        *   `stop`: Останавливает сервер на указанном порту.
        *   `stop_all`: Останавливает все серверы.
        *   `add_route`: Добавляет новый маршрут к серверу. Запрашивает у пользователя HTTP методы (по умолчанию `GET`).
        *   `shutdown`: Останавливает все серверы и завершает работу программы.
        *   `help`: Отображает меню помощи.
        *   `exit`: Завершает работу программы.
    *   Обрабатывает исключения, которые могут возникнуть в процессе выполнения команд, и логирует их с использованием `logger.error`.

Внутри функции `main` происходят следующие логические блоки:

A. Инициализация `CommandHandler`.
|
B. Вход в бесконечный цикл обработки команд.
|
C. Отображение меню команд и получение ввода пользователя.
|
D. Разбор введенной команды и выполнение соответствующих действий на основе этой команды.
|
E. Обработка исключений, которые могут возникнуть при выполнении команд.

**Примеры**:

Запуск сервера на порту 8000:

```
Enter command: start 8000
Enter host address (default: 127.0.0.1): 
```

Остановка сервера на порту 8000:

```
Enter command: stop 8000
```

Остановка всех серверов:

```
Enter command: stop_all
```

Добавление нового маршрута `/test` с методом `POST`:

```
Enter command: add_route /test
Enter HTTP methods (comma-separated, default: GET): POST
```

Завершение работы программы:

```
Enter command: shutdown