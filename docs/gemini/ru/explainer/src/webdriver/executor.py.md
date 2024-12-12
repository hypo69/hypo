## Анализ кода `hypotez/src/webdriver/executor.py`

### 1. <алгоритм>

**Общая схема работы:**

1.  **Инициализация:**
    *   Создается экземпляр класса `ExecuteLocator`. При создании, если передается `driver`, инициализируется объект `ActionChains`.
2.  **`execute_locator`:**
    *   Принимает локатор (словарь или `SimpleNamespace`), таймаут, тип события ожидания, сообщение, скорость печати и флаг `continue_on_error`.
    *   Преобразует локатор в `SimpleNamespace` (если передан словарь).
    *   Вызывает асинхронную функцию `_parse_locator`.
3.  **`_parse_locator`:**
    *   Проверяет, есть ли у локатора `event`, `attribute` или `mandatory`. Если ни одного нет, возвращает `None`.
    *   Определяет тип локатора `By` (например, `By.XPATH`, `By.ID`).
    *   Если есть атрибут (`locator.attribute`), то он обрабатывается функцией `evaluate_locator`.
    *   Если есть событие (`locator.event`), выполняется функция `execute_event`.
    *   Если есть атрибут (`locator.attribute`), выполняется `get_attribute_by_locator`.
    *   В противном случае выполняется функция `get_webelement_by_locator`.
4.  **`evaluate_locator`:**
    *   Принимает атрибут в виде строки, списка строк или словаря.
    *   Если атрибут - список, вызывает `_evaluate` для каждого элемента списка и возвращает результаты.
    *   Если атрибут - строка, то обрабатывается в `_evaluate` (извлекает константы `Keys`).
5.  **`get_attribute_by_locator`:**
    *   Получает веб-элемент с помощью `get_webelement_by_locator`.
    *   Если элемент не найден, возвращает `None`.
    *   Если `locator.attribute` - строка, похожая на словарь, парсит ее в словарь.
    *   Получает атрибут(ы) от веб-элемента(-ов) и возвращает результат.
6.  **`get_webelement_by_locator`:**
    *   Принимает локатор, таймаут и тип события ожидания.
    *   Ожидает появления элемента на странице с таймаутом, если таймаут > 0.
    *   Применяет фильтр к списку веб-элементов, если указан `locator.if_list` (например, "first", "last", "even", "odd").
    *   Возвращает один элемент, список или `None`, если не найден.
7.  **`get_webelement_as_screenshot`:**
    *   Получает веб-элемент через `get_webelement_by_locator` (если не передан).
    *   Делает скриншот элемента.
    *   Возвращает поток байтов изображения.
8.  **`execute_event`:**
    *   Разбирает строку с событиями, разделенную ";".
    *   Получает веб-элемент через `get_webelement_by_locator`.
    *   Выполняет события последовательно.
    *   Поддерживает события: `click()`, `pause()`, `upload_media()`, `screenshot()`, `clear()`, `send_keys()`, `type()`.
9.  **`send_message`:**
    *   Принимает локатор, таймаут, тип события, сообщение и скорость печати.
    *   Получает веб-элемент с помощью `get_webelement_by_locator`.
    *   Вызывает функцию `type_message` для печати сообщения.
10. **`type_message`:**
    *   Печатает сообщение в веб-элемент посимвольно с учетом скорости печати, заменяя некоторые символы (например, ";" на "SHIFT+ENTER").

**Примеры:**

*   **`execute_locator`:**
    ```python
    locator = {"by": "ID", "selector": "myButton", "event": "click()"}
    result = await executor.execute_locator(locator)
    # Кликнет на элемент с id='myButton'
    ```
*   **`get_attribute_by_locator`:**
    ```python
    locator = {"by": "XPATH", "selector": "//input", "attribute": "value"}
    value = await executor.get_attribute_by_locator(locator)
    # Получит значение атрибута 'value' у первого input
    ```
*   **`get_webelement_by_locator`:**
    ```python
    locator = {"by": "CLASS_NAME", "selector": "items", "if_list": "even"}
    elements = await executor.get_webelement_by_locator(locator)
    # Получит все элементы с class='items', вернет только четные
    ```
*  **`execute_event`**
    ```python
    locator = {"by": "ID", "selector": "inputField", "event": "type(test);click()"}
    result = await executor.execute_event(locator)
    # Напечатает "test" в поле с id='inputField' и кликнет на него
    ```
