# Модуль для запуска WebView интерфейса g4f

## Обзор

Этот модуль отвечает за запуск WebView интерфейса для проекта g4f. Он использует библиотеку `webview` для создания окон с веб-контентом, а также предоставляет API для взаимодействия JavaScript кода в WebView с Python кодом. Модуль также обрабатывает аргументы командной строки для настройки WebView.

## Подробней

Модуль предназначен для создания графического интерфейса пользователя (GUI) для g4f. WebView позволяет отображать веб-контент (HTML, CSS, JavaScript) в отдельном окне, используя системный браузер. Это позволяет создавать кросс-платформенные GUI, которые выглядят и работают одинаково на разных операционных системах.

Модуль использует следующие компоненты:

-   `webview`: Библиотека для создания WebView окон.
-   `platformdirs`: Библиотека для определения каталога конфигурации пользователя (опционально).
-   `g4f.gui.gui_parser`: Модуль для разбора аргументов командной строки.
-   `g4f.gui.server.js_api`: Модуль, предоставляющий API для взаимодействия JavaScript кода в WebView с Python кодом.
-   `g4f.version`: Модуль, содержащий информацию о версии g4f.
-   `g4f.debug`: Модуль для отладки.

## Функции

### `run_webview`

```python
def run_webview(
    debug: bool = False,
    http_port: int = None,
    ssl: bool = True,
    storage_path: str = None,
    gui: str = None
) -> None:
    """
    Запускает WebView интерфейс g4f.

    Args:
        debug (bool, optional): Включает режим отладки. По умолчанию False.
        http_port (int, optional): Порт для HTTP сервера. По умолчанию None.
        ssl (bool, optional): Включает SSL. По умолчанию True.
        storage_path (str, optional): Путь для хранения данных WebView. По умолчанию None.
        gui (str, optional):  Не используется.  По умолчанию None.

    Returns:
        None

    Как работает функция:
     1. Определяет путь к каталогу, где находятся файлы WebView (HTML, CSS, JavaScript). Если приложение запущено как замороженный исполняемый файл (например, с помощью PyInstaller), то путь определяется как `sys._MEIPASS`. В противном случае, путь определяется относительно текущего файла.
     2. Устанавливает настройки WebView:
        - `OPEN_EXTERNAL_LINKS_IN_BROWSER`: Открывает внешние ссылки в браузере по умолчанию.
        - `ALLOW_DOWNLOADS`: Разрешает загрузки файлов из WebView.
     3. Создает окно WebView с указанными параметрами:
        - `title`: Заголовок окна, содержащий версию g4f.
        - `url`: Путь к файлу `index.html`, который является точкой входа в WebView приложение.
        - `text_select`: Разрешает выделение текста в WebView.
        - `js_api`: Предоставляет API для взаимодействия JavaScript кода в WebView с Python кодом.
     4. Если `has_platformdirs` истина и `storage_path` не указан, определяет путь для хранения данных WebView, используя `user_config_dir` из библиотеки `platformdirs`. Это позволяет хранить данные WebView в стандартном каталоге конфигурации пользователя для данной операционной системы.
     5. Запускает WebView с указанными параметрами:
        - `private_mode`: Отключает приватный режим.
        - `storage_path`: Путь для хранения данных WebView.
        - `debug`: Включает режим отладки.
        - `http_port`: Порт для HTTP сервера.
        - `ssl`: Включает SSL.

    Внутренние функции:
        Отсутствуют

    ASCII flowchart:

     Определение пути к каталогу WebView
     ↓
     Установка настроек WebView (открытие ссылок в браузере, разрешение загрузок)
     ↓
     Создание окна WebView (заголовок, URL, разрешение выделения текста, API)
     ↓
     Определение пути для хранения данных (если platformdirs доступен и storage_path не указан)
     ↓
     Запуск WebView (приватный режим, путь хранения, отладка, HTTP порт, SSL)

    Примеры:

    1.  Запуск WebView с настройками по умолчанию:

    ```python
    run_webview()
    ```

    2.  Запуск WebView в режиме отладки:

    ```python
    run_webview(debug=True)
    ```

    3.  Запуск WebView с указанным HTTP портом:

    ```python
    run_webview(http_port=8080)
    ```
    """
    if getattr(sys, 'frozen', False):\n        dirname = sys._MEIPASS\n    else:\n        dirname = os.path.dirname(__file__)\n    webview.settings[\'OPEN_EXTERNAL_LINKS_IN_BROWSER\'] = True\n    webview.settings[\'ALLOW_DOWNLOADS\'] = True\n    webview.create_window(\n        f"g4f - {g4f.version.utils.current_version}",\n        os.path.join(dirname, "client/index.html"),\n        text_select=True,\n        js_api=JsApi(),\n    )\n    if has_platformdirs and storage_path is None:\n        storage_path = user_config_dir("g4f-webview")\n    webview.start(\n        private_mode=False,\n        storage_path=storage_path,\n        debug=debug,\n        http_port=http_port,\n        ssl=ssl\n    )\n
```

## Главный блок `if __name__ == "__main__":`

```python
if __name__ == "__main__":
    """
    Точка входа в приложение при запуске скрипта напрямую.
    """
    parser = gui_parser()\n    args = parser.parse_args()\n    if args.debug:\n        g4f.debug.logging = True\n    run_webview(args.debug, args.port, not args.debug)\n
```

**Назначение**:
Определяет точку входа в приложение при запуске скрипта напрямую.

**Как работает**:

1.  Создает экземпляр парсера аргументов командной строки `gui_parser`.
2.  Разбирает аргументы командной строки с помощью `parser.parse_args()`.
3.  Если указан аргумент `--debug`, включает режим отладки в модуле `g4f.debug`.
4.  Вызывает функцию `run_webview` с аргументами, полученными из командной строки. Аргумент `ssl` устанавливается в `not args.debug`, что означает, что SSL будет включен только если режим отладки не активен.

ASCII flowchart:

    Создание парсера аргументов командной строки
    ↓
    Разбор аргументов командной строки
    ↓
    Проверка, включен ли режим отладки
    ↓
    Включение режима отладки (если указан аргумент --debug)
    ↓
    Запуск WebView с аргументами из командной строки

**Примеры**:

1.  Запуск WebView с параметрами по умолчанию:

    ```bash
    python webview.py
    ```

2.  Запуск WebView в режиме отладки:

    ```bash
    python webview.py --debug
    ```

3.  Запуск WebView с указанным портом:

    ```bash
    python webview.py --port 8080