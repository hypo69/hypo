# src.webdriver._examples._example_executor_2.py

## Обзор

Примеры использования класса `ExecuteLocator` для различных сценариев тестирования. В этом файле приведены примеры создания экземпляра `ExecuteLocator` и выполнения различных задач с его помощью.

## Содержание

1. [Обзор](#обзор)
2. [Импорты](#импорты)
3. [Инициализация WebDriver и ExecuteLocator](#инициализация-webdriver-и-executelocator)
4. [Простой пример создания экземпляра и использования методов](#простой-пример-создания-экземпляра-и-использования-методов)
5. [Пример использования с различными событиями и атрибутами](#пример-использования-с-различными-событиями-и-атрибутами)
6. [Пример обработки ошибки и продолжения на ошибки](#пример-обработки-ошибки-и-продолжения-на-ошибки)
7. [Пример использования с `send_message`](#пример-использования-с-send_message)
8. [Пример с использованием списка локаторов](#пример-с-использованием-списка-локаторов)
9. [Пример использования `evaluate_locator`](#пример-использования-evaluate_locator)
10. [Пример с обработкой исключений](#пример-с-обработкой-исключений)
11. [Полный пример теста](#полный-пример-теста)
12. [Закрытие драйвера](#закрытие-драйвера)

## Импорты

```python
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator
from src import gs
from src.logger.exceptions import ExecuteLocatorException
```

Импортируются необходимые модули и классы:
- `webdriver` из `selenium` для управления браузером.
- `ExecuteLocator` из `src.webdriver.executor` для выполнения локаторов.
- `gs` из `src` для глобальных настроек (пути к драйверам).
- `ExecuteLocatorException` из `src.logger.exceptions` для обработки исключений при выполнении локатора.

## Инициализация WebDriver и ExecuteLocator

```python
driver = webdriver.Chrome(executable_path=gs['chrome_driver_path'])
driver.get("https://example.com")
locator = ExecuteLocator(driver)
```
Создается экземпляр веб-драйвера Chrome, выполняется переход на сайт `https://example.com` и создается экземпляр `ExecuteLocator`.

## Простой пример создания экземпляра и использования методов

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
Здесь показано создание простого локатора для получения заголовка страницы (`<h1>`) и его выполнение с использованием метода `execute_locator`. Результат выполнения выводится в консоль.

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
Пример сложного локатора с вложенными элементами. Локатор ищет ссылки на продукты и выполняет клик на пагинацию, после чего нажимает на кнопку "Следующая страница". Результат выполнения выводится в консоль.

## Пример обработки ошибки и продолжения на ошибки

```python
print("\nПример обработки ошибки и продолжения на ошибки")

try:
    locator.execute_locator(complex_locator, continue_on_error=True)
except ExecuteLocatorException as ex:
    print(f"Произошла ошибка: {ex}")
```
Здесь показана обработка ошибки при выполнении локатора. Даже если произойдет ошибка, выполнение продолжится благодаря параметру `continue_on_error=True`.  Если ошибка возникнет, она будет перехвачена и выведена в консоль.

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
Демонстрация использования метода `send_message` для отправки текста в поле поиска. Параметр `typing_speed` задает скорость ввода.

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
Пример работы с множественными локаторами, заданными в виде списков. Здесь выполняется клик по кнопке и ввод текста в поле ввода.

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
Показано использование метода `evaluate_locator` для получения значения атрибута элемента. В данном случае извлекается `content` мета-тега `description`.

## Пример с обработкой исключений

```python
print("\nПример с обработкой исключений")

try:
    locator.execute_locator(simple_locator)
except ExecuteLocatorException as ex:
    print(f"Произошла ошибка при выполнении локатора: {ex}")
```
Пример обработки исключения при выполнении простого локатора. Если возникнет ошибка, она будет перехвачена и выведена в консоль.

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
Полный пример выполнения локатора для получения заголовка страницы.

## Закрытие драйвера

```python
driver.quit()
```
Закрытие браузера.