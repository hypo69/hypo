## <алгоритм>

1. **`driver_mock` fixture:**
   - Создает фиктивный (mock) объект `driver_mock`  с помощью `unittest.mock.MagicMock`.
   - Этот объект имитирует поведение веб-драйвера Selenium, позволяя тестировать логику без реального браузера.
   - Пример: `driver_mock = MagicMock()`.

2. **`execute_locator` fixture:**
   - Создает экземпляр `ExecuteLocator` с фиктивным `driver_mock`.
   - Позволяет тестировать методы класса `ExecuteLocator`.
   - Пример: `execute_locator = ExecuteLocator(driver_mock)`.

3. **`test_get_webelement_by_locator_single_element`:**
   - Создает фиктивный веб-элемент `element` (mock `WebElement`).
   - Настраивает `driver_mock.find_elements` так, чтобы он возвращал список, содержащий `element`.
   - Определяет локатор (словарь `locator`) для поиска элемента (например, по XPATH).
   - Вызывает метод `execute_locator.get_webelement_by_locator(locator)` для получения элемента.
   - Проверяет, что `driver_mock.find_elements` был вызван с правильными параметрами.
   - Проверяет, что возвращенный результат соответствует ожидаемому (т.е., `element`).

4. **`test_get_webelement_by_locator_multiple_elements`:**
   - Создает список из нескольких фиктивных веб-элементов `elements`.
   - Настраивает `driver_mock.find_elements` так, чтобы он возвращал `elements`.
   - Определяет локатор.
   - Вызывает `execute_locator.get_webelement_by_locator(locator)`.
   - Проверяет, что `driver_mock.find_elements` вызван корректно.
   - Проверяет, что возвращенный результат равен `elements`.

5. **`test_get_webelement_by_locator_no_element`:**
   - Настраивает `driver_mock.find_elements` так, чтобы он возвращал пустой список, имитируя отсутствие элементов.
   - Определяет локатор.
   - Вызывает `execute_locator.get_webelement_by_locator(locator)`.
   - Проверяет, что `driver_mock.find_elements` вызван корректно.
   - Проверяет, что возвращенный результат равен `False`.

6. **`test_get_attribute_by_locator`:**
   - Создает фиктивный веб-элемент `element`.
   - Настраивает `element.get_attribute` так, чтобы он возвращал "test_value".
   - Настраивает `driver_mock.find_elements` так, чтобы он возвращал список, содержащий `element`.
   - Определяет локатор, включая атрибут `attribute`.
   - Вызывает `execute_locator.get_attribute_by_locator(locator)`.
   - Проверяет, что `driver_mock.find_elements` и `element.get_attribute` вызваны корректно.
   - Проверяет, что возвращенный результат равен "test_value".

7. **`test_send_message`:**
   - Создает фиктивный веб-элемент `element`.
   - Настраивает `driver_mock.find_elements` так, чтобы он возвращал список, содержащий `element`.
   - Определяет локатор.
   - Определяет сообщение `message`.
   - Вызывает `execute_locator.send_message(locator, message, typing_speed=0, continue_on_error=True)`.
   - Проверяет, что `driver_mock.find_elements` и `element.send_keys` вызваны корректно.
   - Проверяет, что возвращенный результат равен `True`.

8. **`test_send_message_typing_speed`:**
   - Создает фиктивный веб-элемент `element`.
   - Настраивает `driver_mock.find_elements` так, чтобы он возвращал список, содержащий `element`.
   - Определяет локатор, сообщение `message` и скорость печати `typing_speed`.
   - Использует `unittest.mock.patch` для перехвата вызовов `time.sleep`.
   - Вызывает `execute_locator.send_message` с указанной скоростью печати.
   - Проверяет, что `driver_mock.find_elements` вызван корректно.
   - Проверяет, что `element.send_keys` вызывался столько раз, сколько символов в сообщении.
   - Проверяет, что `time.sleep` вызывался с правильной скоростью печати.
   - Проверяет, что возвращенный результат равен `True`.

## <mermaid>

