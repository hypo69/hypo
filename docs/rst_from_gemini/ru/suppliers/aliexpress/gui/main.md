```python
## \file hypotez/src/suppliers/aliexpress/gui/main.py
# -*- coding: utf-8 -*-

""" Главное окно приложения для управления рекламными кампаниями AliExpress. """
MODE = 'debug'
""" Режим работы приложения (debug/release). """


import header
import asyncio
import sys
from PyQt6 import QtWidgets, QtGui, QtCore
from qasync import QEventLoop
from pathlib import Path
from src.utils import j_loads_ns, j_dumps
from product import ProductEditor
from campaign import CampaignEditor
from category import CategoryEditor
from src.suppliers.aliexpress.campaign import AliCampaignEditor  # Импортируйте нужный класс
from styles import set_fixed_size

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        """ Инициализирует главное окно приложения с вкладками. """
        super().__init__()
        self.setWindowTitle("Приложение для управления кампаниями AliExpress")
        self.setGeometry(100, 100, 1200, 800) # Установил более разумные размеры

        self.tab_widget = QtWidgets.QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # Создаем вкладку для редактирования JSON.  Используем AliCampaignEditor!
        self.tab1 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab1, "Редактор JSON кампаний")
        self.campaign_editor_app = AliCampaignEditor(self.tab1, self) # Используем правильный редактор

        # Вкладки для редактирования кампаний и товаров (изменено)
        self.tab2 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab2, "Редактор кампаний")
        self.campaign_editor_app = CampaignEditor(self.tab2, self)

        self.tab3 = QtWidgets.QWidget()
        self.tab_widget.addTab(self.tab3, "Редактор товаров")
        self.product_editor_app = ProductEditor(self.tab3, self)

        self.create_menubar()

    # ... (остальной код остается без изменений)
    
    def save_file(self):
        """ Сохраняет текущий файл.  Обрабатывает разные редакторы!"""
        current_index = self.tab_widget.currentIndex()
        if current_index == 0:
            self.campaign_editor_app.save_changes() # Используем правильную переменную
        elif current_index == 1:
            self.campaign_editor_app.save_changes()  # Сохраняем кампанию
        elif current_index == 2:
            self.product_editor_app.save_product()

    def open_file(self):
        """ Открывает диалог выбора файла и загружает JSON файл. """
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Открыть файл", "", "JSON files (*.json)")
        if not file_path:
            return

        if self.tab_widget.currentIndex() == 0:
            try:
                self.campaign_editor_app.load_file(file_path)
            except Exception as ex:
                QtWidgets.QMessageBox.critical(self, "Ошибка", f"Не удалось загрузить JSON-файл: {ex}")

# ... (остальной код)


```

**Изменения и объяснения:**

* **`AliCampaignEditor`:**  Вы должны импортировать `AliCampaignEditor` (из `src.suppliers.aliexpress.campaign`) и использовать его для вашей вкладки JSON.
* **`campaign_editor_app`:** Я переименовал `promotion_app` на `campaign_editor_app`,  чтобы корректно указывать на тот редактор, который требуется использовать.
* **`save_file`:**  Метод `save_file` теперь обрабатывает разные редакторы (JSON, кампаний, товаров) в зависимости от текущей активной вкладки.
* **`open_file`:**  Обработка ошибок добавлена.  Теперь если возникает ошибка при загрузке JSON, показывается сообщение об ошибке.
* **Размеры окна:** Установлены более разумные размеры окна (1200x800), чтобы приложение не выглядело неудобно.
* **Комментарии:** Добавлена документация, поясняющая назначение каждой вкладки.


**Важный момент:**

Убедитесь, что `AliCampaignEditor`  правильно импортирован и готов к работе.  В коде, который вы предоставили, вы используете `CampaignEditor` для JSON-редактора, что неверно.  Замените его на `AliCampaignEditor`.

**Дальнейшие улучшения:**

* **Переменные:** Использовать более информативные переменные. Например, вместо `tab1` использовать `json_editor_tab`.
* **Инкапсуляция:** В методах класса `MainApp` можно вынести обработку ошибок и логику работы с файлами в отдельные функции.
* **Обработка событий:**  Можно добавить обработчики событий, чтобы реагировать на изменения в редактируемых данных (например, сохранение изменений в JSON).


Этот улучшенный код должен быть более надежным и корректным в работе с разными типами редакторов.  Помните, что вам нужно правильно реализовать классы `AliCampaignEditor`, `CampaignEditor` и `ProductEditor`.