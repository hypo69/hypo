# Анализ кода модуля `main.py`

**Качество кода**
- 7
    - Плюсы
        - Код имеет базовую структуру приложения PyQt6.
        - Реализовано переключение между основными браузерами (Chrome, Firefox, Edge) на уровне профиля.
        - Присутствует системный трей.
        - Добавлены основные действия для работы с окном (свернуть, развернуть, закрыть).
        - Имеется возможность выбора предустановленных URL для Google сервисов и моделей ИИ.
        - Используются `QMessageBox` для диалога выбора браузера.
    - Минусы
        - Не хватает документации в формате reStructuredText (RST).
        - Отсутствует обработка ошибок.
        - Имеется избыточное дублирование строк кода и комментариев.
        - Не используется `logger` для логирования.
        -  Не реализована обработка исключений при загрузке профиля браузера.
        -  URL для моделей Gemini и Claude являются фиктивными и должны быть заменены реальными.

**Рекомендации по улучшению**

1.  Добавить документацию в формате RST для модуля, классов, функций и методов.
2.  Использовать `from src.logger.logger import logger` для логирования ошибок и предупреждений.
3.  Упростить логику выбора браузера, вынеся её в отдельную функцию, и добавить обработку ошибок.
4.  Добавить проверку на существование профиля браузера, прежде чем его использовать.
5.  Использовать константы для URL сервисов.
6.  Переработать обработку событий от кнопок для повышения читаемости кода, избегая анонимных lambda-функций.
7.  Улучшить обработку URL, добавив проверку на корректность ввода и обрабатывая ошибки.
8.  Улучшить комментарии в коде, сделав их более конкретными и информативными.
9.  Добавить обработку ошибок при загрузке URL.
10. Добавить обработку ошибки при показе сообщения о выборе браузера.

**Оптимизированный код**