```mermaid
flowchart TD
    subgraph Fixtures
        driverMockFixture[driver_mock: MagicMock]
        executeLocatorFixture[execute_locator: ExecuteLocator]
    end

    subgraph Tests
        testSingleElement[test_get_webelement_by_locator_single_element]
        testMultipleElements[test_get_webelement_by_locator_multiple_elements]
        testNoElement[test_get_webelement_by_locator_no_element]
        testAttribute[test_get_attribute_by_locator]
        testSendMessage[test_send_message]
        testSendMessageSpeed[test_send_message_typing_speed]
    end

   driverMockFixture --> executeLocatorFixture
    
    executeLocatorFixture --> testSingleElement
    executeLocatorFixture --> testMultipleElements
    executeLocatorFixture --> testNoElement
    executeLocatorFixture --> testAttribute
    executeLocatorFixture --> testSendMessage
    executeLocatorFixture --> testSendMessageSpeed


    testSingleElement --> findSingleElement[driver_mock.find_elements(By.XPATH, selector)]
    findSingleElement --> getElementResult[execute_locator.get_webelement_by_locator]
    getElementResult --> assertSingleElement[assert result == element]

    testMultipleElements --> findMultipleElements[driver_mock.find_elements(By.XPATH, selector)]
    findMultipleElements --> getMultipleElementsResult[execute_locator.get_webelement_by_locator]
    getMultipleElementsResult --> assertMultipleElements[assert result == elements]


   testNoElement --> findNoElement[driver_mock.find_elements(By.XPATH, selector)]
    findNoElement --> getNoElementResult[execute_locator.get_webelement_by_locator]
    getNoElementResult --> assertNoElement[assert result is False]


   testAttribute --> findAttributeElement[driver_mock.find_elements(By.XPATH, selector)]
    findAttributeElement --> getAttribute[element.get_attribute(attribute)]
    getAttribute --> getAttributeResult[execute_locator.get_attribute_by_locator]
    getAttributeResult --> assertAttribute[assert result == "test_value"]
    

    testSendMessage --> findSendMessageElement[driver_mock.find_elements(By.XPATH, selector)]
    findSendMessageElement --> sendKeysMessage[element.send_keys(message)]
    sendKeysMessage --> sendMessageResult[execute_locator.send_message]
    sendMessageResult --> assertSendMessage[assert result is True]

   testSendMessageSpeed --> findSendMessageSpeedElement[driver_mock.find_elements(By.XPATH, selector)]
    findSendMessageSpeedElement --> sendKeysSpeedMessage[element.send_keys(message)]
    sendKeysSpeedMessage --> sleep[time.sleep(typing_speed)]
    sleep --> sendMessageSpeedResult[execute_locator.send_message]
    sendMessageSpeedResult --> assertSendMessageSpeed[assert result is True]
```

**Объяснение зависимостей:**

- **`driverMockFixture`**: Создает mock-объект для имитации веб-драйвера Selenium.
- **`executeLocatorFixture`**: Создает экземпляр `ExecuteLocator`, используя mock-драйвер.
- **Тесты (testSingleElement, testMultipleElements, testNoElement, testAttribute, testSendMessage, testSendMessageSpeed)**: Каждый тест использует `executeLocatorFixture` для тестирования методов `ExecuteLocator`.
- Каждый тест вызывает методы  `driver_mock`  для имитации поиска элементов и взаимодействия с ними.
- `time.sleep` импортирован как mock-обьект через `patch`, это позволяет контролировать задержки.

## <объяснение>

**Импорты:**

-   `pytest`: Фреймворк для написания тестов. Используется для создания фикстур и организации тестов.
-   `unittest.mock`: Модуль для создания фиктивных объектов (mocks).
    -   `MagicMock`: Используется для создания гибких mock-объектов, имитирующих поведение.
    -   `patch`: Используется для замены участков кода mock-объектами на время выполнения тестов.
    - `create_autospec`: Создает mock-объект на основе спецификации.
-   `selenium.webdriver.remote.webelement.WebElement`:  Класс, представляющий веб-элемент на странице.
-   `selenium.webdriver.common.by.By`: Используется для указания типа локатора (XPATH, CSS и т. д.).
-   `selenium.webdriver.common.action_chains.ActionChains`: Класс для создания цепочек действий с веб-элементами. В данном коде не используется напрямую, но импортируется.
-   `selenium.common.exceptions`: Содержит исключения, которые могут возникнуть в Selenium, такие как `NoSuchElementException` и `TimeoutException`.
-   `src.webdriver.executor.ExecuteLocator`: Класс, который выполняет поиск и взаимодействие с элементами.
-   `src.logger.exceptions.ExecuteLocatorException`: Кастомное исключение, которое может быть выброшено в процессе выполнения.

**Фикстуры (`@pytest.fixture`):**

