## <алгоритм>

1. **`driver()` Fixture (module scope):**
   - **Пример:** Инициализирует драйвер Chrome с настройками (headless, путь к chromedriver), открывает `http://example.com`.
   - **Действие:** Создает объект `webdriver.Chrome` с заданными параметрами, открывает URL и предоставляет его тестам, затем закрывает драйвер.
   - **Поток данных:**
        - Создается `webdriver.Chrome` с `Service` и `Options`.
        - Выполняется `driver.get("http://example.com")`.
        - Возвращает объект `webdriver.Chrome` для использования в тестах.

2. **`execute_locator()` Fixture (function scope):**
    - **Пример:** Создает экземпляр `ExecuteLocator` с передачей `driver`.
    - **Действие:** Инициализирует объект `ExecuteLocator`, используя предоставленный `driver` объект.
    - **Поток данных:**
        - Принимает объект `webdriver.Chrome` (из `driver()` fixture).
        - Создает объект `ExecuteLocator` с `driver`.
        - Возвращает объект `ExecuteLocator`.

3. **`test_navigate_to_page(execute_locator, driver)`:**
    - **Пример:** Проверка, что текущий URL равен "http://example.com".
    - **Действие:** Проверяет, что драйвер перешел на нужную страницу.
    - **Поток данных:**
        - Получает `driver` и `execute_locator`.
        - Проверяет значение `driver.current_url`.

4. **`test_get_webelement_by_locator_single_element(execute_locator, driver)`:**
    - **Пример:** Использует локатор `{"by": "XPATH", "selector": "//h1"}` для поиска элемента и проверяет, что он типа `WebElement` и имеет текст "Example Domain".
    - **Действие:** Поиск элемента по локатору.
    - **Поток данных:**
        - Получает `driver` и `execute_locator`.
        - Вызывает `execute_locator.get_webelement_by_locator(locator)`.
        - Проверяет тип и текст полученного элемента.

5. **`test_get_webelement_by_locator_no_element(execute_locator, driver)`:**
    - **Пример:** Использует локатор `{"by": "XPATH", "selector": "//div[@id='nonexistent']"}` (которого нет на странице), проверяет, что метод возвращает `False`.
    - **Действие:** Проверка отсутствия элемента по локатору.
    - **Поток данных:**
        - Получает `driver` и `execute_locator`.
        - Вызывает `execute_locator.get_webelement_by_locator(locator)`.
        - Проверяет, что возвращаемое значение равно `False`.

6. **`test_send_message(execute_locator, driver)`:**
    - **Пример:**  Отправляет сообщение "Hello World" в элемент с локатором `{"by": "XPATH", "selector": "//input[@id='search']"}`.
    - **Действие:** Ввод текста в элемент.
    - **Поток данных:**
        - Получает `driver` и `execute_locator`.
        - Вызывает `execute_locator.send_message(locator, message, ...)`.
        - Проверяет, что возвращаемое значение равно `True`.

7. **`test_get_attribute_by_locator(execute_locator, driver)`:**
    - **Пример:** Получает значение атрибута `href` элемента с локатором `{"by": "XPATH", "selector": "//a[@id='more-information']"}`.
    - **Действие:** Получение атрибута элемента по локатору.
    - **Поток данных:**
        - Получает `driver` и `execute_locator`.
        - Вызывает `execute_locator.get_attribute_by_locator(locator, message="href")`.
        - Проверяет полученное значение атрибута.

8. **`test_execute_locator_event(execute_locator, driver)`:**
    - **Пример:** Выполняет событие "click" на элементе с локатором `{"by": "XPATH", "selector": "//a[@id='more-information']"}`.
    - **Действие:** Выполнение события на элементе.
    - **Поток данных:**
        - Получает `driver` и `execute_locator`.
        - Вызывает `execute_locator.execute_locator(locator, message="click")`.
        - Проверяет, что возвращаемое значение равно `True`.

9.  **`test_get_locator_keys(execute_locator, driver)`:**
    - **Пример:** Проверяет, что `get_locator_keys()` возвращает ожидаемый список ключей.
    - **Действие:** Получение доступных ключей локатора.
    - **Поток данных:**
        - Вызывает `ExecuteLocator.get_locator_keys()`.
        - Проверяет соответствие с ожидаемым результатом.

