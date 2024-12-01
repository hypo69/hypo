Как использовать класс ExecuteLocator
========================================================================================

Описание
-------------------------
Класс `ExecuteLocator` из модуля `src.webdriver` предназначен для выполнения различных действий над элементами веб-страницы с помощью Selenium WebDriver. Он обрабатывает локейторы (словари) для навигации и взаимодействия с веб-страницей.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек и модулей:**
    Класс `ExecuteLocator` импортирует Selenium WebDriver, а также вспомогательные модули для работы с настройками, логированием и обработкой исключений. Это необходимо для взаимодействия с веб-страницей.

2. **Инициализация класса ExecuteLocator:**
    Создайте экземпляр класса `ExecuteLocator`, передав ему экземпляр WebDriver. Это инициализирует драйвер и цепочку действий (`ActionChains`).

    .. code-block:: python
        from selenium import webdriver
        from src.webdriver import ExecuteLocator

        driver = webdriver.Chrome()  # или другой драйвер
        executor = ExecuteLocator(driver)

3. **Использование метода `execute_locator`:**
    Метод `execute_locator` является главным методом для выполнения действий. Он принимает словарь `locator` с параметрами для выполнения действий, необязательные параметры `message`, `typing_speed` и `continue_on_error`.
    Метод определяет какие действия выполнить, основываясь на конфигурации в словаре `locator`.

    .. code-block:: python
        locator_data = {
            "by": "xpath",
            "selector": "//input[@id='search']",
            "action": "send_keys",
            "value": "Python"
        }
        executor.execute_locator(locator_data, message='Ввод', typing_speed=0.1)


4. **Использование методов `get_webelement_by_locator`, `get_attribute_by_locator`, `send_message`:**
    Эти методы позволяют получать веб-элементы, атрибуты элементов и отправлять сообщения (текст) в веб-элементы соответственно.  Они принимают словарь `locator` и (необязательно) сообщение `message`.

    .. code-block:: python
        # Получение элемента
        element = executor.get_webelement_by_locator(locator_data)
        
        # Получение атрибута
        attribute_value = executor.get_attribute_by_locator(locator_data, attribute='value')

        # Отправка сообщения (например, ввода текста)
        executor.send_message(locator_data, "text message")


5. **Обработка ошибок:**
    Класс `ExecuteLocator` обрабатывает исключения (например, `NoSuchElementException`, `TimeoutException`) для обеспечения устойчивости к ошибкам.

Пример использования
-------------------------
.. code-block:: python

    from selenium import webdriver
    from src.webdriver import ExecuteLocator

    driver = webdriver.Chrome()
    executor = ExecuteLocator(driver)
    driver.get("https://www.example.com")

    locator = {
        "by": "id",
        "selector": "search-box",
        "action": "send_keys",
        "value": "python"
    }
    
    try:
        executor.execute_locator(locator)
        print("Успешно ввели текст в поле поиска.")
    except Exception as e:
        print(f"Ошибка при выполнении действия: {e}")
    finally:
        driver.quit()