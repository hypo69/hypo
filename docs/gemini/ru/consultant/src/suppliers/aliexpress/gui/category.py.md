# Анализ кода модуля `category.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован с использованием классов и методов.
    - Присутствует асинхронная обработка задач.
    - Используются `QMessageBox` для обратной связи с пользователем.
    - Применяется `j_loads_ns` для загрузки JSON.
-  Минусы
    - Отсутствует обработка ошибок с использованием `logger.error`.
    - Комментарии в формате reStructuredText (RST) отсутствуют.
    - Не все импорты приведены в соответствие с ранее обработанными файлами.
    - Жестко задан путь к файлам для открытия `c:/user/documents/repos/hypotez/data/aliexpress/campaigns`.

**Рекомендации по улучшению**

1.  Добавить недостающие импорты, включая `logger` из `src.logger.logger`.
2.  Заменить использование `QMessageBox` на логирование ошибок через `logger.error`.
3.  Переписать все комментарии и docstring в формате reStructuredText (RST).
4.  Использовать более гибкий путь для открытия файлов, например, через переменную окружения или параметр конфигурации.
5.  Добавить проверку существования `self.editor` перед его использованием.
6.  Переименовать `campaign_file` в `file_path` для единообразия.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с редактором категорий AliExpress.
=========================================================================================

Этот модуль предоставляет графический интерфейс для подготовки рекламных кампаний на AliExpress.
Он позволяет загружать JSON файлы, отображать информацию о кампаниях и категориях, а также
асинхронно подготавливать категории для рекламных кампаний.

Модуль использует `PyQt6` для создания графического интерфейса, `qasync` для асинхронного
программирования, и `src.utils.jjson` для работы с JSON файлами.

Пример использования
--------------------

Пример использования класса `CategoryEditor`:

.. code-block:: python

    app = QtWidgets.QApplication(sys.argv)
    window = CategoryEditor()
    window.show()
    sys.exit(app.exec())
