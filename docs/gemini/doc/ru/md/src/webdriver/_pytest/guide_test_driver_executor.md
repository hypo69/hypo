# Руководство по запуску и выполнению тестов для `test_driver_executor.py`

## Обзор

Данное руководство предоставляет инструкции по запуску и выполнению тестов, расположенных в файле `test_driver_executor.py`. Оно описывает структуру тестов, тестируемые функции, необходимые зависимости, настройку WebDriver, запуск тестов и интерпретацию результатов.

## Оглавление

* [Введение](#введение)
* [Структура тестов](#структура-тестов)
* [Тестируемые методы и функции](#тестируемые-методы-и-функции)
* [Запуск тестов](#запуск-тестов)
    * [Установка зависимостей](#установка-зависимостей)
    * [Настройка WebDriver](#настройка-webdriver)
    * [Запуск тестов](#запуск-тестов-1)
* [Описание тестов](#описание-тестов)
    * [test_navigate_to_page](#test_navigate_to_page)
    * [test_get_webelement_by_locator_single_element](#test_get_webelement_by_locator_single_element)
    * [test_get_webelement_by_locator_no_element](#test_get_webelement_by_locator_no_element)
    * [test_send_message](#test_send_message)
    * [test_get_attribute_by_locator](#test_get_attribute_by_locator)
    * [test_execute_locator_event](#test_execute_locator_event)
    * [test_get_locator_keys](#test_get_locator_keys)
    * [test_navigate_and_interact](#test_navigate_and_interact)
    * [test_invalid_locator](#test_invalid_locator)
* [Отчеты о тестах](#отчеты-о-тестах)
* [Чеклист](#чеклист)
* [Заключение](#заключение)


## Введение

Данное руководство описывает, как запустить и выполнить тесты для классов `Driver` и `ExecuteLocator`, расположенные в файле `test_driver_executor.py`. Тесты проверяют функциональность методов классов и взаимодействие между `Driver` и `ExecuteLocator`.

## Структура тестов

Файл `test_driver_executor.py` содержит тесты для классов `Driver` и `ExecuteLocator`. Эти тесты проверяют корректность работы методов классов, взаимодействие между ними, а также сценарии использования в различных ситуациях.


## Тестируемые методы и функции

Список тестируемых методов и функций:

- `test_navigate_to_page`: Проверяет корректную загрузку страницы WebDriver.
- `test_get_webelement_by_locator_single_element`: Проверяет получение элемента по локатору.
- `test_get_webelement_by_locator_no_element`: Проверяет работу с отсутствующим элементом.
- `test_send_message`: Проверяет отправку сообщения элементу.
- `test_get_attribute_by_locator`: Проверяет получение атрибута элемента.
- `test_execute_locator_event`: Проверяет выполнение события на локаторе.
- `test_get_locator_keys`: Проверяет получение ключей локатора.
- `test_navigate_and_interact`: Проверяет навигацию и взаимодействие с элементами на другой странице.
- `test_invalid_locator`: Проверяет обработку некорректных локаторов и исключения.



## Запуск тестов

### Установка зависимостей

Перед запуском тестов убедитесь, что установлены все необходимые зависимости:

```bash
pip install -r requirements.txt
```

Убедитесь, что в файле `requirements.txt` перечислены все необходимые библиотеки (например, `pytest`, `selenium`, `pytest-html`).

### Настройка WebDriver

В тестах используется Chrome WebDriver. Убедитесь, что у вас установлен ChromeDriver и укажите путь к `chromedriver` в коде:

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="/path/to/chromedriver")  # Замените на ваш путь
driver = webdriver.Chrome(service=service)
```


### Запуск тестов

Для запуска тестов используйте команду:

```bash
pytest src/webdriver/_pytest/test_driver_executor.py
```


## Описание тестов

### `test_navigate_to_page`

**Цель:** Проверить, что WebDriver корректно загружает указанную страницу.
**Ожидаемый результат:** URL текущей страницы должен быть `"http://example.com"`.

### `test_get_webelement_by_locator_single_element`

**Цель:** Проверить получение элемента по локатору.
**Ожидаемый результат:** Элемент должен быть экземпляром `WebElement` и содержать текст `"Example Domain"`.

### `test_get_webelement_by_locator_no_element`

**Цель:** Проверить работу с отсутствующим элементом.
**Ожидаемый результат:** Метод должен возвращать `False`.

### Остальные тесты (аналогично)

... (описания остальных тестов в соответствии с заданными требованиями)

## Отчеты о тестах

По завершении тестов `pytest` создаст отчет с результатами. Используйте флаги командной строки для более подробных отчетов:

- Для текстового отчета: `pytest src/webdriver/_pytest/test_driver_executor.py -v`
- Для HTML отчета: (установите `pytest-html` `pip install pytest-html` и запустите `pytest --html=report.html`)


## Чеклист

Перед запуском тестов убедитесь, что:

- [ ] Установлены все зависимости.
- [ ] Указан правильный путь к `chromedriver`.
- [ ] Тесты запускаются командой `pytest`.

## Заключение

Следуя этому руководству, вы сможете запустить и проверить тесты. Обращайтесь к разработчикам при возникновении проблем.