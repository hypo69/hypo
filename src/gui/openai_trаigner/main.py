## \file /src/gui/openai_trаigner/main.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.gui.openai_trаigner 
	:platform: Windows, Unix
	:synopsis:

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

class AssistantMainWindow(QMainWindow):
    def __init__(self):
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
        browser_choice = self.ask_for_browser()

        # Создание профиля для выбранного браузера
        if browser_choice == 'Chrome':
            profile_path = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        elif browser_choice == 'Firefox':
            profile_path = os.path.expanduser("~\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles")
        elif browser_choice == 'Edge':
            profile_path = os.path.expanduser("~\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default")
        else:
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
        google_login_action = QAction("Google Login", self)
        google_login_action.triggered.connect(lambda: self.load_url("https://accounts.google.com/"))

        gmail_action = QAction("Gmail", self)
        gmail_action.triggered.connect(lambda: self.load_url("https://mail.google.com/"))

        google_docs_action = QAction("Google Docs", self)
        google_docs_action.triggered.connect(lambda: self.load_url("https://docs.google.com/"))

        google_sheets_action = QAction("Google Sheets", self)
        google_sheets_action.triggered.connect(lambda: self.load_url("https://sheets.google.com/"))

        google_drive_action = QAction("Google Drive", self)
        google_drive_action.triggered.connect(lambda: self.load_url("https://drive.google.com/"))

        google_photos_action = QAction("Google Photos", self)
        google_photos_action.triggered.connect(lambda: self.load_url("https://photos.google.com/"))

        self.url_menu.addAction(google_login_action)
        self.url_menu.addAction(gmail_action)
        self.url_menu.addAction(google_docs_action)
        self.url_menu.addAction(google_sheets_action)
        self.url_menu.addAction(google_drive_action)
        self.url_menu.addAction(google_photos_action)

        # Меню для выбора моделей
        self.model_menu = QMenu("Выбор модели", self)
        chatgpt_action = QAction("ChatGPT", self)
        chatgpt_action.triggered.connect(lambda: self.load_url("https://chat.openai.com/"))

        gemini_action = QAction("Gemini", self)
        gemini_action.triggered.connect(lambda: self.load_url("https://gemini.example.com/"))  # Замените на реальный URL

        claude_action = QAction("Claude", self)
        claude_action.triggered.connect(lambda: self.load_url("https://claude.example.com/"))  # Замените на реальный URL

        self.model_menu.addAction(chatgpt_action)
        self.model_menu.addAction(gemini_action)
        self.model_menu.addAction(claude_action)

        # Кнопки для открытия меню
        self.url_button = QPushButton("Сервисы Google", self.title_bar)
        self.url_button.setMenu(self.url_menu)
        
        self.model_button = QPushButton("Выбор модели", self.title_bar)
        self.model_button.setMenu(self.model_menu)

        title_bar_layout.addWidget(self.url_button)
        title_bar_layout.addWidget(self.model_button)

    def ask_for_browser(self):
        choices = ['Chrome', 'Firefox', 'Edge']
        choice, ok = QMessageBox.getItem(self, "Выберите браузер", "Какой браузер вы используете по умолчанию?", choices, 0, False)

        if ok and choice:
            return choice
        return

    # Метод для загрузки URL
    def load_url(self, url: str = None):
        url = self.url_input.text() if not url else url
        
        if url:
            if not url.startswith("http"):
                url = "http://" + url  # Добавляем http, если не указано
            self.browser.setUrl(QUrl(url))

    # Метод для минимизации окна в трей
    def hide_to_tray(self):
        self.hide()

    # Метод для закрытия приложения
    def quit_app(self):
        self.tray_icon.hide()
        QApplication.quit()

    # Переопределяем closeEvent для скрытия окна в трей при закрытии через "X"
    def closeEvent(self, event):
        event.ignore()  # Игнорируем закрытие окна
        self.hide_to_tray()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)  # Чтобы приложение оставалось в трее

    window = AssistantMainWindow()
    window.show()

    sys.exit(app.exec())
