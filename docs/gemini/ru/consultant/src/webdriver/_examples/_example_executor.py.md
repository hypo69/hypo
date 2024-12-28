# Анализ кода модуля `_example_executor.py`

**Качество кода:** 7/10
-   **Плюсы:**
    *   Код предоставляет ясные примеры использования класса `ExecuteLocator`.
    *   Присутствуют примеры работы с разными типами локаторов и атрибутов.
    *   Код демонстрирует обработку ошибок и продолжение выполнения при ошибках.
    *   Примеры использования методов `send_message` и `evaluate_locator`.
    *   Логика кода хорошо структурирована.

-   **Минусы:**
    *   Отсутствует reStructuredText документация для модуля, функций, классов.
    *   Избыточное использование `print` для отладочного вывода, что не подходит для продакшн кода.
    *   Использование `try-except` для обработки ошибок, что можно было бы заменить на логирование с использованием `logger.error`.
    *   Отсутствует импорт `logger` для логирования.
    *   Некоторые комментарии недостаточно информативны, например, `# Create WebDriver instance (e.g., Chrome)`.
    *   В коде используются  `print` а не `logger`
    *   Присутствуют дублирующиеся блоки кода

**Рекомендации по улучшению:**

1.  **Добавить reStructuredText документацию:**
    *   Добавить документацию модуля в начале файла.
    *   Добавить docstring для функции `main`.

2.  **Использовать `logger` для логирования:**
    *   Импортировать `logger` из `src.logger.logger`.
    *   Заменить все `print` на `logger.info`, `logger.debug` или `logger.error`, в зависимости от ситуации.

3.  **Улучшить обработку ошибок:**
    *   Убрать блоки `try-except` там где возможно, и использовать `logger.error` для логирования ошибок.

4.  **Улучшить комментарии:**
    *   Сделать комментарии более информативными и точными, описывая, что именно делает код.

5.  **Убрать дублирование кода:**
   *   По возможности вынести дублирующийся код в отдельные функции

6.  **Привести в порядок переменные:**
   *   Привести в соответствие имена переменных и параметров с ранее обработанными файлами

**Оптимизированный код:**

