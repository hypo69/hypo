# Анализ кода модуля `main.py`

**Качество кода: 7/10**

* **Плюсы:**
    *   Код хорошо структурирован и разбит на логические функции.
    *   Используется `winreg` для управления реестром Windows, что является корректным подходом для данной задачи.
    *   GUI на `tkinter` обеспечивает простое взаимодействие с пользователем.
    *   Код предоставляет функциональность добавления и удаления пункта контекстного меню.
    *   Обработка ошибок через `try-except` и вывод сообщений через `messagebox`.
    *   Код достаточно хорошо документирован, присутствуют docstring.

* **Минусы:**
    *   Использование `gs.path.src` предполагает наличие внешней конфигурации, что снижает переносимость.
    *   Не все docstring написаны в формате RST.
    *   Не используется `logger` для логирования ошибок.
    *   Используются двойные кавычки в коде, вместо одинарных.
    *   Комментарии не всегда достаточно информативны.
    *   Не хватает описания модуля в начале файла.
    *   Импорт `header` не используется.

**Рекомендации по улучшению:**

1.  **Описание модуля:** Добавить описание модуля в начале файла в формате RST.
2.  **Форматирование docstring:** Привести docstring к стандарту reStructuredText (RST) для корректного отображения в документации.
3.  **Использование logger:** Заменить `messagebox.showerror` на использование `logger.error` для записи ошибок.
4.  **Одинарные кавычки:** Использовать одинарные кавычки для строк в коде.
5.  **Улучшение комментариев:** Добавить более детальные комментарии, объясняющие логику кода.
6.  **Удалить неиспользуемый импорт** `header`
7.  **Использовать `os.path.join`** для формирования пути к файлу.
8.  **Переименовать переменные:** для более ясного понимания кода
9.  **Добавить пример использования** в docstring для функций.

**Оптимизированный код:**

```python
# -*- coding: utf-8 -*-

"""
Модуль для управления контекстным меню Windows
=========================================================================================

Этот модуль предоставляет функциональность для добавления и удаления пункта контекстного меню
'hypo AI assistant' в Windows Explorer. Пункт меню добавляется для фона папок и рабочего стола
и запускает указанный скрипт Python.

Пример использования
--------------------

.. code-block:: python

    if __name__ == "__main__":
        create_gui()

"""
import winreg as reg
import os
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

from src.logger.logger import logger
from src import gs


def add_context_menu_item():
    """
    Добавляет пункт контекстного меню 'hypo AI assistant' для фона папок и рабочего стола.

    Создаёт ключ реестра для добавления пункта меню. При выборе пункта меню выполняется
    скрипт Python.

    Ключи реестра:
        - `key_path`: Directory\\Background\\shell\\hypo_AI_assistant
            Данный ключ добавляет пункт меню в контекстное меню рабочего стола и папок.

        - `command_key`: Directory\\Background\\shell\\hypo_AI_assistant\\command
            Этот под-ключ задаёт команду для выполнения при выборе пункта меню.

    Raises:
        Выводит сообщение об ошибке, если скрипт не найден.

    Example:
        >>> add_context_menu_item()
    """
    key_path = r'Directory\\Background\\shell\\hypo_AI_assistant' # Путь в реестре для пункта контекстного меню.

    try:
        # Код создаёт ключ для пункта меню в реестре.
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path) as key:
            reg.SetValue(key, '', reg.REG_SZ, 'hypo AI assistant') # Устанавливает отображаемое имя пункта меню.

            command_key = rf'{key_path}\\command'  # Путь к ключу команды
            with reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key) as command:
                command_path = Path(gs.path.src) / 'gui' / 'context_menu' / 'main.py' # Формирование пути к скрипту
                if not os.path.exists(command_path):
                    # Код логирует ошибку, если скрипт не найден.
                    logger.error(f'Файл {command_path} не найден.')
                    messagebox.showerror('Ошибка', f'Файл {command_path} не найден.')
                    return

                # Код устанавливает команду для выполнения скрипта Python.
                reg.SetValue(command, '', reg.REG_SZ, f'python "{command_path}" "%1"')
        # Выводит сообщение об успешном добавлении
        messagebox.showinfo('Успех', 'Пункт меню успешно добавлен!')
    except Exception as ex:
        # Код логирует и выводит сообщение об ошибке.
        logger.error(f'Ошибка при добавлении пункта меню: {ex}')
        messagebox.showerror('Ошибка', f'Ошибка: {ex}')


def remove_context_menu_item():
    """
    Удаляет пункт контекстного меню 'hypo AI assistant'.

    Удаляет ключ реестра, отвечающий за отображение пункта меню.

    Ключ реестра:
        - `key_path`: Directory\\Background\\shell\\hypo_AI_assistant
            Удаляет пользовательский пункт контекстного меню из фона рабочего стола и папок.

    Raises:
        Выводит предупреждение, если пункт меню не найден, и сообщение об ошибке, если удаление не удалось.

    Example:
        >>> remove_context_menu_item()
    """
    key_path = r'Directory\\Background\\shell\\hypo_AI_assistant' # Путь в реестре для пункта контекстного меню

    try:
        # Код удаляет ключ реестра.
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path)
        # Выводит сообщение об успешном удалении.
        messagebox.showinfo('Успех', 'Пункт меню успешно удален!')
    except FileNotFoundError:
        # Код выводит предупреждение, если пункт меню не найден.
        messagebox.showwarning('Предупреждение', 'Пункт меню не найден.')
    except Exception as e:
        # Код логирует и выводит сообщение об ошибке.
        logger.error(f'Ошибка при удалении пункта меню: {e}')
        messagebox.showerror('Ошибка', f'Ошибка: {e}')


def create_gui():
    """
    Создаёт простой графический интерфейс для управления пунктом контекстного меню.

    Интерфейс содержит кнопки для добавления, удаления и выхода из программы.
    """
    root = tk.Tk()  # Создание основного окна.
    root.title('Управление контекстным меню')  # Заголовок окна.

    # Код создаёт кнопку добавления пункта меню.
    add_button = tk.Button(root, text='Добавить пункт меню', command=add_context_menu_item)
    add_button.pack(pady=10)

    # Код создаёт кнопку удаления пункта меню.
    remove_button = tk.Button(root, text='Удалить пункт меню', command=remove_context_menu_item)
    remove_button.pack(pady=10)

    # Код создаёт кнопку выхода из программы.
    exit_button = tk.Button(root, text='Выход', command=root.quit)
    exit_button.pack(pady=10)

    root.mainloop()  # Запуск цикла обработки событий GUI.


if __name__ == '__main__':
    create_gui()  # Запуск GUI приложения.
```