10. **`test_navigate_and_interact(execute_locator, driver)`:**
    - **Пример:** Навигация на `https://www.wikipedia.org/`, ввод "Selenium" в поле поиска, нажатие кнопки поиска, проверка загрузки страницы результатов.
    - **Действие:** Последовательность навигации и взаимодействия с элементами.
    - **Поток данных:**
        - Получает `driver` и `execute_locator`.
        - Выполняет навигацию на `https://www.wikipedia.org/`.
        - Выполняет ввод текста в поле поиска через `execute_locator.send_message`.
        - Выполняет клик по кнопке поиска через `execute_locator.execute_locator`.
        - Проверяет, что страница результатов загружена и содержит необходимый текст.

11. **`test_invalid_locator(execute_locator, driver)`:**
    - **Пример:** Использует некорректный локатор с `by="INVALID_BY"` и проверяет, что возникает `ExecuteLocatorException`.
    - **Действие:** Проверка обработки некорректных локаторов.
    - **Поток данных:**
        - Получает `driver` и `execute_locator`.
        - Пытается выполнить `execute_locator.execute_locator` с некорректным локатором.
        - Проверяет, что возникает `ExecuteLocatorException`.

## <mermaid>
```mermaid
flowchart TD
    subgraph Test Setup
        DriverFixture[<code>driver()</code><br>Setup WebDriver]
        ExecuteLocatorFixture[<code>execute_locator()</code><br>Initialize ExecuteLocator]
    end
    
    DriverFixture --> ExecuteLocatorFixture
    
    subgraph Test Functions
    test_navigate_to_page[<code>test_navigate_to_page</code><br>Navigates to Initial Page]
    test_get_webelement_single[<code>test_get_webelement_by_locator_single_element</code><br>Gets Single Element by Locator]
    test_get_webelement_no_element[<code>test_get_webelement_by_locator_no_element</code><br>Handles No Element by Locator]
    test_send_message_element[<code>test_send_message</code><br>Sends Message to Element]
    test_get_attribute_element[<code>test_get_attribute_by_locator</code><br>Gets Element Attribute]
    test_execute_event[<code>test_execute_locator_event</code><br>Executes Event on Locator]
    test_get_keys_locator[<code>test_get_locator_keys</code><br>Gets Available Locator Keys]
    test_navigate_and_interact_page[<code>test_navigate_and_interact</code><br>Navigates and Interacts with Elements]
    test_invalid_locator_test[<code>test_invalid_locator</code><br>Handles Invalid Locator]
   end
    
    ExecuteLocatorFixture --> test_navigate_to_page
    ExecuteLocatorFixture --> test_get_webelement_single
    ExecuteLocatorFixture --> test_get_webelement_no_element
    ExecuteLocatorFixture --> test_send_message_element
    ExecuteLocatorFixture --> test_get_attribute_element
    ExecuteLocatorFixture --> test_execute_event
    ExecuteLocatorFixture --> test_get_keys_locator
    ExecuteLocatorFixture --> test_navigate_and_interact_page
    ExecuteLocatorFixture --> test_invalid_locator_test
    
    style DriverFixture fill:#f9f,stroke:#333,stroke-width:2px
    style ExecuteLocatorFixture fill:#ccf,stroke:#333,stroke-width:2px
    style test_navigate_to_page fill:#cfc,stroke:#333,stroke-width:1px
    style test_get_webelement_single fill:#cfc,stroke:#333,stroke-width:1px
    style test_get_webelement_no_element fill:#cfc,stroke:#333,stroke-width:1px
    style test_send_message_element fill:#cfc,stroke:#333,stroke-width:1px
    style test_get_attribute_element fill:#cfc,stroke:#333,stroke-width:1px
    style test_execute_event fill:#cfc,stroke:#333,stroke-width:1px
    style test_get_keys_locator fill:#cfc,stroke:#333,stroke-width:1px
    style test_navigate_and_interact_page fill:#cfc,stroke:#333,stroke-width:1px
    style test_invalid_locator_test fill:#cfc,stroke:#333,stroke-width:1px
```

## <объяснение>

**Импорты:**

- `pytest`: Фреймворк для написания и запуска тестов.
- `selenium.webdriver`: Основной модуль Selenium для управления браузером.
  - `webdriver.chrome.service.Service`: Класс для настройки сервиса ChromeDriver.
  - `webdriver.common.by.By`: Класс, используемый для определения стратегии поиска элементов (например, по XPATH, ID, CSS).
  - `webdriver.chrome.options.Options`: Класс для установки опций Chrome.
  - `webdriver.remote.webelement.WebElement`: Класс, представляющий веб-элемент на странице.
  - `webdriver.common.action_chains.ActionChains`: Класс для выполнения сложных действий, таких как перемещение мыши или множественные клики.
  - `webdriver.support.ui.WebDriverWait`: Класс для ожидания определенных условий при загрузке страницы.
  - `webdriver.support.expected_conditions as EC`: Модуль с предустановленными ожиданиями для `WebDriverWait`.
