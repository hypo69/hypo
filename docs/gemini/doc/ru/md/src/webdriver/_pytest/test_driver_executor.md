# Модуль `hypotez/src/webdriver/_pytest/test_driver_executor.py`

## Обзор

Этот модуль содержит тесты для класса `ExecuteLocator` и WebDriver, проверяющие корректность работы функций взаимодействия с веб-элементами.  Тесты покрывают различные сценарии, включая навигацию по страницам, поиск элементов по локаторам, отправку сообщений, получение атрибутов и обработку исключений.

## Оглавление

- [Обзор](#обзор)
- [Фикстуры](#фикстуры)
- [Тесты](#тесты)


## Фикстуры

### `driver`

**Описание**: Фикстура, настраивающая и завершающая работу WebDriver.

**Использование**: Создает экземпляр WebDriver (Chrome в данном случае), настраивает его для работы в бескомпромиссном режиме (`headless`), загружает стартовую страницу ("http://example.com") и завершает работу после завершения тестов.

**Параметры**:

-  Не принимает параметров.

**Возвращает**: Экземпляр `webdriver.Chrome`.

**Вызывает исключения**: Возможны исключения, связанные с запуском драйвера (например, если chromedriver не найден по указанному пути).

### `execute_locator`

**Описание**: Фикстура, инициализирующая экземпляр `ExecuteLocator` с заданным драйвером.

**Использование**: Создаёт экземпляр класса `ExecuteLocator`, используя предоставленный в фикстуре `driver`.

**Параметры**:

- `driver`: Экземпляр `webdriver.Chrome`, необходимый для работы `ExecuteLocator`.

**Возвращает**: Экземпляр `ExecuteLocator`.

**Вызывает исключения**: Возможны исключения, связанные с созданием экземпляра `ExecuteLocator`.


## Тесты

### `test_navigate_to_page`

**Описание**: Проверяет, что WebDriver корректно переходит на заданную страницу.

**Параметры**:

- `execute_locator`: Экземпляр `ExecuteLocator`.
- `driver`: Экземпляр `webdriver.Chrome`.

**Возвращает**: `None`.

**Вызывает исключения**: Возможны исключения при навигации по странице.

### `test_get_webelement_by_locator_single_element`

**Описание**: Проверка корректного получения веб-элемента по локатору.

**Параметры**:

- `execute_locator`: Экземпляр `ExecuteLocator`.
- `driver`: Экземпляр `webdriver.Chrome`.

**Возвращает**: `None`.

**Вызывает исключения**: Возможны исключения при поиске элемента.


### `test_get_webelement_by_locator_no_element`

**Описание**: Проверяет, что при отсутствии элемента по локатору возвращается False.

**Параметры**:

- `execute_locator`: Экземпляр `ExecuteLocator`.
- `driver`: Экземпляр `webdriver.Chrome`.

**Возвращает**: `None`.

**Вызывает исключения**: Возможны исключения при поиске элемента.

### `test_send_message`

**Описание**: Тест отправки сообщения элементу.

**Параметры**:

- `execute_locator`: Экземпляр `ExecuteLocator`.
- `driver`: Экземпляр `webdriver.Chrome`.

**Возвращает**: `None`.

**Вызывает исключения**: Возможны исключения при отправке сообщения.  Обработка ошибок включена (`continue_on_error=True`).

### `test_get_attribute_by_locator`

**Описание**: Проверка получения атрибута элемента по локатору.

**Параметры**:

- `execute_locator`: Экземпляр `ExecuteLocator`.
- `driver`: Экземпляр `webdriver.Chrome`.


**Возвращает**: `None`.

**Вызывает исключения**: Возможны исключения при получении атрибута.

### `test_execute_locator_event`

**Описание**: Проверка корректного выполнения события на элементе по локатору.

**Параметры**:

- `execute_locator`: Экземпляр `ExecuteLocator`.
- `driver`: Экземпляр `webdriver.Chrome`.


**Возвращает**: `None`.

**Вызывает исключения**: Возможны исключения при выполнении события.


### `test_get_locator_keys`

**Описание**: Проверка получения доступных ключей локатора.

**Параметры**:

- `execute_locator`: Экземпляр `ExecuteLocator`.
- `driver`: Экземпляр `webdriver.Chrome`.

**Возвращает**: `None`.

**Вызывает исключения**: Возможны исключения при получении ключей.


### `test_navigate_and_interact`

**Описание**: Тест навигации по странице и взаимодействия с элементами.

**Параметры**:

- `execute_locator`: Экземпляр `ExecuteLocator`.
- `driver`: Экземпляр `webdriver.Chrome`.

**Возвращает**: `None`.

**Вызывает исключения**: Возможны исключения при навигации и взаимодействии.

### `test_invalid_locator`

**Описание**: Проверка обработки некорректного локатора.

**Параметры**:

- `execute_locator`: Экземпляр `ExecuteLocator`.
- `driver`: Экземпляр `webdriver.Chrome`.

**Возвращает**: `None`.

**Вызывает исключения**: Должно быть поднято исключение `ExecuteLocatorException` при попытке использования некорректного локатора.