*  **`send_message`:**
    ```python
    locator = {"by": "ID", "selector": "textarea"}
    result = await executor.send_message(locator, message="Hello; World", typing_speed=0.1)
    # Напечатает "Hello" напечатает SHIFT+ENTER, напечатает "World" в textarea
    ```

### 2. <mermaid>

```mermaid
    graph TD
    A[ExecuteLocator] --> B{execute_locator};
    B --> C{locator is SimpleNamespace?};
    C -- Yes --> D[Use locator as is];
    C -- No --> E[Convert dict to SimpleNamespace];
    E --> D;
    D --> F[Define async function _parse_locator];
    F --> G{locator has event, attribute, mandatory?};
    G -- No --> H[Return None];
    G -- Yes --> I[Try to map By and evaluate attribute];
    I --> J[Catch exceptions];
    J --> K{locator has event?};
    K -- Yes --> L[execute_event];
    K -- No --> M{locator has attribute?};
    M -- Yes --> N[get_attribute_by_locator];
    M -- No --> O[get_webelement_by_locator];
    L --> P[Return result of event];
    N --> P[Return attribute result];
    O --> P[Return web element result];
    P --> Q[Return _parse_locator result];
    Q --> R[Return execute_locator result];

    subgraph evaluate_locator
      S[Start] --> T{attribute is list?};
      T -- Yes --> U[Iterate over each attribute in list];
      U --> V[Call _evaluate for each attribute];
      V --> W[Return gathered results from asyncio.gather];
      T -- No --> X[Call _evaluate for single attribute];
      X --> Y[Return result of _evaluate];
      Y --> Z[End];
      W --> Z;
    end

    subgraph get_attribute_by_locator
      AA[Start] --> AB{locator is SimpleNamespace or dict?};
      AB -- Yes --> AC[Convert locator to SimpleNamespace if needed];
      AC --> AD[Call get_webelement_by_locator];
      AD --> AE{web_element is found?};
      AE -- No --> AF[Log debug message and return];
      AE -- Yes --> AG{locator.attribute is a dictionary-like string?};
      AG -- Yes --> AH[Parse locator.attribute string to dict];
      AH --> AI{web_element is a list?};
      AI -- Yes --> AJ[Retrieve attributes for each element in list];
      AJ --> AK[Return list of attributes];
      AI -- No --> AL[Retrieve attributes for a single web_element];
      AL --> AK;
      AG -- No --> AM{web_element is a list?};
      AM -- Yes --> AN[Retrieve attributes for each element in list];
      AN --> AO[Return list of attributes or single attribute];
      AM -- No --> AP[Retrieve attribute for a single web_element];
      AP --> AO;
      AO --> AQ[End];
      AF --> AQ;
    end

    subgraph get_webelement_by_locator
      AR[Start] --> AS[Get driver];
      AS --> AT[Get locator];
       AT --> AU{timeout is 0?};
      AU -- Yes --> AV[Find elements immediately];
      AU -- No --> AW[Define wait condition];
      AW --> AX[Wait for elements with timeout];
      AX --> AY[Parse and filter elements list];
      AY --> AZ[Return element(s)];
       AV --> AY;
      AZ --> BA[End];
    end

    subgraph execute_event
        BB[Start] --> BC[Split events by semicolon];
        BC --> BD[Get webelement];
        BD --> BE{Loop through events};
        BE --> BF{event is click()};
        BF -- Yes --> BG[Execute click];
        BF -- No --> BH{event starts with "pause("};
        BH -- Yes --> BI[Execute pause];
        BH -- No --> BJ{event is "upload_media()"};
        BJ -- Yes --> BK[Execute upload_media];
        BJ -- No --> BL{event is "screenshot()"};
        BL -- Yes --> BM[Execute screenshot];
        BL -- No --> BN{event is "clear()"};
        BN -- Yes --> BO[Execute clear];
        BN -- No --> BP{event starts with "send_keys("};
         BP -- Yes --> BQ[Execute send_keys];
         BP -- No --> BR{event starts with "type("};
         BR -- Yes --> BS[Execute type];
         BR -- No --> BT[Return result of event];
         BG --> BE;
        BI --> BE;
        BK --> BE;
        BM --> BE;
        BO --> BE;
        BQ --> BE;
        BS --> BE;
        BT --> BU[End];
    end

   subgraph send_message
      BV[Start] --> BW[Get webelement];
      BW --> BX[Move to element];
      BX --> BY[Call type_message];
      BY --> BZ[Return True];
      BZ --> CA[End];
   end
   
    subgraph type_message
      CB[Start] --> CC[Split message by space];
      CC --> CD{Loop through words};
       CD --> CE[Loop through letters];
        CE --> CF{letter is in replace_dict?};
        CF -- Yes --> CG[Replace the character];
        CF -- No --> CH[Send the letter];
      CG --> CE;
      CH --> CE;
       CE --> CI[Pause between letters];
      CI --> CE;
      CD --> CJ[Return True];
      CJ --> CK[End];
    end
    
    
    R --> L1[End]
```

