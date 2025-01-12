## <алгоритм>

1. **Инициализация**:
   - Начинается выполнение функции `main()`.
   - Выводится сообщение "Creating a Chrome browser instance...".
   - Создаётся экземпляр класса `Driver` с аргументом `Chrome`, который обозначает использование веб-драйвера Chrome.
   - **Пример:** `chrome_driver = Driver(Chrome)`
2. **Навигация и Проверка**:
    - Устанавливается URL: `url = "https://www.example.com"`
    - Используется метод `get_url()` для перехода по URL. Результат проверяется.
    -  **Пример:** `if chrome_driver.get_url(url):`
     - Если навигация успешна, выводится сообщение `Successfully navigated to ...`, иначе `Failed to navigate to ...`.
3. **Извлечение домена**:
    - Используется метод `extract_domain()` для извлечения домена из URL.
    -  **Пример:** `domain = chrome_driver.extract_domain(url)`
    - Выводится извлеченный домен.
4. **Прокрутка страницы**:
    - Используется метод `scroll()` для прокрутки страницы вниз (на 3 прокрутки).
    -  **Пример:** `if chrome_driver.scroll(scrolls=3, direction='forward'):`
      - Если прокрутка успешна, выводится `Successfully scrolled down the page`, иначе `Failed to scroll down the page`.
5. **Сохранение Cookies**:
    - Используется метод `_save_cookies_localy()` для сохранения cookies в файл `cookies_chrome.pkl`.
    -  **Пример:** `if chrome_driver._save_cookies_localy(to_file='cookies_chrome.pkl'):`
    - Выводится сообщение об успехе или неудаче сохранения cookies.
6. **Закрытие драйвера**:
    - Блок `finally` гарантирует, что метод `quit()` всегда будет вызван для закрытия браузера Chrome.
     - **Пример:** `chrome_driver.quit()`
    - Выводится сообщение "Chrome browser closed.".
7. **Повторение шагов 1-6 для Firefox и Edge**:
   - Процесс повторяется для браузера Firefox с  созданием экземпляра `firefox_driver = Driver(Firefox)`.
     - Прокрутка страницы вверх (2 прокрутки).
     - Сохранение в файл `cookies_firefox.pkl`.
   - Процесс повторяется для браузера Edge с созданием экземпляра `edge_driver = Driver(Edge)`.
      - Прокрутка страницы в обоих направлениях.
      - Сохранение в файл `cookies_edge.pkl`.
8. **Завершение**:
    - После обработки каждого драйвера, каждый из них закрывается в `finally`.
   - Функция `main()` завершает свою работу.

## <mermaid>

```mermaid
flowchart TD
    Start(Start main function) --> ChromeInit[Initialize Chrome Driver];
    ChromeInit --> ChromeNav(Navigate to URL in Chrome and check);
    ChromeNav -- Success --> ChromeExtract(Extract Domain from URL for Chrome);
    ChromeNav -- Failure --> ChromeExtract;
    ChromeExtract --> ChromeScrollDown(Scroll Down in Chrome);
    ChromeScrollDown -- Success --> ChromeSaveCookies(Save Cookies for Chrome);
    ChromeScrollDown -- Failure --> ChromeSaveCookies;
    ChromeSaveCookies -- Success --> ChromeClose(Close Chrome Driver);
    ChromeSaveCookies -- Failure --> ChromeClose;
    ChromeClose --> FirefoxInit(Initialize Firefox Driver);
    FirefoxInit --> FirefoxNav(Navigate to URL in Firefox and check);
    FirefoxNav -- Success --> FirefoxExtract(Extract Domain from URL for Firefox);
    FirefoxNav -- Failure --> FirefoxExtract;
    FirefoxExtract --> FirefoxScrollUp(Scroll Up in Firefox);
    FirefoxScrollUp -- Success --> FirefoxSaveCookies(Save Cookies for Firefox);
    FirefoxScrollUp -- Failure --> FirefoxSaveCookies;
    FirefoxSaveCookies -- Success --> FirefoxClose(Close Firefox Driver);
    FirefoxSaveCookies -- Failure --> FirefoxClose;
    FirefoxClose --> EdgeInit(Initialize Edge Driver);
    EdgeInit --> EdgeNav(Navigate to URL in Edge and check);
    EdgeNav -- Success --> EdgeExtract(Extract Domain from URL for Edge);
    EdgeNav -- Failure --> EdgeExtract;
    EdgeExtract --> EdgeScrollBoth(Scroll both directions in Edge);
    EdgeScrollBoth -- Success --> EdgeSaveCookies(Save Cookies for Edge);
    EdgeScrollBoth -- Failure --> EdgeSaveCookies;
    EdgeSaveCookies -- Success --> EdgeClose(Close Edge Driver);
    EdgeSaveCookies -- Failure --> EdgeClose;
    EdgeClose --> End(End main function);
    classDef step fill:#f9f,stroke:#333,stroke-width:2px
    class Start, ChromeInit, ChromeNav, ChromeExtract, ChromeScrollDown, ChromeSaveCookies, ChromeClose, FirefoxInit, FirefoxNav, FirefoxExtract, FirefoxScrollUp, FirefoxSaveCookies, FirefoxClose, EdgeInit, EdgeNav, EdgeExtract, EdgeScrollBoth, EdgeSaveCookies, EdgeClose, End step
```
**Объяснение `mermaid`:**

