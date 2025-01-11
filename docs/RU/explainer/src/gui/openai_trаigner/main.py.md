## <алгоритм>

1.  **Инициализация приложения:**
    *   Создается экземпляр `QApplication`.
    *   Устанавливается параметр `setQuitOnLastWindowClosed(False)`, чтобы приложение не закрывалось при закрытии последнего окна.
    *   Создается главное окно `AssistantMainWindow`.
    *   Главное окно отображается.
    *   Запускается основной цикл приложения `app.exec()`.
    
    **Пример:**
    ```python
        app = QApplication(sys.argv)
        app.setQuitOnLastWindowClosed(False)
        window = AssistantMainWindow()
        window.show()
        sys.exit(app.exec())
    ```

2.  **Инициализация главного окна `AssistantMainWindow`:**
    *   Устанавливается флаг окна, чтобы убрать кнопку максимизации.
    *   Устанавливаются размеры окна на 75% от экрана.
    *   Вызывается метод `ask_for_browser()` для выбора браузера.
        
        **Пример:** `browser_choice = self.ask_for_browser()`
        
        *   Если выбор есть, то устанавливается путь к профилю браузера.
    *   Создается профиль браузера `QWebEngineProfile`.
    *   Создается `QWebEngineView` для отображения веб-страниц.
    *   Создается верхняя панель инструментов (`QWidget`) для кнопок.
    *   Создается поле ввода URL (`QLineEdit`).
    *   Создается кнопка загрузки URL (`QPushButton`).
    *   Создается кнопка сворачивания в трей (`QPushButton`).
    *   Создается кнопка открытия на весь экран (`QPushButton`).
    *   Создается кнопка закрытия окна (`QPushButton`).
    *   Создается макет (`QHBoxLayout`) для верхней панели.
    *   Создается макет (`QVBoxLayout`) для всего окна.
    *   Создается центральный виджет (`QWidget`) и устанавливается макет для него.
    *   Создается иконка в системном трее (`QSystemTrayIcon`).
    *   Создается контекстное меню для иконки в трее (`QMenu`).
    *   Создается меню для выбора URL-адресов Google (`QMenu`).
    *   Создается меню для выбора модели (`QMenu`).
    *   Создаются кнопки для открытия меню (`QPushButton`).
    *   Добавляются кнопки и виджеты в макеты.
    
    **Пример:**
    ```python
        self.title_bar = QWidget(self)
        self.url_input = QLineEdit(self.title_bar)
        self.load_button = QPushButton("Загрузить", self.title_bar)
        title_bar_layout = QHBoxLayout(self.title_bar)
        main_layout = QVBoxLayout()
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
    ```
    

3.  **Метод `ask_for_browser()`:**
    *   Выводит диалоговое окно `QMessageBox` для выбора браузера из списка.
    *   Возвращает выбранный браузер или `None`.
        
        **Пример:**
        ```python
        choices = ['Chrome', 'Firefox', 'Edge']
        choice, ok = QMessageBox.getItem(self, "Выберите браузер", "Какой браузер вы используете по умолчанию?", choices, 0, False)
        ```

4.  **Метод `load_url()`:**
    *   Если передан URL, то загружает его, иначе берет URL из поля ввода.
    *   Добавляет "http://" если URL не начинается с него.
    *   Устанавливает URL для браузера `QWebEngineView`.
        
        **Пример:**
        ```python
            url = self.url_input.text() if not url else url
            if not url.startswith("http"):
                url = "http://" + url
            self.browser.setUrl(QUrl(url))
        ```
    

5.  **Метод `hide_to_tray()`:**
    *   Скрывает главное окно.
    
        **Пример:** `self.hide()`

6.  **Метод `quit_app()`:**
    *   Скрывает иконку в трее.
    *   Закрывает приложение.
    
    **Пример:**
    ```python
        self.tray_icon.hide()
        QApplication.quit()
    ```

7. **Обработчик `closeEvent()`:**
    * Игнорирует событие закрытия окна (крестик).
    * Вызывает `hide_to_tray` для скрытия окна в трей.
    
    **Пример:**
    ```python
        event.ignore()
        self.hide_to_tray()
    ```

## <mermaid>

