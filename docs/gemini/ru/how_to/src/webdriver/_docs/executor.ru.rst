Как использовать класс ExecuteLocator
=========================================================================================

Описание
-------------------------
Класс `ExecuteLocator` из модуля `src.webdriver` предназначен для взаимодействия с элементами веб-страницы с использованием Selenium WebDriver.  Он обрабатывает различные действия (например, нажатия, отправку сообщений, получение атрибутов) на основе заданных локаторов в виде словарей.  Этот класс абстрагирует взаимодействие с веб-элементами, упрощая написание тестов и повышая их читаемость.

Шаги выполнения
-------------------------
1. **Инициализация:** Создайте экземпляр класса `ExecuteLocator`, передав в конструктор объект `WebDriver` (Selenium):

   ```python
   from selenium import webdriver
   from src.webdriver import ExecuteLocator

   driver = webdriver.Chrome()
   executor = ExecuteLocator(driver)
   ```

2. **Определение локатора:** Подготовьте словарь `locator`, описывающий искомый элемент на веб-странице.  Ключи словаря обычно соответствуют методам поиска Selenium (например, "by", "xpath", "css", "id", "name").

   ```python
   locator = {
       "by": "xpath",
       "selector": "//input[@type='text']"
   }
   ```

3. **Выполнение действия:** Вызовите метод `execute_locator()` класса `ExecuteLocator`, передав в него подготовленный словарь `locator` и необходимые параметры (например, текст для ввода, скорость ввода, поведение при ошибке).

   ```python
   message = "Тестовое значение"
   typing_speed = 0.2  # Скорость ввода (секунды за символ)
   result = executor.execute_locator(locator, message, typing_speed)
   ```

4. **Обработка результата:** Результат выполнения может быть различным, в зависимости от действий, указанных в локаторе.  Обработайте полученный результат в соответствии с ожидаемым типом данных:

   ```python
   if result:
       print(f"Ввод выполнен успешно: {result}")
   else:
       print("Ввод не выполнен.")
   ```

5. **Закрытие драйвера:** После завершения работы не забудьте закрыть объект `WebDriver`:

   ```python
   driver.quit()
   ```

Пример использования
-------------------------
.. code-block:: python

    from selenium import webdriver
    from src.webdriver import ExecuteLocator

    # Инициализация WebDriver
    driver = webdriver.Chrome()
    executor = ExecuteLocator(driver)

    # Локатор для поля поиска
    locator = {
        "by": "id",
        "selector": "search-input"
    }

    # Текст для ввода
    message = "Selenium"
    typing_speed = 0.1

    # Выполнение поиска по локатору
    try:
        executor.execute_locator(locator, message, typing_speed)
        print("Поиск выполнен успешно.")
    except Exception as e:
        print(f"Ошибка: {e}")


    # Закрытие WebDriver
    driver.quit()