-   `driver_mock`:
    -   Создает mock-объект `MagicMock`, который имитирует поведение веб-драйвера.
    -   Это позволяет тестировать логику, зависящую от веб-драйвера, без фактического запуска браузера.
    -   Возвращает: `MagicMock` instance.
-   `execute_locator`:
    -   Создает экземпляр `ExecuteLocator`, передавая в него `driver_mock`.
    -   Предоставляет готовый объект `ExecuteLocator` для тестирования его методов.
    -   Возвращает: `ExecuteLocator` instance.

**Функции (тесты):**

-   `test_get_webelement_by_locator_single_element`:
    -   `execute_locator`: Экземпляр `ExecuteLocator`.
    -   `driver_mock`: Mock-объект веб-драйвера.
    -   Проверяет, что `get_webelement_by_locator` возвращает один веб-элемент, когда он существует.
    -   Создает mock веб-элемент, настраивает `find_elements` для его возвращения.
    -   Проверяет, что `find_elements` был вызван с корректным локатором и что возвращен правильный элемент.
-   `test_get_webelement_by_locator_multiple_elements`:
    -   `execute_locator`: Экземпляр `ExecuteLocator`.
    -   `driver_mock`: Mock-объект веб-драйвера.
    -   Проверяет, что `get_webelement_by_locator` возвращает список веб-элементов.
    -   Создает список mock веб-элементов, настраивает `find_elements` для его возвращения.
    -   Проверяет корректность вызова и возвращения.
-   `test_get_webelement_by_locator_no_element`:
    -   `execute_locator`: Экземпляр `ExecuteLocator`.
    -   `driver_mock`: Mock-объект веб-драйвера.
    -   Проверяет, что `get_webelement_by_locator` возвращает `False`, если элемент не найден.
    -    Настраивает `find_elements` на возврат пустого списка.
    -   Проверяет вызов и возвращение.
-   `test_get_attribute_by_locator`:
    -   `execute_locator`: Экземпляр `ExecuteLocator`.
    -   `driver_mock`: Mock-объект веб-драйвера.
    -   Проверяет, что `get_attribute_by_locator` возвращает атрибут элемента.
    -   Создает mock веб-элемент, настраивает `get_attribute` для возвращения значения, настраивает `find_elements` на возврат элемента.
    -   Проверяет вызовы и возвращаемое значение.
-   `test_send_message`:
    -    `execute_locator`: Экземпляр `ExecuteLocator`.
    -   `driver_mock`: Mock-объект веб-драйвера.
    -   Проверяет, что `send_message` отправляет сообщение элементу.
    -    Создает mock веб-элемент, настраивает `find_elements` на возврат элемента.
    -   Проверяет вызовы и возвращаемое значение.
-   `test_send_message_typing_speed`:
    -    `execute_locator`: Экземпляр `ExecuteLocator`.
    -   `driver_mock`: Mock-объект веб-драйвера.
    -    Проверяет, что `send_message` отправляет сообщение элементу с заданной скоростью.
    -   Использует `patch` для перехвата вызовов `time.sleep`,
    -   Создает mock веб-элемент, настраивает `find_elements` на возврат элемента.
    -   Проверяет количество вызовов `send_keys` и `time.sleep`.

**Переменные:**

-   `locator`: Словарь, содержащий информацию о локаторе элемента (`by`, `selector`, `attribute` ).
-   `element`: Mock-объект класса `WebElement`, представляющий веб-элемент.
-   `elements`: Список mock-объектов класса `WebElement`.
-   `message`: Строка, представляющая сообщение для отправки элементу.
-   `typing_speed`: Число, представляющее задержку между вводом символов (в секундах).
-   `result`: Результат выполнения тестируемой функции.

**Потенциальные улучшения:**

-   Добавить больше проверок на исключения, которые могут возникнуть.
-   Использовать более точные `spec` для mock-объектов, чтобы имитировать поведение Selenium более точно.
-   Покрыть больше случаев использования `ExecuteLocator`.
-    Возможно добавление тестов на негативные сценарии, когда ожидается ошибка.

**Взаимосвязь с другими частями проекта:**

-   Этот модуль (`test_executor.py`) тестирует класс `ExecuteLocator` из `src.webdriver.executor`.
-   Использует кастомное исключение `ExecuteLocatorException` из `src.logger.exceptions`.
-   Зависит от Selenium для взаимодействия с веб-элементами (хотя здесь используется mock-объект).
-  Используется `pytest` для организации тестов и фикстур.