```mermaid
flowchart TD
    Start(Start Application) --> InitApp[Initialize QApplication]
    InitApp --> SetQuitOnLastWindowClosed[app.setQuitOnLastWindowClosed(False)]
    SetQuitOnLastWindowClosed --> InitMainWindow[Initialize AssistantMainWindow]
    InitMainWindow --> SetWindowFlags[Set Window Flags: Remove Maximize]
    SetWindowFlags --> SetGeometry[Set Window Size 3/4 of Screen]
    SetGeometry --> AskForBrowser[browser_choice = ask_for_browser()]
    AskForBrowser -- User Chooses Browser --> SetProfilePath[Set Browser Profile Path]
    SetProfilePath --> CreateProfile[Create QWebEngineProfile]
    CreateProfile --> CreateBrowserView[Create QWebEngineView]
    CreateBrowserView --> CreateTitleBar[Create Title Bar Widget]
    CreateTitleBar --> CreateUrlInput[Create URL Input Field]
    CreateUrlInput --> CreateLoadButton[Create Load URL Button]
    CreateLoadButton --> CreateMinimizeButton[Create Minimize to Tray Button]
    CreateMinimizeButton --> CreateFullscreenButton[Create Fullscreen Button]
    CreateFullscreenButton --> CreateCloseButton[Create Close Button]
    CreateCloseButton --> CreateTitleBarLayout[Create Title Bar Layout]
    CreateTitleBarLayout --> CreateMainLayout[Create Main Layout]
    CreateMainLayout --> CreateCentralWidget[Create Central Widget]
    CreateCentralWidget --> SetCentralWidget[Set Central Widget]
    SetCentralWidget --> CreateSystemTrayIcon[Create QSystemTrayIcon]
    CreateSystemTrayIcon --> CreateTrayMenu[Create Tray Context Menu]
    CreateTrayMenu --> CreateUrlMenu[Create URL Menu]
    CreateUrlMenu --> CreateModelMenu[Create Model Menu]
    CreateModelMenu --> CreateUrlButton[Create URL Menu Button]
    CreateUrlButton --> CreateModelButton[Create Model Menu Button]
    CreateModelButton --> AddButtonsToLayout[Add Buttons to Layout]
    AddButtonsToLayout --> ShowWindow[window.show()]
    ShowWindow --> RunAppLoop[sys.exit(app.exec())]
    RunAppLoop --> End(End Application)

    subgraph Ask For Browser
    AskForBrowser --> BrowserChoiceDialog[Show Browser Choice Dialog]
    BrowserChoiceDialog -- User selects browser --> ReturnBrowserChoice[Return chosen browser]
    BrowserChoiceDialog -- User cancels --> ReturnNone[Return None]
    end
    
    subgraph Load URL
    CreateLoadButton -- Clicked --> LoadUrlFunction[load_url(url)]
    LoadUrlFunction --> GetUrlFromInput[Get URL from input field]
    GetUrlFromInput --> CheckUrlPrefix[Check if URL starts with "http"]
    CheckUrlPrefix -- No "http" prefix --> AddHttpPrefix[Add "http://" prefix]
    AddHttpPrefix --> SetBrowserUrl[browser.setUrl(QUrl(url))]
    CheckUrlPrefix -- "http" prefix present --> SetBrowserUrl
    end
    
    subgraph Hide To Tray
     CreateMinimizeButton -- Clicked --> HideToTrayFunction[hide_to_tray()]
    HideToTrayFunction --> HideMainWindow[mainWindow.hide()]
    end
    
   subgraph Quit App
      CreateCloseButton -- Clicked --> QuitAppFunction[quit_app()]
      QuitAppFunction --> HideTrayIcon[tray_icon.hide()]
      HideTrayIcon --> QuitApplication[QApplication.quit()]
    end

     subgraph Close Event
      MainWindow -- Close Event --> CloseEventFunction[closeEvent(event)]
      CloseEventFunction --> IgnoreCloseEvent[event.ignore()]
       IgnoreCloseEvent --> HideToTrayCall[hide_to_tray()]
    end
```

### **Объяснение Mermaid Diagram:**

