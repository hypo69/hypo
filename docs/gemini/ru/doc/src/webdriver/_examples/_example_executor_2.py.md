# `_example_executor_2.py`

## Обзор

Файл содержит примеры использования класса `ExecuteLocator` для различных сценариев тестирования. В нем показано, как создать экземпляр `ExecuteLocator` и выполнять различные задачи, такие как получение элементов, отправка сообщений, обработка исключений и оценка локаторов.

## Содержание

1.  [Обзор](#обзор)
2.  [Импорт](#импорт)
3.  [Создание экземпляра WebDriver](#создание-экземпляра-webdriver)
4.  [Создание экземпляра ExecuteLocator](#создание-экземпляра-executelocator)
5.  [Простой пример использования методов](#простой-пример-использования-методов)
6.  [Пример использования с различными событиями и атрибутами](#пример-использования-с-различными-событиями-и-атрибутами)
7.  [Пример обработки ошибки и продолжения на ошибки](#пример-обработки-ошибки-и-продолжения-на-ошибки)
8.  [Пример использования с `send_message`](#пример-использования-с-send_message)
9.  [Пример с использованием списка локаторов](#пример-с-использованием-списка-локаторов)
10. [Пример использования `evaluate_locator`](#пример-использования-evaluate_locator)
11. [Пример с обработкой исключений](#пример-с-обработкой-исключений)
12. [Полный пример теста](#полный-пример-теста)
13. [Закрытие драйвера](#закрытие-драйвера)

## Импорт

```python
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator
from src import gs
from src.logger.exceptions import ExecuteLocatorException
```

Импортируются необходимые библиотеки и классы для работы с Selenium WebDriver, локаторами и обработкой исключений.

## Создание экземпляра WebDriver

```python
driver = webdriver.Chrome(executable_path=gs['chrome_driver_path'])
driver.get("https://example.com")
```

Создается экземпляр Chrome WebDriver и выполняется переход на страницу `https://example.com`.

## Создание экземпляра ExecuteLocator

```python
locator = ExecuteLocator(driver)
```

Создается экземпляр класса `ExecuteLocator`, который будет использоваться для выполнения локаторов.

## Простой пример использования методов

```python
print("Простой пример создания экземпляра и использования методов")

simple_locator = {
    "by": "XPATH",
    "selector": "//h1",
    "attribute": "textContent",
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": None,
    "if_list":"first","use_mouse": False,
    "mandatory": True,
    "locator_description": "Получение заголовка страницы"
}

result = locator.execute_locator(simple_locator)
print(f"Результат выполнения простого локатора: {result}")
```

В этом примере показано, как создать простой локатор для получения текста заголовка страницы и выполнить его с помощью `execute_locator`.

## Пример использования с различными событиями и атрибутами

```python
print("\nПример использования с различными событиями и атрибутами")

complex_locator = {
    "product_links": {
        "attribute": "href",
        "by": "XPATH",
        "selector": "//a[contains(@class, \'product\')]",
        "timeout":0,"timeout_for_event":"presence_of_element_located","event": None,
        "if_list":"first","use_mouse": False,
        "mandatory": True,
        "locator_description": "Получение ссылки на продукт"
    },
    "pagination": {
        "ul": {
            "attribute": None,
            "by": "XPATH",
            "selector": "//ul[@class=\'pagination\']",
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()",
            "if_list":"first","use_mouse": False,
            "mandatory": True,
            "locator_description": "Нажатие на пагинацию"
        },
        "->": {
            "attribute": None,
            "by": "XPATH",
            "selector": "//*[@class = \'ui-pagination-navi util-left\']/a[@class=\'ui-pagination-next\']",
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()",
            "if_list":"first","use_mouse": False,
            "mandatory": True,
            "locator_description": "Клик по следующей странице"
        }
    }
}

result = locator.execute_locator(complex_locator)
print(f"Результат выполнения сложного локатора: {result}")
```

Пример показывает использование сложного локатора с разными событиями и атрибутами, такими как клик по пагинации и получение ссылок на товары.

## Пример обработки ошибки и продолжения на ошибки

```python
print("\nПример обработки ошибки и продолжения на ошибки")

try:
    locator.execute_locator(complex_locator, continue_on_error=True)
except ExecuteLocatorException as ex:
    print(f"Произошла ошибка: {ex}")
```

Здесь показано, как обрабатывать ошибки при выполнении локатора и продолжать выполнение теста с параметром `continue_on_error=True`.

## Пример использования с `send_message`

```python
print("\nПример использования с `send_message`")

message_locator = {
    "by": "XPATH",
    "selector": "//input[@name=\'search\']",
    "attribute": None,
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": "%SEARCH%",
    "if_list":"first","use_mouse": False,
    "mandatory": True,
    "locator_description": "Отправка поискового запроса"
}

message = "Купить новый телефон"
result = locator.send_message(message_locator, message, typing_speed=0.05, continue_on_error=True)
print(f"Результат отправки сообщения: {result}")
```

Этот пример демонстрирует отправку сообщения в текстовое поле с использованием метода `send_message` и параметра `continue_on_error=True`.

## Пример с использованием списка локаторов

```python
print("\nПример с использованием списка локаторов")

multi_locator = {
    "by": ["XPATH", "XPATH"],
    "selector": ["//button[@id=\'submit\']", "//input[@id=\'username\']"],
    "attribute": ["textContent", "value"],
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": ["click()", "send_keys(\'user\')"],
    "if_list":"first","use_mouse": [True, False],
    "mandatory": [True, True],
    "locator_description": ["Нажатие кнопки отправки", "Ввод имени пользователя"]
}

results = locator.execute_locator(multi_locator)
print(f"Результаты выполнения множества локаторов: {results}")
```

Здесь показано, как использовать список локаторов для взаимодействия с несколькими элементами одновременно.

## Пример использования `evaluate_locator`

```python
print("\nПример использования `evaluate_locator`")

attribute_locator = {
    "by": "XPATH",
    "selector": "//meta[@name=\'description\']",
    "attribute": "content",
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": None,
    "if_list":"first","use_mouse": False,
    "mandatory": True,
    "locator_description": "Получение значения мета-описания страницы"
}

attribute_value = locator.evaluate_locator(attribute_locator['attribute'])
print(f"Значение атрибута: {attribute_value}")
```

Пример использования метода `evaluate_locator` для получения значения атрибута элемента.

## Пример с обработкой исключений

```python
print("\nПример с обработкой исключений")

try:
    locator.execute_locator(simple_locator)
except ExecuteLocatorException as ex:
    print(f"Произошла ошибка при выполнении локатора: {ex}")
```

Демонстрируется обработка исключений при выполнении простого локатора.

## Полный пример теста

```python
print("\nПолный пример теста")

test_locator = {
    "by": "XPATH",
    "selector": "//h1",
    "attribute": "textContent",
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": None,
    "if_list":"first","use_mouse": False,
    "mandatory": True,
    "locator_description": "Получение заголовка страницы"
}

result = locator.execute_locator(test_locator)
print(f"Результат выполнения тестового локатора: {result}")
```

Полный пример теста, демонстрирующий использование `execute_locator` для получения текста заголовка страницы.

## Закрытие драйвера

```python
driver.quit()
```

В конце закрывается экземпляр WebDriver.