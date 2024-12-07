# Модуль hypotez/src/gui/context_menu/tkinter/main.py

## Обзор

Этот модуль предоставляет функции для добавления или удаления пункта контекстного меню под названием «hypo AI assistant» для фонового пространства каталогов и рабочего стола в проводнике Windows. Он использует реестр Windows для достижения этой цели, реализуя пути и логику для нацеливания на контекстное меню пустого пространства (а не на файлы или папки).

## Функции

### `add_context_menu_item`

**Описание**: Добавляет пункт контекстного меню на рабочий стол и фон папок.

**Параметры**:

Нет параметров.

**Возвращает**:

- `None`: Функция не возвращает значения.

**Вызывает исключения**:

- `Exception`: Возникает при ошибке в процессе работы с реестром или при отсутствии файла скрипта.  В этом случае отображается сообщение об ошибке с подробным описанием. Если файл не найден, отображается сообщение об ошибке и функция возвращает `None`.

### `remove_context_menu_item`

**Описание**: Удаляет пункт контекстного меню «hypo AI assistant».

**Параметры**:

Нет параметров.

**Возвращает**:

- `None`: Функция не возвращает значения.

**Вызывает исключения**:

- `FileNotFoundError`: Возникает, если пункт меню не найден. В этом случае отображается сообщение об ошибке.
- `Exception`: Возникает при ошибке в процессе работы с реестром. В этом случае отображается сообщение об ошибке с подробным описанием.

### `create_gui`

**Описание**: Создает простую графическую оболочку (GUI) для управления пунктом контекстного меню.

**Параметры**:

Нет параметров.

**Возвращает**:

- `None`: Функция не возвращает значения.

**Вызывает исключения**:

- Нет специфических исключений, но могут возникнуть общие исключения Tkinter, если есть проблемы с созданием GUI.


## Константы

### `MODE`

**Описание**: Переменная, вероятно, определяющая режим работы приложения (например, `'dev'` или `'prod'`). Значение по умолчанию — `'dev'`.


## Модули

### `winreg`

Модуль для взаимодействия с реестром Windows.

### `os`

Модуль для манипулирования путями и проверки файлов в операционной системе.

### `tkinter`

Модуль для создания графического интерфейса пользователя (GUI).

### `messagebox`

Подмодуль для создания диалоговых окон сообщений в GUI.

### `header`

Пользовательский модуль, предположительно инициализирующий настройки или константы.

### `src.gs`

Пользовательский модуль, вероятно, содержащий настройки путей или структуру проекта.


##  Подробное описание добавления пункта контекстного меню


При вызове `add_context_menu_item` функция выполняет следующие действия:

1. Определяет путь к записи в реестре для добавления пункта контекстного меню.
2. Создает запись в реестре `HKEY_CLASSES_ROOT\\Directory\\Background\\shell\\hypo_AI_assistant` и устанавливает имя пункта меню.
3. Создает подзапись `HKEY_CLASSES_ROOT\\Directory\\Background\\shell\\hypo_AI_assistant\\command`.
4. Получает путь к скрипту, который нужно запустить, и проверяет его существование. Если файла нет, выводит сообщение об ошибке и завершает функцию.
5. Устанавливает команду в подзаписи `command` для запуска скрипта с помощью Python.
6. Отображает подтверждающее сообщение об успешном добавлении.
7. Обрабатывает исключения, связанные с реестром или отсутствием файла, для обеспечения устойчивости кода.



##  Подробное описание удаления пункта контекстного меню


При вызове `remove_context_menu_item` функция выполняет следующие действия:

1. Определяет путь к записи в реестре для удаления пункта контекстного меню.
2. Попытывается удалить запись в реестре `HKEY_CLASSES_ROOT\\Directory\\Background\\shell\\hypo_AI_assistant`.
3. Отображает подтверждающее сообщение об успешном удалении.
4. Обрабатывает `FileNotFoundError`, если запись не найдена.
5. Обрабатывает исключения, связанные с реестром, для обеспечения устойчивости кода.


##  Графическая оболочка (GUI)

Функция `create_gui` создает простую GUI с кнопками для добавления/удаления пункта контекстного меню и выхода.  Это обеспечивает удобный интерфейс для взаимодействия с функциями реестра.