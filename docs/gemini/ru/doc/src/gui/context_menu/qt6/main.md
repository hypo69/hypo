# Модуль `hypotez/src/gui/context_menu/qt6/main.py`

## Обзор

Данный модуль предоставляет функциональность для добавления или удаления пункта контекстного меню ('hypo AI assistant') в фоновом режиме проводника Windows (для папок и рабочего стола).  Он использует реестр Windows для модификации контекстного меню.

## Функции

### `add_context_menu_item`

**Описание**: Добавляет пункт контекстного меню 'hypo AI assistant' в фоновое меню папок и рабочего стола.

**Параметры**:
Нет параметров.

**Возвращает**:
- `None`: Функция не возвращает значения.

**Вызывает исключения**:
- `Exception`: Возникает при ошибках работы с реестром или если файл скрипта не найден. Выводится сообщение об ошибке и выполнение прерывается.


### `remove_context_menu_item`

**Описание**: Удаляет пункт контекстного меню 'hypo AI assistant' из фонового меню папок и рабочего стола.

**Параметры**:
Нет параметров.

**Возвращает**:
- `None`: Функция не возвращает значения.

**Вызывает исключения**:
- `FileNotFoundError`: Возникает, если пункт меню не найден. Выводится предупреждающее сообщение.
- `Exception`: Возникает при ошибках работы с реестром. Выводится сообщение об ошибке.

## Классы

### `ContextMenuManager`

**Описание**: Главное окно приложения для управления контекстным меню.

**Методы**:

#### `__init__`

**Описание**: Конструктор класса. Инициализирует пользовательский интерфейс.

#### `initUI`

**Описание**: Инициализирует пользовательский интерфейс с кнопками для добавления/удаления пункта меню и выхода.


## Структура

Модуль `main.py` реализует функционал для работы с контекстным меню в проводнике Windows:

- `add_context_menu_item()`: Добавляет пункт меню в реестр.
- `remove_context_menu_item()`: Удаляет пункт меню из реестра.
- `ContextMenuManager()`: Класс для создания главного окна приложения с кнопками для добавления/удаления пункта.

Этот модуль взаимодействует с реестром Windows, чтобы модифицировать контекстное меню в проводнике.

**Важно**: Функции работы с реестром (`add_context_menu_item`, `remove_context_menu_item`) проверяют существование файла скрипта, который должен быть запущен при нажатии пункта меню. Если файл не найден, выводится сообщение об ошибке, и функция возвращает `None`.