```python
"""
Модуль для создания основного окна приложения и управления браузером.
=========================================================================================

Этот модуль содержит класс :class:`AssistantMainWindow`, который используется для создания
основного окна приложения, управления браузером, системным треем и меню.

Пример использования
--------------------

Пример использования класса `AssistantMainWindow`:

.. code-block:: python

    if __name__ == "__main__":
        app = QApplication(sys.argv)
        app.setQuitOnLastWindowClosed(False)
        window = AssistantMainWindow()
        window.show()
        sys.exit(app.exec())
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

import sys
import os
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QSystemTrayIcon, QMenu, QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QMessageBox
)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineProfile

from src.logger.logger import logger
from src.utils.jjson import j_loads_ns

MODE = 'dev'

#: URL-адреса сервисов Google
GOOGLE_SERVICES = {
    "Google Login": "https://accounts.google.com/",
    "Gmail": "https://mail.google.com/",
    "Google Docs": "https://docs.google.com/",
    "Google Sheets": "https://sheets.google.com/",
    "Google Drive": "https://drive.google.com/",
    "Google Photos": "https://photos.google.com/"
}

#: URL-адреса моделей ИИ
AI_MODELS = {
    "ChatGPT": "https://chat.openai.com/",
    "Gemini": "https://gemini.google.com/",  # TODO: Заменить на реальный URL
    "Claude": "https://claude.ai/"  # TODO: Заменить на реальный URL
}

class AssistantMainWindow(QMainWindow):
    """
    Основное окно приложения.

    Этот класс управляет основным окном приложения, включая браузер, системный трей и меню.

    :param QMainWindow: Родительский класс.
    """
    def __init__(self):
        """
        Инициализация главного окна приложения.

        Устанавливает параметры окна, создает браузерный движок, верхнюю панель,
        системный трей и меню.
        """
        super().__init__()

        # Убираем максимизацию, чтобы пользователь мог изменять размер окна
        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowCloseButtonHint)

        # Устанавливаем размеры на 3/4 экрана
        screen_geometry = QApplication.primaryScreen().geometry()
        width = int(screen_geometry.width() * 0.75)
        height = int(screen_geometry.height() * 0.75)
        self.setGeometry((screen_geometry.width() - width) // 2,
                         (screen_geometry.height() - height) // 2,
                         width, height)

        # Запрос браузера по умолчанию
        browser_choice = self._ask_for_browser()
        if not browser_choice:
            logger.error("Браузер не выбран или произошла ошибка при выборе.")
            QMessageBox.warning(self, "Ошибка", "Браузер не выбран или произошла ошибка при выборе.")
            sys.exit()

        # Создание профиля для выбранного браузера
        profile_path = self._get_profile_path(browser_choice)
        if not profile_path:
            QMessageBox.warning(self, "Ошибка", "Браузер не поддерживается или путь к профилю не найден.")
            sys.exit()
        try:
            self.profile = QWebEngineProfile(profile_path)
            self.browser = QWebEngineView(self)
            self.browser.setPage(self.profile.defaultProfile().createDefaultPage())
        except Exception as ex:
            logger.error(f"Ошибка при создании профиля браузера: {ex}")
            QMessageBox.warning(self, "Ошибка", "Ошибка при создании профиля браузера.")
            sys.exit()

        # Верхняя панель с кнопками
        self.title_bar = QWidget(self)
        self.title_bar.setFixedHeight(40)
        self.title_bar.setStyleSheet("background-color: #333;")

        # Поле для ввода URL
        self.url_input = QLineEdit(self.title_bar)
        self.url_input.setPlaceholderText("Введите URL")
        self.url_input.returnPressed.connect(self.load_url)

        # Кнопка для загрузки URL
        self.load_button = QPushButton("Загрузить", self.title_bar)
        self.load_button.clicked.connect(self.load_url)

        # Кнопка для сворачивания в трей
        self.minimize_button = QPushButton(self.title_bar)
        self.minimize_button.setIcon(QIcon.fromTheme("window-minimize"))
        self.minimize_button.setToolTip("Свернуть в трей")
        self.minimize_button.setFixedSize(30, 30)
        self.minimize_button.clicked.connect(self.hide_to_tray)

        # Кнопка для открытия на весь экран
        self.fullscreen_button = QPushButton(self.title_bar)
        self.fullscreen_button.setIcon(QIcon.fromTheme("view-fullscreen"))
        self.fullscreen_button.setToolTip("Открыть на весь экран")
        self.fullscreen_button.setFixedSize(30, 30)
        self.fullscreen_button.clicked.connect(self.showFullScreen)

        # Кнопка для закрытия окна
        self.close_button = QPushButton(self.title_bar)
        self.close_button.setIcon(QIcon.fromTheme("window-close"))
        self.close_button.setToolTip("Закрыть")
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

        # Системный трей
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon.fromTheme("application-exit"))

        # Контекстное меню для иконки в трее
        tray_menu = QMenu()
        restore_action = QAction("Восстановить", self)
        restore_action.triggered.connect(self.showNormal)
        quit_action = QAction("Выход", self)
        quit_action.triggered.connect(self.quit_app)

        tray_menu.addAction(restore_action)
        tray_menu.addAction(quit_action)

        # Установка меню для иконки в трее
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        # Меню для выбора URL
        self.url_menu = QMenu("Сервисы Google", self)
        for service_name, url in GOOGLE_SERVICES.items():
            action = QAction(service_name, self)
            action.triggered.connect(lambda url=url: self.load_url(url))
            self.url_menu.addAction(action)

        # Меню для выбора моделей
        self.model_menu = QMenu("Выбор модели", self)
        for model_name, url in AI_MODELS.items():
            action = QAction(model_name, self)
            action.triggered.connect(lambda url=url: self.load_url(url))
            self.model_menu.addAction(action)

        # Кнопки для открытия меню
        self.url_button = QPushButton("Сервисы Google", self.title_bar)
        self.url_button.setMenu(self.url_menu)

        self.model_button = QPushButton("Выбор модели", self.title_bar)
        self.model_button.setMenu(self.model_menu)

        title_bar_layout.addWidget(self.url_button)
        title_bar_layout.addWidget(self.model_button)

    def _ask_for_browser(self) -> str | None:
        """
        Запрашивает у пользователя выбор браузера по умолчанию.

        :return: Выбранный браузер или None, если выбор не был сделан.
        """
        choices = ['Chrome', 'Firefox', 'Edge']
        choice, ok = QMessageBox.getItem(self, "Выберите браузер", "Какой браузер вы используете по умолчанию?", choices, 0, False)

        if ok and choice:
            return choice
        return None

    def _get_profile_path(self, browser_choice: str) -> str | None:
        """
        Определяет путь к профилю браузера на основе выбора пользователя.

        :param browser_choice: Выбранный браузер.
        :return: Путь к профилю браузера или None, если браузер не поддерживается.
        """
        if browser_choice == 'Chrome':
            return os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        elif browser_choice == 'Firefox':
            return os.path.expanduser("~\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles")
        elif browser_choice == 'Edge':
            return os.path.expanduser("~\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default")
        else:
            return None

    def load_url(self, url: str = None):
        """
        Загружает URL в браузере.

        :param url: URL для загрузки, если None используется URL из поля ввода.
        """
        url = self.url_input.text() if not url else url

        if url:
            if not url.startswith("http"):
                url = "http://" + url # Добавляем http, если не указано
            try:
               self.browser.setUrl(QUrl(url))
            except Exception as ex:
                logger.error(f"Ошибка при загрузке URL: {ex}")
                QMessageBox.warning(self, "Ошибка", "Невозможно загрузить URL")

    def hide_to_tray(self):
        """
        Скрывает окно в системный трей.
        """
        self.hide()

    def quit_app(self):
        """
        Завершает работу приложения.
        """
        self.tray_icon.hide()
        QApplication.quit()

    def closeEvent(self, event):
        """
        Обработчик события закрытия окна.

        :param event: Событие закрытия окна.
        """
        event.ignore() # Игнорируем закрытие окна
        self.hide_to_tray()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False) # Чтобы приложение оставалось в трее

    window = AssistantMainWindow()
    window.show()

    sys.exit(app.exec())
```