Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот код содержит набор тестов для класса `ExecuteLocator`, который используется для взаимодействия с веб-элементами.  Тесты проверяют различные сценарии, включая нахождение элемента по локатору, получение атрибутов элемента, отправку сообщений (ввода текста) и работу с различными ситуациями (нахождение одного или нескольких элементов, отсутствие элемента).  Код использует фикстуры для создания моков веб-драйвера и `ExecuteLocator`, что позволяет изолировать тестирование.

Шаги выполнения
-------------------------
1. **Импорт необходимых библиотек:**  Код импортирует `pytest`, `unittest.mock`, `selenium.webdriver`,  `selenium.common.exceptions`, а также собственные классы из модулей `src.webdriver.executor` и `src.logger.exceptions`.

2. **Определение фикстур:** Фикстура `driver_mock` создает мок объекта веб-драйвера.  Фикстура `execute_locator` использует `driver_mock`, чтобы создать экземпляр класса `ExecuteLocator`, используя мок-объект драйвера.

3. **Написание тестов:** Тесты в файле проверяют различные методы класса `ExecuteLocator`:
    - `test_get_webelement_by_locator_single_element`: Проверяет, что метод `get_webelement_by_locator` возвращает единственный элемент, найденный по локатору.
    - `test_get_webelement_by_locator_multiple_elements`: Проверяет возвращение списка элементов, если найдено несколько элементов по локатору.
    - `test_get_webelement_by_locator_no_element`: Проверяет, что метод возвращает `False`, если по заданному локатору элемент не найден.
    - `test_get_attribute_by_locator`: Проверяет получение значения атрибута элемента.
    - `test_send_message`: Проверяет отправку сообщения (ввода текста) элементу.
    - `test_send_message_typing_speed`: Проверяет отправку сообщения с заданной скоростью ввода.

4. **Использование `MagicMock` и `patch`:**  Моки (`MagicMock`) используются для имитации поведения объектов (например, веб-драйвера).  `patch` используется для замены поведения функции `time.sleep` в тесте `test_send_message_typing_speed`.

5. **Ассерты:**  В каждом тесте используются утверждения (`assert`) для проверки ожидаемого поведения метода `ExecuteLocator`. Используются методы `assert_called_once_with` и `assert_called_once` для проверки вызовов методов веб-драйвера.

Пример использования
-------------------------
.. code-block:: python

    import pytest
    from unittest.mock import MagicMock
    from selenium.webdriver.remote.webelement import WebElement
    from src.webdriver.executor import ExecuteLocator
    
    def test_example_usage():
        # Создайте мок веб-драйвера
        driver_mock = MagicMock()
        # Создайте экземпляр класса ExecuteLocator, используя мок-объект
        execute_locator = ExecuteLocator(driver_mock)
        # Определяем локатор
        locator = {
            "by": "XPATH",
            "selector": "//input[@id='my_input']"
        }
        # Имитируем нахождение элемента
        element = MagicMock(spec=WebElement)
        driver_mock.find_elements.return_value = [element]
        # Введите текст в поле
        result = execute_locator.send_message(locator, "Test input")
        # Проверка, что метод send_message отработал успешно
        assert result is True