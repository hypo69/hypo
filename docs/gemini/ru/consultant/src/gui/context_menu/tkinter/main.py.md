## Анализ кода модуля `main.py`

**Качество кода**

8/10
 -  Плюсы
        - Код хорошо структурирован, функции имеют понятные названия и docstring.
        - Используется `winreg` для работы с реестром Windows.
        - Присутствует обработка ошибок с помощью `try-except` блоков.
        - Есть GUI на основе `tkinter`.
        - Есть логика проверки существования скрипта перед его запуском.
 -  Минусы
    - Отсутствует единый стиль комментариев reStructuredText (RST).
    - Не используется кастомный логгер.
    - Использование `messagebox` для вывода ошибок не всегда информативно.
    - В начале файла много пустых комментариев.
    - Некоторые строки кода длиннее 79 символов.
    - Отсутствуют проверки, для Windows OS
    - Использование `gs.path` без импорта

**Рекомендации по улучшению**

1.  **Привести комментарии к reStructuredText (RST) формату.**
2.  **Использовать кастомный логгер `from src.logger.logger import logger` для логирования ошибок.**
3.  **Заменить `messagebox` на логирование и более информативные сообщения.**
4.  **Убрать лишние пустые комментарии в начале файла.**
5.  **Добавить проверку на OS Windows.**
6.  **Импортировать `gs` как `from src import gs`.**
7.  **Скорректировать длины строк.**
8.  **Обернуть в `if __name__ == "__main__":` основной код, чтобы не запустить его при импорте.**

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для добавления и удаления пунктов контекстного меню для рабочего стола и фона папок.
=========================================================================================

Этот модуль предоставляет функции для добавления или удаления пользовательского пункта
контекстного меню под названием 'hypo AI assistant' для фона каталогов и рабочего стола
в проводнике Windows. Он использует реестр Windows для этого, с путями и логикой,
реализованной для нацеливания на меню правой кнопки мыши на пустых местах (не на файлах или папках).

Пример использования
--------------------

.. code-block:: python

    from src.gui.context_menu.tkinter import main

    if __name__ == "__main__":
       main.create_gui()

"""
import os
import sys
import tkinter as tk
from tkinter import messagebox
import winreg as reg

from src import gs
from src.logger.logger import logger

MODE = 'dev'


def add_context_menu_item():
    """
    Добавляет пункт контекстного меню на рабочий стол и фон папок.

    Эта функция создает ключ реестра в разделе
    'HKEY_CLASSES_ROOT\\Directory\\Background\\shell', чтобы добавить пункт меню
    под названием 'hypo AI assistant' в контекстное меню фона в проводнике Windows.
    Пункт запускает Python-скрипт при выборе.

    Детали пути реестра:
        - ``key_path``: ``Directory\\Background\\shell\\hypo_AI_assistant``
          Этот путь добавляет пункт контекстного меню на фон папок и рабочего стола,
          позволяя пользователям запускать его, щелкая правой кнопкой мыши на пустом месте.

        - ``command_key``: ``Directory\\Background\\shell\\hypo_AI_assistant\\command``
          Этот подраздел определяет действие для пункта контекстного меню и связывает его
          со скриптом или командой (в данном случае, Python-скрипт).

    :raises: Выводит сообщение об ошибке, если файл скрипта не существует.
    """
    if sys.platform != 'win32':
        logger.error("Функция add_context_menu_item предназначена только для Windows.")
        messagebox.showerror("Ошибка", "Данная функция предназначена только для Windows.")
        return

    key_path = r"Directory\\Background\\shell\\hypo_AI_assistant"
    try:
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path) as key:
            reg.SetValue(key, "", reg.REG_SZ, "hypo AI assistant")
            command_key = rf"{key_path}\\command"
            with reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key) as command:
                command_path = gs.path.src / 'gui' / 'context_menu' / 'main.py'
                if not os.path.exists(command_path):
                    logger.error(f"Файл {command_path} не найден.")
                    messagebox.showerror("Ошибка", f"Файл {command_path} не найден.")
                    return
                reg.SetValue(command, "", reg.REG_SZ, f"python \"{command_path}\" \"%1\"")
        messagebox.showinfo("Успех", "Пункт меню успешно добавлен!")
    except Exception as ex:
        logger.error(f"Ошибка при добавлении пункта меню: {ex}")
        messagebox.showerror("Ошибка", f"Ошибка: {ex}")


def remove_context_menu_item():
    """
    Удаляет пункт контекстного меню 'hypo AI assistant'.

    Эта функция удаляет ключ реестра, отвечающий за отображение пользовательского
    пункта контекстного меню, эффективно удаляя его из контекстного меню фона.

    Детали пути реестра:
        - ``key_path``: ``Directory\\Background\\shell\\hypo_AI_assistant``
          Этот путь нацелен на пользовательский пункт контекстного меню и удаляет
          его из контекстного меню фона рабочего стола и папок.

    :raises: Выводит предупреждение, если пункт меню не существует, и ошибку, если
             операция не удается.
    """
    if sys.platform != 'win32':
        logger.error("Функция remove_context_menu_item предназначена только для Windows.")
        messagebox.showerror("Ошибка", "Данная функция предназначена только для Windows.")
        return

    key_path = r"Directory\\Background\\shell\\hypo_AI_assistant"
    try:
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path)
        messagebox.showinfo("Успех", "Пункт меню успешно удален!")
    except FileNotFoundError:
        logger.warning("Пункт меню не найден при попытке удаления.")
        messagebox.showwarning("Предупреждение", "Пункт меню не найден.")
    except Exception as e:
        logger.error(f"Ошибка при удалении пункта меню: {e}")
        messagebox.showerror("Ошибка", f"Ошибка: {e}")


def create_gui():
    """
    Создает простой GUI для управления пользовательским пунктом контекстного меню.

    Эта функция инициализирует GUI на основе tkinter с кнопками для добавления,
    удаления или выхода из менеджера меню. Он обеспечивает удобное взаимодействие
    для модификаций реестра.
    """
    root = tk.Tk()
    root.title("Управление контекстным меню")

    add_button = tk.Button(root, text="Добавить пункт меню",
                           command=add_context_menu_item)
    add_button.pack(pady=10)

    remove_button = tk.Button(root, text="Удалить пункт меню",
                              command=remove_context_menu_item)
    remove_button.pack(pady=10)

    exit_button = tk.Button(root, text="Выход", command=root.quit)
    exit_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    create_gui()