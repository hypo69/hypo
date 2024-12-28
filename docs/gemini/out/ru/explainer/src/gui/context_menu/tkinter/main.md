# <input code>

```python
## \file hypotez/src/gui/context_menu/tkinter/main.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.gui.context_menu.tkinter 
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
  
""" module: src.gui.context_menu.tkinter """


"""Module to add or remove context menu items for the desktop and folder background.

This module provides functions to add or remove a custom context menu item called 
'hypo AI assistant' for the background of directories and the desktop in Windows Explorer.
It uses the Windows Registry to achieve this, with paths and logic implemented to target
the right-click menu on empty spaces (not on files or folders).
"""

import winreg as reg  # Module for interacting with Windows Registry
import os  # Module for OS path manipulation and checks
import tkinter as tk  # Module for GUI creation
from tkinter import messagebox  # Submodule for GUI message boxes

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

    # Registry path for adding a menu item to the background of folders and the desktop
    key_path = r"Directory\\Background\\shell\\hypo_AI_assistant"

    try:
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path) as key:
            reg.SetValue(key, "", reg.REG_SZ, "hypo AI assistant")  # Display name of the context menu item
            
            command_key = rf"{key_path}\\command"
            with reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key) as command:
                command_path = gs.path.src / 'gui' / 'context_menu' / 'main.py'
                if not os.path.exists(command_path):
                    messagebox.showerror("Ошибка", f"Файл {command_path} не найден.")
                    return
                reg.SetValue(command, "", reg.REG_SZ, f"python \\"{command_path}\\" \\"%1\\"")
        messagebox.showinfo("Успех", "Пункт меню успешно добавлен!")
    except Exception as ex:
        messagebox.showerror("Ошибка", f"Ошибка: {ex}")


def remove_context_menu_item():
    """Removes the 'hypo AI assistant' context menu item."""
    key_path = r"Directory\\Background\\shell\\hypo_AI_assistant"
    try:
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path)
        messagebox.showinfo("Успех", "Пункт меню успешно удален!")
    except FileNotFoundError:
        messagebox.showwarning("Предупреждение", "Пункт меню не найден.")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка: {e}")


def create_gui():
    """Creates a simple GUI for managing the custom context menu item."""
    root = tk.Tk()
    root.title("Управление контекстным меню")
    add_button = tk.Button(root, text="Добавить пункт меню", command=add_context_menu_item)
    add_button.pack(pady=10)
    remove_button = tk.Button(root, text="Удалить пункт меню", command=remove_context_menu_item)
    remove_button.pack(pady=10)
    exit_button = tk.Button(root, text="Выход", command=root.quit)
    exit_button.pack(pady=10)
    root.mainloop()


if __name__ == "__main__":
    create_gui()
```

# <algorithm>

```mermaid
graph TD
    A[Запуск create_gui()] --> B{Создание окна Tkinter};
    B --> C[Кнопка "Добавить"];
    B --> D[Кнопка "Удалить"];
    B --> E[Кнопка "Выход"];
    C --> F[Вызов add_context_menu_item()];
    D --> G[Вызов remove_context_menu_item()];
    E --> H[Завершение приложения];
    F --> I[Создание ключа в реестре];
    I --> J{Проверка существования файла};
    J -- Да --> K[Установка пути к скрипту];
    J -- Нет --> L[Ошибка, сообщение пользователю];
    K --> M[Установка значения в реестр];
    M --> N[Успех, сообщение пользователю];
    G --> O[Удаление ключа из реестра];
    O --> P[Успех, сообщение пользователю];
    O -- Нет --> Q[Ошибка, сообщение пользователю];

    subgraph add_context_menu_item()
        I --> J;
        J --> K;
        K --> M;
        M --> N;
    end
    subgraph remove_context_menu_item()
        O --> P;
        O -- Нет --> Q;
    end
```

Пример: Пользователь нажимает кнопку "Добавить". Алгоритм вызывает `add_context_menu_item()`. Функция создает новый ключ в реестре `HKEY_CLASSES_ROOT\Directory\Background\shell\hypo_AI_assistant`. Проверяет существование файла, если файл существует, устанавливает путь к скрипту в реестре и выводит сообщение об успехе. Если файл не найден, выводит сообщение об ошибке и не продолжает работу.

# <mermaid>

