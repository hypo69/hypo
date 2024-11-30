# Руководство по запуску и выполнению тестов для `test_driver_executor.py`

## Обзор

Данное руководство описывает процесс запуска и выполнения тестов для файла `test_driver_executor.py`, содержащего тесты для классов `Driver` и `ExecuteLocator`.  Документация включает в себя описание тестов, их целей, необходимые шаги по установке и настройке, а также способы получения отчетов.

## Оглавление

- [Введение](#введение)
- [Структура тестов](#структура-тестов)
- [Тестируемые методы и функции](#тестируемые-методы-и-функции)
- [Запуск тестов](#запуск-тестов)
    - [Установка зависимостей](#установка-зависимостей)
    - [Настройка WebDriver](#настройка-webdriver)
    - [Запуск тестов](#запуск-тестов-2)
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

Это руководство поможет вам запустить и выполнить тесты для классов `Driver` и `ExecuteLocator` из файла `test_driver_executor.py`. Тесты проверяют корректность работы методов этих классов и их взаимодействие.

## Структура тестов

Файл `test_driver_executor.py` содержит тесты для классов `Driver` и `ExecuteLocator`, проверяя различные аспекты их функциональности, включая взаимодействие с веб-страницами и обработку различных сценариев.

## Тестируемые методы и функции

В файле `test_driver_executor.py` определены следующие тесты:

- `test_navigate_to_page`: Проверяет навигацию к странице.
- `test_get_webelement_by_locator_single_element`: Проверяет поиск элемента по локатору.
- `test_get_webelement_by_locator_no_element`: Проверяет обработку случая, когда элемент не найден.
- `test_send_message`: Проверяет отправку сообщения.
- `test_get_attribute_by_locator`: Проверяет получение атрибута элемента.
- `test_execute_locator_event`: Проверяет выполнение события локатора.
- `test_get_locator_keys`: Проверяет получение ключей локатора.
- `test_navigate_and_interact`: Проверяет последовательность навигации и взаимодействия с элементами.
- `test_invalid_locator`: Проверяет обработку некорректных локаторов.


## Запуск тестов

### Установка зависимостей

Перед запуском тестов убедитесь, что установлены необходимые пакеты, перечисленные в файле `requirements.txt`.  Выполните команду:

```bash
pip install -r requirements.txt
```


### Настройка WebDriver

Тесты используют ChromeDriver. Вам необходимо указать путь к нему:

```python
from selenium.webdriver.chrome.service import Service
service = Service(executable_path="/путь/к/chromedriver") # Замените на ваш путь
```

**Важно!** Замените `/путь/к/chromedriver` на фактический путь к вашему файлу `chromedriver`.

### Запуск тестов

Для запуска тестов используйте команду:

```bash
pytest src/webdriver/_pytest/test_driver_executor.py
```


## Описание тестов

### `test_navigate_to_page`

- **Цель**: Проверить навигацию к странице `http://example.com`.
- **Ожидаемый результат**: Текущий URL браузера должен быть `http://example.com`.

### `test_get_webelement_by_locator_single_element`

- **Цель**: Проверить поиск элемента по локатору.
- **Ожидаемый результат**: Должен быть получен элемент с текстом "Example Domain".


(Остальные описания тестов аналогично, следует заполнить ожидаемые результаты и подробности для каждого теста)


## Отчеты о тестах

Pytest создаст отчет о результатах тестирования.  Для более подробных отчетов используйте флаги командной строки:
- `-v`:  Подробный текстовый отчет.
- `--html=report.html`:  HTML-отчет, который будет сохранен в `report.html`.


## Чеклист

Перед запуском тестов:

- [ ] Установлены все зависимости из `requirements.txt`.
- [ ] Указан корректный путь к `chromedriver`.
- [ ] Текущая версия `chromedriver` совместима с используемым драйвером.


## Заключение

Следуя этому руководству, вы сможете запустить и проверить тесты в `test_driver_executor.py`.  Обратите внимание на детали каждого теста для понимания его цели и ожидаемых результатов.