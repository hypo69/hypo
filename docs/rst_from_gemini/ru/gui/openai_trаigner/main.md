```python
## \file hypotez/src/gui/openai_trаigner/main.py
# -*- coding: utf-8 -*-
 # <- venv win
## ~~~~~~~~~~~~~
""" Модуль: src.gui.openai_trаigner """
import sys
import os
from PyQt6.QtCore import Qt, QUrl, QTimer
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QSystemTrayIcon, QMenu, QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QMessageBox, QLabel
)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineProfile

# Добавление проверки на существование файлов профилей
import platform


class AssistantMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ... (Остальной код инициализации) ...

        # Важная проверка на существование профилей браузера.
        # Исключает ошибку, если папка не существует.
        if not self.check_profile_exists(browser_choice):
            QMessageBox.critical(self, "Ошибка", f"Профиль {browser_choice} не найден.")
            sys.exit()

        # ... (Остальной код инициализации) ...

    def check_profile_exists(self, browser_choice):
        if browser_choice == 'Chrome':
            profile_path = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
        elif browser_choice == 'Firefox':
            profile_path = os.path.expanduser("~\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles")
        elif browser_choice == 'Edge':
            profile_path = os.path.expanduser("~\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default")
        else:
            return False  # Неизвестный браузер

        return os.path.exists(profile_path)
    
    # ... (Остальной код) ...



if __name__ == "__main__":
    # ... (Остальной код) ...

```

**Изменения и пояснения:**

* **`check_profile_exists` функция:**  Добавлена функция для проверки существования папки профиля браузера. Это предотвратит ошибку `QWebEngineProfile` в случае, если папка профиля не существует.  Функция проверяет существование профиля для выбранного браузера и возвращает `True`, если он существует, и `False` в противном случае.
* **Обработка ошибок:**  В коде теперь обрабатывается случай, когда папки профиля браузера нет.  Вместо того, чтобы вызывать ошибку, программа показывает критическое сообщение об ошибке и завершается.

**Важные улучшения:**

* **Устойчивость:**  Код теперь более устойчив к ошибкам, связанным с отсутствием профиля браузера.
* **Проверка:**  Функция `check_profile_exists` явно проверяет существование профиля перед созданием `QWebEngineProfile`.

**Дополнительные рекомендации:**

* **Более подробная диагностика:** Вместо простого `os.path.exists`, можно добавить вывод `QMessageBox` с информацией о том, какой именно профиль браузера не найден и где он должен находиться.
* **Локализация:**  При отображении сообщений об ошибках используйте `QMessageBox` с переводами, чтобы сделать интерфейс более удобным для пользователей с разными языками.
* **Обработка исключений:**  В `check_profile_exists`  можно использовать try...except для более надежной обработки потенциальных ошибок, например, при доступе к файлу.


Этот код предоставляет более надежный и устойчивый способ работы с выбором браузера, обеспечивая корректную работу приложения даже в случае отсутствия соответствующих профилей.  Укажите конкретные браузеры для `QMessageBox`, чтобы пользователь понимал, какой профиль не найден.