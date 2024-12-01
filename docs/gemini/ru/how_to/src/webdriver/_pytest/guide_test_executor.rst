Как использовать тесты для класса ExecuteLocator
==========================================================================================

Описание
-------------------------
Данное руководство описывает, как написать и запустить тесты для класса `ExecuteLocator`, который работает с веб-элементами через Selenium WebDriver. Оно включает в себя инструкции по установке зависимостей, настройке WebDriver, созданию файлов тестов, реализации тестов и запуску процесса тестирования.

Шаги выполнения
-------------------------
1. **Установка зависимостей:**
    - Установите необходимые библиотеки, используя команду:
      ```bash
      pip install -r requirements.txt
      ```
    - Файл `requirements.txt` должен содержать:
      ```text
      pytest==7.4.0
      selenium==4.16.1
      ```

2. **Настройка WebDriver:**
    - Установите WebDriver для вашего браузера (например, ChromeDriver для Chrome) по соответствующей инструкции.

3. **Создание файла тестов:**
    - Создайте файл `test_executor.py` в директории `tests`.  Этот файл будет содержать тесты для `ExecuteLocator`.  Примеры тестов показаны в предоставленном коде.

4. **Реализация тестов:**
    - Реализуйте тесты для каждого метода класса `ExecuteLocator`, используя `pytest` и `unittest.mock` для мокирования веб-драйвера (Selenium).
    - Тесты должны проверять различные сценарии:
        - **`get_webelement_by_locator`:**  проверка поиска одного элемента, нескольких элементов и отсутствия элементов.
        - **`get_attribute_by_locator`:** проверка получения атрибута элемента.
        - **`send_message`:** проверка отправки сообщения элементу, включая проверку с задержкой между символами.
    - Обратите внимание на примеры в предоставленном коде `test_executor.py`, которые демонстрируют, как реализовать тесты для каждого метода.

5. **Запуск тестов:**
    - Перейдите в корневую директорию проекта.
    - Запустите тесты, используя команду:
      ```bash
      pytest tests/test_executor.py
      ```

6. **Проверка результатов:**
    - Проверьте вывод `pytest`. Все тесты должны пройти успешно. Если есть ошибки или неудачи, `pytest` покажет детали и информацию о неисправностях, которые необходимо исправить.

7. **Обновление тестов:**
    - По мере изменений в коде `ExecuteLocator` обновляйте соответствующие тесты, чтобы они проверяли новые или измененные функциональные возможности.
    - Поддерживайте актуальность документации, чтобы отражать изменения в тестах.

Пример использования
-------------------------
.. code-block:: python

    import pytest
    from unittest.mock import MagicMock
    from selenium.webdriver.remote.webelement import WebElement
    from selenium.webdriver.common.by import By
    from src.webdriver.executor import ExecuteLocator

    @pytest.fixture
    def driver_mock():
        return MagicMock()

    @pytest.fixture
    def execute_locator(driver_mock):
        return ExecuteLocator(driver_mock)

    def test_get_webelement_by_locator_single_element(execute_locator, driver_mock):
        element = MagicMock(spec=WebElement)
        driver_mock.find_elements.return_value = [element]
        locator = {"by": "XPATH", "selector": "//div[@id='test']"}
        result = execute_locator.get_webelement_by_locator(locator)
        driver_mock.find_elements.assert_called_once_with(By.XPATH, "//div[@id='test']")
        assert result == element