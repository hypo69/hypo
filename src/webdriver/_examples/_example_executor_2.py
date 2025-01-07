## \file /src/webdriver/_examples/_example_executor_2.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.webdriver._examples 
	:platform: Windows, Unix
	:synopsis:

"""


"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""
  
""" module: src.webdriver._examples """


""" Примеры использования класса `ExecuteLocator` для различных сценариев тестирования.
@details В этом файле приведены примеры создания экземпляра `ExecuteLocator` и выполнения различных задач с его помощью.
"""

from selenium import webdriver
from src.webdriver.executor import ExecuteLocator
from src import gs
from src.logger.exceptions import ExecuteLocatorException

# Создание экземпляра WebDriver (например, Chrome)
driver = webdriver.Chrome(executable_path=gs['chrome_driver_path'])
driver.get("https://example.com")  # Переход на сайт

# Создание экземпляра ExecuteLocator
locator = ExecuteLocator(driver)

# Простой пример создания экземпляра и использования методов

print("Простой пример создания экземпляра и использования методов")

# Простой локатор для получения элемента по XPath
simple_locator = {
    "by": "XPATH",
    "selector": "//h1",
    "attribute": "textContent",
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": None,
    "if_list":"first","use_mouse": False,
    "mandatory": True,
    "locator_description": "Получение заголовка страницы"
}

# Выполнение локатора
result = locator.execute_locator(simple_locator)
print(f"Результат выполнения простого локатора: {result}")

# Пример использования с различными событиями и атрибутами

print("\nПример использования с различными событиями и атрибутами")

# Пример локатора для отправки сообщения и получения атрибута
complex_locator = {
    "product_links": {
        "attribute": "href",
        "by": "XPATH",
        "selector": "//a[contains(@class, 'product')]",
        "timeout":0,"timeout_for_event":"presence_of_element_located","event": None,
        "if_list":"first","use_mouse": False,
        "mandatory": True,
        "locator_description": "Получение ссылки на продукт"
    },
    "pagination": {
        "ul": {
            "attribute": None,
            "by": "XPATH",
            "selector": "//ul[@class='pagination']",
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()",
            "if_list":"first","use_mouse": False,
            "mandatory": True,
            "locator_description": "Нажатие на пагинацию"
        },
        "->": {
            "attribute": None,
            "by": "XPATH",
            "selector": "//*[@class = 'ui-pagination-navi util-left']/a[@class='ui-pagination-next']",
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()",
            "if_list":"first","use_mouse": False,
            "mandatory": True,
            "locator_description": "Клик по следующей странице"
        }
    }
}

# Выполнение локатора с разными событиями
result = locator.execute_locator(complex_locator)
print(f"Результат выполнения сложного локатора: {result}")

# Пример обработки ошибки и продолжения на ошибки

print("\nПример обработки ошибки и продолжения на ошибки")

try:
    locator.execute_locator(complex_locator, continue_on_error=True)
except ExecuteLocatorException as ex:
    print(f"Произошла ошибка: {ex}")

# Пример использования с `send_message`

print("\nПример использования с `send_message`")

# Пример отправки сообщения в текстовое поле
message_locator = {
    "by": "XPATH",
    "selector": "//input[@name='search']",
    "attribute": None,
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": "%SEARCH%",
    "if_list":"first","use_mouse": False,
    "mandatory": True,
    "locator_description": "Отправка поискового запроса"
}

# Отправка сообщения с использованием метода send_message
message = "Купить новый телефон"
result = locator.send_message(message_locator, message, typing_speed=0.05, continue_on_error=True)
print(f"Результат отправки сообщения: {result}")

# Пример с использованием списка локаторов

print("\nПример с использованием списка локаторов")

# Пример работы с множественными локаторами
multi_locator = {
    "by": ["XPATH", "XPATH"],
    "selector": ["//button[@id='submit']", "//input[@id='username']"],
    "attribute": ["textContent", "value"],
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": ["click()", "send_keys('user')"],
    "if_list":"first","use_mouse": [True, False],
    "mandatory": [True, True],
    "locator_description": ["Нажатие кнопки отправки", "Ввод имени пользователя"]
}

# Выполнение локатора с несколькими элементами
results = locator.execute_locator(multi_locator)
print(f"Результаты выполнения множества локаторов: {results}")

# Пример использования `evaluate_locator`

print("\nПример использования `evaluate_locator`")

# Пример оценки локатора
attribute_locator = {
    "by": "XPATH",
    "selector": "//meta[@name='description']",
    "attribute": "content",
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": None,
    "if_list":"first","use_mouse": False,
    "mandatory": True,
    "locator_description": "Получение значения мета-описания страницы"
}

# Оценка локатора и получение атрибута
attribute_value = locator.evaluate_locator(attribute_locator['attribute'])
print(f"Значение атрибута: {attribute_value}")

# Пример с обработкой исключений

print("\nПример с обработкой исключений")

# Пример обработки исключений при выполнении локатора
try:
    locator.execute_locator(simple_locator)
except ExecuteLocatorException as ex:
    print(f"Произошла ошибка при выполнении локатора: {ex}")

# Полный пример теста

print("\nПолный пример теста")

# Пример использования метода execute_locator
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

# Закрытие драйвера
driver.quit()

