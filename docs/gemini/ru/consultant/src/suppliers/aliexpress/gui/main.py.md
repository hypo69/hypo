## Анализ кода модуля `main.py`

**Качество кода**
8/10
- Плюсы
    - Код хорошо структурирован и разделен на классы, что способствует его читаемости и поддержке.
    - Используется асинхронный подход, что улучшает производительность приложения.
    - Присутствуют комментарии, объясняющие назначение основных частей кода.
- Минусы
    - Отсутствует описание модуля в начале файла.
    - Не хватает docstring для методов и классов.
    - Есть стандартные блоки `try-except`, которые можно заменить на обработку через `logger.error`.
    - Используется `j_loads_ns` без импорта.
    - Не все функции имеют комментарии в формате RST.
    - Используются двойные кавычки в операциях вывода.
    - Не используется форматирование строк f-string.

**Рекомендации по улучшению**
1. Добавить описание модуля в начале файла.
2. Добавить docstring для всех классов, методов и переменных.
3. Заменить стандартные блоки `try-except` на обработку ошибок через `logger.error`.
4.  Импортировать `j_loads_ns` из `src.utils.jjson`.
5.  Использовать одинарные кавычки для строк в коде и двойные для операций вывода.
6.  Использовать f-строки для форматирования вывода.
7.  Добавить `from src.logger.logger import logger`.
8.  Пересмотреть использование `QtWidgets.QMessageBox`, заменив на `logger`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для запуска основного GUI приложения.
=========================================================================================

Этот модуль содержит класс :class:`MainApp`, который представляет собой главное окно приложения
с вкладками для редактирования JSON, кампаний и продуктов.

Пример использования
--------------------

Пример запуска приложения:

.. code-block:: python

    if __name__ == "__main__":
        main()
"""

import asyncio
import sys
from pathlib import Path
from typing import Any

from PyQt6 import QtWidgets, QtGui
from qasync import QEventLoop

# from src.utils.jjson import j_loads_ns, j_dumps #TODO: Убрать неиспользуемый импорт
from src.suppliers.aliexpress.gui.product import ProductEditor
from src.suppliers.aliexpress.gui.campaign import CampaignEditor
from src.suppliers.aliexpress.gui.category import CategoryEditor
from src.suppliers.aliexpress.campaign import AliCampaignEditor
from src.suppliers.aliexpress.gui.styles import set_fixed_size
from src.logger.logger import logger # Import logger


class MainApp(QtWidgets.QMainWindow):
    """
    Главное окно приложения с вкладками для редактирования JSON, кампаний и продуктов.

    Args:
        QtWidgets.QMainWindow: Базовый класс для создания главного окна приложения.

    Attributes:
        tab_widget (QtWidgets.QTabWidget): Виджет для отображения вкладок.
        promotion_app (CampaignEditor): Редактор JSON.
        campaign_editor_app (CategoryEditor): Редактор кампаний.
        product_editor_app (ProductEditor): Редактор продуктов.
    """
    def __init__(self):
        """
        Инициализирует главное окно приложения с вкладками.
        """
        super().__init__()
        self.setWindowTitle('Main Application with Tabs')
        self.setGeometry(100, 100, 1800, 800)

        self.tab_widget = QtWidgets.QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # Создание вкладки "JSON Editor"
        self.tab1 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab1, 'JSON Editor')
        self.promotion_app = CampaignEditor(self.tab1, self)

        # Создание вкладки "Campaign Editor"
        self.tab2 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab2, 'Campaign Editor')
        self.campaign_editor_app = CategoryEditor(self.tab2, self)

        # Создание вкладки "Product Editor"
        self.tab3 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab3, 'Product Editor')
        self.product_editor_app = ProductEditor(self.tab3, self)

        self.create_menubar()

    def create_menubar(self):
        """
        Создает меню с опциями для работы с файлами и редактирования.
        """
        menubar = self.menuBar()

        file_menu = menubar.addMenu('File')
        open_action = QtGui.QAction('Open', self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        save_action = QtGui.QAction('Save', self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        exit_action = QtGui.QAction('Exit', self)
        exit_action.triggered.connect(self.exit_application)
        file_menu.addAction(exit_action)

        edit_menu = menubar.addMenu('Edit')
        copy_action = QtGui.QAction('Copy', self)
        copy_action.triggered.connect(self.copy)
        edit_menu.addAction(copy_action)
        paste_action = QtGui.QAction('Paste', self)
        paste_action.triggered.connect(self.paste)
        edit_menu.addAction(paste_action)

        open_product_action = QtGui.QAction('Open Product File', self)
        open_product_action.triggered.connect(self.product_editor_app.open_file)
        file_menu.addAction(open_product_action)

    def open_file(self):
        """
        Открывает диалоговое окно для выбора и загрузки JSON файла.
        """
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Open File', '', 'JSON files (*.json)')
        if not file_path:
            return

        if self.tab_widget.currentIndex() == 0:
            self.load_file(file_path)

    def save_file(self):
        """
        Сохраняет текущий файл в зависимости от активной вкладки.
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

    def copy(self):
        """
        Копирует выделенный текст в буфер обмена.
        """
        widget = self.focusWidget()
        if isinstance(widget, (QtWidgets.QLineEdit, QtWidgets.QTextEdit, QtWidgets.QPlainTextEdit)):
            widget.copy()
        else:
            QtWidgets.QMessageBox.warning(self, 'Warning', 'No text widget in focus to copy.')

    def paste(self):
        """
        Вставляет текст из буфера обмена.
        """
        widget = self.focusWidget()
        if isinstance(widget, (QtWidgets.QLineEdit, QtWidgets.QTextEdit, QtWidgets.QPlainTextEdit)):
            widget.paste()
        else:
            QtWidgets.QMessageBox.warning(self, 'Warning', 'No text widget in focus to paste.')

    def load_file(self, campaign_file):
        """
        Загружает JSON файл.

        Args:
            campaign_file (str): Путь к JSON файлу.
        """
        try:
            self.promotion_app.load_file(campaign_file)
        except Exception as ex:
            logger.error(f'Failed to load JSON file: {ex}') # Use logger instead of QMessageBox
            # QtWidgets.QMessageBox.critical(self, 'Error', f'Failed to load JSON file: {ex}')  #TODO: Заменить на логгер

def main():
    """
    Инициализирует и запускает приложение.
    """
    app = QtWidgets.QApplication(sys.argv)

    # Создание event loop для асинхронных операций
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    main_app = MainApp()
    main_app.show()

    # Запуск event loop
    with loop:
        loop.run_forever()

if __name__ == '__main__':
    main()