**Зависимости:**

*   `selenium.common.exceptions`: Содержит исключения, специфичные для Selenium (например, `NoSuchElementException`).
*   `selenium.webdriver.common.action_chains`: Используется для выполнения сложных действий, таких как нажатие клавиш и перемещение мыши.
*   `selenium.webdriver.common.by`: Определяет способы поиска элементов (например, `By.XPATH`, `By.ID`).
*   `selenium.webdriver.common.keys`: Содержит специальные клавиши (например, `Keys.ENTER`, `Keys.SHIFT`).
*   `selenium.webdriver.remote.webelement`: Представляет веб-элементы.
*   `selenium.webdriver.support.expected_conditions`: Содержит условия ожидания элементов (например, `presence_of_element_located`).
*   `selenium.webdriver.support.ui`: Используется для ожидания элементов с таймаутом.
*   `header`: Внешний модуль, вероятно, для определения заголовков.
*   `src.gs`: Внешний модуль, скорее всего, для глобальных настроек.
*   `src.logger.logger`: Внешний модуль для логирования.
*   `src.logger.exceptions`: Модуль для кастомных исключений.
*   `src.utils.jjson`: Модуль для работы с JSON.
*   `src.utils.printer`: Модуль для вывода данных.
*   `src.utils.image`: Модуль для обработки изображений.
*   `asyncio`: Модуль для асинхронного программирования.
*   `re`: Модуль для работы с регулярными выражениями.
*   `sys`: Модуль для доступа к системным параметрам и функциям.
*   `time`: Модуль для работы со временем.
*   `dataclasses`: Модуль для создания классов данных.
*   `enum`: Модуль для создания перечислений.
*   `pathlib`: Модуль для работы с путями к файлам.
*   `types`: Модуль для работы с типами (например, `SimpleNamespace`).
*   `typing`: Модуль для аннотаций типов.

### 3. <объяснение>

**Импорты:**

*   `asyncio`: Используется для асинхронного программирования, позволяя функциям выполняться параллельно и не блокировать основной поток.
*   `re`: Используется для работы с регулярными выражениями, в частности для извлечения значений из строк (например, при разборе `pause(1000)`).
*   `sys`: Используется для доступа к системным переменным и функциям (не используется в предоставленном коде, возможно, для будущего расширения функционала).
*   `time`: Используется для работы со временем, например, для установки пауз между действиями (не используется напрямую, но используется внутри `asyncio.sleep`).
*   `dataclasses`: Используется для создания классов данных, в данном случае `ExecuteLocator`.
*   `enum`: Используется для создания перечислений (не используется напрямую, но, возможно, будет использован в будущем).
*   `pathlib`: Используется для работы с путями к файлам и директориям (не используется напрямую, но, возможно, будет использован в будущем).
*   `types.SimpleNamespace`: Удобный способ создать объект с динамическими атрибутами, используется для локаторов.
*   `typing`: Используется для аннотаций типов, что улучшает читаемость и помогает при разработке.
*   `selenium`:  Набор библиотек для автоматизации взаимодействия с браузером,  используются для поиска элементов,  выполнения действий и ожидания загрузки страниц.
*   `header`: Внешний модуль для управления заголовками.
*   `src.gs`: Внешний модуль для глобальных настроек.
*   `src.logger`: Модули для логирования, упрощения отладки и  мониторинга ошибок.
*   `src.utils.jjson`: Модуль для работы с JSON,  используются для сериализации и десериализации данных.
*   `src.utils.printer`: Модуль для вывода данных с форматированием,  упрощает читаемость выводимых сообщений.
*  `src.utils.image`: Модуль для работы с изображениями, например, для сохранения скриншотов.

**Классы:**

