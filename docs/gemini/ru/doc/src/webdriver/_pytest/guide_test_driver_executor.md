# Руководство по запуску и выполнению тестов для test_driver_executor.py

## Обзор

Это руководство описывает, как запустить и выполнить тесты для классов `Driver` и `ExecuteLocator`, расположенных в файле `test_driver_executor.py`. Тесты проверяют функциональность методов этих классов и взаимодействие между ними.

## Оглавление

- [Введение](#введение)
- [Структура тестов](#структура-тестов)
- [Тестируемые методы и функции](#тестируемые-методы-и-функции)
- [Запуск тестов](#запуск-тестов)
    - [Установка зависимостей](#установка-зависимостей)
    - [Настройка WebDriver](#настройка-webdriver)
    - [Запуск тестов](#запуск-тестов-1)
- [Описание тестов](#описание-тестов)
    - [test_navigate_to_page](#test_navigate_to_page)
    - [test_get_webelement_by_locator_single_element](#test_get_webelement_by_locator_single_element)
    - [test_get_webelement_by_locator_no_element](#test_get_webelement_by_locator_no_element)
    - [test_send_message](#test_send_message)
    - [test_get_attribute_by_locator](#test_get_attribute_by_locator)
    - [test_execute_locator_event](#test_execute_locator_event)
    - [test_get_locator_keys](#test_get_locator_keys)
    - [test_navigate_and_interact](#test_navigate_and_interact)
    - [test_invalid_locator](#test_invalid_locator)
- [Отчеты о тестах](#отчеты-о-тестах)
- [Чеклист](#чеклист)
- [Заключение](#заключение)


## Введение

В данном руководстве подробно описаны шаги по запуску и выполнению тестов, расположенных в файле `test_driver_executor.py`.  Тесты охватывают проверку работы методов классов `Driver` и `ExecuteLocator`, включая взаимодействие между ними.

## Структура тестов

Файл `test_driver_executor.py` содержит тесты для классов `Driver` и `ExecuteLocator`.  Каждый тест проверяет определенный аспект функциональности или сценарий использования.


## Тестируемые методы и функции

Тесты в `test_driver_executor.py` проверяют следующие методы и функции:

- `test_navigate_to_page`: Проверка навигации WebDriver к указанной странице.
- `test_get_webelement_by_locator_single_element`: Проверка получения элемента по локатору.
- `test_get_webelement_by_locator_no_element`: Проверка обработки случая, когда элемент не найден по локатору.
- `test_send_message`: Проверка отправки сообщения элементу.
- `test_get_attribute_by_locator`: Проверка получения атрибута элемента по локатору.
- `test_execute_locator_event`: Проверка выполнения события на элементе по локатору.
- `test_get_locator_keys`: Проверка получения ключей локатора.
- `test_navigate_and_interact`: Проверка навигации и взаимодействия с элементами на другой странице.
- `test_invalid_locator`: Проверка обработки некорректных локаторов и исключений.


## Запуск тестов

### Установка зависимостей

Перед запуском тестов убедитесь, что установлены все необходимые пакеты:

```bash
pip install -r requirements.txt
```

Убедитесь, что в файле `requirements.txt` перечислены все необходимые библиотеки, включая `pytest`, `selenium` и другие.

### Настройка WebDriver

Тесты используют Chrome WebDriver.  Установите ChromeDriver и укажите путь к нему в коде:

```python
from selenium.webdriver.chrome.service import Service
service = Service(executable_path="/path/to/chromedriver")
# ... (ваш код)
```

Замените `/path/to/chromedriver` на фактический путь к исполняемому файлу ChromeDriver на вашем компьютере.


### Запуск тестов

Для запуска тестов используйте команду:

```bash
pytest src/webdriver/_pytest/test_driver_executor.py
```

Это запустит все тесты в файле `test_driver_executor.py`.

## Описание тестов

### `test_navigate_to_page`

**Цель**: Проверить навигацию WebDriver к указанной странице.
**Ожидаемый результат**: Текущий URL браузера должен соответствовать "http://example.com".

### `test_get_webelement_by_locator_single_element`

**Цель**: Проверить получение элемента по локатору.
**Ожидаемый результат**: Возвращаемый элемент должен быть экземпляром `WebElement` и содержать текст "Example Domain".

### Остальные тесты ( `test_get_webelement_by_locator_no_element`, `test_send_message`, `test_get_attribute_by_locator`, `test_execute_locator_event`, `test_get_locator_keys`, `test_navigate_and_interact`, `test_invalid_locator`):

Описание аналогичным образом описывает цель, ожидаемый результат каждого теста.

## Отчеты о тестах

`pytest` создаёт отчет о результатах тестов. Используйте флаги командной строки для получения более подробных отчетов, например:

```bash
pytest src/webdriver/_pytest/test_driver_executor.py -v --html=report.html
```
(Для HTML отчета).

## Чеклист

Перед запуском тестов:

- [ ] Убедитесь, что установлены все необходимые зависимости (`requirements.txt`).
- [ ] Укажите корректный путь к `chromedriver` в коде.
- [ ] Убедитесь, что `chromedriver` доступен в вашей системе.
- [ ] Правильно настроены параметры для запуска тестов (`headless` режим и т.д.)


## Заключение

Следуя данному руководству, вы сможете успешно запустить и выполнить тесты, проверенные в файле `test_driver_executor.py`.  Обращайтесь за дополнительной информацией при необходимости.