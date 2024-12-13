# src.gui.context_menu.tkinter.main

## Обзор

Модуль `main.py` предоставляет функциональность для управления контекстным меню рабочего стола и фона папок в Windows. Он позволяет добавлять и удалять пункт меню "hypo AI assistant", который запускает Python-скрипт при выборе. Модуль использует реестр Windows для интеграции пункта меню и предоставляет простой графический интерфейс на основе Tkinter для управления этими действиями.

## Содержание

- [Обзор](#обзор)
- [Функции](#функции)
  - [`add_context_menu_item`](#add_context_menu_item)
  - [`remove_context_menu_item`](#remove_context_menu_item)
  - [`create_gui`](#create_gui)

## Функции

### `add_context_menu_item`

**Описание**: Добавляет пункт контекстного меню на рабочий стол и фон папок.

Эта функция создает ключ реестра в `HKEY_CLASSES_ROOT\Directory\Background\shell`, чтобы добавить пункт меню `hypo AI assistant` в контекстное меню фона в проводнике Windows. При выборе этого пункта меню запускается Python-скрипт.

**Детали пути в реестре:**

  - `key_path`: `Directory\Background\shell\hypo_AI_assistant` - добавляет пункт контекстного меню для фона папок и рабочего стола.
  - `command_key`: `Directory\Background\shell\hypo_AI_assistant\command` - определяет действие для пункта контекстного меню и связывает его со скриптом.

**Вызывает исключения**:

- Выводит сообщение об ошибке, если файл скрипта не существует.

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

Эта функция удаляет ключ реестра, отвечающий за отображение пункта контекстного меню, тем самым удаляя его из контекстного меню фона.

**Детали пути в реестре:**

- `key_path`: `Directory\Background\shell\hypo_AI_assistant` - путь к пользовательскому пункту контекстного меню.

**Вызывает исключения**:

- Выводит предупреждение, если пункт меню не найден, и сообщение об ошибке, если операция не удалась.

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

### `create_gui`

**Описание**: Создает простой графический интерфейс для управления пользовательским пунктом контекстного меню.

Эта функция инициализирует GUI на основе Tkinter с кнопками для добавления, удаления и выхода из менеджера меню.

```python
def create_gui():
    """Creates a simple GUI for managing the custom context menu item.

    This function initializes a tkinter-based GUI with buttons to add, remove,
    or exit the menu manager. It provides user-friendly interaction for registry
    modifications.
    """
```