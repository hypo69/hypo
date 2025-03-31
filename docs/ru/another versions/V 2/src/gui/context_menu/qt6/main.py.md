# Модуль `src.gui.context_menu.qt6.main`

## Обзор

Модуль `src.gui.context_menu.qt6.main` предназначен для добавления или удаления пунктов контекстного меню для рабочего стола и фона папок с использованием PyQt6.
Модуль предоставляет функции для добавления или удаления пользовательского пункта контекстного меню под названием 'hypo AI assistant' для фона каталогов и рабочего стола в проводнике Windows.
Он использует реестр Windows для достижения этой цели, с путями и логикой, реализованными для нацеливания меню правого клика на пустых местах (не на файлах или папках).

## Содержание

- [Обзор](#обзор)
- [Функции](#функции)
  - [`add_context_menu_item`](#add_context_menu_item)
  - [`remove_context_menu_item`](#remove_context_menu_item)
- [Классы](#классы)
  - [`ContextMenuManager`](#ContextMenuManager)

## Функции

### `add_context_menu_item`

**Описание**: Добавляет пункт контекстного меню на рабочий стол и фон папок.

Эта функция создает ключ реестра в разделе 'HKEY_CLASSES_ROOT\\Directory\\Background\\shell' чтобы добавить пункт меню с названием 'hypo AI assistant' в контекстное меню фона в проводнике Windows.
Пункт запускает Python скрипт при выборе.

**Детали пути реестра:**

- `key_path`: Directory\\Background\\shell\\hypo_AI_assistant
   Этот путь добавляет пункт контекстного меню на фон папок и рабочий стол, позволяя пользователям запускать его при правом клике на пустом месте.

- `command_key`: Directory\\Background\\shell\\hypo_AI_assistant\\command
   Этот подраздел задает действие для пункта контекстного меню и связывает его со скриптом или командой (в данном случае, Python скрипт).

**Вызывает исключения**:
- `QtWidgets.QMessageBox.critical`:  Отображает сообщение об ошибке, если файл скрипта не существует.

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

**Описание**: Удаляет пункт контекстного меню 'hypo AI assistant'.

Эта функция удаляет ключ реестра, отвечающий за отображение пользовательского пункта контекстного меню, фактически удаляя его из контекстного меню фона.

**Детали пути реестра:**

- `key_path`: Directory\\Background\\shell\\hypo_AI_assistant
   Этот путь нацелен на пользовательский пункт контекстного меню и удаляет его из контекстного меню фона рабочего стола и папок.

**Вызывает исключения**:
- `QtWidgets.QMessageBox.warning`: Отображает предупреждение, если пункт меню не найден.
- `QtWidgets.QMessageBox.critical`: Отображает сообщение об ошибке, если операция не удалась.

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

## Классы

### `ContextMenuManager`

**Описание**: Основное окно приложения для управления пользовательским пунктом контекстного меню.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `ContextMenuManager` и вызывает метод `initUI`.
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