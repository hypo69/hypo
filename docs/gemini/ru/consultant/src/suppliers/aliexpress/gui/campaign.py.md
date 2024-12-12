# Анализ кода модуля `campaign.py`

**Качество кода**
9
-   Плюсы
    -   Код структурирован, использует классы и методы для разделения ответственности.
    -   Используется `QGridLayout` для управления размещением виджетов.
    -   Применяется `QScrollArea` для работы с большим объемом данных.
    -   Используется асинхронность для неблокирующих операций.
    -   Присутствуют docstring для методов.
-   Минусы
    -   Отсутствуют docstring для модуля.
    -   Не все методы имеют подробное описание в docstring.
    -   Используется `QtWidgets.QMessageBox` для отображения ошибок, что может быть не очень удобно при логировании.
    -   Отсутствует явная обработка ошибок при загрузке файла JSON, только `QtWidgets.QMessageBox`.
    -   Не используются константы для размеров виджетов, что затрудняет поддержку и модификацию.
    -   Не используется `logger` для логирования ошибок и действий.
    -   Отсутствуют проверки на наличие данных перед их использованием.

**Рекомендации по улучшению**
1. Добавить docstring для модуля с описанием его назначения и функциональности.
2. Дополнить docstring для каждого метода, включая описание параметров и возвращаемых значений.
3. Использовать `from src.logger.logger import logger` для логирования ошибок вместо `QtWidgets.QMessageBox`.
4. Заменить `QtWidgets.QMessageBox` на логирование с помощью `logger.error` для более детального отслеживания ошибок.
5. Ввести константы для размеров виджетов (например, `WIDGET_WIDTH`, `WIDGET_HEIGHT`) для облегчения дальнейшего изменения размеров.
6. Добавить проверки на наличие данных перед их использованием, чтобы избежать ошибок `AttributeError`.
7. Использовать `j_loads` вместо `j_loads_ns`, если не требуется `SimpleNamespace` (в текущем коде используется `SimpleNamespace`, но явной причины для этого нет).
8. Добавить обработку ошибок при подготовке кампании, включая логирование ошибок с помощью `logger.error`.
9. Добавить возможность сохранения изменений в JSON-файл.
10. Разделить код на более мелкие функции.
11. Использовать `Path` вместо строк для работы с файлами, что более гибко.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для создания и редактирования кампаний AliExpress.
=========================================================================================

Этот модуль предоставляет графический интерфейс для просмотра и редактирования JSON-файлов,
содержащих данные о кампаниях AliExpress. Он позволяет загружать файлы, отображать их содержимое
в виде редактируемых полей и подготавливать кампанию для дальнейшей обработки.

Пример использования
--------------------

Пример создания и отображения окна редактирования кампании:

.. code-block:: python

    app = QtWidgets.QApplication(sys.argv)
    window = CampaignEditor()
    window.show()
    sys.exit(app.exec())
