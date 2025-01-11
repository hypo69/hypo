## Анализ кода модуля `campaign.py`

**Качество кода**
6
- Плюсы
    - Код имеет базовую структуру для создания GUI приложения с использованием PyQt6.
    - Присутствует разделение на методы для настройки UI, загрузки файла и создания виджетов.
    - Используется асинхронный слот для подготовки кампании.
- Минусы
    - Отсутствует обработка ошибок с использованием `logger.error`.
    - Нет документации для функций и методов.
    - Не используются `from src.logger.logger import logger`.
    - Не все строки в коде соответствуют PEP8, например, `if widget not in [self.open_button, self.file_name_label, self.prepare_button]:`.
    - Не используется константы для путей к файлам
    - Отсутсвует описание модуля

**Рекомендации по улучшению**
1. Добавить описание модуля в начале файла.
2. Добавить документацию для каждой функции, метода и класса в формате RST.
3. Заменить использование `QtWidgets.QMessageBox` на `logger.error` для обработки ошибок, где это возможно.
4. Использовать `from src.logger.logger import logger` для логирования ошибок.
5. Привести код в соответствие с PEP8, исправить `if widget not in [self.open_button, self.file_name_label, self.prepare_button]:` на `if widget not in (self.open_button, self.file_name_label, self.prepare_button):`
6. Вынести `c:/user/documents/repos/hypotez/data/aliexpress/campaigns` в константу
7. Использовать `j_dumps` для сохранения данных

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

"""
Модуль для создания и редактирования кампаний AliExpress.
=======================================================

Этот модуль предоставляет графический интерфейс для редактирования и подготовки кампаний AliExpress.
Он позволяет загружать данные кампаний из JSON-файлов, редактировать их и подготавливать к использованию.

Класс :class:`CampaignEditor` является основным компонентом этого модуля и содержит методы для
создания интерфейса, загрузки данных, редактирования полей и подготовки кампаний.

Пример использования
--------------------

.. code-block:: python

    app = QtWidgets.QApplication(sys.argv)
    window = CampaignEditor()
    window.show()
    sys.exit(app.exec())
"""

import asyncio
import sys
from pathlib import Path
from types import SimpleNamespace

from PyQt6 import QtWidgets, QtGui, QtCore
from qasync import QEventLoop, asyncSlot

from src.utils.jjson import j_loads_ns, j_dumps
from src.suppliers.aliexpress.campaign import AliCampaignEditor
from styles import set_fixed_size
from src.logger.logger import logger # импорт logger

CAMPAIGNS_PATH = "c:/user/documents/repos/hypotez/data/aliexpress/campaigns"

