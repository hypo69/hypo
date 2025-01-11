# Анализ кода модуля `category.py`

**Качество кода**
7
- Плюсы
    - Код имеет базовую структуру PyQt6 приложения.
    - Используются асинхронные операции для подготовки категорий.
    - Присутствует обработка ошибок при загрузке файла и подготовке категорий.
    - Используется `j_loads_ns` для загрузки JSON.
- Минусы
    - Отсутствует документация в формате RST для модуля, классов и методов.
    - Не используются логирование через `logger` вместо `QtWidgets.QMessageBox`.
    - Не все комментарии соответствуют стандарту.
    - Есть жестко заданный путь для открытия файла.
    - Нарушение PEP8 в импортах.
    - Есть неиспользуемые переменные и импорты.

**Рекомендации по улучшению**

1.  Добавить документацию в формате RST для модуля, класса и методов.
2.  Использовать `from src.logger.logger import logger` для логирования ошибок вместо `QtWidgets.QMessageBox`.
3.  Убрать жестко заданный путь к файлу.
4.  Привести импорты к стандартам PEP8.
5.  Удалить неиспользуемые импорты.
6.  Избавится от избыточных блоков `try-except`, заменив их на обработку через `logger.error`.
7.  Добавить более информативные сообщения в лог.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с редактором категорий AliExpress.
======================================================

Этот модуль предоставляет класс `CategoryEditor`, который представляет собой
интерфейс для подготовки рекламных кампаний на AliExpress. Он позволяет
загружать JSON файлы с данными о категориях, отображать информацию о них,
а также запускать асинхронную подготовку категорий.

Пример использования
--------------------

.. code-block:: python

    app = QtWidgets.QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    window = CategoryEditor()
    window.show()
    with loop:
        sys.exit(loop.run_forever())
