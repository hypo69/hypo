## <алгоритм>

1. **Начало**: Запускается функция `main`.
2. **Создание экземпляра `Driver` (с `Chrome`):**
   - Создается экземпляр `chrome_driver` класса `Driver`, используя класс `Chrome` в качестве драйвера.
   - Пример: `chrome_driver = Driver(Chrome)`
3. **Переход по URL**:
   - `chrome_driver` вызывает метод `get_url` для навигации на "https://www.example.com".
   - Если навигация успешна, выводится сообщение об успехе.
   - Пример: `if chrome_driver.get_url("https://www.example.com"):`
4. **Извлечение домена**:
    - Метод `extract_domain` извлекает домен из URL, возвращая "www.example.com".
    - Пример: `domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")`
5.  **Сохранение cookie**:
    - Метод `_save_cookies_localy` сохраняет cookie в локальный файл. 
    - Если сохранение успешно, выводится сообщение.
    - Пример: `success = chrome_driver._save_cookies_localy()`
6.  **Обновление страницы**:
    - Метод `page_refresh` обновляет страницу.
    - Если обновление успешно, выводится сообщение.
    - Пример: `if chrome_driver.page_refresh():`
7.  **Прокрутка страницы**:
    - Метод `scroll` прокручивает страницу вниз на 3 раза с размером фрейма 1000 и задержкой 1 секунду.
    - Если прокрутка успешна, выводится сообщение.
    - Пример: `if chrome_driver.scroll(scrolls=3, direction='forward', frame_size=1000, delay=1):`
8.  **Получение языка страницы**:
    - Атрибут `locale` возвращает текущий язык страницы.
    - Пример: `page_language = chrome_driver.locale`
9.  **Создание экземпляра `Driver` с кастомным user-agent**:
    - Создается новый экземпляр `custom_chrome_driver` с кастомным user-agent.
    - Пример: `custom_chrome_driver = Driver(Chrome, user_agent=user_agent)`
10. **Переход по URL (с кастомным user-agent)**:
    - `custom_chrome_driver` переходит на "https://www.example.com", используя кастомный user-agent.
    - Выводится сообщение об успехе.
    - Пример: `if custom_chrome_driver.get_url("https://www.example.com"):`
11. **Поиск элемента**:
    - Метод `find_element` ищет элемент `h1` на странице по CSS селектору.
    - Если элемент найден, выводится его текст.
    - Пример: `element = chrome_driver.find_element(By.CSS_SELECTOR, 'h1')`
12. **Получение текущего URL**:
    - Атрибут `current_url` возвращает текущий URL страницы.
    - Пример: `current_url = chrome_driver.current_url`
13. **Фокусировка окна**:
    - Метод `window_focus` фокусирует окно, убирая фокус с элемента.
    - Выводится сообщение.
    - Пример: `chrome_driver.window_focus()`
14. **Конец**: Завершение функции `main`.

## <mermaid>

```mermaid
flowchart TD
    Start(Start) --> CreateDriver1[Создание chrome_driver: <br>chrome_driver = Driver(Chrome)]
    CreateDriver1 --> Navigate1[Переход по URL: <br> chrome_driver.get_url("https://www.example.com")]
    Navigate1 --> ExtractDomain[Извлечение домена:<br>domain = chrome_driver.extract_domain("https://www.example.com/path/to/page")]
    ExtractDomain --> SaveCookies[Сохранение cookie: <br>chrome_driver._save_cookies_localy()]
    SaveCookies --> RefreshPage[Обновление страницы: <br>chrome_driver.page_refresh()]
    RefreshPage --> ScrollPage[Прокрутка страницы: <br>chrome_driver.scroll(...)]
    ScrollPage --> GetLanguage[Получение языка страницы: <br> page_language = chrome_driver.locale]
    GetLanguage --> CreateDriver2[Создание custom_chrome_driver: <br> custom_chrome_driver = Driver(Chrome, user_agent=user_agent)]
    CreateDriver2 --> Navigate2[Переход по URL (с кастомным user-agent): <br>custom_chrome_driver.get_url("https://www.example.com")]
    Navigate2 --> FindElement[Поиск элемента: <br>element = chrome_driver.find_element(...)]
    FindElement --> GetCurrentUrl[Получение текущего URL: <br>current_url = chrome_driver.current_url]
    GetCurrentUrl --> FocusWindow[Фокусировка окна: <br>chrome_driver.window_focus()]
    FocusWindow --> End(End)
```

