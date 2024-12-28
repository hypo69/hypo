```MD
# <input code>

```python
## \file hypotez/src/gui/context_menu/qt6/main.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.gui.context_menu.qt6 
	:platform: Windows, Unix
	:synopsis:

"""



"""
	:platform: Windows, Unix
	:synopsis:

"""


"""
	:platform: Windows, Unix
	:synopsis:

"""


"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""
  
""" module: src.gui.context_menu.qt6 """


"""Module to add or remove context menu items for the desktop and folder background using PyQt6.

This module provides functions to add or remove a custom context menu item called 
'hypo AI assistant' for the background of directories and the desktop in Windows Explorer.
It uses the Windows Registry to achieve this, with paths and logic implemented to target
the right-click menu on empty spaces (not on files or folders).
"""

import winreg as reg  # Module for interacting with Windows Registry
import os  # Module for OS path manipulation and checks
from PyQt6 import QtWidgets  # Module for GUI creation with PyQt6

import header  # Custom import, assuming it initializes settings or constants
from src import gs  # Custom import, likely for path settings or project structure


def add_context_menu_item():
    """Adds a context menu item to the desktop and folder background.

    This function creates a registry key under 'HKEY_CLASSES_ROOT\Directory\Background\shell' 
    to add a menu item named 'hypo AI assistant' to the background context menu in Windows Explorer.
    The item runs a Python script when selected.

    Registry Path Details:
        - `key_path`: Directory\Background\shell\hypo_AI_assistant
            This path adds the context menu item to the background of folders and 
            the desktop, allowing users to trigger it when right-clicking on empty space.
        
        - `command_key`: Directory\Background\shell\hypo_AI_assistant\command
            This subkey specifies the action for the context menu item and links it to a script 
            or command (in this case, a Python script).
    
    Raises:
        Displays an error message if the script file does not exist.
    """
    
    key_path = r"Directory\\Background\\shell\\hypo_AI_assistant"

    try:
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path) as key:
            reg.SetValue(key, "", reg.REG_SZ, "hypo AI assistant")  
            command_key = rf"{key_path}\\command"
            with reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key) as command:
                command_path = gs.path.src / 'gui' / 'context_menu' / 'main.py'
                if not os.path.exists(command_path):
                    QtWidgets.QMessageBox.critical(None, "Ошибка", f"Файл {command_path} не найден.")
                    return
                reg.SetValue(command, "", reg.REG_SZ, f"python \\"{command_path}\\" \\"%1\\"")
        QtWidgets.QMessageBox.information(None, "Успех", "Пункт меню успешно добавлен!")
    except Exception as ex:
        QtWidgets.QMessageBox.critical(None, "Ошибка", f"Ошибка: {ex}")


def remove_context_menu_item():
    """Removes the 'hypo AI assistant' context menu item.

    This function deletes the registry key responsible for displaying the custom
    context menu item, effectively removing it from the background context menu.

    Registry Path Details:
        - `key_path`: Directory\Background\shell\hypo_AI_assistant
            This path targets the custom context menu item and deletes it from the 
            background context menu of the desktop and folders.
    
    Raises:
        Displays a warning if the menu item does not exist, and an error if the operation fails.
    """
    key_path = r"Directory\\Background\\shell\\hypo_AI_assistant"

    try:
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path)
        QtWidgets.QMessageBox.information(None, "Успех", "Пункт меню успешно удален!")
    except FileNotFoundError:
        QtWidgets.QMessageBox.warning(None, "Предупреждение", "Пункт меню не найден.")
    except Exception as e:
        QtWidgets.QMessageBox.critical(None, "Ошибка", f"Ошибка: {e}")


class ContextMenuManager(QtWidgets.QWidget):
    """Main application window for managing the custom context menu item."""

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """Initializes the user interface with buttons to add, remove, or exit."""
        self.setWindowTitle("Управление контекстным меню")
        layout = QtWidgets.QVBoxLayout()
        add_button = QtWidgets.QPushButton("Добавить пункт меню")
        add_button.clicked.connect(add_context_menu_item)
        layout.addWidget(add_button)
        remove_button = QtWidgets.QPushButton("Удалить пункт меню")
        remove_button.clicked.connect(remove_context_menu_item)
        layout.addWidget(remove_button)
        exit_button = QtWidgets.QPushButton("Выход")
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = ContextMenuManager()
    window.show()
    app.exec()
```

# <algorithm>

**Шаг 1: Импорт необходимых библиотек:** Импортируются `winreg` для работы с реестром Windows, `os` для работы с файлами и `QtWidgets` из `PyQt6` для создания GUI. Также импортируются `header` и `gs`, которые, судя по именам, обеспечивают настройку и пути.

**Шаг 2: `add_context_menu_item()`**
    *  Формирует путь к ключу реестра.
    *  Попытка создать ключ реестра.
    *  Проверка существования файла по пути `gs.path.src / 'gui' / 'context_menu' / 'main.py'`. Если файл не найден, выводится сообщение об ошибке, и функция завершается.
    *  Запись значения в ключ реестра.
    *  Сообщение об успехе или ошибка.

**Шаг 3: `remove_context_menu_item()`**
    *  Формирует путь к ключу реестра.
    *  Попытка удалить ключ реестра.
    *  Если ключ не найден, выводится предупреждение.
    *  Сообщение об успехе или ошибка.

**Шаг 4: `ContextMenuManager`**
    *  Создает основное окно GUI.
    *  Создает кнопки для добавления и удаления пунктов контекстного меню.
    *  Обрабатывает клики кнопок.
    *  Выводит окно.

**Шаг 5: `if __name__ == "__main__":`**
    *  Инициализирует Qt приложение.
    *  Создает экземпляр `ContextMenuManager`.
    *  Отображает окно.
    *  Запускает главный цикл обработки событий Qt.

**Пример данных:**

* Функция `add_context_menu_item`: данные - путь к скрипту (например, `C:/path/to/my/script.py`),  команда `python "C:/path/to/my/script.py" "%1"`. Передаются в `reg.SetValue`.

* Функция `remove_context_menu_item`: данные - путь к ключу реестра (`Directory\\Background\\shell\\hypo_AI_assistant`).

* Класс `ContextMenuManager`: данные - информация о кнопках (текст, обработчик).

# <mermaid>

```mermaid
graph TD
    A[Главное приложение] --> B{if __name__ == "__main__"};
    B --> C[Инициализация Qt приложения];
    B --> D[Создать ContextMenuManager];
    D --> E[Отобразить ContextMenuManager];
    C --> F[Запуск главного цикла Qt];
    
    subgraph Кнопки
        D --> G[Кнопка "Добавить"];
        G --> H[add_context_menu_item()];
        D --> I[Кнопка "Удалить"];
        I --> J[remove_context_menu_item()];
    end
    
    subgraph add_context_menu_item()
        H --> K[Формирование пути];
        K --> L[reg.CreateKey];
        L --> M[reg.SetValue (Имя)];
        L --> N[Формирование пути command_key];
        N --> O[reg.CreateKey];
        O --> P[Проверка существования файла];
        P -- Да --> Q[reg.SetValue(команда)];
        P -- Нет --> R[Ошибка];
        Q --> S[reg.SetValue(Имя)];
        S --> T[Сообщение об успехе];
    end
    
    subgraph remove_context_menu_item()
        J --> K1[Формирование пути];
        K1 --> L1[reg.DeleteKey];
        L1 --> M1[Сообщение об успехе];
        L1 -- Ошибка --> N1[Сообщение об ошибке];
        L1 -- Файл не найден --> O1[Сообщение об отсутсвии файла];
    end

```

**Описание зависимостей:**

* **`PyQt6`:** Используется для создания графического интерфейса.
* **`winreg`:** Используется для взаимодействия с Windows Registry.
* **`os`:** Используется для работы с файловой системой, в частности, для проверки существования файла.
* **`gs`:** Вероятно, содержит настройки пути к файлам и папкам проекта.
* **`header`:** Вероятно, содержит константы и настройки, используемые в коде (не ясен функционал).


# <explanation>

**Импорты:**

* `winreg`: модуль для работы с реестром Windows. Необходим для добавления и удаления пунктов контекстного меню в Windows.
* `os`: модуль для взаимодействия с файловой системой. Используется для проверки существования файла.
* `QtWidgets`:  из `PyQt6`. Обеспечивает создание графического пользовательского интерфейса (GUI) с кнопками для добавления и удаления пунктов меню.
* `header`: Вероятно, содержит константы или настройки, используемые в других модулях проекта.
* `gs`: модуль из проекта `src`, вероятно, содержит функции для получения путей или конфигурации.


**Классы:**

* `ContextMenuManager`: Класс, представляющий главное окно приложения. Он имеет метод `initUI` для создания интерфейса и обработки нажатий кнопок, которые вызывают функции для добавления и удаления пунктов контекстного меню.

**Функции:**

* `add_context_menu_item()`: Добавляет пункт контекстного меню "hypo AI assistant" в контекстное меню папок и рабочего стола. Использует `winreg` для изменения реестра. Важно, что функция проверяет существование файла, прежде чем создавать запись в реестре.
* `remove_context_menu_item()`: Удаляет пункт контекстного меню "hypo AI assistant" из контекстного меню папок и рабочего стола. Также использует `winreg` для изменения реестра. Обрабатывает исключение `FileNotFoundError`, если пункта не существует.

**Переменные:**

* `MODE`: строковая переменная, вероятно, задает режим работы программы (например, 'dev' для разработки).
* `key_path`: путь к ключу реестра.
* `command_key`: путь к подключаемому ключу реестра.
* `command_path`: путь к файлу, который будет запущен при нажатии на пункт контекстного меню.
* `gs.path.src`: переменная, вероятно, содержит путь к папке `src` проекта.

**Возможные ошибки и улучшения:**

* **Обработка ошибок:** Функции `add_context_menu_item` и `remove_context_menu_item` обрабатывают исключения, но можно добавить более подробную логгирование или информативные сообщения пользователю в случае ошибок.
* **Более подробная проверка:** Можно добавить проверку существования папок в `command_path`.
* **Перенос обработки ошибок:** Ошибки обработки реестра можно вынести в отдельную функцию, чтобы улучшить структуру кода и его читабельность.
* **Документация:** Код хорошо прокомментирован, но можно добавить более подробную документацию к функциям и классам, например, описание параметров и возвращаемых значений.
* **Локализация:** Добавить локализации для сообщений об ошибках.


**Связь с другими частями проекта:**

Функции `add_context_menu_item` и `remove_context_menu_item` взаимодействуют с `gs`, вероятно, через переменную `gs.path.src` для определения пути к файлу, который должен быть запущен.  `header` вероятно содержит константы и настройки для других частей проекта.  Связь с другими частями проекта через импорты `header` и `gs`.