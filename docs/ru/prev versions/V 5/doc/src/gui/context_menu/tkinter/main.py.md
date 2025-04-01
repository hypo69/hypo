# Модуль для управления контекстным меню в Windows Explorer (tkinter)

## Обзор

Модуль `main.py` предназначен для добавления или удаления пункта контекстного меню "hypo AI assistant" в Windows Explorer (в контекстном меню, которое появляется при нажатии правой кнопкой мыши на пустом месте в папке или на рабочем столе). Он использует библиотеку `winreg` для внесения изменений в реестр Windows и библиотеку `tkinter` для создания графического интерфейса пользователя (GUI).

## Подробней

Модуль предоставляет функции для:

1.  Добавления пункта контекстного меню "hypo AI assistant" в реестр Windows, который при выборе запускает Python-скрипт.
2.  Удаления пункта контекстного меню "hypo AI assistant" из реестра Windows.
3.  Создания простого GUI с кнопками для добавления, удаления и выхода из приложения.

Этот модуль позволяет пользователям легко управлять интеграцией "hypo AI assistant" в контекстное меню Windows Explorer.

## Функции

### `add_context_menu_item`

```python
def add_context_menu_item():
    """Adds a context menu item to the desktop and folder background.

    This function creates a registry key under 'HKEY_CLASSES_ROOT\\Directory\\Background\\shell' 
    to add a menu item named 'hypo AI assistant' to the background context menu in Windows Explorer.
    The item runs a Python script when selected.

    Registry Path Details:
        - `key_path`: Directory\\Background\\shell\\hypo_AI_assistant
            This path adds the context menu item to the background of folders and 
            the desktop, allowing users to trigger it when right-clicking on empty space.
        
        - `command_key`: Directory\\Background\\shell\\hypo_AI_assistant\\command
            This subkey specifies the action for the context menu item and links it to a script 
            or command (in this case, a Python script).
    
    Raises:
        Displays an error message if the script file does not exist.
    """
```

**Описание**: Добавляет пункт контекстного меню "hypo AI assistant" в фон рабочего стола и папок.

**Как работает функция**:

1.  Определяет путь в реестре Windows, где будет создан ключ для пункта меню.
2.  Пытается создать ключ в реестре.
3.  Устанавливает значение по умолчанию для ключа, которое является отображаемым именем пункта меню ("hypo AI assistant").
4.  Создает под-ключ `command`, который определяет команду для запуска при выборе пункта меню.
5.  Проверяет, существует ли файл скрипта Python, который будет запущен. Если файл не найден, выводит сообщение об ошибке.
6.  Устанавливает значение для под-ключа `command`, которое является командой для запуска скрипта Python с путем к скрипту в качестве аргумента.
7.  Выводит сообщение об успехе, если пункт меню успешно добавлен.
8.  В случае возникновения ошибки выводит сообщение об ошибке.

**Вызывает исключения**:

*   `FileNotFoundError`: Если файл скрипта не найден.
*   `Exception`: Если произошла ошибка при работе с реестром.

**Примеры**:

```python
add_context_menu_item()
```

### `remove_context_menu_item`

```python
def remove_context_menu_item():
    """Removes the 'hypo AI assistant' context menu item.

    This function deletes the registry key responsible for displaying the custom
    context menu item, effectively removing it from the background context menu.

    Registry Path Details:
        - `key_path`: Directory\\Background\\shell\\hypo_AI_assistant
            This path targets the custom context menu item and deletes it from the 
            background context menu of the desktop and folders.
    
    Raises:
        Displays a warning if the menu item does not exist, and an error if the operation fails.
    """
```

**Описание**: Удаляет пункт контекстного меню "hypo AI assistant".

**Как работает функция**:

1.  Определяет путь в реестре Windows, где находится ключ пункта меню.
2.  Пытается удалить ключ из реестра.
3.  Выводит сообщение об успехе, если пункт меню успешно удален.
4.  В случае, если ключ не найден, выводит предупреждение.
5.  В случае возникновения ошибки выводит сообщение об ошибке.

**Вызывает исключения**:

*   `FileNotFoundError`: Если ключ реестра не найден.
*   `Exception`: Если произошла ошибка при работе с реестром.

**Примеры**:

```python
remove_context_menu_item()
```

### `create_gui`

```python
def create_gui():
    """Creates a simple GUI for managing the custom context menu item.

    This function initializes a tkinter-based GUI with buttons to add, remove,
    or exit the menu manager. It provides user-friendly interaction for registry
    modifications.
    """
```

**Описание**: Создает простой GUI для управления пунктом контекстного меню.

**Как работает функция**:

1.  Создает главное окно GUI.
2.  Устанавливает заголовок окна.
3.  Создает кнопки "Добавить пункт меню", "Удалить пункт меню" и "Выход".
4.  Назначает командам кнопок функции `add_context_menu_item`, `remove_context_menu_item` и `root.quit` соответственно.
5.  Размещает кнопки в окне.
6.  Запускает цикл обработки событий GUI.

**Примеры**:

```python
create_gui()