# Модуль `hypotez/src/gui/context_menu/tkinter/main.py`

## Обзор

Этот модуль предоставляет функции для добавления или удаления пункта пользовательского контекстного меню (с названием 'hypo AI assistant') для фона папок и рабочего стола в проводнике Windows. Для этого используется реестр Windows. Логика реализована таким образом, чтобы пункт меню активировался при нажатии правой кнопкой мыши на пустом пространстве, а не на файлах или папках.

## Функции

### `add_context_menu_item`

**Описание**: Добавляет пункт контекстного меню на рабочий стол и в фон папок.

**Детали**: Создает ключ реестра в `HKEY_CLASSES_ROOT\\Directory\\Background\\shell` с именем `hypo AI assistant`.  Когда пользователь кликает по этому пункту, выполняется Python-скрипт.

**Пути в реестре:**

* `key_path`: `Directory\\Background\\shell\\hypo_AI_assistant` — добавляет пункт меню в фон папок и рабочего стола.
* `command_key`: `Directory\\Background\\shell\\hypo_AI_assistant\\command` — указывает действие для пункта меню, связывая его со скриптом.

**Параметры**:

Нет параметров.

**Возвращает**:

- `None`: Функция не возвращает значение.

**Возможные исключения**:

- `Exception`:  Возникает, если возникает какая-либо ошибка при работе с реестром.  В случае ошибки, выводится диалоговое окно с сообщением об ошибке.
- `FileNotFoundError`:  Выводится диалоговое окно с сообщением об ошибке, если указанный в `command_path` скрипт не найден.

### `remove_context_menu_item`

**Описание**: Удаляет пункт контекстного меню 'hypo AI assistant'.

**Детали**: Удаляет ключ реестра, отвечающий за отображение пункта меню.

**Пути в реестре:**

* `key_path`: `Directory\\Background\\shell\\hypo_AI_assistant` — путь к удаляемому пункту меню.

**Параметры**:

Нет параметров.

**Возвращает**:

- `None`: Функция не возвращает значение.

**Возможные исключения**:

- `FileNotFoundError`: Возникает, если пункт меню не найден в реестре. В этом случае выводится диалоговое окно с предупреждением.
- `Exception`: Возникает, если возникает ошибка при удалении ключа реестра.  В случае ошибки, выводится диалоговое окно с сообщением об ошибке.


### `create_gui`

**Описание**: Создаёт графический интерфейс для управления контекстным меню.

**Детали**:  Инициализирует GUI на основе Tkinter, с кнопками для добавления/удаления пункта меню и выхода из приложения. Предоставляет пользователю интуитивно понятный способ работы с настройками реестра.

**Параметры**:

Нет параметров.

**Возвращает**:

- `None`: Функция не возвращает значение.

**Возможные исключения**:

- `Exception`: Возникает, если возникает какая-либо ошибка при работе с Tkinter.  В случае ошибки, выводится диалоговое окно с сообщением об ошибке.

## Модульные импорты

* `winreg`: Для взаимодействия с реестром Windows.
* `os`: Для работы с файлами и путями.
* `tkinter`: Для создания графического интерфейса.
* `tkinter.messagebox`: Для вывода сообщений пользователю.
* `header`: (Предполагается) Модуль для инициализации настроек или констант.
* `src.gs`: (Предполагается) Модуль для настроек путей или структуры проекта.


## Константы

* `MODE`: Стр.  Предположительно, переменная для обозначения режима работы (например, 'dev').