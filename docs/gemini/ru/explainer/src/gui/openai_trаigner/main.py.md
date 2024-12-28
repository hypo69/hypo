## <алгоритм>

1. **Инициализация приложения:**
   - Создается объект `QApplication` для управления GUI приложения.
   - Устанавливается флаг `setQuitOnLastWindowClosed(False)` для предотвращения выхода приложения при закрытии последнего окна.
   - Создается главное окно приложения `AssistantMainWindow`.
   - Главное окно отображается на экране.
   - Запускается основной цикл обработки событий приложения `app.exec()`.

2. **Инициализация `AssistantMainWindow`:**
   - Устанавливаются флаги окна для управления его поведением.
   - Устанавливаются размеры окна на 3/4 экрана и центрируется.
   - Запрашивается выбор браузера по умолчанию (`ask_for_browser()`).
     - Вызывается диалог `QMessageBox.getItem` для выбора браузера (Chrome, Firefox, Edge).
     - Возвращается выбранное имя браузера или `None`, если выбор не сделан или диалог отменен.
   - На основе выбора браузера определяется путь к профилю браузера.
   - Создается профиль веб-движка `QWebEngineProfile`.
   - Создается виджет для отображения веб-страниц `QWebEngineView` и настраивается для использования созданного профиля.
   - Создается верхняя панель `QWidget` и настраивается стилем.
   - Создается поле для ввода URL-адреса `QLineEdit`, подключается событие `returnPressed` к методу `load_url`.
   - Создаются кнопки для управления приложением:
     - Загрузка URL (`load_button`), подключается событие `clicked` к методу `load_url`.
     - Свернуть в трей (`minimize_button`), подключается событие `clicked` к методу `hide_to_tray`.
     - Открыть на весь экран (`fullscreen_button`), подключается событие `clicked` к методу `showFullScreen`.
     - Закрыть окно (`close_button`), подключается событие `clicked` к методу `hide_to_tray`.
   - Создается макет `QHBoxLayout` для верхней панели, добавляются виджеты и кнопки.
   - Создается основной макет окна `QVBoxLayout`, добавляется верхняя панель и виджет `QWebEngineView`.
   - Создается центральный виджет `QWidget`, устанавливается основной макет и устанавливается в главное окно.
   - Создается иконка в системном трее `QSystemTrayIcon`, устанавливается иконка.
   - Создается контекстное меню для иконки в трее:
     - Добавляется действие "Восстановить окно" (`restore_action`), подключается к методу `showNormal`.
     - Добавляется действие "Выход" (`quit_action`), подключается к методу `quit_app`.
   - Устанавливается меню в трее, иконка отображается.
   - Создается меню "Сервисы Google" (`url_menu`):
     - Добавляются действия для популярных сервисов Google (Google Login, Gmail, Docs, Sheets, Drive, Photos), подключаются к методу `load_url` с соответствующим URL.
   - Создается меню "Выбор модели" (`model_menu`):
     - Добавляются действия для выбора моделей (ChatGPT, Gemini, Claude), подключаются к методу `load_url` с соответствующими URL.
   - Создаются кнопки для открытия меню "Сервисы Google" и "Выбор модели" и добавляются в верхнюю панель.

3. **Загрузка URL (`load_url()`):**
   - Получает URL из поля ввода или из параметра.
   - Проверяет, начинается ли URL с "http", и добавляет "http://" при необходимости.
   - Устанавливает URL в `QWebEngineView` для загрузки веб-страницы.

4. **Скрытие в трей (`hide_to_tray()`):**
   - Скрывает главное окно приложения.

5. **Выход из приложения (`quit_app()`):**
   - Скрывает иконку приложения из системного трея.
   - Завершает работу приложения.

6. **Обработка события закрытия окна (`closeEvent()`):**
   - Перехватывает событие закрытия окна.
   - Игнорирует закрытие окна.
   - Вызывает метод `hide_to_tray()` для скрытия окна в системный трей.