*   `ExecuteLocator`:
    *   **Роль:**  Обеспечивает взаимодействие с веб-элементами, обрабатывает локаторы и выполняет действия с ними.
    *   **Атрибуты:**
        *   `driver`:  Экземпляр вебдрайвера.
        *   `actions`: Объект для выполнения действий (`ActionChains`).
        *   `by_mapping`: Словарь, который связывает строковые ключи с методами поиска элементов (`By`).
        *   `mode`: Режим работы.
    *   **Методы:**
        *   `__post_init__()`: Инициализирует `ActionChains` после создания экземпляра.
        *   `execute_locator()`: Основной метод для выполнения действий на веб-элементе.
        *   `evaluate_locator()`:  Обрабатывает атрибуты локаторов.
        *   `get_attribute_by_locator()`: Получает атрибуты веб-элемента.
        *   `get_webelement_by_locator()`: Получает веб-элемент по локатору.
        *   `get_webelement_as_screenshot()`: Делает скриншот веб-элемента.
        *   `execute_event()`: Выполняет события на веб-элементе.
        *   `send_message()`: Отправляет сообщение на веб-элемент.

**Функции:**

*   `execute_locator`:
    *   **Аргументы:** `locator` (словарь или `SimpleNamespace`), `timeout`, `timeout_for_event`, `message`, `typing_speed`, `continue_on_error`.
    *   **Возвращает:** Строку, список, словарь, `WebElement` или `bool` в зависимости от выполненных действий.
    *   **Назначение:** Координирует выполнение действий, используя другие методы класса, проверяет наличие `attribute`, `event` или `mandatory`.
*   `_parse_locator`:
    *   **Аргументы:** `locator` (`dict` или `SimpleNamespace`), `message`.
    *   **Возвращает:** Строку, список, словарь, `WebElement` или `bool`.
    *   **Назначение:**  Обрабатывает локатор, выполняет события, получение атрибутов или получение веб-элементов.
*   `evaluate_locator`:
    *   **Аргументы:** `attribute` (строка, список строк или словарь).
    *   **Возвращает:** Строку, список строк или словарь.
    *   **Назначение:** Извлекает значения из `Keys`, преобразовывает строку в объект.
*   `_evaluate`:
    *   **Аргументы:** `attr` (строка).
    *   **Возвращает:** Строку
    *   **Назначение:**  Возвращает значение константы из класса `Keys`, если строка соответствует паттерну.
*   `get_attribute_by_locator`:
    *   **Аргументы:** `locator` (`dict` или `SimpleNamespace`), `timeout`, `timeout_for_event`, `message`, `typing_speed`, `continue_on_error`.
    *   **Возвращает:**  `WebElement`, список `WebElement` или `None`.
    *   **Назначение:** Получает значения атрибутов из веб-элементов.
*   `_parse_dict_string`:
    *   **Аргументы:** `attr_string` (строка).
    *   **Возвращает:** Словарь или `None` если не удалось распарсить строку.
    *   **Назначение:** Преобразует строку, похожую на словарь, в настоящий словарь.
*   `_get_attributes_from_dict`:
    *   **Аргументы:** `web_element` (`WebElement`), `attr_dict` (словарь).
    *   **Возвращает:** Словарь атрибутов.
    *   **Назначение:** Получает значения атрибутов веб-элемента по ключам из словаря.
*   `get_webelement_by_locator`:
    *   **Аргументы:** `locator` (`dict` или `SimpleNamespace`), `timeout`, `timeout_for_event`.
    *   **Возвращает:** `WebElement`, список `WebElement` или `None`.
    *   **Назначение:** Получает веб-элементы по заданному локатору и условиям ожидания.
*  `_parse_elements_list`
    *   **Аргументы:** `web_elements` (`WebElement`, список `WebElement`), `locator` (`SimpleNamespace`).
    *   **Возвращает:** `WebElement` или список `WebElement`
    *   **Назначение:** Фильтрует список веб-элементов по правилам `if_list`, которые определены в локаторе.
*   `get_webelement_as_screenshot`:
    *   **Аргументы:** `locator` (`dict` или `SimpleNamespace`), `timeout`, `timeout_for_event`, `message`, `typing_speed`, `continue_on_error`, `webelement`.
    *   **Возвращает:** Поток байтов изображения или `None`.
    *   **Назначение:** Делает скриншот веб-элемента.
*   `execute_event`:
    *   **Аргументы:** `locator` (`SimpleNamespace` или `dict`), `timeout`, `timeout_for_event`, `message`, `typing_speed`, `continue_on_error`.
    *   **Возвращает:**  `str`, список `str`, `bytes`, список `bytes` или `bool`.
    *   **Назначение:** Выполняет различные события на веб-элементе (например, клик, ввод текста, загрузка файла).
