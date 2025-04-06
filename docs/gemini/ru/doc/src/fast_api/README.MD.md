# Документация для модуля FastAPI Server Manager

## Обзор

Этот проект предоставляет инструменты для управления серверами FastAPI, включая:

- Интерактивный инструмент CLI на Python для управления серверами.
- Интерактивный скрипт PowerShell для управления серверами.

## Подробнее

Этот код предоставляет инструменты для управления серверами FastAPI, обеспечивая интерактивный интерфейс командной строки (CLI) на Python и скрипт PowerShell для управления состоянием сервера (запуск, остановка, просмотр статуса). Проект использует Singleton паттерн для управления единственным экземпляром сервера FastAPI через CLI. PowerShell скрипт обеспечивает дополнительный уровень управления, включая проверку доступности портов и предотвращение одновременного запуска нескольких экземпляров скрипта.

## Содержание

- [Основные характеристики](#Основные-характеристики)
- [Требования](#Требования)
- [Установка](#Установка)
- [Использование](#Использование)
    - [Python CLI](#Python-CLI)
        - [Команды](#Команды)
        - [Пример использования Python CLI](#Пример-использования-Python-CLI)
    - [PowerShell Script](#PowerShell-Script)
        - [Меню](#Меню)
        - [Команды меню](#Команды-меню)
        - [Пример использования PowerShell Script](#Пример-использования-PowerShell-Script)
        - [PowerShell Script Protection against Simultaneous Launch](#PowerShell-Script-Protection-against-Simultaneous-Launch)
- [Архитектура](#Архитектура)
- [Зависимости](#Зависимости)
- [Лицензия](#Лицензия)

## Основные характеристики

- **Singleton Pattern:** Обеспечивает управление только одним экземпляром сервера FastAPI через CLI.
- **Interactive Management:** Запускает сервер один раз, затем управляет его состоянием (запуск, остановка, просмотр статуса) с помощью команд.
- **Customizable Options:** Возможность указать порт и хост для запуска серверов.
- **Asynchronous Management:** Использует `asyncio` для асинхронного запуска и остановки сервера (в Python CLI).
- **Status Tracking:** Возможность просматривать статус сервера и всех его запущенных портов.
- **Collision Prevention:** Использует мьютекс (в скрипте PowerShell), чтобы гарантировать, что только один экземпляр скрипта может быть запущен одновременно.
- **Interactive Menu:** Предоставляет удобный интерфейс командной строки через PowerShell.
- **Port Checking:** Проверяет доступность портов перед запуском серверов (в скрипте PowerShell).
- **Error Handling:** Регистрирует ошибки во время выполнения скрипта.

## Требования

- Python 3.7+
- Windows (для скрипта PowerShell)
- PowerShell 5.1 или выше (для скрипта PowerShell)
- Установленные зависимости (для Python CLI):
    - `typer`
    - `uvicorn`
    - `fastapi`
    - `pydantic`
    - `loguru` (или аналогичный модуль логирования)

## Установка

1. Клонируйте репозиторий (если применимо) или скопируйте файлы.
2. **Для Python CLI (main.py):**
    * Рекомендуется создать виртуальное окружение.
    * Установите необходимые зависимости, например, через: `pip install -r requirements.txt`, или вручную (если `requirements.txt` отсутствует) `pip install typer uvicorn fastapi pydantic loguru`.
3. **Для скрипта PowerShell (server_manager.ps1):**
    * Убедитесь, что `python.exe` установлен и доступен через переменную среды `PATH`.

## Использование

### Python CLI

1. Убедитесь, что файл `main.py` (Python CLI) находится в вашем рабочем каталоге.
2. Запустите CLI, используя Python:

    ```bash
    python main.py <command> [options]
    ```

#### Команды

- **`start`:** Инициализирует и запускает сервер FastAPI.
    - `--port`: (Optional) Порт для запуска сервера (по умолчанию: 8000).
    - `--host`: (Optional) Адрес хоста для сервера (по умолчанию: 0.0.0.0).

    Пример:

    ```bash
    python main.py start --port 8080
    python main.py start --port 8081 --host 127.0.0.1
    ```

    *Примечание:* Если сервер уже инициализирован, будет отображено сообщение, и сервер не может быть повторно инициализирован.
- **`stop`:** Останавливает сервер FastAPI на указанном порту.
    - `--port`: (Required) Порт сервера для остановки.

    Пример:

    ```bash
    python main.py stop --port 8080
    ```

    *Примечание:* Вы не можете остановить сервер, если он не был запущен.
- **`stop-all`:** Останавливает все запущенные серверы FastAPI.

    Пример:

    ```bash
    python main.py stop-all
    ```

    *Примечание:* Вы не можете остановить сервер, если он не был запущен.
- **`status`:** Отображает статус сервера и всех его запущенных портов.

    Пример:

    ```bash
    python main.py status
    ```

    *Примечание:* Эта информация будет отображаться только в том случае, если сервер был запущен.
- **`--help`:** Отображает справочную информацию для команд.

    Пример:

    ```bash
    python main.py --help
    python main.py start --help
    ```

#### Пример использования Python CLI

1. **Start Server:** Start the server on port 8000:

    ```bash
    python main.py start --port 8000
    ```

2. **View Status:** View the status of the server and its running ports:

    ```bash
    python main.py status
    ```

3. **Attempt to Restart:** Attempt to start the server on a different port (e.g., 8081):

    ```bash
    python main.py start --port 8081
    ```

    A message will be displayed in the console indicating that the server has already been started.

4. **Stop Server on port 8000:** Stop the server on port 8000:

    ```bash
    python main.py stop --port 8000
    ```

5. **View Status after Stop:** View the status of the server:

    ```bash
    python main.py status
    ```

    A message will be displayed indicating that the server is not running on port 8000.
6. **Stop All Servers:**

    ```bash
    python main.py stop-all
    ```

7. **View Status after Stopping All Servers:**

    ```bash
    python main.py status
    ```

    A message will be displayed in the console indicating that the server has not been initialized.

### PowerShell Script

1. Убедитесь, что файлы `server_manager.ps1` (скрипт PowerShell) и `main.py` (Python CLI) находятся в одном каталоге или укажите правильный путь к `main.py` в переменной `$pythonScriptPath`.
2. Запустите PowerShell от имени администратора.
3. Перейдите в каталог, где находится файл `server_manager.ps1`.
4. Выполните скрипт:

    ```powershell
    .\\server_manager.ps1
    ```

#### Меню

После запуска скрипта вы увидите меню:

```
FastAPI Server Manager
----------------------
1. Start Server
2. Stop Server
3. Stop All Servers
4. Get Server Status
5. Exit
```

Выберите опцию, введя соответствующий номер (1-5) и нажмите Enter.

#### Команды меню

- **`1. Start Server`:**
    - Запрашивает порт (по умолчанию: 8000).
    - Запрашивает хост (по умолчанию: 0.0.0.0).
    - Проверяет, доступен ли порт.
    - Вызывает Python CLI `main.py` для запуска сервера FastAPI.

- **`2. Stop Server`:**
    - Запрашивает порт сервера для остановки.
    - Вызывает Python CLI `main.py` для остановки сервера FastAPI на указанном порту.

- **`3. Stop All Servers`:**
    - Вызывает Python CLI `main.py` для остановки всех запущенных серверов FastAPI.

- **`4. Get Server Status`:**
    - Вызывает Python CLI `main.py` для отображения статуса всех запущенных серверов FastAPI.

- **`5. Exit`:**
    - Выходит из скрипта.

#### Пример использования PowerShell Script

1. **Start Server:**
    - Select `1`.
    - Enter a port, e.g., `8080` (or leave it blank to use the default port `8000`).
    - Enter a host, e.g., `127.0.0.1` (or leave it blank to use the default host `0.0.0.0`).
2. **Stop Server:**
    - Select `2`.
    - Enter the port, e.g., `8080`.
3. **Stop All Servers**
    - Select `3`.
4. **View Status:**
    - Select `4`.
5. **Exit**
    - Select `5`.

#### PowerShell Script Protection against Simultaneous Launch
The script uses a mutex to ensure that only one instance of the script can be run at any time. If you try to run a second instance, it will exit with an error.

## Архитектура

- `FastApiServer`: Singleton class representing the FastAPI application and managing server startup (in `main.py`).
- `main.py`: Contains the CLI commands and logic for interactive server management in Python.
- `server_manager.ps1`: PowerShell script providing an interactive interface for managing the FastAPI server through the Python CLI.
- `typer`: Library used for creating the command-line interface (in `main.py`).
- `uvicorn`: ASGI web server for running the FastAPI application (in `main.py`).
- `Test-NetConnection`: PowerShell cmdlet for checking ports (in `server_manager.ps1`).
- `System.Threading.Mutex`: .NET class for implementing a mutex (in `server_manager.ps1`).
- `python.exe`: Invokes Python to run CLI commands in `main.py` (in `server_manager.ps1`).

## Зависимости

- `python.exe`: Must be installed on the system and accessible via the `PATH` environment variable (for PowerShell).
- `fastapi`: Web framework for creating APIs (in Python).
- `typer`: Library for creating command-line interfaces (in Python).
- `uvicorn`: ASGI web server (in Python).
- `pydantic`: Library for data validation (in Python).
- `loguru`: Library for logging (in Python).

## Лицензия

[LICENCE]