## <объяснение>

**Импорты:**

- `from src.webdriver.driver import Driver, Chrome`: Импортирует классы `Driver` и `Chrome` из модуля `src.webdriver.driver`.
  - `Driver` - это базовый класс для управления браузерным драйвером.
  - `Chrome` - это класс, реализующий логику для управления браузером Chrome, наследуясь от `Driver`.
  - Этот импорт устанавливает основную функциональность для работы с браузером.
- `from selenium.webdriver.common.by import By`: Импортирует класс `By` из `selenium.webdriver.common.by`.
  - `By` используется для определения стратегии поиска элементов на веб-странице (например, по CSS селектору, ID, XPath).
  - Этот импорт необходим для метода `find_element` в классе `Driver`.

**Функции:**

- `def main():`: Главная функция, которая демонстрирует использование классов `Driver` и `Chrome`.
  - Она создает экземпляры `Driver` (используя `Chrome`), выполняет различные действия, такие как навигация по URL, сохранение cookie, обновление страницы, прокрутка, получение языка страницы, поиск элементов и фокусировка окна.
  - Функция не принимает аргументов и не возвращает значения.

**Переменные:**

- `chrome_driver`: Экземпляр класса `Driver`, созданный с использованием класса `Chrome`. Используется для управления браузером.
- `domain`: Строка, содержащая доменное имя, извлеченное из URL.
- `success`: Булева переменная, показывающая успех выполнения операции сохранения cookies.
- `page_language`: Строка, содержащая язык текущей страницы.
- `user_agent`: Словарь, представляющий кастомный user-agent для браузера.
- `custom_chrome_driver`: Экземпляр класса `Driver`, созданный с кастомным user-agent.
- `element`: Экземпляр элемента (из selenium), найденного на веб-странице, или None, если не найден.
- `current_url`: Строка, содержащая текущий URL веб-страницы.

**Классы:**

- `class Driver`:
    - Этот класс является базовым для управления веб-драйвером, предоставляя абстрактный интерфейс для навигации по URL, извлечения домена, сохранения cookie, обновления страницы, прокрутки страницы, получения языка страницы, поиска элементов и фокусировки окна.
- `class Chrome`:
    - Этот класс наследуется от `Driver` и реализует специфическую логику для управления браузером Chrome.
    - В нем устанавливается драйвер Chrome и реализуются методы, необходимые для управления браузером.

**Объяснение кода:**
Код является примером использования классов `Driver` и `Chrome` для управления браузером Chrome и выполнения различных действий на веб-странице.
- Класс `Driver` обеспечивает базовый интерфейс для взаимодействия с веб-драйвером.
- Класс `Chrome` расширяет `Driver` и предоставляет специфическую функциональность для браузера Chrome.
- Функция `main` демонстрирует, как создать экземпляр `Driver` с `Chrome` (либо с кастомным user-agent) и использовать его для навигации по URL, извлечения домена, сохранения cookie, обновления страницы, прокрутки, получения языка страницы, поиска элементов, и фокусировки окна.
- Используются методы `get_url`, `extract_domain`, `_save_cookies_localy`, `page_refresh`, `scroll`, `locale`, `find_element`, `current_url`, и `window_focus`, которые демонстрируют возможности класса Driver.
- Код включает примеры использования стандартного и кастомного user-agent, что позволяет управлять тем, как браузер идентифицируется на веб-сайтах.

**Возможные улучшения:**

- **Обработка исключений:** Код не включает обработку исключений. Рекомендуется добавить блоки `try-except` для обработки потенциальных ошибок, таких как неудачная навигация или поиск элемента, это повысит надежность кода.
- **Логирование**: Добавление логирования может помочь отслеживать выполнение программы и выявлять проблемы.

**Взаимосвязь с другими частями проекта:**
- Данный файл является примером использования классов `Driver` и `Chrome`, которые находятся в модуле `src.webdriver.driver`.
- Код показывает, как можно использовать эти классы для автоматизации взаимодействия с веб-браузером.
- Взаимодействие происходит через вызовы методов `Driver`, которые используют возможности `Chrome` для непосредственного управления браузером.