*   **Start Application:** Начальная точка приложения.
*   **Initialize QApplication:** Создание экземпляра `QApplication`.
*   **app.setQuitOnLastWindowClosed(False):**  Установка флага для предотвращения закрытия приложения при закрытии последнего окна.
*   **Initialize AssistantMainWindow:** Создание экземпляра главного окна.
*   **Set Window Flags: Remove Maximize:** Установка флагов окна для удаления кнопки максимизации.
*   **Set Window Size 3/4 of Screen:** Установка размера окна на 75% от размера экрана.
*   **browser_choice = ask_for_browser():** Вызов метода для запроса выбора браузера.
*   **Ask For Browser:** Поток управления, связанный с выбором браузера.
    *   **Show Browser Choice Dialog:** Отображение диалогового окна для выбора браузера.
    *   **Return chosen browser:** Возвращение выбранного браузера.
    *   **Return None:** Возвращение `None`, если пользователь не выбрал браузер.
*   **Set Browser Profile Path:** Установка пути к профилю выбранного браузера.
*   **Create QWebEngineProfile:** Создание экземпляра `QWebEngineProfile`.
*   **Create QWebEngineView:** Создание экземпляра `QWebEngineView` для отображения веб-страниц.
*   **Create Title Bar Widget:** Создание виджета для панели инструментов.
*   **Create URL Input Field:** Создание поля ввода для URL.
*   **Create Load URL Button:** Создание кнопки для загрузки URL.
*   **Create Minimize to Tray Button:** Создание кнопки для сворачивания в трей.
*   **Create Fullscreen Button:** Создание кнопки для открытия на весь экран.
*   **Create Close Button:** Создание кнопки для закрытия окна.
*   **Create Title Bar Layout:** Создание горизонтального макета для панели инструментов.
*   **Create Main Layout:** Создание вертикального макета для всего окна.
*   **Create Central Widget:** Создание центрального виджета.
*   **Set Central Widget:** Установка центрального виджета для главного окна.
*   **Create QSystemTrayIcon:** Создание экземпляра для иконки в трее.
*   **Create Tray Context Menu:** Создание контекстного меню для иконки в трее.
*   **Create URL Menu:** Создание меню для выбора URL-адресов Google.
*   **Create Model Menu:** Создание меню для выбора моделей.
*   **Create URL Menu Button:** Создание кнопки для открытия URL Menu.
*   **Create Model Menu Button:** Создание кнопки для открытия Model Menu.
*   **Add Buttons to Layout:** Добавление кнопок в макет.
*   **window.show():** Отображение главного окна.
*   **sys.exit(app.exec()):** Запуск основного цикла приложения.
*   **Load URL:** Поток управления для загрузки URL
*   **load_url(url):** Вызов функции загрузки URL.
*   **Get URL from input field:** Получение URL из поля ввода.
*   **Check if URL starts with "http":** Проверка, начинается ли URL с префикса "http".
*   **Add "http://" prefix:** Добавление префикса "http://" если URL его не имеет.
*  **browser.setUrl(QUrl(url)):** Установка URL для отображения в браузере.
*   **Hide To Tray:** Поток управления для сворачивания в трей
*  **hide_to_tray():** Вызов метода для скрытия в трей
*   **mainWindow.hide():** Скрытие главного окна
*   **Quit App:** Поток управления для завершения приложения
*   **quit_app():** Вызов метода для завершения приложения
*  **tray_icon.hide():** Скрытие иконки в трее
*   **QApplication.quit():** Завершение приложения
*   **Close Event:** Поток управления для события закрытия окна
*   **closeEvent(event):** Вызов обработчика события закрытия
*  **event.ignore():** Игнорирование события закрытия
*   **hide_to_tray():** Скрытие главного окна в трей

**Зависимости:**

*   Диаграмма показывает зависимости между различными частями кода: от инициализации приложения до загрузки URL, сворачивания в трей и выхода из приложения.
*   Основные зависимости включают взаимодействие между `QApplication`, `QMainWindow`, `QWebEngineView`, `QSystemTrayIcon` и другими виджетами PyQt6.
*   Также отражены зависимости, связанные с пользовательским вводом и действиями (например, нажатие кнопок и выбор браузера).

## <объяснение>

### **Импорты:**

*   `import sys`: Используется для доступа к системным переменным и функциям, в данном случае для завершения приложения (`sys.exit()`).
*   `import os`: Используется для работы с операционной системой, в частности для получения пути к профилю пользователя (`os.path.expanduser()`).
*   `from PyQt6.QtCore import Qt, QUrl`:
    *   `Qt`: Используется для определения констант, таких как флаги окна.
    *   `QUrl`: Используется для работы с URL-адресами.
