## Анализ кода модуля src.gui.openai_trаigner.main

**Качество кода**
8
 -  Плюсы
    - Код хорошо структурирован с использованием классов и функций.
    - Присутствует базовая обработка ошибок при выборе браузера.
    - Используются PyQt6 для создания графического интерфейса, что соответствует назначению модуля.
    - Реализовано сворачивание в системный трей.
    - Есть контекстное меню для иконки в трее.
    - Добавлено меню для выбора предустановленных URL.
    -  Добавлено меню для выбора модели.

 -  Минусы
    - Отсутствует docstring для модуля и классов.
    - Не все функции имеют docstring.
    - Используются `sys.exit()` для выхода, что может быть нежелательно в некоторых случаях.
    - Не используется `logger` для логирования.
    - Избыточное использование `try-except`.
    - Жестко заданы пути к профилям браузеров, что может привести к проблемам на разных системах.
    - Недостаточно комментариев в коде, особенно для более сложных блоков.
    -  Не все функции имеют docstring в формате RST.
    -  `MODE = 'dev'` не используется.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Добавить docstring для модуля, класса и всех методов в формате reStructuredText (RST).
2.  **Логирование**:
    -   Использовать `src.logger.logger` для логирования ошибок вместо `print` или `QMessageBox`.
3.  **Обработка ошибок**:
    -   Избегать избыточного использования `try-except` блоков,  использовать `logger.error` для логирования.
4.  **Универсальные пути**:
    -   Использовать более надежные методы для определения путей к профилям браузеров (например, через переменные окружения или системные вызовы).
5.  **Комментарии**:
    -   Добавить комментарии к коду, объясняющие логику работы.
6.  **Рефакторинг**:
    - Разделить класс AssistantMainWindow на более мелкие компоненты для лучшей читаемости и поддерживаемости.
    - Избегать использования `lambda` функций для  обработчиков событий, использовать отдельные функции.
7. **Удаление неиспользуемых переменных**:
   - Удалить `MODE = 'dev'`, если она не используется.

