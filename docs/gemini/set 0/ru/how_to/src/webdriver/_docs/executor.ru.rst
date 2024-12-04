Как использовать класс ExecuteLocator
================================================================================
Описание
-------------------------
Класс `ExecuteLocator` из модуля `src.webdriver` предназначен для выполнения действий с элементами веб-страницы на основе предоставленных локаторов.  Он использует Selenium WebDriver для взаимодействия с браузером и предоставляет методы для поиска элементов, отправки сообщений, получения атрибутов и выполнения других операций.  Класс обрабатывает различные типы локаторов (xpath, id, name и др.) и предоставляет механизм для обработки ошибок, обеспечивая гибкость и надёжность.

Шаги выполнения
-------------------------
1. **Инициализация:** Создайте экземпляр класса `ExecuteLocator`, передав в конструктор объект `webdriver` (Selenium WebDriver).
   ```python
   from selenium import webdriver
   from src.webdriver import ExecuteLocator

   driver = webdriver.Chrome()  # Или другой драйвер
   executor = ExecuteLocator(driver)
   ```
2. **Подготовка локатора:** Подготовьте словарь `locator`, содержащий информацию о целевом элементе.  Ключи словаря определяют тип локатора (например, "xpath", "id"), значение -  идентификатор.  Пример:
   ```python
   locator = {
       "by": "xpath",
       "selector": "//input[@id='search']"
   }
   ```
3. **Выполнение действия с помощью `execute_locator`:** Вызовите метод `execute_locator` класса `ExecuteLocator`, передав ему подготовленный словарь `locator` и дополнительные параметры (например, `message` для отправки текста, `typing_speed` для скорости набора, `continue_on_error` для продолжения при ошибках).
   ```python
   message = "some text"
   executor.execute_locator(locator, message=message)
   ```

   Метод `execute_locator` автоматически определяет необходимую операцию на основе значений в словаре `locator`.

4. **Получение элемента или атрибута:** Используйте методы `get_webelement_by_locator` или `get_attribute_by_locator` для получения ссылки на элемент или его атрибута на основе локатора.
   ```python
   element = executor.get_webelement_by_locator(locator)
   attribute_value = executor.get_attribute_by_locator(locator, attribute="value")
   ```

5. **Отправка сообщения:** Используйте метод `send_message` для отправки сообщения элементу, например, для заполнения поля ввода.
   ```python
   message = "Test message"
   executor.send_message(locator, message, typing_speed=0.1, continue_on_error=True)
   ```


Пример использования
-------------------------
.. code-block:: python

    from selenium import webdriver
    from src.webdriver import ExecuteLocator

    # Инициализация драйвера
    driver = webdriver.Chrome()
    executor = ExecuteLocator(driver)

    # Локатор для элемента input
    locator = {
        "by": "id",
        "selector": "search_input"
    }

    # Отправка текста в поле поиска
    message = "Test search query"
    executor.send_message(locator, message, typing_speed=0.1, continue_on_error=True)

    # Закрытие браузера
    driver.quit()
```