```mermaid
graph LR
    subgraph Tkinter GUI
        A[create_gui()] --> B(root window);
        B --> C[add_button];
        B --> D[remove_button];
        B --> E[exit_button];
        C --> F[add_context_menu_item()];
        D --> G[remove_context_menu_item()];
        E --> H[root.quit()];
    end

    F --> I[reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)];
    I --> J[reg.SetValue(key, "", reg.REG_SZ, "hypo AI assistant")];
    J --> K[reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key)];
    K --> L[command_path calculation];
    L --> M[os.path.exists(command_path)];
    M -- True --> N[reg.SetValue(command, "", reg.REG_SZ, python command)];
    M -- False --> O[messagebox.showerror("Ошибка")];
    N --> P[messagebox.showinfo("Успех")];

    G --> Q[reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path)];
    Q --> R[messagebox.showinfo("Успех")];
    Q -- Exception --> S[messagebox.showerror("Ошибка")];
    Q -- FileNotFoundError --> T[messagebox.showwarning("Предупреждение")];


    subgraph winreg
        I --> U[HKEY_CLASSES_ROOT];
        U --> V[Directory];
        V --> W[Background];
        W --> X[shell];
    end

    subgraph src
      L --> Y[gs.path.src];
      Y --> Z[gui];
      Z --> AA[context_menu];
      AA --> BB[main.py];
    end

    style I fill:#f9f,stroke:#333,stroke-width:2px;
```

**Объяснение диаграммы:**

Диаграмма изображает взаимодействие компонентов. Tkinter GUI отвечает за создание и управление окном приложения, кнопками и обработкой событий. winreg взаимодействует с системным реестром Windows, добавляя или удаляя записи. src.gs необходим для работы с путями, в частности, к файлу, выполняемому при нажатии на пункт меню.

# <explanation>

**Импорты:**

- `winreg`: Модуль для взаимодействия с реестром Windows. (`import winreg as reg`) Необходим для добавления и удаления записей в реестре.
- `os`: Модуль для работы с операционной системой, в частности для проверки существования файлов. (`import os`)
- `tkinter`: Библиотека для создания графического интерфейса пользователя (GUI). (`import tkinter as tk`)
- `messagebox`: Подмодуль `tkinter` для вывода сообщений пользователю. (`from tkinter import messagebox`)
- `header`: Вероятно, модуль для инициализации настроек или констант. (`import header`)
- `gs`: Модуль, вероятно, из пакета `src`, который предоставляет доступ к настройкам пути к ресурсам, каталогам и т.д. (`from src import gs`)

**Классы:**

Код не содержит явных классов, но использует классы из `tkinter` (например, `Tk`, `Button`).

**Функции:**

- `add_context_menu_item()`: Добавляет пункт меню в контекстное меню папок и рабочего стола. Использует реестр Windows для создания ключа и задания команды выполнения скрипта. Обрабатывает возможную ошибку, если скрипт не найден.
- `remove_context_menu_item()`: Удаляет созданный пункт меню из контекстного меню. Обрабатывает случаи, когда пункт меню не найден.
- `create_gui()`: Создает графический интерфейс пользователя (Tkinter) с кнопками для добавления/удаления пункта контекстного меню и выхода.

**Переменные:**

- `MODE`: Переменная, вероятно, хранит режим работы приложения (например, `dev` или `prod`).
- `key_path`: Путь к ключу в реестре, где хранятся параметры контекстного меню.
- `command_key`: Путь к ключу в реестре, содержащий команду для выполнения скрипта.
- `command_path`: Путь к файлу Python-скрипта, который выполняется при нажатии на пункт меню.

**Возможные ошибки и улучшения:**

- **Обработка исключений:** Код обрабатывает большинство исключений (`try...except`), но обработка некоторых специфичных ошибок (например, если реестр недоступен) могла бы быть улучшена.
- **Валидация ввода:** Если пользователь может изменять настройки через GUI, необходима проверка корректности введенных данных.
- **Логирование:** Добавление логирования (например, с использованием `logging`) может помочь в отладке и диагностике проблем.
- **Документация:** Добавьте подробную документацию к параметрам, используемым в функциях, для более понятного использования модуля.

**Взаимосвязи с другими частями проекта:**

Модуль `gs` явно необходим для получения пути к скрипту `main.py` из папки `src/gui/context_menu`.  `header` предположительно используется для инициализации конфигурационных данных.  Без этих модулей функция `add_context_menu_item()` не сможет корректно определить путь к исполняемому файлу.