"""
import asyncio
import sys
from pathlib import Path
from PyQt6 import QtWidgets, QtGui, QtCore
from qasync import QEventLoop, asyncSlot
from src.utils.jjson import j_loads #  заменен j_loads_ns на j_loads
from src.suppliers.aliexpress.campaign import AliCampaignEditor
from styles import set_fixed_size
from src.logger.logger import logger # импортирован logger
from typing import Any


MODE = 'dev'

WIDGET_WIDTH = 500 # добавлены константы
WIDGET_HEIGHT = 25
BUTTON_WIDTH = 250

class CampaignEditor(QtWidgets.QWidget):
    """
    Виджет для редактирования кампаний AliExpress.

    :ivar data: Данные кампании, загруженные из JSON файла.
    :vartype data: dict
    :ivar current_campaign_file: Путь к текущему файлу кампании.
    :vartype current_campaign_file: str
    :ivar editor: Объект редактора кампании.
    :vartype editor: AliCampaignEditor
    """
    data: dict = None
    current_campaign_file: str = None
    editor: AliCampaignEditor = None


    def __init__(self, parent=None, main_app=None):
        """
        Инициализирует виджет редактора кампаний.

        :param parent: Родительский виджет.
        :type parent: QtWidgets.QWidget, optional
        :param main_app: Экземпляр главного приложения.
        :type main_app: Any, optional
        """
        super().__init__(parent)
        self.main_app = main_app  # Сохранение экземпляра MainApp
        self.setup_ui()
        self.setup_connections()

    def setup_ui(self):
        """
        Настраивает пользовательский интерфейс.
        """
        self.setWindowTitle("Campaign Editor")
        self.resize(1800, 800)

        # Создание QScrollArea
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        # Создание QWidget для содержимого QScrollArea
        self.scroll_content_widget = QtWidgets.QWidget()
        self.scroll_area.setWidget(self.scroll_content_widget)

        # Создание layout для содержимого QScrollArea
        self.layout = QtWidgets.QGridLayout(self.scroll_content_widget)
        self.layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        # Определение UI компонентов
        self.open_button = QtWidgets.QPushButton("Open JSON File")
        self.open_button.clicked.connect(self.open_file)
        set_fixed_size(self.open_button, width=BUTTON_WIDTH, height=WIDGET_HEIGHT)

        self.file_name_label = QtWidgets.QLabel("No file selected")
        set_fixed_size(self.file_name_label, width=WIDGET_WIDTH, height=WIDGET_HEIGHT)

        self.prepare_button = QtWidgets.QPushButton("Prepare Campaign")
        self.prepare_button.clicked.connect(self.prepare_campaign)
        set_fixed_size(self.prepare_button, width=BUTTON_WIDTH, height=WIDGET_HEIGHT)

        # Добавление компонентов в layout
        self.layout.addWidget(self.open_button, 0, 0)
        self.layout.addWidget(self.file_name_label, 0, 1)
        self.layout.addWidget(self.prepare_button, 1, 0, 1, 2)  # Span across two columns

        # Добавление QScrollArea в основной layout виджета
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(self.scroll_area)
        self.setLayout(main_layout)

    def setup_connections(self):
        """
        Настраивает соединения сигнал-слот.
        """
        pass

    def open_file(self):
        """
        Открывает диалоговое окно выбора файла для загрузки JSON файла.
        """
        campaign_file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Open JSON File",
            "c:/user/documents/repos/hypotez/data/aliexpress/campaigns",
            "JSON files (*.json)"
        )
        if not campaign_file:
            return

        self.load_file(campaign_file)

    def load_file(self, campaign_file):
        """
        Загружает JSON файл.

        :param campaign_file: Путь к JSON файлу.
        :type campaign_file: str
        """
        try:
            self.data = j_loads(campaign_file) # загрузка файла
            self.current_campaign_file = campaign_file
            self.file_name_label.setText(f"File: {self.current_campaign_file}")
            self.create_widgets(self.data)
            self.editor = AliCampaignEditor(campaign_file=campaign_file)
        except Exception as ex:
            logger.error(f"Failed to load JSON file: {ex}", exc_info=True) # логирование ошибки
            # QtWidgets.QMessageBox.critical(self, "Error", f"Failed to load JSON file: {ex}") # убрано

    def create_widgets(self, data: dict):
        """
        Создает виджеты на основе данных, загруженных из JSON файла.

        :param data: Данные кампании.
        :type data: dict
        """
        layout = self.layout

        # Удаление предыдущих виджетов кроме кнопок открытия и подготовки и лейбла имени файла
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget not in [self.open_button, self.file_name_label, self.prepare_button]:
                widget.deleteLater()
        # проверка на наличие данных
        if not data:
           logger.error("No data loaded")
           return
        # Создание полей для редактирования
        self.title_input = QtWidgets.QLineEdit(data.get('title', '')) # проверка на наличие title
        layout.addWidget(QtWidgets.QLabel("Title:"), 2, 0)
        layout.addWidget(self.title_input, 2, 1)
        set_fixed_size(self.title_input, width=WIDGET_WIDTH, height=WIDGET_HEIGHT)

        self.description_input = QtWidgets.QLineEdit(data.get('description', '')) # проверка на наличие description
        layout.addWidget(QtWidgets.QLabel("Description:"), 3, 0)
        layout.addWidget(self.description_input, 3, 1)
        set_fixed_size(self.description_input, width=WIDGET_WIDTH, height=WIDGET_HEIGHT)

        self.promotion_name_input = QtWidgets.QLineEdit(data.get('promotion_name', '')) # проверка на наличие promotion_name
        layout.addWidget(QtWidgets.QLabel("Promotion Name:"), 4, 0)
        layout.addWidget(self.promotion_name_input, 4, 1)
        set_fixed_size(self.promotion_name_input, width=WIDGET_WIDTH, height=WIDGET_HEIGHT)

    @asyncSlot()
    async def prepare_campaign(self):
        """
        Асинхронно подготавливает кампанию.
        """
        if not self.editor: # проверка на наличие редактора
            logger.error("Editor is not initialized.") # логирование ошибки
            return
        try:
            await self.editor.prepare()
            QtWidgets.QMessageBox.information(self, "Success", "Campaign prepared successfully.")
        except Exception as ex:
            logger.error(f"Failed to prepare campaign: {ex}", exc_info=True) # логирование ошибки
            # QtWidgets.QMessageBox.critical(self, "Error", f"Failed to prepare campaign: {ex}") # убрано
```