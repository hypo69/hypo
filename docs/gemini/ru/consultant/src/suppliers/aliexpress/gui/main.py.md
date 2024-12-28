# Анализ кода модуля `main.py`

**Качество кода**
8
-  Плюсы
    -  Код хорошо структурирован с использованием классов и функций, что повышает читаемость и поддерживаемость.
    -  Используется `PyQt6` для создания графического интерфейса, что является хорошей практикой для настольных приложений.
    -  Присутствует разделение на вкладки, что делает интерфейс более удобным для пользователя.
    -  Логика работы с файлами вынесена в отдельные методы `open_file`, `save_file`, `load_file`.
    -  Используется `QEventLoop` для асинхронной работы, что предотвращает зависание интерфейса.
    -  Обработка ошибок реализована с использованием `try-except` блоков.
    -  Реализованы функции копирования и вставки текста из виджетов.
-  Минусы
    -  Отсутствует документация в формате reStructuredText (RST).
    -  Некоторые комментарии не соответствуют стандарту RST.
    -  Обработка ошибок реализована через `QMessageBox`, что не всегда удобно. Лучше использовать `logger.error`.
    -  Используется стандартный `json.load` вместо `j_loads_ns` из `src.utils.jjson`.
    -  Нет импорта `logger`.
    -  В методе `load_file` не корректно обрабатывается исключение, не используется логирование.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Добавить docstring в формате RST для всех модулей, классов, методов и функций.
2.  **Импорты**:
    -   Добавить `from src.logger.logger import logger` для логирования ошибок.
    -   Заменить `from src.utils.jjson import j_loads_ns, j_dumps` на `from src.utils.jjson import j_loads, j_dumps`
3.  **Обработка ошибок**:
    -   Заменить `QMessageBox.critical` на `logger.error` для логирования ошибок.
    -   Убрать избыточное использование `try-except` блоков, где это возможно.
4.  **Использование `j_loads`**:
    -   Использовать `j_loads` вместо `json.load` при чтении файлов.
5.  **Рефакторинг**:
    -   Вынести повторяющийся код по проверке виджетов в отдельную функцию.
    -   Удалить неиспользуемые переменные и импорты.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Главный модуль графического интерфейса для управления рекламными кампаниями.
============================================================================

Этот модуль содержит класс :class:`MainApp`, который является основным окном приложения
и позволяет управлять различными редакторами, такими как редактор JSON, редактор кампаний и редактор продуктов.

Пример использования
--------------------

Пример запуска приложения::

    if __name__ == "__main__":
        main()
"""
MODE = 'dev'

import asyncio
import sys
from PyQt6 import QtWidgets, QtGui, QtCore
from qasync import QEventLoop
from pathlib import Path
# from src.utils.jjson import j_loads_ns, j_dumps # заменен на
from src.utils.jjson import j_loads, j_dumps
from product import ProductEditor
from campaign import CampaignEditor
from category import CategoryEditor
from src.suppliers.aliexpress.campaign import AliCampaignEditor
from styles import set_fixed_size
from src.logger.logger import logger

class MainApp(QtWidgets.QMainWindow):
    """
    Основной класс приложения, представляющий главное окно с вкладками.

    :param QtWidgets.QMainWindow: Родительский класс.
    """
    def __init__(self):
        """
        Инициализирует главное окно приложения с вкладками.
        """
        super().__init__()
        self.setWindowTitle("Main Application with Tabs")
        self.setGeometry(100, 100, 1800, 800)

        self.tab_widget = QtWidgets.QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # Создание вкладки редактора JSON и добавление её на панель вкладок
        self.tab1 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab1, "JSON Editor")
        self.promotion_app = CampaignEditor(self.tab1, self)

        # Создание вкладки редактора кампаний и добавление её на панель вкладок
        self.tab2 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab2, "Campaign Editor")
        self.campaign_editor_app = CategoryEditor(self.tab2, self)

        # Создание вкладки редактора продуктов и добавление её на панель вкладок
        self.tab3 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab3, "Product Editor")
        self.product_editor_app = ProductEditor(self.tab3, self)

        self.create_menubar()

    def create_menubar(self):
        """
        Создает меню с опциями для операций с файлами и командами редактирования.
        """
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")
        open_action = QtGui.QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        save_action = QtGui.QAction("Save", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        exit_action = QtGui.QAction("Exit", self)
        exit_action.triggered.connect(self.exit_application)
        file_menu.addAction(exit_action)

        edit_menu = menubar.addMenu("Edit")
        copy_action = QtGui.QAction("Copy", self)
        copy_action.triggered.connect(self.copy)
        edit_menu.addAction(copy_action)
        paste_action = QtGui.QAction("Paste", self)
        paste_action.triggered.connect(self.paste)
        edit_menu.addAction(paste_action)

        open_product_action = QtGui.QAction("Open Product File", self)
        open_product_action.triggered.connect(self.product_editor_app.open_file)
        file_menu.addAction(open_product_action)

    def open_file(self):
        """
        Открывает диалоговое окно для выбора и загрузки JSON-файла.
        """
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open File", "", "JSON files (*.json)")
        if not file_path:
            return

        if self.tab_widget.currentIndex() == 0:
            self.load_file(file_path)

    def save_file(self):
        """
        Сохраняет текущий файл в зависимости от выбранной вкладки.
        """
        current_index = self.tab_widget.currentIndex()
        if current_index == 0:
            self.promotion_app.save_changes()
        elif current_index == 2:
            self.product_editor_app.save_product()

    def exit_application(self):
        """
        Закрывает приложение.
        """
        self.close()

    def _check_text_widget_focus(self):
       """
       Проверяет, является ли виджет в фокусе текстовым виджетом.

       :return: True, если виджет является текстовым, иначе False.
       :rtype: bool
       """
       widget = self.focusWidget()
       return isinstance(widget, (QtWidgets.QLineEdit, QtWidgets.QTextEdit, QtWidgets.QPlainTextEdit))


    def copy(self):
        """
        Копирует выделенный текст в буфер обмена.
        """
        if self._check_text_widget_focus():
            self.focusWidget().copy()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "No text widget in focus to copy.")

    def paste(self):
        """
        Вставляет текст из буфера обмена.
        """
        if self._check_text_widget_focus():
            self.focusWidget().paste()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "No text widget in focus to paste.")

    def load_file(self, campaign_file):
        """
        Загружает JSON-файл.
        
        :param campaign_file: Путь к файлу.
        :type campaign_file: str
        """
        try:
            # Код выполняет загрузку файла в приложение promotion_app
            self.promotion_app.load_file(campaign_file)
        except Exception as ex:
            # Код логирует ошибку, возникшую при загрузке файла
            logger.error(f"Failed to load JSON file: {ex}")
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load JSON file: {ex}")


def main():
    """
    Инициализирует и запускает приложение.
    """
    app = QtWidgets.QApplication(sys.argv)

    # Создание цикла событий для асинхронных операций
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    main_app = MainApp()
    main_app.show()

    # Запуск цикла событий
    with loop:
        loop.run_forever()

if __name__ == "__main__":
    main()
```