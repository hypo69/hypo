# Анализ кода модуля `main.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и разделен на классы и функции, что облегчает понимание и поддержку.
    - Используется `QTabWidget` для организации интерфейса, что удобно для пользователя.
    - Есть обработка событий для меню и действий пользователя.
    - Применение `QEventLoop` для поддержки асинхронных операций.
- Минусы
    - Отсутствует явная обработка ошибок при загрузке и сохранении файлов, что может привести к неожиданному поведению.
    - Не все функции имеют docstring, что затрудняет понимание их назначения.
    - Использования `j_loads` или `j_loads_ns` не обнаружено, вместо этого используется `json.load` что не соответствует инструкции.
    - Нет явного указания типов для переменных и аргументов функций, что снижает читаемость кода.
    - Не используется логгер для записи ошибок и отладочной информации.

**Рекомендации по улучшению**

1.  **Добавить docstring**:
    - Добавить описание модуля в формате reStructuredText (RST).
    - Добавить docstring ко всем функциям и методам.
2.  **Использовать `j_loads_ns`**:
    - Заменить `json.load` на `j_loads_ns` для чтения файлов.
3.  **Обработка ошибок**:
    - Заменить `QtWidgets.QMessageBox.critical` на `logger.error` для логирования ошибок.
    - Добавить `try-except` блоки вокруг операций с файлами и другими потенциально опасными операциями.
4.  **Типизация**:
    - Добавить аннотации типов для аргументов функций и переменных.
5.  **Логирование**:
    - Использовать логгер для записи ошибок и отладочной информации.
6.  **Улучшение комментариев**:
    - Переписать комментарии в формате reStructuredText (RST).

**Оптимизированный код**

```python
"""
Модуль для запуска основного GUI приложения.
=========================================================================================

Этот модуль содержит класс :class:`MainApp`, который является основным окном приложения
и управляет различными редакторами (продуктов, кампаний, категорий).

Пример использования
--------------------

Пример запуска приложения:

.. code-block:: python

    if __name__ == "__main__":
        main()
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

MODE = 'dev'


import asyncio
import sys
from pathlib import Path
from typing import Any
from PyQt6 import QtWidgets, QtGui, QtCore
from qasync import QEventLoop
# from src.utils.jjson import j_loads_ns, j_dumps # TODO: использовать j_loads_ns
from src.suppliers.aliexpress.campaign import AliCampaignEditor
from src.suppliers.aliexpress.gui.product import ProductEditor
from src.suppliers.aliexpress.gui.campaign import CampaignEditor
from src.suppliers.aliexpress.gui.category import CategoryEditor
from src.suppliers.aliexpress.gui.styles import set_fixed_size
from src.logger.logger import logger


class MainApp(QtWidgets.QMainWindow):
    """
    Основное окно приложения с табами для различных редакторов.

    :param QtWidgets.QMainWindow: Базовый класс для главного окна.
    """
    def __init__(self):
        """
        Инициализирует главное окно приложения с табами.
        """
        super().__init__()
        self.setWindowTitle("Main Application with Tabs")
        self.setGeometry(100, 100, 1800, 800)

        self.tab_widget = QtWidgets.QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # Создание таба JSON Editor и добавление его в tab widget
        self.tab1 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab1, "JSON Editor")
        self.promotion_app = CampaignEditor(self.tab1, self)

        # Создание таба Campaign Editor и добавление его в tab widget
        self.tab2 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab2, "Campaign Editor")
        self.campaign_editor_app = CategoryEditor(self.tab2, self)

        # Создание таба Product Editor и добавление его в tab widget
        self.tab3 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab3, "Product Editor")
        self.product_editor_app = ProductEditor(self.tab3, self)

        self.create_menubar()

    def create_menubar(self) -> None:
        """
        Создает меню в верхней части окна с опциями для операций с файлами и редактирования.
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

    def open_file(self) -> None:
        """
        Открывает диалоговое окно для выбора и загрузки JSON файла.
        """
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open File", "", "JSON files (*.json)")
        if not file_path:
            return

        if self.tab_widget.currentIndex() == 0:
            self.load_file(file_path)

    def save_file(self) -> None:
        """
        Сохраняет текущий файл.
        """
        current_index = self.tab_widget.currentIndex()
        if current_index == 0:
            self.promotion_app.save_changes()
        elif current_index == 2:
            self.product_editor_app.save_product()

    def exit_application(self) -> None:
        """
        Закрывает приложение.
        """
        self.close()

    def copy(self) -> None:
        """
        Копирует выбранный текст в буфер обмена.
        """
        widget = self.focusWidget()
        if isinstance(widget, (QtWidgets.QLineEdit, QtWidgets.QTextEdit, QtWidgets.QPlainTextEdit)):
            widget.copy()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "No text widget in focus to copy.")

    def paste(self) -> None:
        """
        Вставляет текст из буфера обмена.
        """
        widget = self.focusWidget()
        if isinstance(widget, (QtWidgets.QLineEdit, QtWidgets.QTextEdit, QtWidgets.QPlainTextEdit)):
            widget.paste()
        else:
            QtWidgets.QMessageBox.warning(self, "Warning", "No text widget in focus to paste.")

    def load_file(self, campaign_file: str) -> None:
        """
        Загружает JSON файл.
        :param campaign_file: Путь к файлу JSON.
        """
        try:
            self.promotion_app.load_file(campaign_file)
        except Exception as ex:
            logger.error(f"Failed to load JSON file: {ex}", exc_info=True) # Заменено на logger.error
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load JSON file: {ex}") # TODO: удалить если нет необходимости показывать ошибку пользователю


def main() -> None:
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


if __name__ == "__main__":
    main()
```