Диаграмма представляет собой блок-схему, отображающую последовательность действий в функции `main()`. 
- **`Start`**: начало функции main.
- **`ChromeInit`**: Создание экземпляра драйвера Chrome.
- **`ChromeNav`**: Переход по URL и проверка успешности в Chrome.
- **`ChromeExtract`**: Извлечение домена из URL для Chrome.
- **`ChromeScrollDown`**: Прокрутка страницы вниз в Chrome.
- **`ChromeSaveCookies`**: Сохранение cookies в Chrome.
- **`ChromeClose`**: Закрытие драйвера Chrome.
- Аналогичные блоки для Firefox и Edge.
- **`End`**: Завершение функции main.
- Вся последовательность действий  запускается для Chrome, затем Firefox и в конце Edge.
- Зеленым цветом выделены все блоки для визуального разделения.

## <объяснение>

**Импорты:**

- `from src.webdriver.driver import Driver, Chrome, Firefox, Edge`:
    - Импортирует класс `Driver`, а также классы `Chrome`, `Firefox`, и `Edge` из модуля `src.webdriver.driver`. 
    - `Driver` - это класс, который управляет веб-драйвером.
    - `Chrome`, `Firefox`, и `Edge` - это классы, представляющие конкретные веб-драйверы для соответствующих браузеров.
    -  Использование этих классов позволяет создать экземпляр драйвера для управления различными браузерами.

**Функции:**

- `def main():`:
    - Главная функция, которая демонстрирует использование класса `Driver`.
    - Не принимает аргументов.
    - Не возвращает значения (возвращает `None` по умолчанию).
    - Организует создание экземпляров `Driver` для Chrome, Firefox и Edge, а также выполнение основных действий: навигация, извлечение домена, прокрутка страницы, сохранение cookies и закрытие драйвера.

**Переменные:**

- `chrome_driver`, `firefox_driver`, `edge_driver`:
    - Экземпляры класса `Driver`, представляющие собой драйверы для Chrome, Firefox и Edge соответственно.
    - Тип: `Driver`.
- `url`:
    - URL-адрес для навигации в браузере.
    - Тип: `str`.
- `domain`:
    - Извлеченный домен из URL.
    - Тип: `str`.

**Классы:**

- `Driver`:
    - Это класс, который управляет веб-драйвером.
    - В данном примере, экземпляры `Driver` создаются с аргументами `Chrome`, `Firefox`, и `Edge`, которые указывают, какой веб-драйвер использовать.
    - Методы класса `Driver` (из файла `driver.py`) позволяют выполнять такие действия, как:
        - `get_url(url)`: переходит по указанному URL.
        - `extract_domain(url)`: извлекает домен из URL.
        - `scroll(scrolls, direction)`: прокручивает страницу в указанном направлении и на определенное количество прокруток.
        - `_save_cookies_localy(to_file)`: сохраняет cookies в файл.
        - `quit()`: закрывает браузер.

**Объяснение работы кода:**

1. Код создает три экземпляра драйвера для каждого браузера: Chrome, Firefox и Edge.
2. Для каждого браузера выполняет последовательность действий:
   - Открывает указанный url `https://www.example.com`.
   - Извлекает домен.
   - Прокручивает страницу в различных направлениях (вниз для Chrome, вверх для Firefox, в обе стороны для Edge).
   - Сохраняет cookie в отдельный файл (cookies_chrome.pkl, cookies_firefox.pkl, cookies_edge.pkl).
3. Каждый экземпляр драйвера закрывается после завершения работы с ним, что гарантируется блоком `finally`.

**Взаимосвязь с другими частями проекта:**

- Данный файл `_example_driver.py` является демонстрационным примером использования класса `Driver`, определенного в файле `src.webdriver.driver.py`.
- Код не зависит от других частей проекта, кроме импорта из `src.webdriver.driver`.

**Потенциальные ошибки и области для улучшения:**

- **Обработка исключений**: Код не содержит обработки исключений в блоках `try`. Если произойдет ошибка при навигации, прокрутке или сохранении cookies, программа может завершиться аварийно. Можно добавить более детальную обработку исключений.
- **Пути к файлам**: Файлы `cookies_*.pkl` сохраняются локально. Для более гибкого решения можно задать путь к файлам через переменные окружения или параметры.
- **Проверка возвращаемых значений**:  Методы `get_url`, `scroll` и `_save_cookies_localy` возвращают `True` или `False`, но не обрабатывают возможные ошибки более детально. Можно добавить логирование ошибок.
- **Жестко заданные URL**: URL `https://www.example.com` задан в коде. Для гибкости можно передавать URL как параметр.
- **Управление драйвером**: Код не обрабатывает ситуации, когда драйвер не запускается или возникают ошибки при его использовании.