## <алгоритм>

1.  **Инициализация**:
    *   Создается экземпляр класса `Edge`.
    *   Если `user_agent` не передан, генерируется случайный `user_agent` с помощью `fake_useragent.UserAgent().random`.
    *   Загружаются настройки из `edge.json`.
    *   Создается объект `EdgeOptions`.
    *   Устанавливается `user-agent` в опциях браузера.
        *   Пример: `options_obj.add_argument(f'user-agent={self.user_agent}')`
    *   Если переданы дополнительные `options`, они добавляются в `EdgeOptions`.
        *   Пример: `options_obj.add_argument('--disable-notifications')`
    *   Из настроек, если они есть, добавляются `options`.
        *   Пример: если `settings.options` содержит `['--disable-infobars']`, то `options_obj.add_argument('--disable-infobars')`
    *    Из настроек, если они есть, добавляются `headers`.
        *   Пример: если `settings.headers` содержит `{'accept_language': 'en-US'}`, то `options_obj.add_argument('--accept_language=en-US')`

2.  **Запуск WebDriver**:
    *   Из настроек извлекается путь к `edgedriver`.
    *   Создается объект `EdgeService` с указанным путем к `edgedriver`.
        *   Пример: `service = EdgeService(executable_path=str(edgedriver_path))`
    *   Создается экземпляр `WebDriver` (`selenium.webdriver.Edge`) с `options` и `service`.
        *   Пример: `super().__init__(options=options_obj, service=service)`
    *   Вызывается метод `_payload` для установки дополнительных функций.
        *   Если происходит ошибка при старте, то логируется критическая ошибка и  возвращается `None`

3.  **Метод `_payload`**:
    *   Создается экземпляр класса `JavaScript` с передачей текущего WebDriver.
    *   Методы `JavaScript` устанавливаются как методы экземпляра класса `Edge`:
        *   `get_page_lang`
        *   `ready_state`
        *   `get_referrer`
        *   `unhide_DOM_element`
        *   `window_focus`
    *   Создается экземпляр класса `ExecuteLocator` с передачей текущего WebDriver.
    *   Методы `ExecuteLocator` устанавливаются как методы экземпляра класса `Edge`:
        *   `execute_locator`
        *   `get_webelement_as_screenshot`
        *   `get_webelement_by_locator`
        *   `get_attribute_by_locator`
        *   `send_message` и `send_key_to_webelement` (указывают на один метод)

4.  **Метод `set_options`**:
    *   Создает экземпляр `EdgeOptions`.
    *   Если переданы дополнительные опции, они добавляются к `EdgeOptions`.
    *   Возвращается настроенный объект `EdgeOptions`.

5.  **Пример использования (`if __name__ == "__main__":`)**:
    *   Создается экземпляр `Edge` с параметрами `options=["--headless", "--disable-gpu"]`.
    *   Загружается страница `https://www.example.com`.

## <mermaid>

```mermaid
graph LR
    A[Начало] --> B{user_agent передан?};
    B -- Да --> C[user_agent = user_agent];
    B -- Нет --> D[user_agent = UserAgent().random];
    C --> E[Загрузка настроек из edge.json];
    D --> E;
    E --> F[Создание EdgeOptions()];
    F --> G[Установка user-agent];
    G --> H{options переданы?};
     H -- Да --> I[Добавление options из списка];
     I --> J{Настройки.options?};
     H -- Нет --> J;
     J -- Да --> K[Добавление options из настроек];
     K --> L{Настройки.headers?};
     J -- Нет --> L;
    L -- Да --> M[Добавление headers из настроек];
     L -- Нет --> N[Извлечение edgedriver_path];
    M --> N;
    N --> O[Создание EdgeService()];
    O --> P[Создание WebDriver (Edge)];
    P --> Q[Вызов _payload()];
    Q --> R[Создание JavaScript()];
    R --> S[Привязка методов JavaScript];
    S --> T[Создание ExecuteLocator()];
    T --> U[Привязка методов ExecuteLocator];
    U --> V[Завершение];
     V --> W{Проверка на __name__ == "__main__"};
    W -- Да --> X[Создание экземпляра Edge с опциями];
     X --> Y[Загрузка страницы "https://www.example.com"];
     Y --> Z[Конец];
      W -- Нет --> Z;
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style Z fill:#f9f,stroke:#333,stroke-width:2px
```

**Описание зависимостей `mermaid`**:

*   **Начало/Конец**: `Начало` и `Конец` обозначают начало и завершение выполнения кода.
*   **Инициализация `user_agent`**:
    *   `user_agent` либо используется переданный аргумент, либо генерируется случайный.
