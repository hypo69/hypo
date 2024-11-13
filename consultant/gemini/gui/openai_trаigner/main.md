```python
## \file hypotez/src/gui/openai_trаigner/main.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.gui.openai_trаigner """
import sys
import os
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QSystemTrayIcon, QMenu, QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QMessageBox, QFileDialog
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
        
        # ... (Rest of the code is the same)


        # ... (Rest of the code, including URL menus)

    def ask_for_browser(self):
        # Improved browser selection
        choices = ['Chrome', 'Firefox', 'Edge']
        selected_browser = None
        for choice in choices:
          if os.path.exists(self.get_profile_path(choice)):
            selected_browser = choice
            break
        
        if not selected_browser:
          msg_box = QMessageBox(self)
          msg_box.setIcon(QMessageBox.Icon.Warning)
          msg_box.setText("Не найден подходящий браузер. Пожалуйста, установите Chrome, Firefox или Edge.")
          msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
          msg_box.exec()
          sys.exit()
        
        return selected_browser
      
    def get_profile_path(self, browser_name):
        if browser_name == 'Chrome':
            profile_path = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        elif browser_name == 'Firefox':
            profile_path = os.path.expanduser("~\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles")
        elif browser_name == 'Edge':
            profile_path = os.path.expanduser("~\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default")
        else:
          return None
        return profile_path

    # ... (Rest of the code)
```

**Изменения и объяснения:**

1. **Улучшенный выбор браузера (`ask_for_browser`)**:
   - Теперь код проверяет, существует ли папка профиля браузера. Это очень важно для предотвращения ошибок и позволяет пользователю видеть сообщение об ошибке, если браузер не установлен.
   -  Если ни один из поддерживаемых браузеров не найден, программа выходит с сообщением об ошибке.
   - Это намного надежнее, чем просто спрашивать у пользователя, потому что он может ввести что-то, что приложение не знает.

2. **Функция `get_profile_path`**:
   - Эта функция теперь отделена, что делает код более организованным и поддерживаемым. Она возвращает путь к профилю браузера.

3. **Обработка отсутствующего браузера**:
   - Добавлена обработка случая, когда ни один из поддерживаемых браузеров не найден. Программа теперь завершается с сообщением об ошибке, вместо того чтобы пытаться создать браузер с несуществующим профилем.

**Как использовать:**

1. Убедитесь, что на вашей системе установлены Chrome, Firefox или Edge.
2. Запустите приложение.
3. Оно автоматически выберет наиболее подходящий браузер, если таковой имеется. Если нет, вы увидите окно с сообщением об ошибке и приложение завершится.

**Важно**:

- Пути к профилям браузеров могут отличаться в зависимости от вашей системы. Это важная проверка, чтобы избежать ошибок.
-  **Удалите или измените ссылки на несуществующие URL в коде для моделей Gemini и Claude.**  Вы должны заменить `https://gemini.example.com/` и `https://claude.example.com/` на правильные ссылки.

Эти изменения значительно улучшают надежность и устойчивость приложения.  Если вы используете другой браузер, обновите функцию `get_profile_path`, чтобы она соответствовала его расположению.