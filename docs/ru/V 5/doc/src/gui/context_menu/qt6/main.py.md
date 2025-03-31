# Модуль для управления контекстным меню в Windows Explorer

## Обзор

Модуль `main.py` предоставляет функциональность для добавления и удаления пункта контекстного меню "hypo AI assistant" в Windows Explorer. Этот пункт появляется при щелчке правой кнопкой мыши на пустом месте в папке или на рабочем столе. Модуль использует библиотеку `winreg` для взаимодействия с реестром Windows и библиотеку `PyQt6` для создания графического интерфейса.

## Подробней

Модуль позволяет пользователям добавлять и удалять пункт контекстного меню, который запускает Python-скрипт.  Он состоит из функций для добавления и удаления пункта меню, а также класса `ContextMenuManager`, который создает графический интерфейс для управления пунктом меню.
При добавлении пункта меню создаются ключи в реестре Windows, указывающие на Python-скрипт, который должен быть запущен при выборе пункта меню. При удалении пункта меню соответствующие ключи реестра удаляются.

## Классы

### `ContextMenuManager`

**Описание**: Класс `ContextMenuManager` представляет собой главное окно приложения для управления пунктом контекстного меню.

**Как работает класс**:
Класс `ContextMenuManager` наследуется от `QtWidgets.QWidget` и создает графический интерфейс с кнопками для добавления, удаления и выхода из приложения. При нажатии на кнопки вызываются соответствующие функции для добавления или удаления пункта контекстного меню.

**Методы**:
- `__init__`: Инициализирует класс `ContextMenuManager` и вызывает метод `initUI` для создания пользовательского интерфейса.
- `initUI`: Создает пользовательский интерфейс с кнопками для добавления, удаления и выхода.

**Параметры**:
- Отсутствуют.

**Примеры**:
```python
app = QtWidgets.QApplication([])
window = ContextMenuManager()
window.show()
app.exec()
```

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
    ...
```

**Описание**: Добавляет пункт контекстного меню "hypo AI assistant" в фон рабочего стола и папок.

**Как работает функция**:
Функция создает ключи реестра в `HKEY_CLASSES_ROOT\\Directory\\Background\\shell`, чтобы добавить пункт меню "hypo AI assistant" в контекстное меню фона в Windows Explorer. Когда пункт выбран, запускается Python-скрипт. Функция сначала создает ключ для пункта меню, затем создает под-ключ `command`, который указывает путь к Python-скрипту для запуска. Если скрипт не найден, отображается сообщение об ошибке.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- `QtWidgets.QMessageBox.critical`: Если не удается создать или изменить ключи реестра.

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
    ...
```

**Описание**: Удаляет пункт контекстного меню "hypo AI assistant".

**Как работает функция**:
Функция удаляет ключ реестра, отвечающий за отображение пользовательского пункта контекстного меню, удаляя его из контекстного меню фона.
Она пытается удалить ключ реестра, связанный с пунктом контекстного меню. Если пункт меню не найден, отображается предупреждение. Если операция завершается неудачно, отображается сообщение об ошибке.

**Параметры**:
- Отсутствуют.

**Возвращает**:
- Отсутствует.

**Вызывает исключения**:
- `QtWidgets.QMessageBox.warning`: Если пункт меню не найден.
- `QtWidgets.QMessageBox.critical`: Если не удается удалить ключи реестра.

**Примеры**:

```python
remove_context_menu_item()
```