"""

import sys
import asyncio
from pathlib import Path
from types import SimpleNamespace

from PyQt6 import QtWidgets
from qasync import QEventLoop, asyncSlot

from src.utils.jjson import j_loads_ns
from src.suppliers.aliexpress.campaign import AliCampaignEditor
from src.logger.logger import logger

class CategoryEditor(QtWidgets.QWidget):
    """
    Виджет для редактирования категорий AliExpress.

    :param parent: Родительский виджет.
    :type parent: QtWidgets.QWidget, optional
    :param main_app: Экземпляр главного приложения.
    :type main_app: Any, optional
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

        Сохраняет экземпляр главного приложения, настраивает пользовательский интерфейс и
        соединения между сигналами и слотами.
        """
        super().__init__(parent)
        self.main_app = main_app  # Сохраняет экземпляр MainApp
        self.setup_ui()
        self.setup_connections()

    def setup_ui(self):
        """
        Настраивает пользовательский интерфейс.

        Устанавливает заголовок окна, размеры и создает основные компоненты UI:
        кнопки для открытия файла, подготовки всех и конкретных категорий,
        а также метку для отображения имени файла.
        """
        self.setWindowTitle('Category Editor')
        self.resize(1800, 800)

        # Определяет компоненты UI
        self.open_button = QtWidgets.QPushButton('Open JSON File')
        self.open_button.clicked.connect(self.open_file)

        self.file_name_label = QtWidgets.QLabel('No file selected')

        self.prepare_all_button = QtWidgets.QPushButton('Prepare All Categories')
        self.prepare_all_button.clicked.connect(self.prepare_all_categories_async)

        self.prepare_specific_button = QtWidgets.QPushButton('Prepare Category')
        self.prepare_specific_button.clicked.connect(self.prepare_category_async)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.open_button)
        layout.addWidget(self.file_name_label)
        layout.addWidget(self.prepare_all_button)
        layout.addWidget(self.prepare_specific_button)

        self.setLayout(layout)

    def setup_connections(self):
        """
        Настраивает соединения между сигналами и слотами.

        В данном случае пока не используется, но может быть расширено
        для дополнительных взаимодействий с UI.
        """
        pass

    def open_file(self):
        """
        Открывает диалоговое окно для выбора и загрузки JSON файла.

        Выводит диалоговое окно открытия файла, позволяя пользователю выбрать
        JSON файл. В случае успешного выбора вызывает метод загрузки файла.
        """
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Open JSON File',
            '', # Убираем жестко заданный путь
            'JSON files (*.json)'
        )
        if not file_path:
            return  # Файл не выбран

        self.load_file(file_path)

    def load_file(self, campaign_file):
        """
        Загружает JSON файл и создает виджеты на основе загруженных данных.

        :param campaign_file: Путь к загружаемому JSON файлу.
        :type campaign_file: str
        """
        try:
            #  код исполняет загрузку данных из JSON файла
            self.data = j_loads_ns(campaign_file)
            self.campaign_file = campaign_file
            self.file_name_label.setText(f'File: {self.campaign_file}')
            self.campaign_name = self.data.campaign_name
            path = Path(campaign_file)
            self.language = path.stem  # Получает имя файла без расширения
            self.editor = AliCampaignEditor(campaign_file=campaign_file)
            self.create_widgets(self.data)
        except Exception as ex:
            # Логируем ошибку при загрузке файла
            logger.error(f'Failed to load JSON file: {ex}', exc_info=True)
            QtWidgets.QMessageBox.critical(self, 'Error', f'Failed to load JSON file: {ex}')


    def create_widgets(self, data):
        """
        Создает виджеты на основе данных, загруженных из JSON файла.

        :param data: Данные из JSON файла, представленные в виде SimpleNamespace.
        :type data: SimpleNamespace
        """
        layout = self.layout()

        # Удаляет предыдущие виджеты, кроме кнопок "Open", "Prepare All", "Prepare Specific" и метки файла
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget not in [self.open_button, self.file_name_label, self.prepare_all_button, self.prepare_specific_button]:
                widget.deleteLater()

        title_label = QtWidgets.QLabel(f'Title: {data.title}')
        layout.addWidget(title_label)

        campaign_label = QtWidgets.QLabel(f'Campaign Name: {data.campaign_name}')
        layout.addWidget(campaign_label)

        # Обработка SimpleNamespace как словаря
        for category in data.categories:
            category_label = QtWidgets.QLabel(f'Category: {category.name}')
            layout.addWidget(category_label)

    @asyncSlot()
    async def prepare_all_categories_async(self):
        """
        Асинхронно подготавливает все категории.

        Вызывает метод подготовки всех категорий в редакторе кампаний и
        выводит сообщение об успехе или ошибке.
        """
        if self.editor:
            try:
                # Код исполняет подготовку всех категорий
                await self.editor.prepare_all_categories()
                QtWidgets.QMessageBox.information(self, 'Success', 'All categories prepared successfully.')
            except Exception as ex:
                # Логируем ошибку при подготовке всех категорий
                logger.error(f'Failed to prepare all categories: {ex}', exc_info=True)
                QtWidgets.QMessageBox.critical(self, 'Error', f'Failed to prepare all categories: {ex}')

    @asyncSlot()
    async def prepare_category_async(self):
        """
        Асинхронно подготавливает конкретную категорию.

        Вызывает метод подготовки конкретной категории в редакторе кампаний и
        выводит сообщение об успехе или ошибке.
        """
        if self.editor:
            try:
                # Код исполняет подготовку выбранной категории
                await self.editor.prepare_category(self.data.campaign_name)
                QtWidgets.QMessageBox.information(self, 'Success', 'Category prepared successfully.')
            except Exception as ex:
                # Логируем ошибку при подготовке категории
                logger.error(f'Failed to prepare category: {ex}', exc_info=True)
                QtWidgets.QMessageBox.critical(self, 'Error', f'Failed to prepare category: {ex}')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    window = CategoryEditor()
    window.show()
    with loop:
        sys.exit(loop.run_forever())
```