**Оптимизиробанный код**
```python
"""
Модуль для создания основного окна приложения-ассистента.
=========================================================================================

Этот модуль содержит класс :class:`AssistantMainWindow`, который используется для создания
главного окна приложения, системного трея и управления браузером.
"""

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
#MODE = 'dev' # не используется

class AssistantMainWindow(QMainWindow):
    """
    Основное окно приложения-ассистента.

    :ivar profile: Профиль браузера.
    :vartype profile: QWebEngineProfile
    :ivar browser: Веб-браузер.
    :vartype browser: QWebEngineView
    :ivar title_bar: Панель заголовка.
    :vartype title_bar: QWidget
    :ivar url_input: Поле для ввода URL.
    :vartype url_input: QLineEdit
    :ivar load_button: Кнопка для загрузки URL.
    :vartype load_button: QPushButton
    :ivar minimize_button: Кнопка для сворачивания окна.
    :vartype minimize_button: QPushButton
    :ivar fullscreen_button: Кнопка для открытия на весь экран.
    :vartype fullscreen_button: QPushButton
    :ivar close_button: Кнопка для закрытия окна.
    :vartype close_button: QPushButton
    :ivar tray_icon: Иконка в системном трее.
    :vartype tray_icon: QSystemTrayIcon
    :ivar url_menu: Меню для выбора URL.
    :vartype url_menu: QMenu
    :ivar model_menu: Меню для выбора модели.
    :vartype model_menu: QMenu
    :ivar url_button: Кнопка для открытия меню URL.
    :vartype url_button: QPushButton
    :ivar model_button: Кнопка для открытия меню модели.
    :vartype model_button: QPushButton
    """
    def __init__(self):
        """Инициализирует главное окно приложения."""
        super().__init__()
        self._setup_ui()
        self._setup_tray_icon()
        self._setup_menus()

    def _setup_ui(self):
        """Настраивает пользовательский интерфейс."""
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

        # Создание профиля для выбранного браузера
        profile_path = self._get_browser_profile_path(browser_choice)
        if not profile_path:
             QMessageBox.warning(self, "Ошибка", "Браузер не поддерживается.")
             sys.exit()


        self.profile = QWebEngineProfile(profile_path)
        self.browser = QWebEngineView(self)
        self.browser.setPage(self.profile.defaultProfile().createDefaultPage())

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

        # Кнопки для открытия меню
        self.url_button = QPushButton("Сервисы Google", self.title_bar)
        self.model_button = QPushButton("Выбор модели", self.title_bar)
        title_bar_layout.addWidget(self.url_button)
        title_bar_layout.addWidget(self.model_button)


    def _setup_tray_icon(self):
        """Настраивает иконку в системном трее."""
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

    def _setup_menus(self):
        """Настраивает меню для URL и моделей."""
        # Меню для выбора URL
        self.url_menu = QMenu("Сервисы Google", self)
        self._add_url_action("Google Login", "https://accounts.google.com/", self.url_menu)
        self._add_url_action("Gmail", "https://mail.google.com/", self.url_menu)
        self._add_url_action("Google Docs", "https://docs.google.com/", self.url_menu)
        self._add_url_action("Google Sheets", "https://sheets.google.com/", self.url_menu)
        self._add_url_action("Google Drive", "https://drive.google.com/", self.url_menu)
        self._add_url_action("Google Photos", "https://photos.google.com/", self.url_menu)

        # Меню для выбора моделей
        self.model_menu = QMenu("Выбор модели", self)
        self._add_url_action("ChatGPT", "https://chat.openai.com/", self.model_menu)
        self._add_url_action("Gemini", "https://gemini.example.com/", self.model_menu)
        self._add_url_action("Claude", "https://claude.example.com/", self.model_menu)

        # Установка меню для кнопок
        self.url_button.setMenu(self.url_menu)
        self.model_button.setMenu(self.model_menu)


    def _add_url_action(self, text: str, url: str, menu: QMenu):
        """Добавляет действие в меню для загрузки URL.
        
        :param text: Текст действия.
        :type text: str
        :param url: URL для загрузки.
        :type url: str
        :param menu: Меню, в которое нужно добавить действие.
        :type menu: QMenu
        """
        action = QAction(text, self)
        action.triggered.connect(lambda: self.load_url(url))
        menu.addAction(action)

    def _get_browser_profile_path(self, browser_choice: str) -> str:
         """Определяет путь к профилю браузера.

        :param browser_choice: Выбор браузера.
        :type browser_choice: str
        :return: Путь к профилю браузера или None, если браузер не поддерживается.
        :rtype: str | None
        """
         if browser_choice == 'Chrome':
             return os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
         elif browser_choice == 'Firefox':
            return os.path.expanduser("~\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles")
         elif browser_choice == 'Edge':
             return os.path.expanduser("~\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default")
         else:
             return None

    def _ask_for_browser(self) -> str:
        """Запрашивает у пользователя выбор браузера.
        
        :return: Выбор браузера пользователя.
        :rtype: str
        """
        choices = ['Chrome', 'Firefox', 'Edge']
        choice, ok = QMessageBox.getItem(self, "Выберите браузер", "Какой браузер вы используете по умолчанию?", choices, 0, False)
        if ok and choice:
            return choice
        return None

    def load_url(self, url: str = None):
        """Загружает URL в браузере.

        :param url: URL для загрузки, если None использует значение из `url_input`.
        :type url: str, optional
        """
        url = self.url_input.text() if not url else url

        if url:
            if not url.startswith("http"):
                url = "http://" + url  # Добавляем http, если не указано
            try:
                self.browser.setUrl(QUrl(url))
            except Exception as ex:
                logger.error(f'Ошибка при загрузке URL {url=}', exc_info=ex)

    def hide_to_tray(self):
        """Скрывает окно в системный трей."""
        self.hide()

    def quit_app(self):
        """Завершает приложение."""
        self.tray_icon.hide()
        QApplication.quit()

    def closeEvent(self, event):
        """Переопределяет событие закрытия окна для скрытия в трей.
        
        :param event: Событие закрытия окна.
        :type event: QCloseEvent
        """
        event.ignore()  # Игнорируем закрытие окна
        self.hide_to_tray()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)  # Чтобы приложение оставалось в трее

    window = AssistantMainWindow()
    window.show()

    sys.exit(app.exec())