Как использовать метакласс для динамического создания класса Driver
========================================================================================

Описание
-------------------------
Этот код определяет метакласс `DriverMeta`, который динамически создаёт класс `Driver`, наследующий от базового класса `Driver` и указанного класса Selenium WebDriver (`Chrome`, `Firefox` или `Edge`). Метакласс отвечает за создание правильного сочетания этих классов.  Он обеспечивает гибкую и динамическую инициализацию WebDriver с дополнительными настраиваемыми функциями.

Шаги выполнения
-------------------------
1. **Определение метакласса `DriverMeta`:**  Создаётся метакласс `DriverMeta`, отвечающий за создание новых классов `Driver`.

2. **Метод `__call__`:** Этот метод вызывается при создании экземпляра класса `Driver`.
    - Принимает `cls` (базовый класс `Driver`), `webdriver_cls` (класс Selenium WebDriver), а также `*args` и `**kwargs` (аргументы и ключевые аргументы для конструктора класса `Driver`).
    - Проверяет, что `webdriver_cls` является классом (`isinstance`) и является подклассом одного из разрешённых WebDriver классов (`Chrome`, `Firefox`, `Edge`) (`issubclass`).
    - Динамически создаёт новый класс `Driver`, наследующий от `cls` и `webdriver_cls`.
    - В конструкторе нового класса `Driver` (`__init__`) происходит логирование инициализации WebDriver с его именем и аргументами.
    - Используется `super()` для вызова конструкторов родительских классов.
    - Вызывается метод `driver_payload`.

3. **Метод `driver_payload`:** Этот метод, определённый в динамически созданном классе `Driver`, вызывается метод `driver_payload` из базового класса `Driver`. Это гарантирует выполнение любой дополнительной инициализации, необходимой классу `Driver`.

4. **Возвращение динамического класса:**  Созданный динамически класс `Driver` возвращается с предоставленными аргументами.

Пример использования
-------------------------
.. code-block:: python

    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options  # Пример использования options
    from webdriver import Driver, DriverMeta, Chrome, Firefox # Подставьте путь к вашим файлам


    # Пример использования с Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Пример использования options
    service = Service('path/to/chromedriver')  # Замените на свой путь
    chrome_driver = Driver[DriverMeta](webdriver.Chrome(service=service, options=chrome_options), *args, **kwargs)

    # Пример использования с Firefox
    firefox_driver = Driver[DriverMeta](webdriver.Firefox(), *args, **kwargs)

    # Пример использования с любым из поддерживаемых WebDriver (Chrome, Firefox, Edge)
    driver = Driver[DriverMeta](webdriver_cls, *args, **kwargs)


    # Далее, вы можете использовать chrome_driver или firefox_driver как обычный объект WebDriver.
    chrome_driver.get("https://www.example.com")
    # ...