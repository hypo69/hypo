# src.gui.context_menu.tkinter.main

## Обзор

Модуль предоставляет функции для добавления или удаления пользовательского пункта контекстного меню 'hypo AI assistant' для фона каталогов и рабочего стола в Windows Explorer. Он использует реестр Windows для достижения этой цели, с путями и логикой, реализованными для нацеливания на контекстное меню при щелчке правой кнопкой мыши на пустых местах (не на файлах или папках).

## Оглавление

- [Функции](#функции)
    - [`add_context_menu_item`](#add_context_menu_item)
    - [`remove_context_menu_item`](#remove_context_menu_item)
    - [`create_gui`](#create_gui)

## Функции

### `add_context_menu_item`

**Описание**: Добавляет пункт контекстного меню на рабочий стол и фон папок.

Эта функция создает ключ реестра в `HKEY_CLASSES_ROOT\Directory\Background\shell`, чтобы добавить пункт меню с именем `hypo AI assistant` в контекстное меню фона в Windows Explorer. При выборе этого пункта запускается Python-скрипт.

**Детали пути в реестре:**
    - `key_path`: `Directory\Background\shell\hypo_AI_assistant`
        Этот путь добавляет пункт контекстного меню к фону папок и рабочего стола, позволяя пользователям запускать его, щелкая правой кнопкой мыши на пустом месте.
    - `command_key`: `Directory\Background\shell\hypo_AI_assistant\command`
        Этот подраздел определяет действие для пункта контекстного меню и связывает его со скриптом или командой (в данном случае Python-скрипт).
 
**Вызывает исключения**:
    - Отображает сообщение об ошибке, если файл скрипта не существует.

```python
def add_context_menu_item():
    """
    Adds a context menu item to the desktop and folder background.

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

Эта функция удаляет ключ реестра, отвечающий за отображение пользовательского пункта контекстного меню, фактически удаляя его из контекстного меню фона.

**Детали пути в реестре:**
   - `key_path`: `Directory\Background\shell\hypo_AI_assistant`
       Этот путь нацелен на пользовательский пункт контекстного меню и удаляет его из контекстного меню фона рабочего стола и папок.

**Вызывает исключения**:
    - Выводит предупреждение, если пункт меню не существует, и сообщение об ошибке, если операция не удалась.

```python
def remove_context_menu_item():
    """
    Removes the 'hypo AI assistant' context menu item.

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

Эта функция инициализирует GUI на основе tkinter с кнопками для добавления, удаления или выхода из менеджера меню. Он обеспечивает удобное для пользователя взаимодействие для изменения реестра.

```python
def create_gui():
    """
    Creates a simple GUI for managing the custom context menu item.

    This function initializes a tkinter-based GUI with buttons to add, remove,
    or exit the menu manager. It provides user-friendly interaction for registry
    modifications.
    """
```