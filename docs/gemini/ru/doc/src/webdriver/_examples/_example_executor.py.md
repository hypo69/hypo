# src.webdriver._examples._example_executor.py

## Обзор

Этот модуль демонстрирует примеры использования класса `ExecuteLocator` для взаимодействия с веб-элементами с помощью Selenium WebDriver. Примеры включают выполнение простых и сложных локаторов, обработку ошибок, отправку сообщений, работу с множественными локаторами, оценку атрибутов и полную проверку.

## Оглавление

- [Обзор](#обзор)
- [Импорты](#импорты)
- [Функция `main`](#функция-main)
    - [Создание экземпляра WebDriver](#создание-экземпляра-webdriver)
    - [Создание экземпляра ExecuteLocator](#создание-экземпляра-executelocator)
    - [Простой пример локатора](#простой-пример-локатора)
    - [Сложный пример локатора](#сложный-пример-локатора)
    - [Пример обработки ошибок](#пример-обработки-ошибок)
    - [Пример использования `send_message`](#пример-использования-send_message)
    - [Пример использования нескольких локаторов](#пример-использования-нескольких-локаторов)
    - [Пример `evaluate_locator`](#пример-evaluatelocator)
    - [Пример обработки исключений](#пример-обработки-исключений)
    - [Полный пример теста](#полный-пример-теста)
    - [Закрытие драйвера](#закрытие-драйвера)

## Импорты

- `selenium.webdriver` (webdriver.Chrome): Для управления браузером.
- `src.webdriver.executor` (ExecuteLocator): Для выполнения локаторов.
- `src.settings` (gs): Для доступа к настройкам.
- `src.logger.exceptions` (ExecuteLocatorException): Для обработки исключений, связанных с выполнением локатора.

## Функция `main`

Основная функция, демонстрирующая работу с `ExecuteLocator`.

### Создание экземпляра WebDriver
   - Инициализирует экземпляр `webdriver.Chrome` с путем к драйверу из настроек `gs`.
   - Переходит по адресу `https://example.com`.
   
### Создание экземпляра ExecuteLocator
   - Создает экземпляр `ExecuteLocator` для выполнения локаторов на странице.

### Простой пример локатора

   - Определяет простой локатор для получения заголовка страницы (`h1`).
   - Выводит результат выполнения локатора.

### Сложный пример локатора

   - Создаёт сложный локатор, включающий в себя нахождение ссылок на продукты и работу с пагинацией.
    - Выводит результат выполнения локатора.
    
### Пример обработки ошибок
   - Выполняет сложный локатор с параметром `continue_on_error=True` для демонстрации обработки ошибок.
   - Выводит сообщение об ошибке, если она возникает.

### Пример использования `send_message`
   - Создаёт локатор для отправки сообщения в текстовое поле.
   - Использует метод `send_message` для отправки сообщения "Buy a new phone" с заданной скоростью печати.
   - Выводит результат отправки сообщения.

### Пример использования нескольких локаторов
   - Создаёт локатор с массивом параметров для поиска нескольких элементов.
   - Выполняет локаторы и выводит результат.

### Пример `evaluate_locator`

   - Создаёт локатор для получения мета-описания страницы.
   - Использует метод `evaluate_locator` для получения значения атрибута.
   - Выводит полученное значение.
   
### Пример обработки исключений

   - Демонстрирует обработку исключений при выполнении локатора.
   - Выводит сообщение об ошибке в случае ее возникновения.

### Полный пример теста

   - Создаёт тестовый локатор для проверки получения заголовка страницы.
   - Выводит результат выполнения тестового локатора.

### Закрытие драйвера
   - Закрывает браузер, завершая работу WebDriver.

   ```python
   def main():
        """
        Основная функция, демонстрирующая работу с ExecuteLocator.
        """
        # Create WebDriver instance (e.g., Chrome)
        driver = webdriver.Chrome(executable_path=gs['chrome_driver_path'])
        driver.get("https://example.com")  # Navigate to the website

        # Create an instance of ExecuteLocator
        locator = ExecuteLocator(driver)

        # Simple example of creating an instance and using methods
        print("Simple example of creating an instance and using methods")

        # Simple locator to get an element by XPath
        simple_locator = {
            "by": "XPATH",
            "selector": "//h1",
            "attribute": "textContent",
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": None,
            "if_list":"first","use_mouse": False,
            "mandatory": True,
            "locator_description": "Getting the page title"
        }

        # Execute the locator
        result = locator.execute_locator(simple_locator)
        print(f"Result of executing simple locator: {result}")

        # Example of using different events and attributes
        print("\nExample of using different events and attributes")

        # Locator for sending a message and getting an attribute
        complex_locator = {
            "product_links": {
                "attribute": "href",
                "by": "XPATH",
                "selector": "//a[contains(@class, 'product')]",
                "timeout":0,"timeout_for_event":"presence_of_element_located","event": None,
                "if_list":"first","use_mouse": False,
                "mandatory": True,
                "locator_description": "Getting the product link"
            },
            "pagination": {
                "ul": {
                    "attribute": None,
                    "by": "XPATH",
                    "selector": "//ul[@class='pagination']",
                    "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()",
                    "if_list":"first","use_mouse": False,
                    "mandatory": True,
                    "locator_description": "Click on pagination"
                },
                "->": {
                    "attribute": None,
                    "by": "XPATH",
                    "selector": "//*[@class = 'ui-pagination-navi util-left']/a[@class='ui-pagination-next']",
                    "timeout":0,"timeout_for_event":"presence_of_element_located","event": "click()",
                    "if_list":"first","use_mouse": False,
                    "mandatory": True,
                    "locator_description": "Click on the next page"
                }
            }
        }

        # Execute locator with different events
        result = locator.execute_locator(complex_locator)
        print(f"Result of executing complex locator: {result}")

        # Example of error handling and continuing on errors
        print("\nExample of error handling and continuing on errors")

        try:
            locator.execute_locator(complex_locator, continue_on_error=True)
        except ExecuteLocatorException as ex:
            print(f"An error occurred: {ex}")

        # Example of using `send_message`
        print("\nExample of using `send_message`")

        # Locator for sending a message to a text field
        message_locator = {
            "by": "XPATH",
            "selector": "//input[@name='search']",
            "attribute": None,
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": "%SEARCH%",
            "if_list":"first","use_mouse": False,
            "mandatory": True,
            "locator_description": "Sending a search query"
        }

        # Send a message using the send_message method
        message = "Buy a new phone"
        result = locator.send_message(message_locator, message, typing_speed=0.05, continue_on_error=True)
        print(f"Result of sending message: {result}")

        # Example of using a list of locators
        print("\nExample of using a list of locators")

        # Locator for multiple elements
        multi_locator = {
            "by": ["XPATH", "XPATH"],
            "selector": ["//button[@id='submit']", "//input[@id='username']"],
            "attribute": ["textContent", "value"],
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": ["click()", "send_keys('user')"],
            "if_list":"first","use_mouse": [True, False],
            "mandatory": [True, True],
            "locator_description": ["Click the submit button", "Enter username"]
        }

        # Execute locator with multiple elements
        results = locator.execute_locator(multi_locator)
        print(f"Results of executing multiple locators: {results}")

        # Example of `evaluate_locator`
        print("\nExample of using `evaluate_locator`")

        # Locator for evaluating an attribute
        attribute_locator = {
            "by": "XPATH",
            "selector": "//meta[@name='description']",
            "attribute": "content",
             "timeout":0,"timeout_for_event":"presence_of_element_located","event": None,
            "if_list":"first","use_mouse": False,
            "mandatory": True,
            "locator_description": "Getting the page meta-description"
        }

        # Evaluate the locator and get the attribute
        attribute_value = locator.evaluate_locator(attribute_locator['attribute'])
        print(f"Attribute value: {attribute_value}")

        # Example of exception handling
        print("\nExample of exception handling")

        # Example of handling exceptions when executing a locator
        try:
            locator.execute_locator(simple_locator)
        except ExecuteLocatorException as ex:
            print(f"An error occurred during locator execution: {ex}")

        # Full test example
        print("\nFull test example")

        # Test locator example
        test_locator = {
            "by": "XPATH",
            "selector": "//h1",
            "attribute": "textContent",
            "timeout":0,"timeout_for_event":"presence_of_element_located","event": None,
            "if_list":"first","use_mouse": False,
            "mandatory": True,
            "locator_description": "Getting the page title"
        }

        # Execute the test locator
        result = locator.execute_locator(test_locator)
        print(f"Result of executing test locator: {result}")

        # Close the driver
        driver.quit()

   ```