class CampaignEditor(QtWidgets.QWidget):
    """
    Виджет для редактирования кампаний.

    :ivar data: SimpleNamespace - данные кампании.
    :ivar current_campaign_file: str - путь к текущему файлу кампании.
    :ivar editor: AliCampaignEditor - редактор кампаний.

    :param parent: QWidget - родительский виджет.
    :param main_app: QtWidgets.QApplication - главное приложение.
    """
    data: SimpleNamespace = None
    current_campaign_file: str = None
    editor: AliCampaignEditor

    def __init__(self, parent=None, main_app=None):
        """
        Инициализирует виджет CampaignEditor.

        Args:
            parent (QWidget, optional): Родительский виджет. Defaults to None.
            main_app (QtWidgets.QApplication, optional): Главное приложение. Defaults to None.
        """
        super().__init__(parent)
        self.main_app = main_app  # Сохранение экземпляра MainApp
        self.setup_ui()
        self.setup_connections()

    def setup_ui(self):
        """
        Настраивает пользовательский интерфейс.
        """
        self.setWindowTitle('Campaign Editor')
        self.resize(1800, 800)

        # Создание QScrollArea
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        # Создание QWidget для контента scroll area
        self.scroll_content_widget = QtWidgets.QWidget()
        self.scroll_area.setWidget(self.scroll_content_widget)

        # Создание layout для scroll content widget
        self.layout = QtWidgets.QGridLayout(self.scroll_content_widget)
        self.layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        # Определение UI компонентов
        self.open_button = QtWidgets.QPushButton('Open JSON File')
        self.open_button.clicked.connect(self.open_file)
        set_fixed_size(self.open_button, width=250, height=25)

        self.file_name_label = QtWidgets.QLabel('No file selected')
        set_fixed_size(self.file_name_label, width=500, height=25)

        self.prepare_button = QtWidgets.QPushButton('Prepare Campaign')
        self.prepare_button.clicked.connect(self.prepare_campaign)
        set_fixed_size(self.prepare_button, width=250, height=25)

        # Добавление компонентов в layout
        self.layout.addWidget(self.open_button, 0, 0)
        self.layout.addWidget(self.file_name_label, 0, 1)
        self.layout.addWidget(self.prepare_button, 1, 0, 1, 2)  # Занимает две колонки

        # Добавление scroll area в основной layout виджета
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.scroll_area)
        self.setLayout(main_layout)

    def setup_connections(self):
        """
        Настраивает связи сигнал-слот.
        """
        pass

    def open_file(self):
        """
         Открывает диалоговое окно выбора файла для загрузки JSON-файла.
        """
        campaign_file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            'Open JSON File',
            CAMPAIGNS_PATH,
            'JSON files (*.json)'
        )
        if not campaign_file:
            return

        self.load_file(campaign_file)

    def load_file(self, campaign_file):
        """
        Загружает JSON-файл.

        Args:
            campaign_file (str): Путь к файлу кампании.
        """
        try:
            self.data = j_loads_ns(campaign_file)
            self.current_campaign_file = campaign_file
            self.file_name_label.setText(f'File: {self.current_campaign_file}')
            self.create_widgets(self.data)
            self.editor = AliCampaignEditor(campaign_file=campaign_file)
        except Exception as ex:
            logger.error(f'Failed to load JSON file: {ex}')
            QtWidgets.QMessageBox.critical(self, 'Error', f'Failed to load JSON file: {ex}')

    def create_widgets(self, data):
        """
        Создает виджеты на основе данных, загруженных из JSON-файла.

        Args:
            data (SimpleNamespace): Данные кампании.
        """
        layout = self.layout

        # Удаление предыдущих виджетов, кроме кнопок открытия файла и метки имени файла
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget not in (self.open_button, self.file_name_label, self.prepare_button):
                widget.deleteLater()

        self.title_input = QtWidgets.QLineEdit(data.title)
        layout.addWidget(QtWidgets.QLabel('Title:'), 2, 0)
        layout.addWidget(self.title_input, 2, 1)
        set_fixed_size(self.title_input, width=500, height=25)

        self.description_input = QtWidgets.QLineEdit(data.description)
        layout.addWidget(QtWidgets.QLabel('Description:'), 3, 0)
        layout.addWidget(self.description_input, 3, 1)
        set_fixed_size(self.description_input, width=500, height=25)

        self.promotion_name_input = QtWidgets.QLineEdit(data.promotion_name)
        layout.addWidget(QtWidgets.QLabel('Promotion Name:'), 4, 0)
        layout.addWidget(self.promotion_name_input, 4, 1)
        set_fixed_size(self.promotion_name_input, width=500, height=25)

    @asyncSlot()
    async def prepare_campaign(self):
        """
        Асинхронно подготавливает кампанию.
        """
        if self.editor:
            try:
                await self.editor.prepare()
                QtWidgets.QMessageBox.information(self, 'Success', 'Campaign prepared successfully.')
            except Exception as ex:
                logger.error(f'Failed to prepare campaign: {ex}')
                QtWidgets.QMessageBox.critical(self, 'Error', f'Failed to prepare campaign: {ex}')