*   **Загрузка настроек**:
    *   Настройки загружаются из файла `edge.json`.
*  **Создание `EdgeOptions`**:
    *   Создается экземпляр `EdgeOptions` для настройки параметров браузера.
*  **Настройка `user_agent`**:
    *   В опциях браузера устанавливается `user_agent`.
*  **Добавление пользовательских `options`**:
    *   Добавляются переданные `options`.
*  **Добавление `options` из настроек**:
    *  Добавляются `options` из настроек, если они есть.
*  **Добавление `headers` из настроек**:
    *   Добавляются `headers` из настроек, если они есть.
*   **Запуск `WebDriver`**:
    *   Извлекается путь к `edgedriver`.
    *   Создается `EdgeService` с указанным путем.
    *   Создается экземпляр `WebDriver` с `options` и `service`.
*   **Метод `_payload`**:
    *   Создается `JavaScript` и  `ExecuteLocator`.
    *   Их методы привязываются к экземпляру класса `Edge`.
*  **Выполнение основного блока**:
    *   При запуске `if __name__ == "__main__":` создается экземпляр `Edge` и открывается страница.

## <объяснение>

### Импорты

*   `os`: Используется для работы с операционной системой (в данном коде явно не используется, но может быть использован в других частях проекта).
*   `pathlib.Path`: Используется для работы с путями к файлам и директориям, в частности для загрузки конфигурации `edge.json`.
*   `typing.Optional, List`: Используются для аннотации типов, обозначая, что переменная может быть `None` или списком.
*   `selenium.webdriver.Edge`: Основной класс для управления браузером Edge.
*   `selenium.webdriver.edge.service.Service`: Класс для запуска и управления сервисом EdgeDriver.
*   `selenium.webdriver.edge.options.Options`: Класс для настройки параметров запуска браузера Edge.
*   `selenium.common.exceptions.WebDriverException`: Класс для обработки исключений, возникающих при работе с WebDriver.
*   `src.webdriver.executor.ExecuteLocator`: Класс для выполнения локаторов на веб-странице, предоставляет методы для взаимодействия с элементами (часть кастомного модуля).
*   `src.webdriver.js.JavaScript`: Класс, который реализует javascript функции для webdriver.
*   `fake_useragent.UserAgent`: Класс для генерации случайных user-agent строк.
*   `src.gs`:  Предположительно содержит глобальные настройки или константы для проекта.
*   `src.logger.logger`: Модуль для ведения логов, используется для отслеживания ошибок и общей работы скрипта.
*   `src.utils.jjson.j_loads_ns`: Функция для загрузки JSON-файлов и предоставления доступа к данным через атрибуты объекта.

**Взаимосвязь с другими пакетами `src`**:

*   `src.webdriver.executor`: Предоставляет функциональность для поиска и взаимодействия с элементами веб-страницы.
*   `src.webdriver.js`:  Предоставляет набор методов для выполнения javascript.
*   `src.gs`:  Может предоставлять глобальные пути и другие настройки, необходимые для работы `webdriver`
*   `src.logger`: Обеспечивает ведение логов для отслеживания работы и ошибок.
*   `src.utils.jjson`: Предоставляет функцию для загрузки и обработки JSON-файлов.

### Классы

*   **`Edge(WebDriver)`**:
    *   **Роль**: Кастомный класс, расширяющий возможности `selenium.webdriver.Edge` для упрощения настройки и использования.
    *   **Атрибуты**:
        *   `driver_name` (str): Название драйвера, по умолчанию `'edge'`.
    *   **Методы**:
        *   `__init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs)`:
            *   Инициализирует `Edge` драйвер, настраивая `user_agent` и `options`.
            *   Загружает настройки из `edge.json`.
            *   Создает и настраивает `EdgeOptions`.
            *   Запускает `Edge WebDriver`.
            *   Устанавливает дополнительные функции (`_payload`).
        *   `_payload(self)`:
            *   Инициализирует и привязывает методы `JavaScript` и `ExecuteLocator`.
        *   `set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions`:
            *   Создает и настраивает `EdgeOptions`, возвращает объект для дальнейшего использования.
* **Взаимодействие**:
    *   Класс `Edge` расширяет класс `selenium.webdriver.Edge` и добавляет дополнительную функциональность: возможность автоматической генерации `user_agent`, загрузку настроек из JSON, интеграцию с кастомными модулями `ExecuteLocator` и `JavaScript`.

### Функции

