# Модуль `hypotez/src/webdriver/_pytest/test_driver_executor.py`

## Обзор

Этот модуль содержит тесты для модуля `src.webdriver.executor`, проверяющие корректность работы с `WebDriver` и `ExecuteLocator`.  Тесты охватывают различные сценарии, включая навигацию по страницам, поиск элементов, отправку сообщений и обработку исключений.


## Фикстуры

### `driver`

**Описание**: Фикстура для инициализации и закрытия экземпляра `WebDriver`.  Создает экземпляр `webdriver.Chrome` в бескрайнем режиме, переходит на страницу `http://example.com` и закрывает браузер по завершению теста.

**Аргументы**:

-  Нет

**Возвращает**:
- `webdriver.Chrome`: Экземпляр WebDriver.

**Примечание**: Путь к chromedriver необходимо изменить на правильный.


### `execute_locator`

**Описание**: Фикстура для инициализации экземпляра `ExecuteLocator` с предоставленным экземпляром `WebDriver`.

**Аргументы**:
- `driver`: Экземпляр `WebDriver`.

**Возвращает**:
- `ExecuteLocator`: Экземпляр `ExecuteLocator`.


## Функции

### `test_navigate_to_page`

**Описание**: Проверяет, что `WebDriver` корректно переходит на указанную страницу.

**Аргументы**:
- `execute_locator`: Экземпляр `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Возвращает**:
- Нет

**Примечание**: Тест проверяет, что текущая страница `driver` соответствует ожидаемому адресу (`http://example.com`).


### `test_get_webelement_by_locator_single_element`

**Описание**: Проверяет, что метод `get_webelement_by_locator` возвращает элемент по валидному локатору.

**Аргументы**:
- `execute_locator`: Экземпляр `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Возвращает**:
- Нет

**Примечание**: Тест проверяет, что возвращаемое значение является элементом `WebElement` и его текст соответствует ожидаемому значению (`Example Domain`).

### `test_get_webelement_by_locator_no_element`

**Описание**: Проверяет работу метода `get_webelement_by_locator` при отсутствии элемента по локатору.

**Аргументы**:
- `execute_locator`: Экземпляр `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Возвращает**:
- Нет

**Примечание**: Тест проверяет, что в случае отсутствия элемента по локатору функция возвращает `False`.


### `test_send_message`

**Описание**: Проверяет отправку сообщения элементу.

**Аргументы**:
- `execute_locator`: Экземпляр `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Возвращает**:
- Нет

**Примечание**: Тест отправляет сообщение заданному элементу (используется `//input[@id='search']`).  Убедитесь, что locator верен и соответствует элементу на странице.


### `test_get_attribute_by_locator`

**Описание**: Проверяет получение атрибута элемента по локатору.

**Аргументы**:
- `execute_locator`: Экземпляр `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Возвращает**:
- Нет

**Примечание**: Тест проверяет, что метод `get_attribute_by_locator` возвращает значение атрибута (`href`).  Убедитесь, что locator верен и соответствует элементу на странице.


### `test_execute_locator_event`

**Описание**: Проверяет выполнение события на элементе по локатору.

**Аргументы**:
- `execute_locator`: Экземпляр `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Возвращает**:
- Нет

**Примечание**: Тест проверяет, что выполнение события ("click") успешно.  Убедитесь, что locator верен и соответствует элементу на странице.


### `test_get_locator_keys`

**Описание**: Проверяет получение доступных ключей локатора.

**Аргументы**:
- `execute_locator`: Экземпляр `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Возвращает**:
- Нет

**Примечание**: Тест проверяет, что возвращаемый набор ключей локатора совпадает с ожидаемым набором.


### `test_navigate_and_interact`

**Описание**: Проверяет навигацию к новой странице и взаимодействие с элементами.

**Аргументы**:
- `execute_locator`: Экземпляр `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Возвращает**:
- Нет

**Примечание**: Тест навигации к `https://www.wikipedia.org/` и отправки запроса в поиск.


### `test_invalid_locator`

**Описание**: Проверка обработки некорректного локатора.

**Аргументы**:
- `execute_locator`: Экземпляр `ExecuteLocator`.
- `driver`: Экземпляр `WebDriver`.

**Возвращает**:
- Нет

**Примечание**: Тест проверяет, что при использовании неверного локатора генерируется ожидаемое исключение `ExecuteLocatorException`.