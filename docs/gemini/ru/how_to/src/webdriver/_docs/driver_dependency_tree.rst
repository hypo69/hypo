Как использовать этот модуль `src.webdriver`
========================================================================================

Описание
-------------------------
Модуль `src.webdriver` содержит классы для управления веб-драйверами (например, Chrome, Firefox, Edge). Он предоставляет абстракцию над конкретными веб-драйверами, позволяя использовать их через единый интерфейс.  Этот модуль использует Selenium для взаимодействия с браузером.  Он также включает логику работы с локальными файлами cookie, обработку исключений и общие методы для работы с элементами веб-страницы.

Шаги выполнения
-------------------------
1. **Импорт необходимых классов:** Импортируйте нужные классы веб-драйверов (например, `Chrome`, `Firefox`, `Edge`) из модуля `src.webdriver`.

2. **Создание экземпляра драйвера:** Создайте экземпляр класса веб-драйвера, передавая необходимые аргументы в конструктор.  Например, для Chrome:
   ```python
   from src.webdriver import Driver, Chrome
   d = Driver(Chrome) 
   ```

3. **Использование методов драйвера:**  Выполняйте действия с веб-страницей, используя методы, предоставляемые классом `Driver`:
    - `get_url(self, url: str) -> bool`: Загружает указанную страницу.
    - `click(self, locator: str) -> None`: Нажимает на элемент с указателем.
    - `send_key_to_webelement(self, element, keys: str) -> None`: Отправляет последовательность нажатий клавиш на указанный элемент.
    - `scroll(self, scrolls: int, frame_size: int, direction: str, delay: float) -> None | bool`:  Прокручивает страницу.
    - `locale(self) -> None | str`: Получает текущий язык веб-страницы.
    - `extract_domain(self, url: str) -> str`: Извлекает доменное имя из URL.
    - `wait(self, interval: float)`: Задержка выполнения.

4. **Обработка исключений:** Используйте обработку исключений, чтобы справиться с возможными ошибками (например, `ElementNotVisibleException`) при работе с веб-драйвером.

Пример использования
-------------------------
.. code-block:: python

    from src.webdriver import Driver, Chrome
    from selenium.webdriver.common.by import By
    import time


    d = Driver(Chrome)
    try:
        d.get_url("https://example.com")
        time.sleep(5)  # Дать время для загрузки страницы
        d.click(By.ID, "my_button") # Нажимаем на кнопку с id 'my_button'
        d.send_key_to_webelement(d.find_element(By.ID, "my_input"), "Some text")
        result = d.get_attribute_by_locator(By.ID, 'result')
        print(result)  # Выводим атрибут элемента
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        d.quit()