- `src.webdriver.executor.ExecuteLocator`: Класс, используемый для поиска, взаимодействия и выполнения действий с элементами на веб-странице.
- `src.logger.exceptions.ExecuteLocatorException`: Пользовательское исключение, выбрасываемое при ошибках в `ExecuteLocator`.

**Классы:**

- **`ExecuteLocator`:**  Этот класс (из файла `src/webdriver/executor.py` - не включен в предоставленный код)  используется для выполнения действий с элементами на веб-странице.  Он принимает `webdriver` в качестве параметра. Методы этого класса используются в тестах для поиска элементов, отправки сообщений, получения атрибутов и выполнения событий.

**Фикстуры:**

- **`driver()`:**  
  - **Назначение**: Подготавливает и предоставляет драйвер браузера Chrome для тестов.  
  - **Работа:**
      - Создает `Options` объект, устанавливая режим headless.
      - Инициализирует `Service` с указанием пути к `chromedriver`.
      - Создает экземпляр `webdriver.Chrome` с использованием `Service` и `Options`.
      - Открывает страницу `http://example.com`.
      - Использует `yield` для передачи драйвера тестам.
      - После выполнения тестов закрывает драйвер `driver.quit()`.
  - **Область видимости:** `module`, то есть драйвер создается один раз для всех тестов в модуле.
- **`execute_locator(driver)`:**
  - **Назначение**: Подготавливает и предоставляет экземпляр класса `ExecuteLocator`.
  - **Работа:**
     - Принимает `driver` (созданный фикстурой `driver`).
     - Создает экземпляр класса `ExecuteLocator`, используя `driver`.
     - Возвращает экземпляр `ExecuteLocator` тестам.
  - **Область видимости**: `function`, то есть экземпляр `ExecuteLocator` создается для каждого теста.

**Тестовые функции:**

