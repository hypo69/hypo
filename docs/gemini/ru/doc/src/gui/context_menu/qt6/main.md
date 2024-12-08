# Модуль `hypotez/src/gui/context_menu/qt6/main.py`

## Обзор

Модуль `hypotez/src/gui/context_menu/qt6/main.py` предоставляет функции для добавления или удаления пункта пользовательского контекстного меню ("hypo AI assistant") в контекстном меню рабочего стола и папок в Windows Explorer.  Модуль использует реестр Windows для изменения контекстного меню, позволяя пользователю выполнять действия при щелчке правой кнопкой мыши на пустом месте папки или рабочего стола.

## Функции

### `add_context_menu_item()`

**Описание**: Добавляет пункт контекстного меню "hypo AI assistant" в контекстное меню рабочего стола и папок.

**Детали**: Эта функция создает запись в реестре Windows под ключом `HKEY_CLASSES_ROOT\\Directory\\Background\\shell\\hypo_AI_assistant`.  Создаётся подключаемый пункт меню, который, при выборе, выполняет указанный Python-скрипт.  Функция проверяет существование файла скрипта и выводит сообщение об ошибке, если он не найден.

**Параметры**:  Функция не принимает параметров.

**Возвращает**: Функция не возвращает значение.

**Вызывает исключения**:
- `QtWidgets.QMessageBox.critical`: Если файл скрипта не найден, отображается сообщение об ошибке.
- `Exception`: Выводится любое другое исключение, возникшее при взаимодействии с реестром.

### `remove_context_menu_item()`

**Описание**: Удаляет пункт контекстного меню "hypo AI assistant" из контекстного меню рабочего стола и папок.

**Детали**: Эта функция удаляет запись в реестре Windows под ключом `HKEY_CLASSES_ROOT\\Directory\\Background\\shell\\hypo_AI_assistant`.

**Параметры**: Функция не принимает параметров.

**Возвращает**: Функция не возвращает значение.

**Вызывает исключения**:
- `FileNotFoundError`: Если пункт контекстного меню не найден, отображается предупреждение.
- `Exception`: Выводится любое другое исключение, возникшее при взаимодействии с реестром.

## Классы

### `ContextMenuManager`

**Описание**: Главное окно приложения для управления пользовательским контекстным меню.

**Методы**:

- `__init__()`: Инициализирует главное окно приложения.
- `initUI()`: Инициализирует интерфейс пользователя с кнопками для добавления, удаления пункта контекстного меню и выхода.


##  Модульные импорты

- `winreg` (`reg`): Для взаимодействия с реестром Windows.
- `os`: Для работы с файлами и путями.
- `PyQt6.QtWidgets`: Для создания элементов графического интерфейса (GUI) и сообщений.
- `header`: (Предполагаемый импорт) для инициализации настроек или констант.
- `gs`: (Предполагаемый импорт) для получения пути к проекту или других настроек.

##  Примечания

-  Переменная `MODE = 'dev'`  подразумевает режим разработки.
-  Путь к скрипту (`gs.path.src / 'gui' / 'context_menu' / 'main.py'`) зависит от структуры проекта и должен быть скорректирован для конкретного случая.
- При использовании `gs.path.src`, необходимо убедиться, что модуль `gs` корректно импортирован и определяет переменную `path` с корректным путем.