## <mermaid>
```mermaid
flowchart TD
    Start[Начало приложения] --> CreateApp[Создать QApplication];
    CreateApp --> SetQuitOnLastWindowClosed[app.setQuitOnLastWindowClosed(False)];
    SetQuitOnLastWindowClosed --> CreateWindow[Создать AssistantMainWindow];
    CreateWindow --> ShowWindow[window.show()];
    ShowWindow --> StartEventLoop[Запустить app.exec()];
    StartEventLoop --> End[Конец приложения];

    subgraph AssistantMainWindow
        CreateWindow --> InitMainWindow[__init__()]
        InitMainWindow --> SetWindowFlags[Настроить флаги окна]
        SetWindowFlags --> SetGeometry[Установить размеры и положение окна]
        SetGeometry --> AskBrowser[ask_for_browser()]
        AskBrowser --> DetermineProfilePath{Определить путь к профилю браузера}
        DetermineProfilePath -- Chrome --> ChromeProfilePath[Путь к профилю Chrome]
        DetermineProfilePath -- Firefox --> FirefoxProfilePath[Путь к профилю Firefox]
        DetermineProfilePath -- Edge --> EdgeProfilePath[Путь к профилю Edge]
        DetermineProfilePath -- Unknown --> BrowserError[Сообщение об ошибке и выход]
        ChromeProfilePath --> CreateWebEngineProfile[Создать QWebEngineProfile]
        FirefoxProfilePath --> CreateWebEngineProfile
        EdgeProfilePath --> CreateWebEngineProfile
        CreateWebEngineProfile --> CreateWebView[Создать QWebEngineView]
        CreateWebView --> CreateTitleBar[Создать верхнюю панель (QWidget)]
        CreateTitleBar --> CreateUrlInput[Создать поле ввода URL (QLineEdit)]
        CreateUrlInput --> ConnectUrlInput[Подключить returnPressed к load_url]
        ConnectUrlInput --> CreateButtons[Создать кнопки управления]
        CreateButtons --> SetupTitleBarLayout[Настроить макет верхней панели (QHBoxLayout)]
        SetupTitleBarLayout --> SetupMainLayout[Настроить основной макет окна (QVBoxLayout)]
        SetupMainLayout --> CreateCentralWidget[Создать центральный виджет (QWidget)]
        CreateCentralWidget --> SetCentralWidget[Установить центральный виджет]
        SetCentralWidget --> CreateSystemTrayIcon[Создать иконку в системном трее (QSystemTrayIcon)]
        CreateSystemTrayIcon --> SetupTrayMenu[Настроить контекстное меню для трея (QMenu)]
         SetupTrayMenu --> ShowTrayIcon[tray_icon.show()]
        ShowTrayIcon --> CreateUrlMenu[Создать меню "Сервисы Google"]
         CreateUrlMenu --> CreateModelMenu[Создать меню "Выбор модели"]
         CreateModelMenu --> CreateMenuButtons[Создать кнопки открытия меню]
        CreateMenuButtons --> AddMenuButtonsToTitleBar[Добавить кнопки меню на верхнюю панель]
        AddMenuButtonsToTitleBar --> InitDone[Инициализация завершена]
        InitDone --> ShowWindow
    end

    subgraph BrowserChoice
        AskBrowser --> ShowBrowserDialog[QMessageBox.getItem()]
         ShowBrowserDialog --> BrowserSelected{Браузер выбран?}
         BrowserSelected -- Yes --> ReturnBrowserName[Вернуть имя браузера]
         BrowserSelected -- No --> ReturnNone[Вернуть None]
    end
    subgraph LoadUrl
        load_url --> GetUrlFromInput{Получить URL из поля ввода}
        GetUrlFromInput --> CheckUrlProtocol{URL начинается с "http"?}
        CheckUrlProtocol -- Yes --> LoadPage[browser.setUrl(QUrl(url))]
         CheckUrlProtocol -- No --> AddHttpToUrl[Добавить "http://" к URL]
         AddHttpToUrl --> LoadPage
    end
   
    subgraph HideToTray
        hide_to_tray --> HideMainWindow[self.hide()]
    end
     subgraph QuitApp
         quit_app --> HideTrayIcon[self.tray_icon.hide()]
         HideTrayIcon --> ExitApp[QApplication.quit()]
     end
      subgraph CloseEvent
        closeEvent --> IgnoreCloseEvent[event.ignore()]
        IgnoreCloseEvent --> CallHideToTray[self.hide_to_tray()]
      end
    
    CreateButtons --> MinimizeButton[Кнопка "Свернуть"]
    CreateButtons --> FullscreenButton[Кнопка "На весь экран"]
    CreateButtons --> CloseButton[Кнопка "Закрыть"]
    CreateButtons --> LoadButton[Кнопка "Загрузить"]
    
    MinimizeButton -- click --> HideToTray
    FullscreenButton -- click --> ShowFullScreen
    CloseButton -- click --> HideToTray
     LoadButton -- click --> load_url
     ConnectUrlInput -- returnPressed --> load_url
    
     HideMainWindow --> StartEventLoop
      ExitApp --> End
     CallHideToTray --> StartEventLoop
  
```