*   `__init__(self, user_agent: Optional[str] = None, options: Optional[List[str]] = None, *args, **kwargs)`:
    *   **Аргументы**:
        *   `user_agent` (Optional[str]): User-agent строка, по умолчанию `None`, в этом случае генерируется случайная.
        *   `options` (Optional[List[str]]): Список опций для браузера, по умолчанию `None`.
        *   `*args`, `**kwargs`: Дополнительные аргументы для родительского конструктора.
    *   **Возвращаемое значение**: `None`
    *   **Назначение**: Инициализация `Edge` драйвера. Настраивает `user_agent`, загружает настройки, создает объект `EdgeOptions`, запускает драйвер и вызывает `_payload`.
    *   **Примеры**:
        *   `driver = Edge()`
        *   `driver = Edge(user_agent='custom_user_agent')`
        *   `driver = Edge(options=['--headless', '--disable-gpu'])`

*   `_payload(self)`:
    *   **Аргументы**: `self`
    *   **Возвращаемое значение**: `None`
    *   **Назначение**: Устанавливает и привязывает к объекту методы из `JavaScript` и `ExecuteLocator`.
    *   **Примеры**:
        *   `self._payload()`

*   `set_options(self, opts: Optional[List[str]] = None) -> EdgeOptions`:
    *   **Аргументы**:
        *  `opts` (Optional[List[str]]): Список опций для добавления.
    *   **Возвращаемое значение**: `EdgeOptions`.
    *   **Назначение**: Создает и настраивает `EdgeOptions` объект, добавляет переданные `opts`.
    *   **Примеры**:
        *   `options = self.set_options(['--headless'])`

### Переменные

*   `MODE`: Строковая переменная, определяющая режим работы (в данном коде установлено значение 'dev').
*   `self.user_agent`: Строковая переменная, хранящая user-agent.
*   `settings`: Объект, который содержит загруженные настройки из файла `edge.json`.
*   `options_obj`: Экземпляр класса `EdgeOptions`, содержащий опции запуска браузера.
*   `edgedriver_path`: Строковая переменная, содержащая путь к исполняемому файлу `edgedriver`.
*   `service`: Экземпляр класса `EdgeService`, необходимый для запуска драйвера.
*   `j`: Экземпляр класса `JavaScript` для выполнения JS-кода.
*   `execute_locator`: Экземпляр класса `ExecuteLocator`, реализующий поиск элементов на странице.
*   `opts`: Список дополнительных опций.
*   `options`: Экземпляр класса `EdgeOptions`, хранящий опции запуска браузера.

### Потенциальные ошибки и области для улучшения

*   **Обработка ошибок**: Хотя код и ловит `WebDriverException`, общая обработка исключений может быть улучшена. Можно добавить более конкретные обработки для различных ошибок, например: ошибка не найденного `edgedriver`, неверный формат json, проблемы с сетью.
*   **Конфигурация `edgedriver_path`**: Код предполагает, что `edgedriver_path` корректно определен в файле `edge.json`.  Можно добавить проверку на наличие файла и правильность пути.
*   **Улучшение логгирования**: В коде есть логирование `logger.info('Starting Edge WebDriver')` и  `logger.critical('Edge WebDriver failed to start:', ex)`,  но можно было бы добавить больше логов для отслеживания ошибок.
*   **Гибкость `user_agent`**: Можно добавить возможность указания конкретной `user_agent` строки, помимо случайной или опции переопределения через метод
*   **Возможность загрузки `edge.json` из разных мест**: Сейчас файл загружается из жестко заданного места, можно сделать гибкую загрузку, например, через переменную окружения.

### Цепочка взаимосвязей с другими частями проекта

1.  **`src.webdriver.edge.edge` -> `src.webdriver.executor.ExecuteLocator`**: `Edge` использует `ExecuteLocator` для поиска элементов и взаимодействия с ними.
2.  **`src.webdriver.edge.edge` -> `src.webdriver.js.JavaScript`**: `Edge` использует `JavaScript` для выполнения javascript функций в браузере.
3.  **`src.webdriver.edge.edge` -> `src.gs`**: `Edge` может использовать глобальные настройки из `src.gs`, например, пути к файлам конфигурации или другие глобальные значения.
4.  **`src.webdriver.edge.edge` -> `src.logger.logger`**: `Edge` использует `logger` для записи логов в процессе выполнения.
5.  **`src.webdriver.edge.edge` -> `src.utils.jjson.j_loads_ns`**: `Edge` использует функцию `j_loads_ns` для загрузки настроек из файла `edge.json`.
6.  **`src.webdriver.edge.edge` -> `fake_useragent.UserAgent`**: `Edge` использует `UserAgent` для генерации случайного `user-agent`.

Таким образом, класс `Edge` является важным компонентом для управления браузером Edge, который взаимодействует с другими модулями проекта для выполнения своих функций.