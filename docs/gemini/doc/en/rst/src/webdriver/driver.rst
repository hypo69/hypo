hypotez/src/webdriver/driver.py
============================

.. module:: hypotez.src.webdriver.driver
   :platform: Windows, Unix
   :synopsis: Модуль для работы с веб-драйверами Selenium.

   Основное назначение класса `Driver` — обеспечение унифицированного интерфейса для работы с веб-драйверами Selenium.

   Основные функции:

   1. **Инициализация драйвера**: создание экземпляра Selenium WebDriver.
   2. **Навигация**: переход по URL, прокрутка и извлечение контента.
   3. **Работа с куки**: сохранение и управление куки.
   4. **Обработка исключений**: логирование ошибок.

   Пример использования:
       >>> from selenium.webdriver import Chrome
       >>> driver = Driver(Chrome, executable_path='/path/to/chromedriver')
       >>> driver.get_url('https://example.com')


Classes
-------

.. autoclass:: Driver
   :members:
   :undoc-members:
   :show-inheritance:


Functions
---------

.. autofunction:: hypotez.src.webdriver.driver.__init__
.. autofunction:: hypotez.src.webdriver.driver.__init_subclass__
.. autofunction:: hypotez.src.webdriver.driver.__getattr__
.. autofunction:: hypotez.src.webdriver.driver.scroll
.. autofunction:: hypotez.src.webdriver.driver.carousel
.. autofunction:: hypotez.src.webdriver.driver.locale
.. autofunction:: hypotez.src.webdriver.driver.get_url
.. autofunction:: hypotez.src.webdriver.driver.window_open
.. autofunction:: hypotez.src.webdriver.driver.wait
.. autofunction:: hypotez.src.webdriver.driver._save_cookies_localy
.. autofunction:: hypotez.src.webdriver.driver.fetch_html