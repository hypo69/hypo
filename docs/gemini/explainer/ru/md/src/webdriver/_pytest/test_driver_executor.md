# Тесты для модуля `src.webdriver._pytest.test_driver_executor.py`

Этот файл содержит модульные тесты для класса `ExecuteLocator`, отвечающего за взаимодействие с веб-драйвером. Тесты проверяют корректность навигации по страницам, поиск элементов, отправку сообщений, получение атрибутов, выполнение событий на элементах, а также обработку некорректных локаторов.

**Описание тестов:**

* **`test_navigate_to_page`:** Проверяет, что WebDriver корректно переходит на указанную страницу (`http://example.com`).
* **`test_get_webelement_by_locator_single_element`:** Проверяет поиск элемента по XPath-локатору (`//h1`). Убеждается, что возвращаемый элемент является экземпляром `WebElement` и содержит текст "Example Domain".
* **`test_get_webelement_by_locator_no_element`:** Проверяет поведение при поиске несуществующего элемента по XPath-локатору (`//div[@id='nonexistent']`). Ожидается, что метод вернет `False`.
* **`test_send_message`:** Проверяет отправку сообщения (`"Hello World"`) в текстовое поле по заданному XPath-локатору.  Важная деталь: тест использует `typing_speed=0` и `continue_on_error=True`, что может влиять на поведение теста. Нужно убедиться, что поле ввода с id `search` существует на странице `http://example.com`.
* **`test_get_attribute_by_locator`:** Проверяет получение значения атрибута (`href`) элемента по XPath-локатору (`//a[@id='more-information']`). Проверяет совпадение с ожидаемым значением `https://www.iana.org/domains/example`.  Необходимо проверить актуальность этого значения на тестовой странице.
* **`test_execute_locator_event`:** Проверяет выполнение события `click` на элементе по XPath-локатору (`//a[@id='more-information']`). Ожидается, что метод вернет `True`.
* **`test_get_locator_keys`:** Проверяет, что метод `ExecuteLocator.get_locator_keys()` возвращает ожидаемый набор ключей локатора.
* **`test_navigate_and_interact`:** Тест комплексной навигации и взаимодействия с элементами. Переходит на страницу `https://www.wikipedia.org/`, вводит текст в поле поиска "Selenium", нажимает кнопку поиска и проверяет, что на странице результатов есть заголовок с текстом "Selenium".
* **`test_invalid_locator`:** Проверяет обработку некорректного локатора (`"by": "INVALID_BY"`). Ожидается, что произойдет исключение `ExecuteLocatorException`.

**Важные замечания:**

* **Пути к драйверам:** В фикстуре `driver` указан путь к исполняемому файлу `chromedriver`.  Замените `/path/to/chromedriver` на фактический путь к вашему драйверу.
* **Тестовая страница:** Тесты предполагают использование тестовой страницы `http://example.com`.  Если тесты выполняются на другой странице, соответствующие ожидания (например, значения атрибутов) должны быть обновлены.
* **ID элементов:** В тестах используются идентификаторы элементов. Убедитесь, что эти идентификаторы корректны для тестовой страницы `http://example.com`. В `test_send_message` необходимо заменить `"//input[@id='search']"` на правильный локатор, если он не соответствует ожидаемому.
* **`--headless`:** Флаг `--headless` позволяет запускать браузер в фоновом режиме без графического интерфейса, что полезно для автоматизированных тестов.
* **Selenium:**  Используется библиотека Selenium для управления браузером.
* **`ExecuteLocatorException`:** Обработка ошибок через исключение `ExecuteLocatorException` улучшает надежность тестов.
* **Фикстуры:** Фикстуры (`driver`, `execute_locator`) упрощают организацию тестов, обеспечивая правильное создание и освобождение ресурсов.

Этот файл является хорошим примером тестирования взаимодействия с веб-драйвером и демонстрирует структуру тестов для проверки функциональности класса `ExecuteLocator`.