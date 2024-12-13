# src.gui.context_menu.qt6.main

## Обзор

Модуль `main.py` предназначен для добавления и удаления пользовательского пункта контекстного меню "hypo AI assistant" в контекстное меню рабочего стола и папок в Windows. Для этого используется реестр Windows. Модуль также включает в себя графический интерфейс пользователя (GUI) на основе PyQt6 для управления этими операциями.

## Оглавление

- [Обзор](#обзор)
- [Функции](#функции)
    - [`add_context_menu_item`](#add_context_menu_item)
    - [`remove_context_menu_item`](#remove_context_menu_item)
- [Классы](#классы)
    - [`ContextMenuManager`](#contextmenumanager)

## Функции

### `add_context_menu_item`

**Описание**: Добавляет пункт контекстного меню на рабочий стол и фон папок.

Эта функция создает ключ реестра в `HKEY_CLASSES_ROOT\\Directory\\Background\\shell` для добавления пункта меню с именем `hypo AI assistant` в контекстное меню фона в проводнике Windows. Пункт меню запускает Python-скрипт при выборе.

**Детали пути в реестре**:
- `key_path`: `Directory\\Background\\shell\\hypo_AI_assistant` - путь для добавления пункта в контекстное меню фона папок и рабочего стола.
- `command_key`: `Directory\\Background\\shell\\hypo_AI_assistant\\command` - путь к подключу, определяющему действие контекстного меню, которое запускает Python-скрипт.

**Вызывает исключения**:
- Выводит сообщение об ошибке, если файл скрипта не найден.

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

### `remove_context_menu_item`

**Описание**: Удаляет пункт контекстного меню `hypo AI assistant`.

Эта функция удаляет ключ реестра, отвечающий за отображение пользовательского пункта контекстного меню, тем самым удаляя его из контекстного меню фона.

**Детали пути в реестре**:
- `key_path`: `Directory\\Background\\shell\\hypo_AI_assistant` - путь к пользовательскому пункту меню, который удаляется из контекстного меню фона рабочего стола и папок.

**Вызывает исключения**:
- Выводит предупреждение, если пункт меню не найден.
- Выводит сообщение об ошибке, если операция завершилась неудачно.

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

## Классы

### `ContextMenuManager`

**Описание**: Основное окно приложения для управления пользовательским пунктом контекстного меню.

Этот класс создает главное окно приложения, которое предоставляет пользователю кнопки для добавления, удаления и выхода из программы.

**Методы**:
- `__init__`: Инициализирует класс и вызывает `initUI` для настройки интерфейса.
- `initUI`: Инициализирует пользовательский интерфейс с кнопками для добавления, удаления и выхода.

```python
class ContextMenuManager(QtWidgets.QWidget):
    """Main application window for managing the custom context menu item."""

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """Initializes the user interface with buttons to add, remove, or exit."""
```