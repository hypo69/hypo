# Анализ кода модуля `main.py`

**Качество кода**
7
-  Плюсы
    - Код структурирован, используются классы для организации GUI.
    - Присутствует основная функциональность: загрузка URL, сворачивание в трей, контекстное меню.
    - Используются layouts для организации элементов интерфейса.
    - Есть меню для выбора предустановленных URL-ов и моделей.
-  Минусы
    - Отсутствует логирование ошибок.
    - Жестко заданы пути к профилям браузеров, что не является кроссплатформенным решением.
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Нет документации к функциям, методам и классам.
    - Не используется `logger` из `src.logger.logger`.
    - Одинарные кавычки не везде используются.

**Рекомендации по улучшению**

1.  **Добавить описание модуля:**
    - Добавить в начало файла описание модуля в формате docstring.
2.  **Добавить импорты:**
    - Добавить `from src.logger.logger import logger`
    - Добавить `from pathlib import Path`
3.  **Использовать одинарные кавычки:**
    - Исправить двойные кавычки на одинарные, где это требуется.
4.  **Документировать код:**
    - Добавить docstring для всех классов, методов и функций.
5.  **Логирование ошибок:**
    - Использовать `logger.error` для записи ошибок вместо `QMessageBox.warning`.
    - Убрать `sys.exit()` и обработать ошибку с помощью `logger.error`.
6.  **Пути к профилям:**
    - Реализовать более гибкий способ определения путей к профилям браузеров, возможно через конфигурационный файл.
7.  **Обработка URL:**
    - Улучшить обработку URL, например, проверять корректность URL перед загрузкой.
    - Вынести логику проверки URL в отдельную функцию.
8.  **Улучшить взаимодействие с треем:**
    - Добавить возможность восстановления окна из трея по двойному клику на иконку.
    - Вынести логику работы с треем в отдельный метод.
9.  **Использовать `j_loads`:**
   - В данном коде нет чтения данных из файла, но если бы оно было, то нужно было бы использовать `j_loads` или `j_loads_ns` из `src.utils.jjson`.
10. **Рефакторинг:**
    - Разбить метод `__init__` на более мелкие и логически связанные методы.
11. **Убрать избыточность кода:**
    - Избавиться от дублирования кода при создании действий меню, например, вынести в отдельную функцию.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-

"""
Модуль для создания и управления главным окном ассистента.
=========================================================================================

Этот модуль содержит класс :class:`AssistantMainWindow`, который создает главное окно приложения с функционалом
загрузки URL в QWebEngineView, сворачивания в трей, выбора предустановленных URL и моделей.

Пример использования
--------------------

Пример запуска приложения:

.. code-block:: python

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        app.setQuitOnLastWindowClosed(False)  # Чтобы приложение оставалось в трее

        window = AssistantMainWindow()
        window.show()

        sys.exit(app.exec())
"""
import sys
import os
from pathlib import Path
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QSystemTrayIcon, QMenu, QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QMessageBox
)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineProfile

from src.logger.logger import logger #  Импорт logger

