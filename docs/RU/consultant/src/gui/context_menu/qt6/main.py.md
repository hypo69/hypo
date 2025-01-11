# Анализ кода модуля `main.py`

**Качество кода**
7
- Плюсы
    - Код хорошо структурирован, функции и классы имеют понятные имена.
    - Присутствуют docstrings, объясняющие назначение функций и классов.
    - Используются `try-except` блоки для обработки исключений, хотя их можно улучшить.
    -  Логика добавления и удаления элементов контекстного меню реализована корректно.
    -  Используются `QtWidgets.QMessageBox` для вывода сообщений пользователю.
- Минусы
    -  Импорт `header` не используется.
    -  Присутствуют лишние пустые docstrings.
    -  Не используется `from src.logger.logger import logger` для логирования ошибок.
    -  Используется `os.path.exists` вместо `Path.exists` из `pathlib` (может привести к проблемам на разных ОС).
    -  Отсутствует форматирование кода, из за этого текст плохо читаемый

**Рекомендации по улучшению**
1.  Удалить неиспользуемый импорт `header`.
2.  Удалить лишние пустые docstrings.
3.  Заменить  `os.path.exists` на `Path.exists` из модуля `pathlib`.
4.  Использовать `from src.logger.logger import logger` для логирования ошибок.
5.  Переписать блоки `try-except` с использованием `logger.error` для отлова ошибок и вывода их в консоль.
6.  Добавить комментарии в формате RST к методам и классам.
7.  Улучшить форматирование кода в соответствии с PEP 8.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
"""
Модуль для управления элементами контекстного меню в Windows.
=========================================================================================

Этот модуль содержит функции для добавления и удаления пункта меню 'hypo AI assistant'
в контекстное меню рабочего стола и фона папок в Windows. Использует реестр Windows
для управления этими пунктами меню.

Пример использования
--------------------

Пример использования класса `ContextMenuManager`:

.. code-block:: python

    app = QtWidgets.QApplication([])
    window = ContextMenuManager()
    window.show()
    app.exec()
"""
import winreg as reg
import os
from pathlib import Path
from PyQt6 import QtWidgets

from src import gs
from src.logger.logger import logger


def add_context_menu_item():
    """Добавляет пункт контекстного меню на рабочий стол и фон папок.

    Создает ключ реестра для добавления пункта меню 'hypo AI assistant'
    в контекстное меню рабочего стола и фона папок в Windows Explorer.
    Пункт меню запускает Python-скрипт при выборе.

    Подробности о пути в реестре:
        - `key_path`: Directory\\Background\\shell\\hypo_AI_assistant
            Этот путь добавляет пункт меню в фон папок и рабочего стола.
        - `command_key`: Directory\\Background\\shell\\hypo_AI_assistant\\command
            Этот подраздел указывает команду для запуска при выборе пункта меню.

    Raises:
        Выводит сообщение об ошибке, если файл скрипта не существует.
    """
    key_path = r'Directory\\Background\\shell\\hypo_AI_assistant'

    try:
        with reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path) as key:
            reg.SetValue(key, '', reg.REG_SZ, 'hypo AI assistant')
            command_key = rf'{key_path}\\command'
            with reg.CreateKey(reg.HKEY_CLASSES_ROOT, command_key) as command:
                command_path = gs.path.src / 'gui' / 'context_menu' / 'main.py'
                if not Path(command_path).exists():
                     # Вывод сообщения об ошибке, если файл скрипта не найден
                    QtWidgets.QMessageBox.critical(None, 'Ошибка', f'Файл {command_path} не найден.')
                    return
                reg.SetValue(command, '', reg.REG_SZ, f'python "{command_path}" "%1"')
            # Вывод сообщения об успешном добавлении
        QtWidgets.QMessageBox.information(None, 'Успех', 'Пункт меню успешно добавлен!')
    except Exception as ex:
        # Логирование ошибки с помощью logger.error
        logger.error('Ошибка при добавлении пункта меню в реестр', exc_info=ex)
        QtWidgets.QMessageBox.critical(None, 'Ошибка', f'Ошибка: {ex}')


def remove_context_menu_item():
    """Удаляет пункт контекстного меню 'hypo AI assistant'.

    Удаляет ключ реестра, отвечающий за отображение пользовательского пункта меню,
    эффективно удаляя его из контекстного меню.

    Подробности о пути в реестре:
        - `key_path`: Directory\\Background\\shell\\hypo_AI_assistant
            Этот путь определяет пользовательский пункт меню для удаления.

    Raises:
        Выводит предупреждение, если пункт меню не найден, и ошибку, если операция не удалась.
    """
    key_path = r'Directory\\Background\\shell\\hypo_AI_assistant'

    try:
        reg.DeleteKey(reg.HKEY_CLASSES_ROOT, key_path)
        # Вывод сообщения об успешном удалении
        QtWidgets.QMessageBox.information(None, 'Успех', 'Пункт меню успешно удален!')
    except FileNotFoundError:
          # Вывод предупреждения, если пункт меню не найден
        QtWidgets.QMessageBox.warning(None, 'Предупреждение', 'Пункт меню не найден.')
    except Exception as e:
        # Логирование ошибки с помощью logger.error
        logger.error('Ошибка при удалении пункта меню из реестра', exc_info=e)
        QtWidgets.QMessageBox.critical(None, 'Ошибка', f'Ошибка: {e}')


class ContextMenuManager(QtWidgets.QWidget):
    """
    Главное окно приложения для управления пользовательским пунктом контекстного меню.

    :param parent: Родительский виджет (по умолчанию None).

    :ivar layout: Основной макет для размещения виджетов.
    :vartype layout: QtWidgets.QVBoxLayout
    :ivar add_button: Кнопка для добавления пункта меню.
    :vartype add_button: QtWidgets.QPushButton
    :ivar remove_button: Кнопка для удаления пункта меню.
    :vartype remove_button: QtWidgets.QPushButton
    :ivar exit_button: Кнопка для выхода из приложения.
    :vartype exit_button: QtWidgets.QPushButton

    :example:
        >>> app = QtWidgets.QApplication([])
        >>> window = ContextMenuManager()
        >>> window.show()
        >>> app.exec()
    """

    def __init__(self):
        """Инициализирует главное окно приложения."""
        super().__init__()
        self.initUI()

    def initUI(self):
        """Инициализирует пользовательский интерфейс с кнопками для добавления, удаления и выхода."""
        self.setWindowTitle('Управление контекстным меню')
        layout = QtWidgets.QVBoxLayout()

        add_button = QtWidgets.QPushButton('Добавить пункт меню')
        add_button.clicked.connect(add_context_menu_item)
        layout.addWidget(add_button)

        remove_button = QtWidgets.QPushButton('Удалить пункт меню')
        remove_button.clicked.connect(remove_context_menu_item)
        layout.addWidget(remove_button)

        exit_button = QtWidgets.QPushButton('Выход')
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = ContextMenuManager()
    window.show()
    app.exec()
```