"""
import sys
import asyncio
from pathlib import Path
from types import SimpleNamespace
from PyQt6 import QtWidgets, QtGui, QtCore
from qasync import QEventLoop, asyncSlot

#  Импорт необходимых модулей
from src.utils.jjson import j_loads_ns, j_dumps
from src.suppliers.aliexpress.campaign import AliCampaignEditor
from src.logger.logger import logger

MODE = 'dev'
# Window interface for preparing advertising campaigns


class CategoryEditor(QtWidgets.QWidget):
    """
    Класс для создания графического интерфейса редактора категорий.

    :ivar campaign_name: Имя рекламной кампании.
    :vartype campaign_name: str
    :ivar data: Данные кампании, загруженные из JSON.
    :vartype data: SimpleNamespace
    :ivar language: Язык кампании.
    :vartype language: str
    :ivar currency: Валюта кампании.
    :vartype currency: str
    :ivar file_path: Путь к файлу с данными кампании.
    :vartype file_path: str
    :ivar editor: Экземпляр класса AliCampaignEditor.
    :vartype editor: AliCampaignEditor
    """
    campaign_name: str = None
    data: SimpleNamespace = None
    language: str = 'EN'
    currency: str = 'USD'
    file_path: str = None
    editor: AliCampaignEditor

    def __init__(self, parent=None, main_app=None):
        """
        Инициализирует главное окно редактора категорий.

        :param parent: Родительский виджет.
        :type parent: QtWidgets.QWidget, optional
        :param main_app: Экземпляр главного приложения.
        :type main_app: QtWidgets.QApplication, optional
        """
        super().__init__(parent)
        self.main_app = main_app  # Сохраняет экземпляр MainApp

        self.setup_ui()
        self.setup_connections()

    def setup_ui(self):
        """
        Настраивает пользовательский интерфейс.
        """
        self.setWindowTitle("Category Editor")
        self.resize(1800, 800)

        # Определяет компоненты интерфейса
        self.open_button = QtWidgets.QPushButton("Open JSON File")
        #  Устанавливает соединение сигнала нажатия кнопки с методом open_file
        self.open_button.clicked.connect(self.open_file)

        self.file_name_label = QtWidgets.QLabel("No file selected")

        self.prepare_all_button = QtWidgets.QPushButton("Prepare All Categories")
        #  Устанавливает соединение сигнала нажатия кнопки с методом prepare_all_categories_async
        self.prepare_all_button.clicked.connect(self.prepare_all_categories_async)

        self.prepare_specific_button = QtWidgets.QPushButton("Prepare Category")
        #  Устанавливает соединение сигнала нажатия кнопки с методом prepare_category_async
        self.prepare_specific_button.clicked.connect(self.prepare_category_async)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.open_button)
        layout.addWidget(self.file_name_label)
        layout.addWidget(self.prepare_all_button)
        layout.addWidget(self.prepare_specific_button)

        self.setLayout(layout)

    def setup_connections(self):
        """
        Устанавливает соединения сигнал-слот.
        """
        pass

    def open_file(self):
        """
        Открывает диалог выбора файла для загрузки JSON файла.
        """
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Open JSON File",
            "c:/user/documents/repos/hypotez/data/aliexpress/campaigns",
            "JSON files (*.json)"
        )
        if not file_path:
            return  # Если файл не выбран, выход

        self.load_file(file_path)

    def load_file(self, file_path):
        """
        Загружает JSON файл и инициализирует необходимые данные.

        :param file_path: Путь к файлу с данными кампании.
        :type file_path: str
        """
        try:
            #  Загрузка данных из JSON файла
            self.data = j_loads_ns(file_path)
            self.file_path = file_path
            self.file_name_label.setText(f"File: {self.file_path}")
            self.campaign_name = self.data.campaign_name
            path = Path(file_path)
             #  Извлекает имя файла без расширения
            self.language = path.stem
            self.editor = AliCampaignEditor(campaign_file=file_path)
            self.create_widgets(self.data)
        except Exception as ex:
            #  Логирование ошибки загрузки файла
            logger.error(f'Не удалось загрузить JSON файл: {ex}', exc_info=True)
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load JSON file: {ex}")
            

    def create_widgets(self, data):
        """
        Создает виджеты на основе загруженных данных из JSON файла.

        :param data: Данные кампании, загруженные из JSON.
        :type data: SimpleNamespace
        """
        layout = self.layout()

        # Удаляет предыдущие виджеты, кроме кнопок open и label
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget not in [self.open_button, self.file_name_label, self.prepare_all_button, self.prepare_specific_button]:
                widget.deleteLater()

        title_label = QtWidgets.QLabel(f"Title: {data.title}")
        layout.addWidget(title_label)

        campaign_label = QtWidgets.QLabel(f"Campaign Name: {data.campaign_name}")
        layout.addWidget(campaign_label)

        #  Проходит по всем категориям и добавляет их на форму
        for category in data.categories:
            category_label = QtWidgets.QLabel(f"Category: {category.name}")
            layout.addWidget(category_label)

    @asyncSlot()
    async def prepare_all_categories_async(self):
        """
        Асинхронно подготавливает все категории.
        """
        if not self.editor:
            logger.error('Редактор не инициализирован')
            return
        try:
            #  Подготавливает все категории
            await self.editor.prepare_all_categories()
            QtWidgets.QMessageBox.information(self, "Success", "All categories prepared successfully.")
        except Exception as ex:
            #  Логирование ошибки подготовки всех категорий
            logger.error(f'Не удалось подготовить все категории: {ex}', exc_info=True)
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to prepare all categories: {ex}")

    @asyncSlot()
    async def prepare_category_async(self):
        """
        Асинхронно подготавливает конкретную категорию.
        """
        if not self.editor:
             #  Логирование ошибки, если редактор не инициализирован
            logger.error('Редактор не инициализирован')
            return
        try:
            #  Подготавливает конкретную категорию
            await self.editor.prepare_category(self.data.campaign_name)
            QtWidgets.QMessageBox.information(self, "Success", "Category prepared successfully.")
        except Exception as ex:
            #  Логирование ошибки подготовки категории
            logger.error(f'Не удалось подготовить категорию: {ex}', exc_info=True)
            QtWidgets.QMessageBox.critical(self, "Error", f"Failed to prepare category: {ex}")
```