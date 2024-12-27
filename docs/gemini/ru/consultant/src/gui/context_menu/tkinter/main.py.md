# Анализ кода модуля `main.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разбит на логические блоки, что облегчает понимание и поддержку.
    - Используются комментарии для пояснения работы основных частей кода.
    - Применяются try-except блоки для обработки возможных ошибок.
    - GUI-интерфейс, хоть и простой, обеспечивает понятное взаимодействие с пользователем.
    - Код соответствует PEP 8 в базовых моментах, таких как пробелы вокруг операторов.
    -  Логика добавления и удаления пунктов меню проста и понятна.
- Минусы
    - Отсутствует docstring для модуля в начале файла.
    - Не хватает RST-документации для всех функций и методов, что затрудняет понимание их работы.
    -  Используются стандартные блоки `try-except` вместо логирования ошибок через `logger.error`.
    -  Используется стандартный `messagebox` из `tkinter` для вывода сообщений.
    -  Присутствуют избыточные комментарии, например, `# Module for interacting with Windows Registry`.
    -  Некоторые комментарии недостаточно информативны, например, `# Display any error that occurs during the registry modification`.
    -  Импорт `header` нигде не используется.
    -  Переменная `MODE` не используется в коде, ее наличие не имеет смысла.
    -  `#! venv/Scripts/python.exe` и `#! venv/bin/python/python3.12` дублируются и не нужны в коде, являются артефактом копирования,  в коде нет указания на использование shebang.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля в начале файла в формате reStructuredText (RST).
2.  Добавить RST-документацию для всех функций, методов, переменных.
3.  Использовать `logger.error` для логирования ошибок вместо `try-except` в `add_context_menu_item` и `remove_context_menu_item`.
4.  Удалить неиспользуемые импорты, переменные и дублирующие комментарии.
5.  Использовать `os.path.join` вместо `/` для формирования путей.
6.  Переписать комментарии в коде в более информативный и конкретный вид.

**Оптимизиробанный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для управления элементами контекстного меню в Windows.
=========================================================================================

Этот модуль предоставляет функции для добавления и удаления пользовательского пункта меню
'hypo AI assistant' в контекстное меню рабочего стола и фона папок в Windows. Использует
реестр Windows для реализации этой функциональности.

Пример использования
--------------------

Пример использования:

.. code-block:: python

    from src.gui.context_menu.tkinter.main import create_gui

    if __name__ == "__main__":
        create_gui()
"""

import winreg as reg
import os
import tkinter as tk
from tkinter import messagebox

from src import gs
from src.logger.logger import logger


def add_context_menu_item():
    """Добавляет пункт контекстного меню 'hypo AI assistant' для рабочего стола и фона папок.

    Создаёт ключ реестра для добавления пункта меню, который запускает скрипт при выборе.
    
    :raises: Выводит сообщение об ошибке, если файл скрипта не найден.
    """
    key_path = r"Directory\\Background\\shell\\hypo_AI_assistant"
    try:
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path) as key:
            reg.SetValue(key, "", reg.REG_SZ, "hypo AI assistant")
            command_key = rf"{key_path}\\command"
            with reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key) as command:
                command_path = os.path.join(gs.path.src, 'gui', 'context_menu', 'main.py')
                if not os.path.exists(command_path):
                    messagebox.showerror("Ошибка", f"Файл {command_path} не найден.")
                    return

                reg.SetValue(command, "", reg.REG_SZ, f"python \"{command_path}\" \"%1\"")
        messagebox.showinfo("Успех", "Пункт меню успешно добавлен!")

    except Exception as ex:
        logger.error(f"Ошибка при добавлении пункта меню: {ex}", exc_info=True)
        messagebox.showerror("Ошибка", f"Ошибка: {ex}")


def remove_context_menu_item():
    """Удаляет пункт контекстного меню 'hypo AI assistant'.

    Удаляет ключ реестра, отвечающий за отображение пункта меню.
    
    :raises: Выводит предупреждение, если пункт меню не найден. Выводит сообщение об ошибке при сбое удаления.
    """
    key_path = r"Directory\\Background\\shell\\hypo_AI_assistant"
    try:
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path)
        messagebox.showinfo("Успех", "Пункт меню успешно удален!")
    except FileNotFoundError:
        messagebox.showwarning("Предупреждение", "Пункт меню не найден.")
    except Exception as e:
        logger.error(f"Ошибка при удалении пункта меню: {e}", exc_info=True)
        messagebox.showerror("Ошибка", f"Ошибка: {e}")


def create_gui():
    """Создает графический интерфейс для управления пунктом контекстного меню.

    Инициализирует окно tkinter с кнопками для добавления, удаления и выхода.
    """
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