class AssistantMainWindow(QMainWindow):
    """
    Главное окно приложения.

    Этот класс создает основное окно приложения, содержащее браузер, панель инструментов
    и меню для выбора URL и моделей.
    """
    def __init__(self):
        """
        Инициализация главного окна.

        Устанавливает размеры окна, создает браузер, панель инструментов,
        меню и системный трей.
        """
        super().__init__()
        self._setup_window()
        self._create_browser_profile()
        self._create_ui()
        self._create_tray_icon()
        self._create_menus()
        
    def _setup_window(self):
        """Настраивает основные параметры окна."""
        # Убираем максимизацию, чтобы пользователь мог изменять размер окна
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowCloseButtonHint)

        # Устанавливаем размеры на 3/4 экрана
        screen_geometry = QApplication.primaryScreen().geometry()
        width = int(screen_geometry.width() * 0.75)
        height = int(screen_geometry.height() * 0.75)
        self.setGeometry((screen_geometry.width() - width) // 2,
                         (screen_geometry.height() - height) // 2,
                         width, height)
    
    def _create_browser_profile(self):
        """Создает профиль для выбранного браузера."""
        # Запрос браузера по умолчанию
        browser_choice = self.ask_for_browser()

        # Создание профиля для выбранного браузера
        if browser_choice == 'Chrome':
            profile_path = os.path.expanduser('~\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
        elif browser_choice == 'Firefox':
            profile_path = os.path.expanduser('~\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles')
        elif browser_choice == 'Edge':
            profile_path = os.path.expanduser('~\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default')
        else:
            logger.error('Браузер не поддерживается')
            return  # Завершаем функцию, если браузер не поддерживается

        try:
             self.profile = QWebEngineProfile(profile_path)
             self.browser = QWebEngineView(self)
             self.browser.setPage(self.profile.defaultProfile().createDefaultPage())
        except Exception as ex:
            logger.error(f'Ошибка создания профиля браузера', exc_info=ex)
            # Вместо sys.exit() обрабатываем ошибку через logger
            return
    
    def _create_ui(self):
        """Создает пользовательский интерфейс."""
         # Верхняя панель с кнопками
        self.title_bar = QWidget(self)
        self.title_bar.setFixedHeight(40)
        self.title_bar.setStyleSheet('background-color: #333;')

        # Поле для ввода URL
        self.url_input = QLineEdit(self.title_bar)
        self.url_input.setPlaceholderText('Введите URL')
        self.url_input.returnPressed.connect(self.load_url)

        # Кнопка для загрузки URL
        self.load_button = QPushButton('Загрузить', self.title_bar)
        self.load_button.clicked.connect(self.load_url)

        # Кнопка для сворачивания в трей
        self.minimize_button = QPushButton(self.title_bar)
        self.minimize_button.setIcon(QIcon.fromTheme('window-minimize'))
        self.minimize_button.setToolTip('Свернуть в трей')
        self.minimize_button.setFixedSize(30, 30)
        self.minimize_button.clicked.connect(self.hide_to_tray)

        # Кнопка для открытия на весь экран
        self.fullscreen_button = QPushButton(self.title_bar)
        self.fullscreen_button.setIcon(QIcon.fromTheme('view-fullscreen'))
        self.fullscreen_button.setToolTip('Открыть на весь экран')
        self.fullscreen_button.setFixedSize(30, 30)
        self.fullscreen_button.clicked.connect(self.showFullScreen)

        # Кнопка для закрытия окна
        self.close_button = QPushButton(self.title_bar)
        self.close_button.setIcon(QIcon.fromTheme('window-close'))
        self.close_button.setToolTip('Закрыть')
        self.close_button.setFixedSize(30, 30)
        self.close_button.clicked.connect(self.hide_to_tray)

        # Layout для верхней панели
        title_bar_layout = QHBoxLayout(self.title_bar)
        title_bar_layout.addWidget(self.url_input)
        title_bar_layout.addWidget(self.load_button)
        title_bar_layout.addStretch(1)
        title_bar_layout.addWidget(self.minimize_button)
        title_bar_layout.addWidget(self.fullscreen_button)
        title_bar_layout.addWidget(self.close_button)
        title_bar_layout.setContentsMargins(0, 0, 0, 0)

        # Основной layout окна
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.title_bar)
        main_layout.addWidget(self.browser)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Центральный виджет и установка layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
    
    def _create_tray_icon(self):
        """Создает и настраивает иконку в системном трее."""
        # Системный трей
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon.fromTheme('application-exit'))

        # Контекстное меню для иконки в трее
        tray_menu = QMenu()
        restore_action = QAction('Восстановить', self)
        restore_action.triggered.connect(self.showNormal)
        quit_action = QAction('Выход', self)
        quit_action.triggered.connect(self.quit_app)

        tray_menu.addAction(restore_action)
        tray_menu.addAction(quit_action)

        # Установка меню для иконки в трее
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        
    def _create_menus(self):
        """Создает меню для выбора URL и моделей."""
         # Меню для выбора URL
        self.url_menu = QMenu('Сервисы Google', self)
        self._add_url_action(self.url_menu, 'Google Login', 'https://accounts.google.com/')
        self._add_url_action(self.url_menu, 'Gmail', 'https://mail.google.com/')
        self._add_url_action(self.url_menu, 'Google Docs', 'https://docs.google.com/')
        self._add_url_action(self.url_menu, 'Google Sheets', 'https://sheets.google.com/')
        self._add_url_action(self.url_menu, 'Google Drive', 'https://drive.google.com/')
        self._add_url_action(self.url_menu, 'Google Photos', 'https://photos.google.com/')

        # Меню для выбора моделей
        self.model_menu = QMenu('Выбор модели', self)
        self._add_model_action(self.model_menu, 'ChatGPT', 'https://chat.openai.com/')
        self._add_model_action(self.model_menu, 'Gemini', 'https://gemini.example.com/')  # Замените на реальный URL
        self._add_model_action(self.model_menu, 'Claude', 'https://claude.example.com/')  # Замените на реальный URL

        # Кнопки для открытия меню
        self.url_button = QPushButton('Сервисы Google', self.title_bar)
        self.url_button.setMenu(self.url_menu)
        
        self.model_button = QPushButton('Выбор модели', self.title_bar)
        self.model_button.setMenu(self.model_menu)

        title_bar_layout = self.title_bar.layout()
        title_bar_layout.addWidget(self.url_button)
        title_bar_layout.addWidget(self.model_button)
    
    def _add_url_action(self, menu: QMenu, text: str, url: str):
        """Создает и добавляет действие URL в меню."""
        action = QAction(text, self)
        action.triggered.connect(lambda: self.load_url(url))
        menu.addAction(action)
    
    def _add_model_action(self, menu: QMenu, text: str, url: str):
       """Создает и добавляет действие модели в меню."""
       action = QAction(text, self)
       action.triggered.connect(lambda: self.load_url(url))
       menu.addAction(action)

    def ask_for_browser(self) -> str | None:
        """
        Запрашивает у пользователя выбор браузера по умолчанию.

        Returns:
            str: Выбранный браузер ('Chrome', 'Firefox', 'Edge') или None, если выбор не сделан.
        """
        choices = ['Chrome', 'Firefox', 'Edge']
        choice, ok = QMessageBox.getItem(self, 'Выберите браузер', 'Какой браузер вы используете по умолчанию?', choices, 0, False)

        if ok and choice:
            return choice
        return None

    def load_url(self, url: str = None):
        """
        Загружает URL в QWebEngineView.

        Args:
            url (str, optional): URL для загрузки. Если не указан, используется текст из self.url_input.
        """
        url = self.url_input.text() if not url else url

        if url:
            if not url.startswith('http'):
                url = 'http://' + url # Добавляем http, если не указано
            try:
                self.browser.setUrl(QUrl(url))
            except Exception as ex:
                logger.error(f'Ошибка при загрузке URL: {url}', exc_info=ex)

    def hide_to_tray(self):
        """Скрывает окно и помещает его в системный трей."""
        self.hide()

    def quit_app(self):
        """Закрывает приложение."""
        self.tray_icon.hide()
        QApplication.quit()

    def closeEvent(self, event):
        """
        Обработчик события закрытия окна.

        Переопределяет closeEvent для скрытия окна в трей при закрытии через "X".
        """
        event.ignore()  # Игнорируем закрытие окна
        self.hide_to_tray()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)  # Чтобы приложение оставалось в трее

    window = AssistantMainWindow()
    window.show()

    sys.exit(app.exec())
```