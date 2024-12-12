## <алгоритм>

**1. Инициализация драйвера:**

   - Пользователь вызывает `Driver(WebDriver_Class)`, где `WebDriver_Class` - класс конкретного веб-драйвера (например, `Chrome`, `Firefox`).
   - Метакласс `DriverMeta` перехватывает вызов.
   - `DriverMeta.__call__()` создает динамический класс `Driver`, который наследуется от `DriverBase` и переданного класса `WebDriver_Class`.
   - Создается экземпляр динамического класса `Driver`.
   - В методе `__init__()` созданного класса вызывается метод `driver_payload()`, который инициализирует объекты `JavaScript` и `ExecuteLocator`.

**Пример:**
    ```python
    from src.webdriver.driver import Driver, Chrome
    driver_instance = Driver(Chrome) 
    ```

**2. Переход по URL:**

   - Пользователь вызывает `driver_instance.get_url(url)`.
   - Метод `get_url` устанавливает `referrer` и `previous_url`.
   - Метод использует `driver.get(url)` для перехода по URL.
   - Вызывается `wait_for_page_load()` для ожидания полной загрузки страницы.
   - В случае неудачного перехода выбрасывается исключение `WebDriverException`.

**Пример:**
    ```python
    driver_instance.get_url("https://example.com")
    ```

**3. Прокрутка страницы:**

   - Пользователь вызывает `driver_instance.scroll(scrolls, frame_size, direction, delay)`.
   - Метод вызывает JavaScript-метод `scroll_by_frame(frame_size, direction)`, передавая ему параметры.
   -  В цикле, повторяющемся `scrolls` раз, выполняется прокрутка и задержка `delay`.

**Пример:**
   ```python
   driver_instance.scroll(scrolls=3, frame_size=500, direction='forward', delay=0.5)
   ```

**4. Определение языка страницы:**

   - Пользователь вызывает `driver_instance.locale()`.
   - Метод выполняет JavaScript-код для получения языка страницы.
   - Возвращает язык страницы или `None`, если не удалось получить.

**Пример:**
   ```python
   page_language = driver_instance.locale()
   ```

**5. Сохранение куки:**

   - Пользователь вызывает `driver_instance._save_cookies_localy(filepath)`.
   - Метод получает куки драйвера.
   - Сохраняет куки в файл pickle по указанному пути.

**Пример:**
    ```python
    driver_instance._save_cookies_localy('cookies.pkl')
    ```
**6. Обновление страницы:**

   - Пользователь вызывает `driver_instance.page_refresh()`.
   - Метод обновляет текущую страницу.

**Пример:**
   ```python
   driver_instance.page_refresh()
   ```

## <mermaid>

```mermaid
graph LR
    A[Пользователь] --> B(Driver(WebDriver_Class));
    B --> C(DriverMeta.__call__);
    C --> D[Создание класса Driver];
    D --> E(Driver.__init__);
    E --> F(driver_payload());
    F --> G[Инициализация JavaScript];
    F --> H[Инициализация ExecuteLocator];
    A --> I(driver_instance.get_url(url));
    I --> J[Установка referrer и previous_url];
    J --> K(driver.get(url));
    K --> L(wait_for_page_load());
     L -- Успешно --> M[Загрузка страницы];
     L -- Ошибка --> N[WebDriverException];
    A --> O(driver_instance.scroll(scrolls, frame_size, direction, delay));
     O --> P[Цикл прокрутки];
      P -- Прокрутка --> Q(JavaScript.scroll_by_frame);
       Q --> P
    A --> R(driver_instance.locale());
     R --> S(JavaScript.get_page_lang);
       S --> T[Возвращение языка страницы]
    A --> U(driver_instance._save_cookies_localy(filepath));
    U --> V[Получение куки];
    V --> W[Сохранение куки в файл];
    A --> X(driver_instance.page_refresh());
    X --> Y[Обновление страницы];
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#ccf,stroke:#333,stroke-width:2px
    style C fill:#ccf,stroke:#333,stroke-width:2px
    style D fill:#ccf,stroke:#333,stroke-width:2px
    style E fill:#ccf,stroke:#333,stroke-width:2px
    style F fill:#ccf,stroke:#333,stroke-width:2px
    style G fill:#eef,stroke:#333,stroke-width:2px
    style H fill:#eef,stroke:#333,stroke-width:2px
    style I fill:#f9f,stroke:#333,stroke-width:2px
    style J fill:#eef,stroke:#333,stroke-width:2px
    style K fill:#eef,stroke:#333,stroke-width:2px
    style L fill:#eef,stroke:#333,stroke-width:2px
     style M fill:#eef,stroke:#333,stroke-width:2px
     style N fill:#eef,stroke:#333,stroke-width:2px
    style O fill:#f9f,stroke:#333,stroke-width:2px
     style P fill:#eef,stroke:#333,stroke-width:2px
      style Q fill:#eef,stroke:#333,stroke-width:2px
      style R fill:#f9f,stroke:#333,stroke-width:2px
       style S fill:#eef,stroke:#333,stroke-width:2px
     style T fill:#eef,stroke:#333,stroke-width:2px
      style U fill:#f9f,stroke:#333,stroke-width:2px
      style V fill:#eef,stroke:#333,stroke-width:2px
      style W fill:#eef,stroke:#333,stroke-width:2px
       style X fill:#f9f,stroke:#333,stroke-width:2px
      style Y fill:#eef,stroke:#333,stroke-width:2px
```

