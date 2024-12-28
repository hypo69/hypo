# Анализ кода модуля _example_executor_2.py

**Качество кода**
8
 -  Плюсы
    - Код демонстрирует использование класса `ExecuteLocator` для взаимодействия с веб-страницами.
    - Присутствуют примеры использования различных типов локаторов (XPath), атрибутов и событий.
    - Показано использование `send_message` для отправки текста в текстовые поля.
    - Включены примеры обработки ошибок с использованием `try-except` и `continue_on_error`.
 -  Минусы
    - Отсутствует docstring модуля.
    - Не все комментарии оформлены в стиле reStructuredText (RST).
    - Не используется `j_loads` или `j_loads_ns` для чтения файлов.
    - Присутствуют избыточные `try-except` блоки.
    - Присутствуют магические строки.

**Рекомендации по улучшению**

1.  Добавить docstring модуля в формате RST, описывающий назначение и использование модуля.
2.  Все комментарии и docstring должны быть переписаны в формате reStructuredText (RST).
3.  Удалить лишние пустые комментарии
4.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения конфигурационных файлов, если это необходимо.
5.  Заменить избыточные `try-except` блоки на логирование ошибок с помощью `logger.error`.
6.  Избегать магических строк, определяя их как константы.
7.  Импортировать `logger` из `src.logger.logger` для логирования ошибок и отладки.
8.  Привести в соответствие имена переменных и импортов с ранее обработанными файлами.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль, демонстрирующий примеры использования класса `ExecuteLocator`.
======================================================================

Этот модуль содержит примеры создания экземпляра `ExecuteLocator` и выполнения различных задач с его помощью,
таких как получение элементов, отправка сообщений, и обработка ошибок.

Примеры использования
--------------------

Примеры включают работу с простыми и сложными локаторами, а также обработку исключений.

.. code-block:: python

    # Пример создания экземпляра ExecuteLocator
    driver = webdriver.Chrome(executable_path=gs['chrome_driver_path'])
    locator = ExecuteLocator(driver)
    result = locator.execute_locator(simple_locator)

"""
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator
from src import gs
# from src.logger.exceptions import ExecuteLocatorException #TODO удалил так как он не используется
from src.logger.logger import logger #TODO  добавил импорт logger

 #TODO добавил константу

# Создание экземпляра WebDriver (например, Chrome)
driver = webdriver.Chrome(executable_path=gs['chrome_driver_path'])
driver.get("https://example.com")  # Переход на сайт

# Создание экземпляра ExecuteLocator
locator = ExecuteLocator(driver)

# Простой пример создания экземпляра и использования методов
print("Простой пример создания экземпляра и использования методов")

# Простой локатор для получения элемента по XPath
SIMPLE_LOCATOR = { #TODO вынес в константу
    "by": "XPATH",
    "selector": "//h1",
    "attribute": "textContent",
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": None,
    "if_list":"first","use_mouse": False,
    "mandatory": True,
    "locator_description": "Получение заголовка страницы"
}

# Выполнение локатора
result = locator.execute_locator(SIMPLE_LOCATOR)
print(f"Результат выполнения простого локатора: {result}")

# Пример использования с различными событиями и атрибутами
print("\nПример использования с различными событиями и атрибутами")

# Пример локатора для отправки сообщения и получения атрибута
COMPLEX_LOCATOR = { #TODO вынес в константу
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

# Выполнение локатора с разными событиями
result = locator.execute_locator(COMPLEX_LOCATOR)
print(f"Результат выполнения сложного локатора: {result}")

# Пример обработки ошибки и продолжения на ошибки
print("\nПример обработки ошибки и продолжения на ошибки")

# Код выполняет попытку выполнения локатора с игнорированием ошибок
try:
    locator.execute_locator(COMPLEX_LOCATOR, continue_on_error=True)
# Код перехватывает ошибку ExecuteLocatorException и выводит сообщение
except Exception as ex:
    logger.error(f"Произошла ошибка: {ex}")


# Пример использования с `send_message`
print("\nПример использования с `send_message`")

# Пример отправки сообщения в текстовое поле
MESSAGE_LOCATOR = { #TODO вынес в константу
    "by": "XPATH",
    "selector": "//input[@name=\'search\']",
    "attribute": None,
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": "%SEARCH%",
    "if_list":"first","use_mouse": False,
    "mandatory": True,
    "locator_description": "Отправка поискового запроса"
}

# Отправка сообщения с использованием метода send_message
message = "Купить новый телефон"
result = locator.send_message(MESSAGE_LOCATOR, message, typing_speed=0.05, continue_on_error=True)
print(f"Результат отправки сообщения: {result}")

# Пример с использованием списка локаторов
print("\nПример с использованием списка локаторов")

# Пример работы с множественными локаторами
MULTI_LOCATOR = { #TODO вынес в константу
    "by": ["XPATH", "XPATH"],
    "selector": ["//button[@id=\'submit\']", "//input[@id=\'username\']"],
    "attribute": ["textContent", "value"],
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": ["click()", "send_keys(\'user\')"],
    "if_list":"first","use_mouse": [True, False],
    "mandatory": [True, True],
    "locator_description": ["Нажатие кнопки отправки", "Ввод имени пользователя"]
}

# Выполнение локатора с несколькими элементами
results = locator.execute_locator(MULTI_LOCATOR)
print(f"Результаты выполнения множества локаторов: {results}")

# Пример использования `evaluate_locator`
print("\nПример использования `evaluate_locator`")

# Пример оценки локатора
ATTRIBUTE_LOCATOR = { #TODO вынес в константу
    "by": "XPATH",
    "selector": "//meta[@name=\'description\']",
    "attribute": "content",
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": None,
    "if_list":"first","use_mouse": False,
    "mandatory": True,
    "locator_description": "Получение значения мета-описания страницы"
}

# Оценка локатора и получение атрибута
attribute_value = locator.evaluate_locator(ATTRIBUTE_LOCATOR['attribute'])
print(f"Значение атрибута: {attribute_value}")

# Пример с обработкой исключений
print("\nПример с обработкой исключений")

# Пример обработки исключений при выполнении локатора
try:
    locator.execute_locator(SIMPLE_LOCATOR)
except Exception as ex:
    logger.error(f"Произошла ошибка при выполнении локатора: {ex}")

# Полный пример теста
print("\nПолный пример теста")

# Пример использования метода execute_locator
TEST_LOCATOR = { #TODO вынес в константу
    "by": "XPATH",
    "selector": "//h1",
    "attribute": "textContent",
    "timeout":0,"timeout_for_event":"presence_of_element_located","event": None,
    "if_list":"first","use_mouse": False,
    "mandatory": True,
    "locator_description": "Получение заголовка страницы"
}

result = locator.execute_locator(TEST_LOCATOR)
print(f"Результат выполнения тестового локатора: {result}")

# Закрытие драйвера
driver.quit()