Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код определяет класс `CampaignEditor`, который представляет собой виджет PyQt6 для редактирования кампаний, загружаемых из файла JSON.  Он предоставляет интерфейс пользователя для открытия файла, загрузки данных, отображения и редактирования информации о кампании, а также подготовки кампании.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек:** Код импортирует необходимые библиотеки PyQt6, асинхронный фреймворк `qasync`, вспомогательные функции `j_loads_ns`, `j_dumps`, класс `AliCampaignEditor` и стили.

2. **Определение класса `CampaignEditor`:**  Класс наследуется от `QtWidgets.QWidget`.  Он хранит данные кампании (`data`), путь к загруженному файлу (`current_campaign_file`), и экземпляр класса `AliCampaignEditor` (`editor`).

3. **Инициализация (`__init__`):** При создании экземпляра класса, выполняется настройка интерфейса (`setup_ui`) и установление соединений между элементами (`setup_connections`).

4. **Настройка интерфейса (`setup_ui`):** Создаются элементы управления: кнопка "Открыть JSON файл", метка для отображения имени файла, кнопка "Подготовить кампанию". Элементы добавляются в макет с использованием `QGridLayout`, а также `QScrollArea` для удобства просмотра больших данных.

5. **Открытие файла (`open_file`):** При нажатии кнопки "Открыть JSON файл" вызывается диалоговое окно для выбора файла JSON. Загруженные данные обрабатываются и отображаются.

6. **Загрузка файла (`load_file`):** Функция загружает JSON-файл, используя `j_loads_ns`, и сохраняет загруженные данные в `self.data`.  Если загрузка не удалась, выводится сообщение об ошибке.

7. **Создание виджетов (`create_widgets`):**  На основе загруженных данных создаются виджеты для отображения и редактирования  информации о кампании (например, названия, описания и т.д.). Старые виджеты удаляются, чтобы избежать дублирования.

8. **Подготовка кампании (`prepare_campaign`):**  Асинхронно запускает подготовку кампании с помощью `self.editor.prepare()`. Выводит сообщения об успехе или ошибке.


Пример использования
-------------------------
.. code-block:: python

    import sys
    from PyQt6.QtWidgets import QApplication
    from hypotez.src.suppliers.aliexpress.gui.campaign import CampaignEditor

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        campaign_editor = CampaignEditor()
        campaign_editor.show()
        sys.exit(app.exec())