**Зависимости диаграммы:**

-   **Пользователь**: Инициирует создание драйвера и вызывает методы для взаимодействия с веб-страницей.
-   **Driver(WebDriver_Class)**: Создает экземпляр драйвера для конкретного браузера. Зависит от класса WebDriver (например, Chrome).
-   **DriverMeta.\_\_call\_\_**: Метакласс, создает динамический класс `Driver`.
-   **Создание класса Driver**:  Динамическое создание класса, наследованного от `DriverBase` и  `WebDriver_Class`.
-  **Driver.\_\_init\_\_**: Инициализация экземпляра драйвера и вызов `driver_payload()`
-   **driver\_payload()**: Инициализирует `JavaScript` и `ExecuteLocator`, создает экземпляры этих объектов, чтобы работать с веб-страницей.
-   **JavaScript**: Класс для выполнения JavaScript-кода на странице.
-   **ExecuteLocator**: Класс для выполнения поиска элементов на странице.
-  **driver_instance.get_url(url)**: Метод класса `DriverBase`, вызываемый для перехода на URL.
-   **Установка referrer и previous\_url**: В методе `get_url`,  установка соответствующих значений для отслеживания истории переходов
-  **driver.get(url)**: Метод selenium для перехода на страницу.
- **wait_for_page_load()**: Ожидание загрузки страницы.
- **WebDriverException**: Исключение, выбрасываемое в случае проблем с загрузкой.
- **driver\_instance.scroll(scrolls, frame\_size, direction, delay)**: Метод для прокрутки страницы.
-   **Цикл прокрутки**: Цикл, выполняющий множественную прокрутку.
-   **JavaScript.scroll\_by\_frame**: Метод JavaScript для прокрутки.
-   **driver\_instance.locale()**: Метод для получения языка страницы.
-  **JavaScript.get_page_lang**: Метод JavaScript для получения языка.
-   **Возвращение языка страницы**: Результат работы функции.
- **driver_instance.\_save\_cookies\_localy(filepath)**: Метод для сохранения куки в файл.
- **Получение куки**: получение куки текущего драйвера.
- **Сохранение куки в файл**: Сохранение куки в файл pickle.
- **driver_instance.page_refresh()**: Метод для обновления текущей страницы.
- **Обновление страницы**: Перезагрузка текущей страницы.

## <объяснение>

**Импорты:**

-   `sys`: Используется для доступа к параметрам командной строки и системным функциям. В данном коде не используется напрямую.
-   `pickle`: Используется для сериализации и десериализации объектов Python, например, куки, для сохранения их в файл и загрузки из него.
-   `time`: Используется для работы со временем, например, для добавления пауз в процессе выполнения скрипта.
-   `copy`: Используется для создания копий объектов. В коде не используется, вероятно, может быть использовано в будущем.
-   `pathlib.Path`: Используется для работы с файловыми путями в кроссплатформенном режиме.
-   `typing.Type, typing.Union`: Используется для аннотации типов, что улучшает читаемость и поддержку кода, а также позволяет использовать статические анализаторы кода.
-   `urllib.parse`: Используется для разбора и конструирования URL-адресов.
-   `selenium.webdriver.common.action_chains.ActionChains`: Используется для выполнения сложных действий, таких как перемещение мыши, двойные клики и т.д.
-   `selenium.webdriver.common.keys.Keys`: Используется для представления специальных клавиш на клавиатуре, таких как Enter, Escape и т.д.
-   `selenium.webdriver.common.by.By`: Используется для указания метода поиска элемента на странице, например, по ID, CSS-селектору и т.д.
-   `selenium.webdriver.support.expected_conditions as EC`: Используется для определения условий, которые должны быть выполнены перед продолжением работы, например, ожидание появления элемента на странице.
-   `selenium.webdriver.support.ui.WebDriverWait`: Используется для ожидания появления элемента на странице с заданным тайм-аутом.
-   `selenium.webdriver.remote.webelement.WebElement`: Используется для представления веб-элементов на странице.
-   `selenium.common.exceptions.*`: Используется для обработки исключений, которые могут возникнуть при взаимодействии с веб-драйвером.
-  `src.gs`:  Импортируется  модуль `gs` из каталога `src`, может содержать глобальные настройки или константы.
-  `src.webdriver.executor.ExecuteLocator`: Импортируется класс `ExecuteLocator` из `src/webdriver/executor`,  предназначен для поиска элементов с помощью локаторов.
-  `src.webdriver.javascript.js.JavaScript`: Импортируется класс `JavaScript` из `src/webdriver/javascript`,  предназначен для управления и выполнения js на странице.
-   `src.utils.printer.pprint`: Импортируется функция `pprint` из `src/utils/printer`, для красивого вывода данных.
-   `src.logger.logger.logger`: Импортируется объект `logger` из `src/logger/logger`, используется для логирования событий.
-   `src.logger.exceptions.WebDriverException`: Импортируется класс `WebDriverException` из `src/logger/exceptions`, используется для создания кастомных исключений WebDriver.

