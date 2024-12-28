# Анализ кода модуля `campaign.py`

**Качество кода**
9
-   Плюсы
    - Код хорошо структурирован и разбит на отдельные функции для каждой задачи, что улучшает читаемость и сопровождение.
    -   Используется `QScrollArea` для корректного отображения контента, который может не поместиться на экране.
    - Применение `j_loads_ns` вместо `json.load` для загрузки JSON-файлов.
    -   Использование `asyncSlot` для асинхронного выполнения длительных задач, таких как подготовка кампании.
    -   Наличие `try-except` блоков для обработки исключений.
    -   Применение `set_fixed_size` для управления размерами виджетов.
-   Минусы
    -   Отсутствует документация в формате reStructuredText (RST) для модуля, классов, методов и переменных.
    -  Отсутствуют импорты `logger` для логгирования ошибок и `j_loads` для загрузки json файлов
    -  Жестко задан путь для диалога открытия файлов `"c:/user/documents/repos/hypotez/data/aliexpress/campaigns"`

**Рекомендации по улучшению**

1.  Добавить документацию в формате reStructuredText (RST) для модуля, классов, методов и переменных.
2.  Добавить импорт `logger` для логирования ошибок и `j_loads` для загрузки json файлов
3.  Использовать `logger.error` для логирования ошибок вместо стандартного `QtWidgets.QMessageBox.critical`, чтобы обеспечить централизованное логирование.
4.  Убрать жестко заданный путь для диалога открытия файлов, или вынести его в настройки приложения.
5.  Заменить стандартные `try-except` блоки на конструкцию с `logger.error` для обработки исключений.
6.  Добавить проверку на наличие данных перед созданием виджетов.
7.  Улучшить обработку ошибок при загрузке файла, добавив больше информации в лог.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для создания и редактирования кампаний AliExpress.
========================================================

Этот модуль предоставляет графический интерфейс для редактирования и подготовки кампаний AliExpress.
Он позволяет пользователям загружать данные кампаний из JSON-файлов, просматривать и редактировать
основные параметры кампании, такие как заголовок, описание и название акции.

Класс :class:`CampaignEditor` является основным виджетом для редактирования кампаний.

Пример использования
--------------------

.. code-block:: python

    app = QtWidgets.QApplication(sys.argv)
    campaign_editor = CampaignEditor()
    campaign_editor.show()
    sys.exit(app.exec())