*    `send_message`:
    *   **Аргументы:** `locator` (`SimpleNamespace` или `dict`), `timeout`, `timeout_for_event`, `message`, `typing_speed`, `continue_on_error`.
    *   **Возвращает:** `bool`
    *   **Назначение:** Отправляет сообщение в текстовое поле веб-элемента.
*    `type_message`:
    *   **Аргументы:** `el` (`WebElement`), `message` (`str`), `replace_dict` (`dict`), `typing_speed` (`float`).
    *   **Возвращает:** `bool`
    *   **Назначение:**  Посимвольный ввод сообщения в текстовое поле веб-элемента, с использованием  замен из словаря.

**Переменные:**

*   `MODE`:  Переменная для определения режима работы (например, `dev`, `debug`).
*   `locator`: Используется для хранения данных о местоположении веб-элементов, обычно в виде словаря или `SimpleNamespace`.
*   `timeout`:  Таймаут для ожидания веб-элементов (в секундах).
*   `timeout_for_event`: Тип события, которое нужно ожидать перед взаимодействием с элементом.
*   `message`: Сообщение, которое нужно отправить в текстовое поле или использовать при загрузке медиа-файлов.
*   `typing_speed`:  Скорость ввода символов в секундах.
*   `continue_on_error`: Флаг, определяющий, нужно ли продолжать выполнение при возникновении ошибки.
*   `web_elements`, `web_element`: Переменные для хранения одного или нескольких найденных веб-элементов.
*   `actions`: Экземпляр `ActionChains` для выполнения сложных действий с веб-элементами.
*   `by_mapping`: Словарь, связывающий строковые ключи с `By`-объектами.
*   `result`: Переменная для хранения результатов выполнения функций.
*   `keys_to_send`: Список ключей для отправки в `send_keys`.
*  `if_list`:  Правило фильтрации для списков веб-элементов.
*   `events`: Список событий, которые нужно выполнить.
* `screenshot_stream`: Поток байтов, содержащий данные изображения

**Потенциальные ошибки и улучшения:**

*   **Обработка ошибок:**
    *   Не все исключения обрабатываются в блоках `try-except` (например, некоторые ошибки в `type_message` игнорируются).
    *   Используется общий `Exception`, необходимо конкретизировать исключения для лучшего отслеживания проблем.
    *   Повторяющийся код в обработке ошибок. Вынести логику логирования в отдельную функцию.
*   **Модульность:**
    *   Функция `type_message` имеет прямую зависимость от `self.actions` и класса `ExecuteLocator`. Необходимо отвязать ее от класса и вынести отдельно.
    *   Логика `_parse_elements_list` слишком перегружена. Необходимо вынести в отдельную функцию.
*   **`send_message`:**
    *   Используется `self.actions.perform()` после каждой буквы, что может быть медленным. Можно накапливать действия и выполнять их одним вызовом.
    *   Логика обработки `replace_dict` не завершена. Необходимо правильно обрабатывать `SHIFT+ENTER` и другие комбинации клавиш.
    *   Не перехватываются ошибки при печати сообщения.
*   **`execute_event`:**
    *   Слишком много вариантов событий. Возможно стоит выделить обработку каждого события в отдельную функцию для лучшей читаемости и поддержки кода.
    *   `send_keys` не поддерживает удержание клавиш, только разовые нажатия.
*   **`get_webelement_by_locator`:**
    *   В блоке `try` есть два варианта поиска элементов, возможно стоит избавиться от if-else.
    *   Слишком сложное определение `condition` ожидания.
*   **`evaluate_locator`:**
    *    Обработка атрибута если `attribute` имеет тип `dict`,  не реализовано.
*   **`execute_locator`:**
     *   Возвращает `None` если `locator.attribute and locator.selector` не определены.  В этой ситуации, код не будет работать корректно,  особенно если `attribute` или `selector` обязательное условие.

**Цепочка взаимосвязей с другими частями проекта:**

*   `src.gs`: Используется для получения глобальных настроек (например, `MODE`).
*   `src.logger`: Используется для логирования информации и ошибок.
*   `src.utils`: Содержит вспомогательные функции, например, для работы с JSON и вывода данных.
*   `header`: Возможно, используется для добавления заголовков к запросам.

**Заключение:**

Код `executor.py` является важной частью проекта, обеспечивая взаимодействие с веб-элементами. Он поддерживает различные типы локаторов, действия и события, а также обеспечивает гибкость и возможность обработки ошибок. Однако есть области, которые можно улучшить, в частности, обработку ошибок, модульность, асинхронную работу и читаемость.