**Классы:**

-   **`DriverBase`**:
    -   **Роль**: Базовый класс для всех веб-драйверов, предоставляющий общие методы и атрибуты.
    -   **Атрибуты**:
        -   `previous_url`: Хранит URL предыдущей страницы.
        -   `referrer`: Хранит реферер страницы.
        -   `page_lang`: Хранит язык страницы.
        -  `js`: экземпляр `JavaScript` для выполнения JavaScript на странице.
        - `locator`: экземпляр `ExecuteLocator` для поиска элементов на странице.
    -   **Методы**:
        -   `driver_payload()`: Инициализирует атрибуты `js` и `locator`.
        -   `scroll()`: Прокручивает страницу.
        -   `locale()`: Определяет язык страницы.
        -   `get_url(url: str)`: Переходит по указанному URL.
        -   `extract_domain(url: str)`: Извлекает доменное имя из URL.
        -   `_save_cookies_localy(to_file: Union[str, Path])`: Сохраняет куки в файл.
        -   `page_refresh()`: Обновляет страницу.
        -   `window_focus()`: Восстанавливает фокус окна.
        -   `wait(interval: float)`: Делает паузу.
        -  `wait_for_page_load`: Ожидание загрузки страницы
        -  `delete_driver_logs`: Удаление логов и временных файлов

-   **`DriverMeta`**:
    -   **Роль**: Метакласс, создающий динамические классы `Driver`.
    -   **Метод `__call__`**: Создает новый класс `Driver`, наследующий от `DriverBase` и переданного класса веб-драйвера.

-   **`Driver`**:
    -   **Роль**: Динамический класс, представляющий конкретный веб-драйвер.
    -   **Атрибуты**: Наследует атрибуты и методы от `DriverBase` и конкретного веб-драйвера.

**Функции:**

-   Все методы внутри классов `DriverBase`, `DriverMeta` и `Driver` выполняют специфические действия, связанные с управлением веб-драйвером и взаимодействием со страницей.

**Переменные:**

-   Переменные внутри методов используются для хранения промежуточных значений, таких как URL, параметры прокрутки, и т.д.
-   Атрибуты класса хранят состояние объекта, такое как `previous_url`, `referrer`, `page_lang`.

**Потенциальные ошибки и области для улучшения:**

-   **Обработка исключений**: В некоторых методах могут отсутствовать полные блоки `try...except` для обработки исключений. Например, в методе `_save_cookies_localy` не обрабатываются ошибки при работе с файловой системой.
-   **Управление драйвером**: Методы `delete_driver_logs()` и `quit()` не представлены, необходимо их включить для более полного управления драйвером.
-   **Логирование**: Добавить более детальное логирование действий.
-   **Конфигурация**: Можно добавить параметры для конфигурации времени ожидания, путей к драйверам и т.д.

**Взаимосвязи с другими частями проекта:**

-   `src.webdriver.executor.ExecuteLocator`:  Используется для поиска элементов на странице.
-   `src.webdriver.javascript.js.JavaScript`: Используется для выполнения JavaScript-кода на странице.
-   `src.utils.printer`: Используется для форматированного вывода.
-   `src.logger`: Используется для логирования действий и ошибок.

**Дополнительные замечания:**
- Код предоставляет гибкую структуру для работы с различными веб-драйверами, используя метаклассы для динамического создания классов.
-  Методы предоставляют базовые возможности для навигации, прокрутки, взаимодействия со страницей и работы с куками.
- Код является частью более крупного проекта, и его функциональность должна быть расширена в соответствии с потребностями проекта.