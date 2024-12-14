## Анализ кода модуля src.gui.context_menu.qt6.main

**Качество кода**
7
 -  Плюсы
        - Код хорошо структурирован и разделен на функции, что улучшает читаемость и возможность повторного использования.
        - Присутствуют docstring для функций и класса, описывающие их назначение.
        - Используется `QtWidgets` для создания графического интерфейса, что соответствует цели модуля.
 -  Минусы
    - Некоторые docstring не соответствуют стандарту RST.
    - Отсутствуют явные импорты из `src.logger.logger` для логирования ошибок.
    - Использование `try-except` без логирования в некоторых местах.
    - Много пустых строк в начале файла.
    - Использование `QtWidgets.QMessageBox` для вывода сообщений, хотя для логирования ошибок предпочтительнее `logger.error`.
    - Переменная `MODE` определена дважды.
**Рекомендации по улучшению**
1.  Переписать все docstring в формате reStructuredText (RST).
2.  Добавить импорт `from src.logger.logger import logger` для логирования ошибок.
3.  Заменить использование `QtWidgets.QMessageBox.critical` для ошибок на `logger.error` с сохранением вывода сообщения пользователю через `QtWidgets.QMessageBox`.
4.  Удалить дублирующую переменную `MODE` и пустые строки в начале файла.
5.  Добавить обработку ошибок с помощью `logger.error` для записи в лог файл.
6.  Использовать `gs.path.src` и подобные константы в соответствии со структурой проекта.
7.  Добавить docstring к конструктору класса `ContextMenuManager`.
8.  Уточнить docstring с описанием конкретных действий, которые выполняет функция.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для добавления или удаления пунктов контекстного меню для рабочего стола и фона папки с использованием PyQt6.
==============================================================================================================

Этот модуль предоставляет функции для добавления или удаления пользовательского пункта контекстного меню
под названием 'hypo AI assistant' для фона каталогов и рабочего стола в Windows Explorer. Он использует
реестр Windows для достижения этой цели, с путями и логикой, реализованными для нацеливания на меню
правой кнопки мыши в пустых местах (не на файлах или папках).

Пример использования
--------------------

Пример использования:

.. code-block:: python

   from PyQt6 import QtWidgets
   from src.gui.context_menu.qt6.main import ContextMenuManager

   if __name__ == "__main__":
       app = QtWidgets.QApplication([])
       window = ContextMenuManager()
       window.show()
       app.exec()
"""
import winreg as reg
import os
from PyQt6 import QtWidgets
from src.logger.logger import logger
import header
from src import gs


MODE = 'dev'


def add_context_menu_item():
    """
    Добавляет пункт контекстного меню на рабочий стол и фон папок.

    Эта функция создает раздел реестра в ``HKEY_CLASSES_ROOT\\Directory\\Background\\shell``
    чтобы добавить пункт меню под названием 'hypo AI assistant' в контекстное меню фона в проводнике Windows.
    Пункт запускает скрипт Python при выборе.

    Детали пути реестра:
        - ``key_path``: ``Directory\\Background\\shell\\hypo_AI_assistant``
            Этот путь добавляет пункт контекстного меню в фон папок и рабочий стол, позволяя
            пользователям запускать его, щелкая правой кнопкой мыши на пустом месте.

        - ``command_key``: ``Directory\\Background\\shell\\hypo_AI_assistant\\command``
            Этот подраздел определяет действие для пункта контекстного меню и связывает его со скриптом
            или командой (в данном случае, скрипт Python).

    :raises FileNotFoundError:  Выводит сообщение об ошибке, если файл скрипта не существует.
    """
    key_path = r"Directory\\Background\\shell\\hypo_AI_assistant"
    try:
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path) as key:
            reg.SetValue(key, "", reg.REG_SZ, "hypo AI assistant")
            command_key = rf"{key_path}\\command"
            with reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key) as command:
                command_path = gs.path.src / 'gui' / 'context_menu' / 'main.py'
                if not os.path.exists(command_path):
                    logger.error(f"Файл {command_path} не найден.")
                    QtWidgets.QMessageBox.critical(None, "Ошибка", f"Файл {command_path} не найден.")
                    return

                reg.SetValue(command, "", reg.REG_SZ, f"python \"{command_path}\" \"%1\"")
        QtWidgets.QMessageBox.information(None, "Успех", "Пункт меню успешно добавлен!")
    except Exception as ex:
         logger.error(f"Ошибка добавления пункта меню: {ex}")
         QtWidgets.QMessageBox.critical(None, "Ошибка", f"Ошибка: {ex}")

def remove_context_menu_item():
    """
    Удаляет пункт контекстного меню 'hypo AI assistant'.

    Эта функция удаляет раздел реестра, отвечающий за отображение пользовательского
    пункта контекстного меню, эффективно удаляя его из контекстного меню фона.

    Детали пути реестра:
        - ``key_path``: ``Directory\\Background\\shell\\hypo_AI_assistant``
            Этот путь нацелен на пользовательский пункт контекстного меню и удаляет его из
            контекстного меню фона рабочего стола и папок.

     :raises FileNotFoundError:  Выводит предупреждение, если пункт меню не существует.
     :raises Exception:  Выводит сообщение об ошибке, если операция не удалась.
    """
    key_path = r"Directory\\Background\\shell\\hypo_AI_assistant"
    try:
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path)
        QtWidgets.QMessageBox.information(None, "Успех", "Пункт меню успешно удален!")
    except FileNotFoundError:
        logger.warning("Пункт меню не найден.")
        QtWidgets.QMessageBox.warning(None, "Предупреждение", "Пункт меню не найден.")
    except Exception as e:
        logger.error(f"Ошибка удаления пункта меню: {e}")
        QtWidgets.QMessageBox.critical(None, "Ошибка", f"Ошибка: {e}")


class ContextMenuManager(QtWidgets.QWidget):
    """
    Главное окно приложения для управления пользовательским пунктом контекстного меню.
    """
    def __init__(self):
        """
        Инициализирует главное окно приложения.
        """
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Инициализирует пользовательский интерфейс с кнопками для добавления, удаления или выхода.

        Этот метод устанавливает заголовок окна, создает вертикальный макет,
        добавляет кнопки для добавления и удаления пункта меню, а также кнопку выхода.
        """
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