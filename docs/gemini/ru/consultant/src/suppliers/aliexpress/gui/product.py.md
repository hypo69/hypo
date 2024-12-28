# Анализ кода модуля `product`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован, используется `PyQt6` для создания GUI, есть отдельные функции для настройки интерфейса и обработки данных.
    - Присутствует обработка ошибок при загрузке файла и подготовке продукта.
    - Используется `j_loads_ns` для загрузки данных из JSON.
    - Асинхронный метод для подготовки продукта.
- Минусы
    - Отсутствуют docstring для модуля, классов и методов.
    - Не используется `logger` для логирования ошибок.
    - Нет явной обработки ошибок при открытии файла.
    - Не все комментарии соответствуют формату reStructuredText.
    - Импорт `header` и переменная `MODE` не используются.
    - Отсутствует обработка путей к файлам в разных ОС
    - Магические строки в пути к файлу

**Рекомендации по улучшению**
1.  Добавить docstring для модуля, классов и методов в формате reStructuredText (RST).
2.  Использовать `logger` из `src.logger.logger` для логирования ошибок вместо `QtWidgets.QMessageBox`.
3.  Убрать импорт `header` и переменную `MODE`, если они не используются.
4.  Добавить проверку на существование `file_path` перед его использованием.
5.  Сделать `QtWidgets.QMessageBox` отдельным методом для гибкости.
6.  Упростить удаление виджетов.
7.  Избегать дублирования кода обработки исключений.
8.  Убрать магические строки в путях к файлам.
9.  Добавить обработку путей к файлам в разных ОС.
10. Убрать неиспользуемый `setup_connections`

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для создания и редактирования продуктов.
=========================================================================================

Этот модуль предоставляет класс :class:`ProductEditor`, который используется для создания
и редактирования информации о продуктах, загружаемой из JSON файлов.

:platform: Windows, Unix
:synopsis:
    Интерфейс для редактирования продуктов.

Пример использования
--------------------

Пример использования класса `ProductEditor`:

.. code-block:: python

    app = QtWidgets.QApplication(sys.argv)
    editor = ProductEditor()
    editor.show()
    sys.exit(app.exec())
"""

import sys
from pathlib import Path
from types import SimpleNamespace
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtCore import pyqtSlot as asyncSlot
from src.utils.jjson import j_loads_ns
from src.suppliers.aliexpress.campaign import AliCampaignEditor
from src.logger.logger import logger
import os


class ProductEditor(QtWidgets.QWidget):
    """
    Виджет редактора продукта.

    :ivar data: Данные продукта, загруженные из JSON файла.
    :vartype data: SimpleNamespace
    :ivar language: Язык продукта.
    :vartype language: str
    :ivar currency: Валюта продукта.
    :vartype currency: str
    :ivar file_path: Путь к файлу с данными продукта.
    :vartype file_path: str
    :ivar editor: Экземпляр редактора кампании AliExpress.
    :vartype editor: AliCampaignEditor
    """
    data: SimpleNamespace = None
    language: str = 'EN'
    currency: str = 'USD'
    file_path: str = None
    editor: AliCampaignEditor

    def __init__(self, parent=None, main_app=None):
        """
        Инициализация виджета ProductEditor.

        :param parent: Родительский виджет.
        :type parent: QtWidgets.QWidget
        :param main_app: Экземпляр главного приложения.
        :type main_app: QtWidgets.QWidget
        """
        super().__init__(parent)
        self.main_app = main_app  # Сохранение экземпляра MainApp

        self.setup_ui()
        # self.setup_connections()  # Удалено, т.к. не используется

    def setup_ui(self):
        """
        Настройка пользовательского интерфейса.
        """
        self.setWindowTitle("Product Editor")
        self.resize(1800, 800)

        # Определение компонентов UI
        self.open_button = QtWidgets.QPushButton("Open JSON File")
        self.open_button.clicked.connect(self.open_file)

        self.file_name_label = QtWidgets.QLabel("No file selected")

        self.prepare_button = QtWidgets.QPushButton("Prepare Product")
        self.prepare_button.clicked.connect(self.prepare_product_async)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.open_button)
        layout.addWidget(self.file_name_label)
        layout.addWidget(self.prepare_button)

        self.setLayout(layout)

    # def setup_connections(self):
    #     """
    #     Установка связей сигнал-слот.
    #     """
    #     pass  # Удалено, т.к. не используется

    def open_file(self):
        """
        Открытие диалогового окна для выбора и загрузки JSON файла.
        """
        # Код исполняет открытие диалогового окна для выбора файла
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Open JSON File",
            os.path.join(Path.home(), "Documents", "repos", "hypotez", "data", "aliexpress", "products"),
            "JSON files (*.json)"
        )
        if not file_path:
            return  # Если файл не выбран

        self.load_file(file_path)

    def load_file(self, file_path):
        """
        Загрузка JSON файла.

        :param file_path: Путь к файлу.
        :type file_path: str
        """
        try:
            # Код исполняет загрузку данных из JSON файла
            self.data = j_loads_ns(file_path)
            self.file_path = file_path
            self.file_name_label.setText(f"File: {self.file_path}")
            self.editor = AliCampaignEditor(file_path=file_path)
            self.create_widgets(self.data)
        except Exception as ex:
            # Код исполняет вывод сообщения об ошибке через QMessageBox
            self._show_message('Error', f'Failed to load JSON file: {ex}', QtWidgets.QMessageBox.critical)
            logger.error('Ошибка при загрузке JSON файла', exc_info=ex)

    def create_widgets(self, data):
        """
        Создание виджетов на основе данных, загруженных из JSON файла.

        :param data: Данные продукта.
        :type data: SimpleNamespace
        """
        layout = self.layout()

        # Код исполняет удаление предыдущих виджетов, кроме кнопок
        for i in reversed(range(layout.count())):
             widget = layout.itemAt(i).widget()
             if widget not in [self.open_button, self.file_name_label, self.prepare_button]:
                 widget.deleteLater()


        # Код исполняет добавление виджета с заголовком продукта
        title_label = QtWidgets.QLabel(f"Product Title: {data.title}")
        layout.addWidget(title_label)

        # Код исполняет добавление виджета с деталями продукта
        product_details_label = QtWidgets.QLabel(f"Product Details: {data.details}")
        layout.addWidget(product_details_label)

    @asyncSlot()
    async def prepare_product_async(self):
        """
        Асинхронная подготовка продукта.
        """
        if self.editor:
            try:
                # Код исполняет подготовку продукта через editor
                await self.editor.prepare_product()
                # Код исполняет вывод сообщения об успешной подготовке
                self._show_message('Success', 'Product prepared successfully.', QtWidgets.QMessageBox.information)
            except Exception as ex:
                # Код исполняет вывод сообщения об ошибке при подготовке
                self._show_message('Error', f'Failed to prepare product: {ex}', QtWidgets.QMessageBox.critical)
                logger.error('Ошибка при подготовке продукта', exc_info=ex)

    def _show_message(self, title, message, icon):
         """
         Отображение сообщения пользователю

         :param title: Заголовок сообщения
         :type title: str
         :param message: Текст сообщения
         :type message: str
         :param icon: Тип сообщения (информационное, ошибка)
         :type icon: QtWidgets.QMessageBox
         """
         icon(self, title, message)
```