"""


import asyncio
import sys
from pathlib import Path
from types import SimpleNamespace
from PyQt6 import QtWidgets, QtGui, QtCore
from qasync import QEventLoop, asyncSlot
from src.utils.jjson import j_loads_ns, j_dumps, j_loads
from src.suppliers.aliexpress.campaign import AliCampaignEditor
from styles import set_fixed_size
from src.logger.logger import logger # импорт логгера


class CampaignEditor(QtWidgets.QWidget):
    """
    Виджет для редактирования кампаний.
    ====================================

    :ivar data: SimpleNamespace - Данные кампании, загруженные из JSON файла.
    :ivar current_campaign_file: str - Путь к текущему редактируемому файлу кампании.
    :ivar editor: AliCampaignEditor - Объект редактора кампании.

    :param parent: Родительский виджет (по умолчанию None).
    :param main_app: Главное приложение (по умолчанию None).
    """
    data: SimpleNamespace = None
    current_campaign_file: str = None
    editor: AliCampaignEditor

    def __init__(self, parent=None, main_app=None):
        """
        Инициализирует виджет CampaignEditor.

        :param parent: Родительский виджет.
        :param main_app: Экземпляр главного приложения.
        """
        super().__init__(parent)
        self.main_app = main_app  # Сохраняет экземпляр MainApp

        self.setup_ui()
        self.setup_connections()

    def setup_ui(self):
        """
        Настраивает пользовательский интерфейс виджета.
        """
        self.setWindowTitle("Campaign Editor")
        self.resize(1800, 800)

        # Создание QScrollArea
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        # Создание QWidget для содержимого scroll area
        self.scroll_content_widget = QtWidgets.QWidget()
        self.scroll_area.setWidget(self.scroll_content_widget)

        # Создание layout для содержимого scroll widget
        self.layout = QtWidgets.QGridLayout(self.scroll_content_widget)
        self.layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        # Определение компонентов UI
        self.open_button = QtWidgets.QPushButton("Open JSON File")
        self.open_button.clicked.connect(self.open_file)
        set_fixed_size(self.open_button, width=250, height=25)

        self.file_name_label = QtWidgets.QLabel("No file selected")
        set_fixed_size(self.file_name_label, width=500, height=25)

        self.prepare_button = QtWidgets.QPushButton("Prepare Campaign")
        self.prepare_button.clicked.connect(self.prepare_campaign)
        set_fixed_size(self.prepare_button, width=250, height=25)

        # Добавление компонентов в layout
        self.layout.addWidget(self.open_button, 0, 0)
        self.layout.addWidget(self.file_name_label, 0, 1)
        self.layout.addWidget(self.prepare_button, 1, 0, 1, 2)  # Span across two columns

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
         Открывает диалог выбора файла для загрузки JSON-файла.
        """
        campaign_file, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Open JSON File",
            # "c:/user/documents/repos/hypotez/data/aliexpress/campaigns", # TODO: Убрать жесткий путь
            "",
            "JSON files (*.json)"
        )
        if not campaign_file:
            return

        self.load_file(campaign_file)

    def load_file(self, campaign_file):
        """
        Загружает JSON-файл и отображает данные в виджетах.

        :param campaign_file: Путь к файлу кампании.
        """
        try:
            # код исполняет загрузку файла
            data = j_loads(campaign_file)
            self.data = j_loads_ns(campaign_file)
            self.current_campaign_file = campaign_file
            self.file_name_label.setText(f"File: {self.current_campaign_file}")
            if data:  # Проверяем, что данные загружены
                 self.create_widgets(self.data)
            else:
                logger.error(f"Не удалось загрузить данные из файла: {campaign_file}")
                QtWidgets.QMessageBox.critical(self, "Error", f"Не удалось загрузить данные из файла: {campaign_file}")
                return
            self.editor = AliCampaignEditor(campaign_file=campaign_file)

        except Exception as ex:
            logger.error(f"Ошибка при загрузке JSON файла: {ex}", exc_info=True)  # логирование ошибки
            QtWidgets.QMessageBox.critical(self, "Error", f"Не удалось загрузить JSON файл: {ex}") # сообщение об ошибке

    def create_widgets(self, data):
        """
        Создает виджеты на основе данных, загруженных из JSON-файла.

        :param data: Данные кампании в виде SimpleNamespace.
        """
        layout = self.layout

        # удаляет предыдущие виджеты, кроме open_button и file_label
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget not in [self.open_button, self.file_name_label, self.prepare_button]:
                widget.deleteLater()


        self.title_input = QtWidgets.QLineEdit(data.title)
        layout.addWidget(QtWidgets.QLabel("Title:"), 2, 0)
        layout.addWidget(self.title_input, 2, 1)
        set_fixed_size(self.title_input, width=500, height=25)

        self.description_input = QtWidgets.QLineEdit(data.description)
        layout.addWidget(QtWidgets.QLabel("Description:"), 3, 0)
        layout.addWidget(self.description_input, 3, 1)
        set_fixed_size(self.description_input, width=500, height=25)

        self.promotion_name_input = QtWidgets.QLineEdit(data.promotion_name)
        layout.addWidget(QtWidgets.QLabel("Promotion Name:"), 4, 0)
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
                QtWidgets.QMessageBox.information(self, "Success", "Кампания успешно подготовлена.")
            except Exception as ex:
                logger.error(f"Не удалось подготовить кампанию: {ex}", exc_info=True)
                QtWidgets.QMessageBox.critical(self, "Error", f"Не удалось подготовить кампанию: {ex}")
```