**Зависимости:**

- `PyQt6.QtCore`: Основные классы и функции для работы с Qt, включая `Qt` для флагов окна и `QUrl` для работы с URL.
- `PyQt6.QtGui`: Классы для работы с графическим интерфейсом, включая `QIcon` для иконок, `QAction` для действий меню.
- `PyQt6.QtWidgets`: Классы для создания виджетов, включая `QApplication` для приложения, `QMainWindow` для главного окна, `QSystemTrayIcon` для иконки в трее, `QMenu` для меню, `QPushButton` для кнопок, `QVBoxLayout` и `QHBoxLayout` для макетов, `QWidget` для контейнеров, `QLineEdit` для ввода текста, `QMessageBox` для диалогов.
- `PyQt6.QtWebEngineWidgets`: Классы для отображения веб-контента, включая `QWebEngineView` для просмотра веб-страниц.
- `PyQt6.QtWebEngineCore`: Классы для работы с веб-профилями, включая `QWebEngineProfile` для управления настройками браузера.
- `sys`: Стандартный модуль для доступа к параметрам командной строки и функциям выхода.
- `os`: Стандартный модуль для работы с операционной системой, например, для определения пути к профилям браузера.

## <объяснение>

### Импорты

-   `sys`: Используется для доступа к аргументам командной строки (sys.argv) и для завершения работы приложения (sys.exit).
-   `os`: Используется для работы с путями к файлам и каталогам, в частности, для получения пути к профилю браузера пользователя.
-   `PyQt6.QtCore`:
    -   `Qt`: Предоставляет перечисление констант, например, для флагов окон (Qt.WindowType).
    -   `QUrl`: Используется для представления URL-адресов и их обработки.
-   `PyQt6.QtGui`:
    -   `QIcon`: Используется для создания иконок для кнопок и иконки в системном трее.
    -   `QAction`: Используется для создания действий в меню.
-   `PyQt6.QtWidgets`:
    -   `QApplication`: Управляет жизненным циклом приложения и его основными параметрами.
    -   `QMainWindow`: Класс для создания главного окна приложения.
    -   `QSystemTrayIcon`: Позволяет отображать иконку приложения в системном трее.
    -   `QMenu`: Создает меню для кнопок и иконки в трее.
    -   `QPushButton`: Создает кнопки, которые реагируют на нажатия.
    -   `QVBoxLayout`, `QHBoxLayout`: Управляют расположением виджетов в контейнерах.
    -   `QWidget`: Базовый класс для создания виджетов и контейнеров.
    -   `QLineEdit`: Поле для ввода URL-адреса.
    -    `QMessageBox`: Используется для отображения диалоговых окон, таких как запрос на выбор браузера.
-   `PyQt6.QtWebEngineWidgets`:
    -   `QWebEngineView`: Используется для отображения веб-страниц в приложении.
-   `PyQt6.QtWebEngineCore`:
    -   `QWebEngineProfile`: Используется для управления профилем веб-движка, позволяя использовать профили браузера пользователя.

### Классы

#### `AssistantMainWindow`

-   **Роль:** Главное окно приложения, управляет всеми остальными элементами GUI.
-   **Атрибуты:**
    -   `profile`: Экземпляр `QWebEngineProfile` для управления профилем браузера.
    -   `browser`: Экземпляр `QWebEngineView` для отображения веб-страниц.
    -   `title_bar`: Виджет `QWidget`, представляющий верхнюю панель приложения.
    -   `url_input`: Виджет `QLineEdit` для ввода URL-адреса.
    -   `load_button`, `minimize_button`, `fullscreen_button`, `close_button`: Виджеты `QPushButton` для управления приложением.
    -   `tray_icon`: Экземпляр `QSystemTrayIcon` для управления иконкой в системном трее.
    -   `url_menu`: Виджет `QMenu`, представляющий меню сервисов Google.
     -   `model_menu`: Виджет `QMenu`, представляющий меню выбора моделей.
    -   `url_button`: Виджет `QPushButton`, открывающий меню сервисов Google.
    -   `model_button`: Виджет `QPushButton`, открывающий меню выбора моделей.
-   **Методы:**
    -   `__init__()`: Конструктор класса, инициализирует все компоненты главного окна.
    -   `ask_for_browser()`: Запрашивает у пользователя выбор браузера по умолчанию.
    -   `load_url(url: str = None)`: Загружает указанный URL в `QWebEngineView`.
    -   `hide_to_tray()`: Скрывает окно приложения и помещает его иконку в системный трей.
    -   `quit_app()`: Завершает работу приложения.
    -   `closeEvent(event)`: Переопределенный метод, обрабатывает событие закрытия окна, скрывая его в трей.

