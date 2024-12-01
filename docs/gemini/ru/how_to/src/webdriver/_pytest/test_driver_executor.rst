Как использовать этот блок кода
=========================================================================================

Описание
-------------------------
Этот блок кода содержит набор тестов для проверки функциональности класса `ExecuteLocator`.  Тесты проверяют различные аспекты работы с WebDriver (Selenium), включая навигацию по страницам, поиск элементов, отправку сообщений, получение атрибутов и обработку событий.  Он использует `pytest` для организации и запуска тестов, а также `pytest` фикстуры для настройки WebDriver и `ExecuteLocator`.

Шаги выполнения
-------------------------
1. **Импортирование необходимых библиотек:** Импортируются `pytest`, `selenium` (для работы с WebDriver),  `webdriver.Chrome`, `by` (для локаторов), `ActionChains`, `WebDriverWait`, `expected_conditions`, `ExecuteLocator`, и `ExecuteLocatorException`.

2. **Инициализация `WebDriver` (фиксча `driver`):**  Создается экземпляр `webdriver.Chrome` с использованием `Options` (с аргументом `--headless` для работы в бескрайнем режиме). Устанавливается путь к chromedriver.  Открывается стартовая страница `http://example.com`.  Этот метод инициализирует браузер и устанавливает начальную страницу для тестов.

3. **Инициализация `ExecuteLocator` (фиксча `execute_locator`):** Создается экземпляр класса `ExecuteLocator` с переданным `driver`, чтобы использовать его в тестах.

4. **Определение тестов:**  Определены различные тестовые функции (`test_navigate_to_page`, `test_get_webelement_by_locator_single_element`, и т.д.) для проверки разных функциональных возможностей.

5. **Проверка функций `ExecuteLocator`:** Каждая тестовая функция использует методы класса `ExecuteLocator` (например, `get_webelement_by_locator`, `send_message`, `execute_locator`) для взаимодействия с WebDriver и выполнения определённых действий.


6. **Использование ассертов (assert):** В каждом тесте используются утверждения `assert`, чтобы проверить корректность результатов выполнения методов `ExecuteLocator`.

7. **Обработка исключений:**  Тест `test_invalid_locator` демонстрирует использование `pytest.raises` для проверки обработки исключения `ExecuteLocatorException` в случае некорректного локатора.

8. **Закрытие WebDriver (фиксча `driver`):** После выполнения всех тестов WebDriver закрывается с помощью `driver.quit()`.


Пример использования
-------------------------
.. code-block:: python

    import pytest
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from src.webdriver.executor import ExecuteLocator
    from src.logger.exceptions import ExecuteLocatorException

    # ... (Импорт необходимых библиотек - см. выше)


    @pytest.fixture(scope="module")
    def driver():
        # ... (Инициализация WebDriver - см. выше)

    @pytest.fixture
    def execute_locator(driver):
        # ... (Инициализация ExecuteLocator - см. выше)


    def test_navigate_and_interact(execute_locator, driver):
        # Навигация на новую страницу
        driver.get("https://www.wikipedia.org/")
        assert driver.current_url == "https://www.wikipedia.org/"

        # Поиск и отправка текста в поле поиска
        locator = {"by": "XPATH", "selector": "//input[@id='searchInput']"}
        execute_locator.send_message(locator, "Selenium", typing_speed=0, continue_on_error=True)

        # Поиск и клик по кнопке поиска
        locator = {"by": "XPATH", "selector": "//button[@type='submit']"}
        execute_locator.execute_locator(locator, message="click")

        # Проверка наличия результата поиска
        assert "Selenium" in driver.title

        # Дополнительная проверка элемента на странице результатов
        result_locator = {"by": "XPATH", "selector": "//h1[contains(text(), 'Selenium')]"}
        result = execute_locator.get_webelement_by_locator(result_locator)
        assert isinstance(result, WebElement)
        assert result.text == "Selenium"