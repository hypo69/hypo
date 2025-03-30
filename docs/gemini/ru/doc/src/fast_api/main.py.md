# Модуль `main.py`

## Обзор

Модуль `main.py` является точкой входа для управления FastAPI сервером. Он предоставляет интерфейс командной строки для запуска, остановки и управления серверами, а также для добавления новых маршрутов.

## Подробней

Этот модуль позволяет пользователю взаимодействовать с сервером через командную строку, выполняя такие действия, как запуск сервера на определенном порту, просмотр статуса серверов, добавление новых маршрутов и остановка серверов. Он использует класс `CommandHandler` из модуля `src.fast_api.fast_api` для обработки команд. Расположение файла `/src/fast_api/main.py` говорит о том, что это основной исполняемый файл для fastAPI.

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

**Описание**: Выводит в консоль список доступных команд и их описание.

**Как работает функция**:

Функция просто печатает список доступных команд и их краткое описание в консоль.

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

**Описание**: Основная функция управления сервером, реализующая логику обработки команд и взаимодействия с `CommandHandler`.

**Как работает функция**:

1.  Создает экземпляр класса `CommandHandler`.
2.  В бесконечном цикле:
    *   Вызывает функцию `display_menu` для отображения доступных команд.
    *   Принимает ввод пользователя с помощью `input`.
    *   Разделяет введенную строку на части, чтобы определить команду и ее аргументы.
    *   Обрабатывает различные команды, такие как `start`, `status`, `routes`, `stop`, `stop_all`, `add_route`, `shutdown`, `help` и `exit`.
    *   Вызывает соответствующие методы `CommandHandler` для выполнения команд.
    *   Обрабатывает исключения, которые могут возникнуть в процессе выполнения команд, и логирует их с помощью `logger.error`.

**Примеры**:

Запуск сервера на порту 8000:

```
Enter command: start 8000
Enter host address (default: 127.0.0.1):
```

Просмотр статуса серверов:

```
Enter command: status
```

Остановка сервера на порту 8000:

```
Enter command: stop 8000
```

Добавление нового маршрута `/test`:

```
Enter command: add_route /test
Enter HTTP methods (comma-separated, default: GET): POST,PUT
```

Остановка всех серверов и выход:

```
Enter command: shutdown