*   `from PyQt6.QtGui import QIcon, QAction`:
    *   `QIcon`: Используется для создания иконок для кнопок и трея.
    *   `QAction`: Используется для создания действий в меню.
*   `from PyQt6.QtWidgets import (QApplication, QMainWindow, QSystemTrayIcon, QMenu, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QMessageBox)`:
    *   `QApplication`: Основа любого приложения PyQt6.
    *   `QMainWindow`: Главное окно приложения.
    *   `QSystemTrayIcon`: Иконка в системном трее.
    *   `QMenu`: Меню, используемое для иконки в трее и выпадающих списков.
    *   `QPushButton`: Кнопка.
    *   `QVBoxLayout`: Вертикальный макет.
    *   `QHBoxLayout`: Горизонтальный макет.
    *   `QWidget`: Базовый виджет, используемый для контейнеров.
    *   `QLineEdit`: Поле ввода текста.
    *   `QMessageBox`: Диалоговое окно для вывода сообщений.
*   `from PyQt6.QtWebEngineWidgets import QWebEngineView`: Используется для отображения веб-страниц.
*   `from PyQt6.QtWebEngineCore import QWebEngineProfile`: Используется для создания и управления профилями браузера.

### **Классы:**

*   **`AssistantMainWindow(QMainWindow)`**:
    *   **Роль:** Главное окно приложения, отвечает за создание и управление интерфейсом.
    *   **Атрибуты:**
        *   `browser`: Экземпляр `QWebEngineView` для отображения веб-страниц.
        *   `profile`: Экземпляр `QWebEngineProfile` для управления профилем браузера.
        *   `title_bar`: `QWidget` для верхней панели инструментов.
        *   `url_input`: `QLineEdit` для ввода URL.
        *   `load_button`: `QPushButton` для загрузки URL.
        *   `minimize_button`, `fullscreen_button`, `close_button`: Кнопки для управления окном.
        *   `tray_icon`: `QSystemTrayIcon` для иконки в трее.
        *   `url_menu`, `model_menu`: Меню для выбора URL и модели.
        *   `url_button`, `model_button`: Кнопки для открытия меню.
    *   **Методы:**
        *   `__init__`: Конструктор, инициализирует интерфейс, настраивает размеры и обрабатывает запросы браузера.
        *   `ask_for_browser`: Запрашивает у пользователя выбор браузера.
        *   `load_url`: Загружает URL в `QWebEngineView`.
        *   `hide_to_tray`: Скрывает окно и помещает иконку в трей.
        *   `quit_app`: Завершает приложение.
        *   `closeEvent`: Обработчик события закрытия окна, перехватывает закрытие и сворачивает в трей.
    * **Взаимодействие**: Взаимодействует с `QApplication`, `QWebEngineView` и системным треем, а также с другими элементами интерфейса (кнопки, меню).

### **Функции:**

*   **`__init__(self)`**:
    *   **Аргументы:** `self` (ссылка на экземпляр класса).
    *   **Возвращаемое значение:** Нет.
    *   **Назначение:** Инициализация главного окна, установка размеров, создание виджетов, обработка сигналов кнопок, настройка иконки в системном трее и меню.
    *   **Пример:** Создает экземпляр окна, устанавливает начальный размер, вызывает `ask_for_browser`, создает браузерное окно и необходимые кнопки, а так же устанавливает обработчики сигналов.
*   **`ask_for_browser(self)`**:
    *   **Аргументы:** `self`.
    *   **Возвращаемое значение:** Строка с именем выбранного браузера или `None`.
    *   **Назначение:** Выводит диалоговое окно для выбора браузера.
    *   **Пример:** `browser_choice = self.ask_for_browser()`, диалоговое окно предлагает пользователю выбрать `Chrome`, `Firefox` или `Edge`.
*   **`load_url(self, url=None)`**:
    *   **Аргументы:** `self`, `url` (необязательный, URL для загрузки).
    *   **Возвращаемое значение:** Нет.
    *   **Назначение:** Загружает URL в `QWebEngineView`. Если `url` не указан, берет его из поля ввода. Добавляет "http://", если URL не начинается с него.
    *   **Пример:** `self.load_url("https://www.google.com")` или `self.load_url()`, если URL введен в поле `url_input`.
