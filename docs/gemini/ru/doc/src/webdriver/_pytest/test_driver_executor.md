# Модуль `hypotez/src/webdriver/_pytest/test_driver_executor.py`

## Обзор

Этот модуль содержит тестовые функции для проверки функциональности класса `ExecuteLocator` и взаимодействия с `WebDriver` в контексте тестирования. Тесты охватывают различные сценарии, включая навигацию по страницам, поиск элементов, отправку сообщений, получение атрибутов и обработку ошибок.

## Фикстуры

### `driver()`

**Описание**: Фикстура для инициализации и завершения работы `WebDriver` (Selenium).

**Возвращает**:
- `webdriver.Chrome`: Экземпляр драйвера Chrome.

**Инициализация**:
- Создает экземпляр `webdriver.Chrome` с опцией `headless` для бескриптового режима.
- Устанавливает путь к `chromedriver`.
- Переходит на стартовую страницу ("http://example.com").

**Завершение**:
- Закрывает драйвер (`driver.quit()`).

### `execute_locator(driver)`

**Описание**: Фикстура для инициализации экземпляра `ExecuteLocator`.

**Аргументы**:
- `driver`: Экземпляр `WebDriver`, полученный из фикстуры `driver()`.

**Возвращает**:
- `ExecuteLocator`: Экземпляр класса `ExecuteLocator` с заданным `WebDriver`.


## Тесты

### `test_navigate_to_page(execute_locator, driver)`

**Описание**: Тестирует навигацию WebDriver на указанную страницу.

**Аргументы**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Проверяет**:
- Что текущий URL `driver.current_url` равен ожидаемой странице ("http://example.com").

### `test_get_webelement_by_locator_single_element(execute_locator, driver)`

**Описание**: Тестирует получение элемента по локатору.

**Аргументы**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Проверяет**:
- Что метод `execute_locator.get_webelement_by_locator` возвращает экземпляр `WebElement`.
- Что текст полученного элемента соответствует ожидаемому ("Example Domain").

### `test_get_webelement_by_locator_no_element(execute_locator, driver)`

**Описание**: Тестирует случай, когда элемент не найден по локатору.

**Аргументы**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Проверяет**:
- Что метод `execute_locator.get_webelement_by_locator` возвращает `False`, если элемент не найден.

### `test_send_message(execute_locator, driver)`

**Описание**: Тестирует отправку сообщения элементу.

**Аргументы**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Проверяет**:
- Что метод `execute_locator.send_message` корректно отправляет сообщение заданному элементу.

### `test_get_attribute_by_locator(execute_locator, driver)`

**Описание**: Тестирует получение атрибута элемента по локатору.

**Аргументы**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Проверяет**:
- Что метод `execute_locator.get_attribute_by_locator` возвращает корректное значение атрибута.


### `test_execute_locator_event(execute_locator, driver)`

**Описание**: Тестирует выполнение события на элементе.

**Аргументы**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Проверяет**:
- Что метод `execute_locator.execute_locator` корректно выполняет событие (в данном случае клик) на элементе.

### `test_get_locator_keys(execute_locator, driver)`

**Описание**: Тестирует получение доступных ключей локатора.

**Аргументы**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Проверяет**:
- Что метод `ExecuteLocator.get_locator_keys` возвращает ожидаемый набор ключей локатора.

### `test_navigate_and_interact(execute_locator, driver)`

**Описание**: Тестирует навигацию на новую страницу и взаимодействие с элементами.

**Аргументы**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Проверяет**:
- Что WebDriver переходит на новую страницу.
- Что поиск, отправка сообщения и нажатие кнопки работают корректно.
- Что на целевой странице присутствует ожидаемый элемент.


### `test_invalid_locator(execute_locator, driver)`

**Описание**: Тестирует обработку некорректных локаторов.

**Аргументы**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Проверяет**:
- Что при использовании некорректного локатора генерируется исключение `ExecuteLocatorException`.