```python
# -*- coding: utf-8 -*-
"""
Модуль содержит примеры использования класса ExecuteLocator для демонстрации
различных способов взаимодействия с веб-элементами.
========================================================================

Этот модуль демонстрирует, как использовать класс :class:`ExecuteLocator` для выполнения
различных действий с веб-элементами, таких как получение текста, отправка сообщений,
клик и т.д.

Примеры включают:

    - Простые и сложные локаторы.
    - Обработку ошибок.
    - Использование метода `send_message`.
    - Использование списка локаторов.
    - Использование метода `evaluate_locator`.

Пример использования
--------------------

Пример запуска модуля:

.. code-block:: python

    if __name__ == "__main__":
        main()
"""
from selenium import webdriver
from src.webdriver.executor import ExecuteLocator
from src import gs
# Импортируем logger для логирования
from src.logger.logger import logger
from src.logger.exceptions import ExecuteLocatorException


def main():
    """
    Главная функция для демонстрации работы с ExecuteLocator.

    Создает экземпляр веб-драйвера, переходит на заданную страницу,
    создает экземпляр ExecuteLocator и выполняет различные примеры
    использования этого класса.
    """
    # Создание экземпляра веб-драйвера (например, Chrome)
    try:
        driver = webdriver.Chrome(executable_path=gs['chrome_driver_path'])
        logger.info('Драйвер Chrome успешно запущен.')
    except Exception as ex:
        logger.error(f'Ошибка при инициализации драйвера: {ex}')
        return

    try:
        driver.get("https://example.com")  # Переход на веб-страницу
        logger.info(f"Успешно перешли на страницу: https://example.com")
    except Exception as ex:
        logger.error(f'Ошибка при переходе на страницу: {ex}')
        driver.quit()  # Закрыть драйвер в случае ошибки
        return
    # Создание экземпляра ExecuteLocator
    locator = ExecuteLocator(driver)
    logger.info('Экземпляр ExecuteLocator создан.')

    # Простой пример использования локатора
    logger.info('Простой пример использования локатора')
    simple_locator = {
        "by": "XPATH",
        "selector": "//h1",
        "attribute": "textContent",
        "timeout": 0, "timeout_for_event": "presence_of_element_located", "event": None,
        "if_list": "first", "use_mouse": False,
        "mandatory": True,
        "locator_description": "Получение заголовка страницы"
    }

    # Выполнение простого локатора
    result = locator.execute_locator(simple_locator)
    logger.info(f"Результат выполнения простого локатора: {result}")


    # Пример использования разных событий и атрибутов
    logger.info('Пример использования разных событий и атрибутов')
    complex_locator = {
        "product_links": {
            "attribute": "href",
            "by": "XPATH",
            "selector": "//a[contains(@class, \'product\')]",
            "timeout": 0, "timeout_for_event": "presence_of_element_located", "event": None,
            "if_list": "first", "use_mouse": False,
            "mandatory": True,
            "locator_description": "Получение ссылки на продукт"
        },
        "pagination": {
            "ul": {
                "attribute": None,
                "by": "XPATH",
                "selector": "//ul[@class=\'pagination\']",
                "timeout": 0, "timeout_for_event": "presence_of_element_located", "event": "click()",
                "if_list": "first", "use_mouse": False,
                "mandatory": True,
                "locator_description": "Клик по пагинации"
            },
            "->": {
                "attribute": None,
                "by": "XPATH",
                "selector": "//*[@class = \'ui-pagination-navi util-left\']/a[@class=\'ui-pagination-next\']",
                "timeout": 0, "timeout_for_event": "presence_of_element_located", "event": "click()",
                "if_list": "first", "use_mouse": False,
                "mandatory": True,
                "locator_description": "Клик по следующей странице"
            }
        }
    }

    # Выполнение локатора с разными событиями
    result = locator.execute_locator(complex_locator)
    logger.info(f"Результат выполнения сложного локатора: {result}")

    # Пример обработки ошибок и продолжения выполнения при ошибках
    logger.info('Пример обработки ошибок и продолжения выполнения при ошибках')
    try:
        locator.execute_locator(complex_locator, continue_on_error=True)
    except ExecuteLocatorException as ex:
        logger.error(f"Произошла ошибка при выполнении локатора, но выполнение продолжилось: {ex}")

    # Пример использования `send_message`
    logger.info('Пример использования `send_message`')
    message_locator = {
        "by": "XPATH",
        "selector": "//input[@name=\'search\']",
        "attribute": None,
        "timeout": 0, "timeout_for_event": "presence_of_element_located", "event": "%SEARCH%",
        "if_list": "first", "use_mouse": False,
        "mandatory": True,
        "locator_description": "Отправка поискового запроса"
    }

    # Отправка сообщения с использованием метода send_message
    message = "Купить новый телефон"
    result = locator.send_message(message_locator, message, typing_speed=0.05, continue_on_error=True)
    logger.info(f"Результат отправки сообщения: {result}")

    # Пример использования списка локаторов
    logger.info('Пример использования списка локаторов')
    multi_locator = {
        "by": ["XPATH", "XPATH"],
        "selector": ["//button[@id=\'submit\']", "//input[@id=\'username\']"],
        "attribute": ["textContent", "value"],
        "timeout": 0, "timeout_for_event": "presence_of_element_located", "event": ["click()", "send_keys(\'user\')"],
        "if_list": "first", "use_mouse": [True, False],
        "mandatory": [True, True],
        "locator_description": ["Клик по кнопке submit", "Ввод имени пользователя"]
    }

    # Выполнение локатора с несколькими элементами
    results = locator.execute_locator(multi_locator)
    logger.info(f"Результаты выполнения нескольких локаторов: {results}")

    # Пример использования `evaluate_locator`
    logger.info('Пример использования `evaluate_locator`')
    attribute_locator = {
        "by": "XPATH",
        "selector": "//meta[@name=\'description\']",
        "attribute": "content",
        "timeout": 0, "timeout_for_event": "presence_of_element_located", "event": None,
        "if_list": "first", "use_mouse": False,
        "mandatory": True,
        "locator_description": "Получение мета-описания страницы"
    }

    # Оценка локатора и получение атрибута
    attribute_value = locator.evaluate_locator(attribute_locator['attribute'])
    logger.info(f"Значение атрибута: {attribute_value}")

    # Пример обработки исключений при выполнении локатора
    logger.info('Пример обработки исключений при выполнении локатора')

    try:
        locator.execute_locator(simple_locator)
    except ExecuteLocatorException as ex:
        logger.error(f"Произошла ошибка при выполнении локатора: {ex}")

    # Полный пример теста
    logger.info('Полный пример теста')
    test_locator = {
        "by": "XPATH",
        "selector": "//h1",
        "attribute": "textContent",
        "timeout": 0, "timeout_for_event": "presence_of_element_located", "event": None,
        "if_list": "first", "use_mouse": False,
        "mandatory": True,
        "locator_description": "Получение заголовка страницы (тестовый локатор)"
    }

    # Выполнение тестового локатора
    result = locator.execute_locator(test_locator)
    logger.info(f"Результат выполнения тестового локатора: {result}")


    # Закрытие драйвера
    driver.quit()
    logger.info('Драйвер закрыт.')

if __name__ == "__main__":
    main()
```