### Функции

-   `ask_for_browser(self)`:
    -   **Аргументы:** `self` (ссылка на экземпляр класса `AssistantMainWindow`).
    -   **Возвращаемое значение:** Строка с выбранным браузером ('Chrome', 'Firefox', 'Edge') или `None`, если выбор не сделан.
    -   **Назначение:** Вызывает диалоговое окно для выбора браузера по умолчанию.
    -   **Пример:**
        ```python
        browser = self.ask_for_browser()
        if browser == 'Chrome':
            print("Выбран браузер Chrome.")
        ```
-   `load_url(self, url: str = None)`:
    -   **Аргументы:**
        -   `self` (ссылка на экземпляр класса `AssistantMainWindow`).
        -   `url` (опционально): URL-адрес для загрузки.
    -   **Возвращаемое значение:** Нет.
    -   **Назначение:** Загружает веб-страницу по указанному URL.
    -   **Пример:**
        ```python
        self.load_url("https://www.google.com") # Загрузка Google
        self.load_url() # Загрузка URL из поля ввода
        ```
-   `hide_to_tray(self)`:
    -   **Аргументы:** `self` (ссылка на экземпляр класса `AssistantMainWindow`).
    -   **Возвращаемое значение:** Нет.
    -   **Назначение:** Скрывает главное окно приложения.
    -   **Пример:**
        ```python
        self.hide_to_tray()
        ```
-   `quit_app(self)`:
    -   **Аргументы:** `self` (ссылка на экземпляр класса `AssistantMainWindow`).
    -   **Возвращаемое значение:** Нет.
    -   **Назначение:** Завершает работу приложения.
    -   **Пример:**
        ```python
        self.quit_app()
        ```
-  `closeEvent(self, event)`:
    -   **Аргументы:**
          -   `self` (ссылка на экземпляр класса `AssistantMainWindow`).
          -   `event` (событие закрытия окна).
    -   **Возвращаемое значение:** Нет.
    -   **Назначение:** Перехватывает событие закрытия окна и скрывает окно в трей.
    -   **Пример:**
          ```python
          def closeEvent(self, event):
               event.ignore()
               self.hide_to_tray()
          ```
### Переменные

-   `app`: Экземпляр `QApplication`, управляющий приложением.
-   `window`: Экземпляр `AssistantMainWindow`, представляющий главное окно приложения.
-   `screen_geometry`: Геометрия экрана, используется для позиционирования окна.
-   `width`, `height`: Размеры окна, вычисляемые на основе геометрии экрана.
-   `browser_choice`: Строка, содержащая выбор браузера пользователя.
-   `profile_path`: Путь к профилю выбранного браузера.
-  `google_login_action`,`gmail_action`,`google_docs_action`,`google_sheets_action`, `google_drive_action`,`google_photos_action`: Действия в меню "Сервисы Google", открывающие соответствующие URL.
   `chatgpt_action`,`gemini_action`,`claude_action`: Действия в меню "Выбор модели", открывающие соответствующие URL.

### Потенциальные ошибки и области для улучшения

-   **Обработка ошибок при выборе браузера:** Если пользователь не выбирает браузер или выбирает неподдерживаемый, приложение завершается. Можно улучшить обработку, позволяя пользователю выбрать другой браузер или предлагая варианты по умолчанию.
-   **Некорректные URL:** Нет валидации URL перед загрузкой. Можно добавить проверку на корректность URL и обработку ошибок.
-   **Пути к профилям браузеров:** Пути к профилям жёстко заданы и могут не работать для всех пользователей и разных версий ОС. Можно сделать их более гибкими, например, использовать переменные окружения или системные вызовы.
-   **Отсутствие поддержки других браузеров:** Поддерживаются только Chrome, Firefox и Edge. Можно добавить поддержку других браузеров, если требуется.
-   **Иконки:** Иконки загружаются из системной темы, что может отличаться на разных системах. Можно добавить свои иконки для единообразия.
-   **Gemini и Claude URL:** Заглушки URL для Gemini и Claude.
-   **Локализация:** Нет локализации интерфейса.

### Взаимосвязи с другими частями проекта

-   Этот модуль `main.py` является точкой входа в GUI приложение и не взаимодействует напрямую с другими частями проекта. Все импорты связаны с PyQt6 и стандартными библиотеками Python.