*   **`hide_to_tray(self)`**:
    *   **Аргументы:** `self`.
    *   **Возвращаемое значение:** Нет.
    *   **Назначение:** Скрывает главное окно.
    *   **Пример:** Вызывается при нажатии кнопки минимизации или при закрытии окна через "X".
*   **`quit_app(self)`**:
    *   **Аргументы:** `self`.
    *   **Возвращаемое значение:** Нет.
    *   **Назначение:** Скрывает иконку в трее и завершает приложение.
    *   **Пример:** Вызывается при выборе пункта "Выход" из контекстного меню трея.
*   **`closeEvent(self, event)`**:
    *   **Аргументы:** `self`, `event` (событие закрытия окна).
    *   **Возвращаемое значение:** Нет.
    *   **Назначение:** Переопределяет стандартное поведение закрытия окна, игнорируя его и вызывая `hide_to_tray`.
    *  **Пример:** При нажатии на кнопку закрытия "X" на главном окне.

### **Переменные:**

*   `app`: Экземпляр `QApplication`, главный объект приложения.
*   `window`: Экземпляр `AssistantMainWindow`, главное окно.
*   `browser_choice`: Строка, хранящая выбор браузера пользователя.
*   `profile_path`: Строка, хранящая путь к профилю браузера.
*  `profile`: Экземпляр `QWebEngineProfile`, представляет профиль браузера.
*  `browser`: Экземпляр `QWebEngineView`, виджет для отображения веб-страниц.
*  `title_bar`: Экземпляр `QWidget`, панель с кнопками.
*  `url_input`: Экземпляр `QLineEdit`, поле ввода URL.
*  `load_button`, `minimize_button`, `fullscreen_button`, `close_button`: Экземпляры `QPushButton`, кнопки для взаимодействия с пользователем.
*  `tray_icon`: Экземпляр `QSystemTrayIcon`, иконка приложения в системном трее.
*  `tray_menu`, `url_menu`, `model_menu`: Экземпляры `QMenu`, выпадающие меню.
*  `google_login_action`, `gmail_action`, `google_docs_action` , `google_sheets_action`, `google_drive_action`, `google_photos_action`: Экземпляры `QAction`, действия для меню `url_menu`.
*  `chatgpt_action`, `gemini_action`, `claude_action`: Экземпляры `QAction`, действия для меню `model_menu`.
*   `url`, переменная для хранения URL.

### **Потенциальные ошибки и области для улучшения:**

*   **Обработка ошибок выбора браузера:** Если пользователь не выбирает браузер, приложение завершается. Можно добавить обработку этого случая и предложить пользователю повторить выбор.
*   **Поддержка других браузеров:** В данный момент поддерживаются только Chrome, Firefox и Edge. Можно расширить список поддерживаемых браузеров.
*   **Валидация URL:** Можно добавить валидацию введенного URL, чтобы убедиться, что он имеет корректный формат.
*   **Использование `QSettings`**:  Для сохранения выбора браузера, размера окна и других пользовательских настроек можно использовать `QSettings`. Это позволит пользователям не выбирать браузер каждый раз при запуске.
*   **Замена  `https://gemini.example.com/` и `https://claude.example.com/` на реальные URL**
*   **Отсутствие явного отображения ошибки:**  Если пользователь введет URL с ошибкой, например `htpp://`, браузер не загрузит страницу, но пользователь не увидит уведомления об этом.
*   **Отсутствие функции обновления страницы**
*   **Обработка случаев, когда пользователь нажимает "X" на форме выбора браузера.**

### **Взаимосвязи с другими частями проекта:**

*   Данный файл является частью GUI, отвечающего за отображение веб-интерфейса для работы с моделями.
*   Использует стандартные библиотеки Python (`sys`, `os`) и библиотеку PyQt6 для построения графического интерфейса.
*   Может зависеть от других частей проекта, если, например, для работы с моделями потребуется вызывать дополнительные функции.
*   Непосредственной связи с `header.py` в данном коде нет, поэтому `mermaid` блок для него не требуется.

**В заключение:**
Этот код представляет собой приложение на PyQt6, которое позволяет пользователю просматривать веб-страницы, выбирать браузер, сворачивать окно в трей и выбирать предопределенные URL-адреса. Код включает в себя обработку событий, настройку интерфейса и управление браузером.