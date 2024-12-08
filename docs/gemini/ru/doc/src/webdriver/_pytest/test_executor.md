# Модуль hypotez/src/webdriver/_pytest/test_executor.py

## Обзор

Этот модуль содержит тесты для класса `ExecuteLocator`, отвечающего за взаимодействие с веб-элементами.  Тесты проверяют различные сценарии, включая нахождение элементов по локеторам, получение атрибутов элементов, отправку сообщений (ввода текста) и поведение при отсутствии элементов.  Модуль использует фикстуры для создания имитаций веб-драйвера.


## Фикстуры

### `driver_mock`

**Описание**: Создает фиктивный объект веб-драйвера, используемый для тестирования методов `ExecuteLocator`.

**Возвращает**:
- `MagicMock`: Объект, имитирующий веб-драйвер.


### `execute_locator`

**Описание**: Создает экземпляр класса `ExecuteLocator` с использованием фикстуры `driver_mock`.

**Параметры**:
- `driver_mock`: Фикстура, представляющая имитацию веб-драйвера.


**Возвращает**:
- `ExecuteLocator`: Экземпляр класса `ExecuteLocator`.


## Тесты

### `test_get_webelement_by_locator_single_element`

**Описание**: Проверяет корректное получение единственного элемента по заданному локетору.

**Параметры**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver_mock`: Фикстура, представляющая имитацию веб-драйвера.


**Локатор**:
- `by`: XPATH
- `selector`: "//div[@id='test']"


**Ожидаемый результат**:
- Возвращаемый элемент `WebElement`.
- Вызов метода `driver_mock.find_elements` с указанным локетором.


### `test_get_webelement_by_locator_multiple_elements`

**Описание**: Проверяет корректное получение списка элементов по заданному локетору.

**Параметры**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver_mock`: Фикстура, представляющая имитацию веб-драйвера.


**Локатор**:
- `by`: XPATH
- `selector`: "//div[@class='test']"


**Ожидаемый результат**:
- Возвращаемый список элементов `WebElement`.
- Вызов метода `driver_mock.find_elements` с указанным локетором.


### `test_get_webelement_by_locator_no_element`

**Описание**: Проверяет обработку случая, когда элемент не найден по заданному локетору.

**Параметры**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver_mock`: Фикстура, представляющая имитацию веб-драйвера.


**Локатор**:
- `by`: XPATH
- `selector`: "//div[@id='not_exist']"


**Ожидаемый результат**:
- Возвращаемое значение `False`.
- Вызов метода `driver_mock.find_elements` с указанным локетором.


### `test_get_attribute_by_locator`

**Описание**: Проверяет получение атрибута элемента по заданному локетору.

**Параметры**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver_mock`: Фикстура, представляющая имитацию веб-драйвера.


**Локатор**:
- `by`: XPATH
- `selector`: "//div[@id='test']"
- `attribute`: "data-test"


**Ожидаемый результат**:
- Возвращаемое значение атрибута "data-test".
- Вызов метода `element.get_attribute` с аргументом "data-test".
- Вызов метода `driver_mock.find_elements` с указанным локетором.



### `test_send_message`

**Описание**: Проверяет отправку сообщения (ввода текста) элементу по заданному локетору.

**Параметры**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver_mock`: Фикстура, представляющая имитацию веб-драйвера.


**Локатор**:
- `by`: XPATH
- `selector`: "//input[@id='test']"


**Сообщение**:
- `"Hello World"`


**Ожидаемый результат**:
- Возвращаемое значение `True`.
- Вызов метода `element.send_keys` с переданным сообщением.
- Вызов метода `driver_mock.find_elements` с указанным локетором.



### `test_send_message_typing_speed`

**Описание**: Проверяет отправку сообщения (ввода текста) элементу с заданной скоростью набора.

**Параметры**:
- `execute_locator`: Экземпляр класса `ExecuteLocator`.
- `driver_mock`: Фикстура, представляющая имитацию веб-драйвера.


**Локатор**:
- `by`: XPATH
- `selector`: "//input[@id='test']"


**Сообщение**:
- `"Hello"`


**Скорость набора**:
- `0.1`


**Ожидаемый результат**:
- Возвращаемое значение `True`.
- Вызов метода `element.send_keys` несколько раз (равно количеству символов в сообщении).
- Вызов метода `time.sleep` с переданной скоростью.
- Вызов метода `driver_mock.find_elements` с указанным локетором.