- **`test_navigate_to_page(execute_locator, driver)`**:
    - **Назначение**: Проверяет, что драйвер браузера успешно перешел на целевую страницу (http://example.com).
    - **Аргументы**: `execute_locator` (экземпляр `ExecuteLocator`), `driver` (экземпляр `webdriver.Chrome`).
    - **Действия**: Проверяет, что текущий URL драйвера совпадает с http://example.com.
    - **Возвращаемое значение**: Нет.

- **`test_get_webelement_by_locator_single_element(execute_locator, driver)`**:
    - **Назначение**: Проверяет, что метод `get_webelement_by_locator` корректно находит элемент и возвращает его.
    - **Аргументы**: `execute_locator`, `driver`.
    - **Действия**:
        - Создает локатор для заголовка `h1`.
        - Вызывает `execute_locator.get_webelement_by_locator` с этим локатором.
        - Проверяет, что возвращенный элемент является экземпляром `WebElement` и его текст "Example Domain".
    - **Возвращаемое значение**: Нет.

- **`test_get_webelement_by_locator_no_element(execute_locator, driver)`**:
    - **Назначение**: Проверяет, что метод `get_webelement_by_locator` возвращает `False`, если элемент не найден.
    - **Аргументы**: `execute_locator`, `driver`.
    - **Действия**:
        - Создает локатор для несуществующего элемента.
        - Вызывает `execute_locator.get_webelement_by_locator` с этим локатором.
        - Проверяет, что возвращено значение `False`.
    - **Возвращаемое значение**: Нет.

- **`test_send_message(execute_locator, driver)`**:
    - **Назначение**: Проверяет, что метод `send_message` отправляет сообщение элементу на странице.
    - **Аргументы**: `execute_locator`, `driver`.
    - **Действия**:
        - Создает локатор для поля ввода (предположительно, с `id='search'`).
        - Вызывает `execute_locator.send_message` с локатором, сообщением "Hello World".
        - Проверяет, что возвращено значение `True`.
    - **Возвращаемое значение**: Нет.

- **`test_get_attribute_by_locator(execute_locator, driver)`**:
    - **Назначение**: Проверяет, что метод `get_attribute_by_locator` корректно возвращает значение атрибута элемента.
    - **Аргументы**: `execute_locator`, `driver`.
    - **Действия**:
        - Создает локатор для элемента `a` c id more-information.
        - Вызывает `execute_locator.get_attribute_by_locator`, чтобы получить значение атрибута `href`.
        - Проверяет, что возвращенное значение соответствует ожидаемому.
    - **Возвращаемое значение**: Нет.

- **`test_execute_locator_event(execute_locator, driver)`**:
    - **Назначение**: Проверяет, что метод `execute_locator` корректно выполняет событие (в данном случае `click`) на элементе.
    - **Аргументы**: `execute_locator`, `driver`.
    - **Действия**:
        - Создает локатор для элемента.
        - Вызывает `execute_locator.execute_locator` с локатором и событием `click`.
        - Проверяет, что возвращено значение `True`.
    - **Возвращаемое значение**: Нет.
- **`test_get_locator_keys(execute_locator, driver)`**:
    - **Назначение**: Проверяет, что метод `get_locator_keys` возвращает правильные ключи локатора.
    - **Аргументы**: `execute_locator`, `driver`.
    - **Действия**:
        - Вызывает `ExecuteLocator.get_locator_keys()`.
        - Проверяет соответствие возвращенных ключей ожидаемому набору.
    - **Возвращаемое значение**: Нет.
- **`test_navigate_and_interact(execute_locator, driver)`**:
    - **Назначение**: Проверяет последовательность навигации и взаимодействия с элементами.
    - **Аргументы**: `execute_locator`, `driver`.
    - **Действия**:
        - Навигирует на страницу Википедии.
        - Находит поле ввода поиска, вводит "Selenium", нажимает кнопку поиска.
        - Проверяет загрузку страницы результатов поиска и наличие заголовка с текстом "Selenium".
    - **Возвращаемое значение**: Нет.

- **`test_invalid_locator(execute_locator, driver)`**:
    - **Назначение**: Проверяет, что обработка некорректного локатора приводит к ожидаемому исключению.
    - **Аргументы**: `execute_locator`, `driver`.
    - **Действия**:
        - Создает локатор с некорректным значением ключа `by`.
        - Пытается выполнить событие через `execute_locator.execute_locator`.
        - Проверяет, что выбрасывается исключение `ExecuteLocatorException`.
    - **Возвращаемое значение**: Нет.

**Переменные:**

- Все переменные внутри функций (например, `locator`, `element`, `message`, `result`, `attribute_value`) - локальные и используются только в контексте своих функций.

**Потенциальные ошибки и улучшения:**

- **Зависимость от жестко заданного пути к `chromedriver`**: Путь `/path/to/chromedriver` должен быть настроен в соответствии с реальным расположением.
- **Жестко заданный URL**: URL `http://example.com` и URL википедии жёстко заданы в коде. Их следует вынести в переменные окружения или конфигурационные файлы.
- **Недостаточная проверка `send_message`**: Тест `send_message` не проверяет фактически отправленное сообщение.
- **Повторение локаторов:**  Локаторы для одних и тех же элементов повторяются в разных тестах. Это можно исправить, вынеся их в константы или переменные.
- **Непонятное ожидание** - в некоторых тестах используется `assert result is True`, без явной проверки того, что действие действительно произошло (например клик).
- **Отсутствие тестов для других событий** - кроме клика, можно было бы протестировать другие возможные события (например, `hover`, `focus`, `blur`,  и т.д.)
- **Отсутствие тестов для других типов локаторов** - кроме xpath, можно было бы протестировать другие типы (например, `ID`, `CSS_SELECTOR`, `LINK_TEXT`).
- **Отсутствие обработки ошибок** - тесты могут ломаться, если какой-то из элементов не найден на странице, и это нужно обрабатывать (например, можно обернуть вызовы `get_webelement_by_locator` в `try/except`).

**Цепочка взаимосвязей с другими частями проекта:**

- `src.webdriver.executor.ExecuteLocator`:  Этот класс предположительно управляет взаимодействием с веб-элементами с использованием `selenium.webdriver` и является частью основного модуля `webdriver`.
- `src.logger.exceptions.ExecuteLocatorException`: Это исключение, определенное в модуле `logger`, используется для обработки ошибок, возникающих в `ExecuteLocator`.
- `selenium`:  это внешняя библиотека, используемая для автоматизации браузера.

Этот код представляет собой набор тестов, которые проверяют функциональность `ExecuteLocator` и взаимодействие с веб-элементами через `selenium`.