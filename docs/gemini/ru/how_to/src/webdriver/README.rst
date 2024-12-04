Как использовать ExecuteLocator
========================================================================================

Описание
-------------------------
Этот модуль предоставляет класс `ExecuteLocator`, который используется для автоматизации взаимодействия с веб-страницами с помощью Selenium WebDriver. Он обрабатывает словари локейторов, содержащие инструкции по поиску и взаимодействию с элементами страницы, и выполняет заданные действия.  Класс умеет выполнять навигацию, взаимодействовать с элементами, получать атрибуты, отправлять сообщения (текст) и делать скриншоты элементов.

Шаги выполнения
-------------------------
1. **Инициализация:** Создайте экземпляр класса `ExecuteLocator`, передав в конструктор экземпляр WebDriver.
   ```python
   from selenium import webdriver
   from src.webdriver import ExecuteLocator

   driver = webdriver.Chrome()  # Или другой WebDriver
   executor = ExecuteLocator(driver)
   ```
2. **Обработка локейтора:** Используйте метод `execute_locator` для выполнения действий, описанных в словаре локейтора.
   ```python
   locator_data = {
       "locator_type": "xpath",
       "selector": "//button[@id='submit']",
       "action": "click"
   }
   executor.execute_locator(locator_data)
   ```
3. **Получение элемента:**  Используйте метод `get_webelement_by_locator` для получения элемента страницы по заданным параметрам локейтора.  Метод возвращает `WebElement`, список `WebElement` или `False`, если элемент не найден.
   ```python
   element = executor.get_webelement_by_locator({"locator_type": "id", "selector": "myElement"})
   if element:
       # Обработка найденного элемента
       print(element.text)
   ```

4. **Получение атрибута элемента:** Метод `get_attribute_by_locator` позволяет получить атрибут найденного элемента.
   ```python
   attribute_value = executor.get_attribute_by_locator({"locator_type": "css", "selector": "input#myInput", "attribute": "value"})
   ```
5. **Отправка сообщения (ввода текста):** Метод `send_message` позволяет отправить текст в элемент ввода.
   ```python
   executor.send_message({"locator_type": "name", "selector": "myInput"}, "some text", 0.1) # 0.1 - скорость печати
   ```
6. **Скриншот элемента:**  Метод `get_webelement_as_screenshot` сохраняет скриншот элемента в файл.
   ```python
   screenshot = executor.get_webelement_as_screenshot({"locator_type": "id", "selector": "myImage"})
   ```
7. **Выполнение действия клика:** Метод `click` выполняет клик на элементе.
   ```python
   executor.click({"locator_type": "css", "selector": "a.some-class"})
   ```
8. **Обработка ошибок:** Модуль содержит обработку исключений (например, `NoSuchElementException`, `TimeoutException`), позволяющую обрабатывать ситуации, когда элемент не найден или ожидание истекло.


Пример использования
-------------------------
```python
from selenium import webdriver
from src.webdriver import ExecuteLocator

driver = webdriver.Chrome()
executor = ExecuteLocator(driver)

locator = {
    'locator_type': 'id',
    'selector': 'myElement',
    'action': 'click'
}

try:
    executor.execute_locator(locator)
    print("Action successfully executed")
except Exception as e:
    print(f"Error: {e}")

driver.quit()
```
```
```
```
```
```
```
```